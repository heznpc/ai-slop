#!/usr/bin/env python3
"""
AMSM Multi-Model Panel — Locked Runner
=======================================

Pre-registered protocol: ./protocol.md (locked 2026-05-21)

Calls 3 LLMs (Claude Opus 4.7, Claude Sonnet 4.6, Gemini 2.5 Pro) with the
identical prompt for each of 8 content formats. Collects 5 AMSM dimension
scores per (rater, format) cell, computes inter-rater agreement, derives
panel-mean AMSM, and re-runs the H2 Spearman test against panel-mean PDA.

Outputs:
    results/raw/<rater>_<format>.txt            raw stdout from each CLI call
    results/raw/<rater>_<format>.json           parsed JSON object
    results/scores_raw.csv                      120 individual scores (3 x 8 x 5)
    results/panel_mean.csv                      8 x 5 panel-mean AMSM
    results/pda_comparison.csv                  author-PDA vs panel-PDA per format
    results/irr_stats.json                      Krippendorff alpha + pairwise
    results/h2_rerun.json                       Spearman against panel-mean PDA
    results/run_metadata.json                   timestamps, CLI versions, costs
    results/limitations.md                      JSON-parse failures, retries
    results/run.log                             per-event log
"""

from __future__ import annotations

import json
import re
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr

HERE = Path(__file__).parent
RESULTS = HERE / "results"
RAW = RESULTS / "raw"
RESULTS.mkdir(exist_ok=True)
RAW.mkdir(exist_ok=True)

BOOTSTRAP_N = 10000
SEED = 20260521
DIMS = ["PCA", "DDI", "EDP", "AAS", "RCG"]

RATERS = [
    {
        "id": "opus47",
        "label": "Claude Opus 4.7",
        "cmd": ["claude", "--print", "--no-session-persistence", "--model", "claude-opus-4-7", "--max-budget-usd", "5"],
        "uses_stdin": True,
    },
    {
        "id": "sonnet46",
        "label": "Claude Sonnet 4.6",
        "cmd": ["claude", "--print", "--no-session-persistence", "--model", "sonnet", "--max-budget-usd", "5"],
        "uses_stdin": True,
    },
    {
        "id": "gemini25pro",
        "label": "Gemini 2.5 Pro",
        "cmd": ["gemini", "-m", "gemini-2.5-pro", "-p"],
        "uses_stdin": False,  # prompt passed as last positional arg
    },
]

# Author's original LLM-assisted PDA scores from papers/framework/paper/main.tex
# (PCA, DDI per format -> PDA = mean). Used for before/after comparison.
AUTHOR_AMSM = {
    "video":             {"PCA": 3, "DDI": 2, "EDP": 2},
    "audio":             {"PCA": 3, "DDI": 2, "EDP": 2},
    "image":             {"PCA": 4, "DDI": 3, "EDP": 3},
    "text":              {"PCA": 5, "DDI": 4, "EDP": 3},
    "hybrid_card_news":  {"PCA": 5, "DDI": 5, "EDP": 3},
    "fake_reviews":      {"PCA": 5, "DDI": 4, "EDP": 4},
    "academic_papers":   {"PCA": 4, "DDI": 4, "EDP": 5},
    "news_articles":     {"PCA": 4, "DDI": 3, "EDP": 4},
}


def call_rater(rater: dict, prompt: str, log) -> tuple[str, float, int]:
    """Invoke a rater CLI with prompt. Returns (stdout_text, elapsed_seconds, returncode)."""
    t0 = time.time()
    if rater["uses_stdin"]:
        proc = subprocess.run(
            rater["cmd"],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=180,
        )
    else:
        proc = subprocess.run(
            rater["cmd"] + [prompt],
            text=True,
            capture_output=True,
            timeout=180,
        )
    elapsed = time.time() - t0
    out = proc.stdout or ""
    # Gemini prints "Loaded cached credentials." stderr lines that don't matter
    return out, elapsed, proc.returncode


_JSON_RE = re.compile(r"\{[^{}]*\"PCA\"[^{}]*\}", re.DOTALL)


def parse_scores(text: str) -> dict | None:
    """Extract the AMSM JSON from a raw model response. Returns None on failure."""
    # Strip markdown fences
    text = re.sub(r"^```(?:json)?\s*", "", text.strip(), flags=re.MULTILINE)
    text = re.sub(r"```\s*$", "", text.strip(), flags=re.MULTILINE)
    # Try direct JSON parse first
    candidates = []
    try:
        candidates.append(json.loads(text.strip()))
    except json.JSONDecodeError:
        pass
    # Otherwise try regex match
    if not candidates:
        m = _JSON_RE.search(text)
        if m:
            try:
                candidates.append(json.loads(m.group(0)))
            except json.JSONDecodeError:
                pass
    # Otherwise try broader match including rationale field
    if not candidates:
        broad = re.search(r"\{.*?\"PCA\".*?\}", text, re.DOTALL)
        if broad:
            blob = broad.group(0)
            # Trim trailing junk after last }
            last = blob.rfind("}")
            if last >= 0:
                try:
                    candidates.append(json.loads(blob[: last + 1]))
                except json.JSONDecodeError:
                    pass
    for c in candidates:
        if all(k in c for k in DIMS):
            if all(isinstance(c[k], int) and 1 <= c[k] <= 5 for k in DIMS):
                return c
    return None


def krippendorff_alpha_ordinal(matrix: np.ndarray) -> float:
    """Krippendorff's alpha for ordinal data.

    `matrix` is (n_raters x n_units). Missing values must be np.nan.
    Implementation: standard formula with squared rank-difference distance for ordinal.
    """
    M = np.asarray(matrix, dtype=float)
    n_raters, n_units = M.shape
    # Per-unit pairable values
    units = []
    for u in range(n_units):
        col = M[:, u]
        col = col[~np.isnan(col)]
        if len(col) >= 2:
            units.append(col)
    if not units:
        return float("nan")
    # All pairable values
    all_vals = np.concatenate(units)
    # Compute per-unit disagreement (squared diff over all pairs)
    Do = 0.0
    n_pairs_total = 0
    for col in units:
        m = len(col)
        if m < 2:
            continue
        diffs_sq = 0.0
        for i in range(m):
            for j in range(m):
                if i != j:
                    diffs_sq += (col[i] - col[j]) ** 2
        Do += diffs_sq / (m - 1)
        n_pairs_total += m
    if n_pairs_total == 0:
        return float("nan")
    Do = Do / n_pairs_total
    # Expected disagreement under chance
    n = len(all_vals)
    De = 0.0
    for i in range(n):
        for j in range(n):
            if i != j:
                De += (all_vals[i] - all_vals[j]) ** 2
    De = De / (n * (n - 1))
    if De == 0:
        return 1.0 if Do == 0 else float("nan")
    return 1.0 - Do / De


def main() -> int:
    log_lines: list[str] = []

    def log(msg: str) -> None:
        ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
        line = f"[{ts}] {msg}"
        print(line, flush=True)
        log_lines.append(line)

    cfg = json.loads((HERE / "prompts.json").read_text())
    template = (HERE / "prompt_template.txt").read_text()

    started_at = datetime.now(timezone.utc).isoformat()
    log(f"AMSM multi-model panel start. snapshot={started_at}")
    log(f"raters: {[r['label'] for r in RATERS]}")
    log(f"formats: {len(cfg['formats'])}")

    failures: list[str] = []
    rows: list[dict] = []
    call_log: list[dict] = []
    parse_retries: int = 0

    for rater in RATERS:
        for fmt in cfg["formats"]:
            prompt = template.replace("{format_name}", fmt["name"]).replace("{format_description}", fmt["description"])
            label = f"{rater['id']}/{fmt['name']}"
            json_path = RAW / f"{rater['id']}_{fmt['name']}.json"
            if json_path.exists():
                try:
                    cached = json.loads(json_path.read_text())
                    if all(k in cached for k in DIMS):
                        log(f"skip {label} (cached)")
                        rows.append({"rater": rater["id"], "format": fmt["name"], **{k: cached[k] for k in DIMS}, "rationale": cached.get("rationale", "")})
                        call_log.append({"rater": rater["id"], "format": fmt["name"], "elapsed_s": 0.0, "returncode": 0, "attempt": 0, "cached": True})
                        continue
                except (json.JSONDecodeError, OSError):
                    pass
            log(f"call {label}")
            for attempt in range(2):  # 1 initial + 1 retry on parse failure
                try:
                    out, elapsed, rc = call_rater(rater, prompt, log)
                except subprocess.TimeoutExpired:
                    log(f"  TIMEOUT on {label}")
                    out, elapsed, rc = "", 180.0, -1
                (RAW / f"{rater['id']}_{fmt['name']}.txt").write_text(out)
                parsed = parse_scores(out)
                if parsed is not None:
                    (RAW / f"{rater['id']}_{fmt['name']}.json").write_text(json.dumps(parsed, indent=2))
                    log(f"  ok: {dict((k, parsed[k]) for k in DIMS)} ({elapsed:.1f}s)")
                    call_log.append({
                        "rater": rater["id"], "format": fmt["name"],
                        "elapsed_s": elapsed, "returncode": rc, "attempt": attempt + 1,
                    })
                    rows.append({"rater": rater["id"], "format": fmt["name"], **{k: parsed[k] for k in DIMS}, "rationale": parsed.get("rationale", "")})
                    break
                else:
                    log(f"  PARSE-FAIL attempt {attempt+1}/2 (returncode={rc}, output len={len(out)})")
                    parse_retries += 1
                    if attempt == 0:
                        # Append strict instruction for retry
                        prompt = prompt + "\n\nREMINDER: Reply with the JSON object only. No markdown, no commentary, no leading or trailing text."
                    else:
                        failures.append(f"{label}: parse failed after 2 attempts")
                        rows.append({"rater": rater["id"], "format": fmt["name"], **{k: np.nan for k in DIMS}, "rationale": "<<PARSE FAILURE>>"})

    if not rows:
        log("FATAL: no successful calls")
        return 1

    df_scores = pd.DataFrame(rows)
    df_scores.to_csv(RESULTS / "scores_raw.csv", index=False)
    log(f"scores_raw.csv written ({len(df_scores)} rows)")

    # ---- Panel mean ----
    rater_ids = [r["id"] for r in RATERS]
    format_order = [f["name"] for f in cfg["formats"]]

    panel = pd.DataFrame(index=format_order, columns=DIMS, dtype=float)
    for fmt in format_order:
        for dim in DIMS:
            vals = df_scores[(df_scores["format"] == fmt)][dim].dropna()
            panel.loc[fmt, dim] = vals.mean()
    panel.index.name = "format"
    panel.to_csv(RESULTS / "panel_mean.csv")
    log(f"panel_mean.csv written: {panel.round(2).to_dict()}")

    # ---- IRR statistics ----
    # Build raters x units matrix (units = 40 = 8 formats x 5 dims)
    unit_labels = [(fmt, dim) for fmt in format_order for dim in DIMS]
    M = np.full((len(rater_ids), len(unit_labels)), np.nan)
    for i, rid in enumerate(rater_ids):
        for j, (fmt, dim) in enumerate(unit_labels):
            sub = df_scores[(df_scores["rater"] == rid) & (df_scores["format"] == fmt)][dim]
            if len(sub) and not pd.isna(sub.values[0]):
                M[i, j] = float(sub.values[0])
    alpha_full = krippendorff_alpha_ordinal(M)
    log(f"krippendorff alpha (all 40 cells, ordinal) = {alpha_full:.4f}")

    per_dim_alpha = {}
    for dim_idx, dim in enumerate(DIMS):
        cols = [j for j, (_, d) in enumerate(unit_labels) if d == dim]
        per_dim_alpha[dim] = krippendorff_alpha_ordinal(M[:, cols])
        log(f"  alpha[{dim}] = {per_dim_alpha[dim]:.4f}")

    pairwise = {}
    for ra, rb in combinations(rater_ids, 2):
        a = M[rater_ids.index(ra), :]
        b = M[rater_ids.index(rb), :]
        mask = ~np.isnan(a) & ~np.isnan(b)
        if mask.sum() >= 3:
            r_pearson, p_pearson = pearsonr(a[mask], b[mask])
            disagree2 = int(np.sum(np.abs(a[mask] - b[mask]) >= 2))
            pairwise[f"{ra}__vs__{rb}"] = {
                "n_cells": int(mask.sum()),
                "pearson_r": float(r_pearson),
                "pearson_p": float(p_pearson),
                "cells_disagree_>=2pt": disagree2,
                "frac_disagree_>=2pt": float(disagree2 / mask.sum()),
            }
            log(f"  pairwise {ra} vs {rb}: r={r_pearson:.3f} (n={int(mask.sum())}, disagree>=2: {disagree2})")

    irr = {
        "n_raters": len(rater_ids),
        "n_units": len(unit_labels),
        "krippendorff_alpha_overall_ordinal": float(alpha_full),
        "krippendorff_alpha_per_dimension": {k: float(v) for k, v in per_dim_alpha.items()},
        "pairwise": pairwise,
        "interpretation": (
            "Krippendorff alpha thresholds: >=0.667 acceptable, >=0.80 good."
        ),
    }
    (RESULTS / "irr_stats.json").write_text(json.dumps(irr, indent=2))

    # ---- PDA comparison ----
    h2_counts_path = HERE.parent / "h2_misallocation" / "results" / "paper_counts.csv"
    h2_counts = pd.read_csv(h2_counts_path)
    h2_map = dict(zip(h2_counts["format"], h2_counts["deduped_count"]))

    cmp_rows = []
    for fmt in format_order:
        author = AUTHOR_AMSM[fmt]
        author_pda = (author["PCA"] + author["DDI"]) / 2.0
        panel_pca = float(panel.loc[fmt, "PCA"])
        panel_ddi = float(panel.loc[fmt, "DDI"])
        panel_pda = (panel_pca + panel_ddi) / 2.0
        cmp_rows.append({
            "format": fmt,
            "author_PCA": author["PCA"],
            "author_DDI": author["DDI"],
            "author_PDA": author_pda,
            "panel_PCA": round(panel_pca, 2),
            "panel_DDI": round(panel_ddi, 2),
            "panel_PDA": round(panel_pda, 2),
            "delta_PDA": round(panel_pda - author_pda, 2),
            "openalex_count": h2_map.get(fmt),
        })
    cmp_df = pd.DataFrame(cmp_rows)
    cmp_df.to_csv(RESULTS / "pda_comparison.csv", index=False)
    log("pda_comparison.csv written")

    # ---- H2 re-run with panel PDA ----
    counts = cmp_df["openalex_count"].to_numpy()
    panel_pda_vec = cmp_df["panel_PDA"].to_numpy()
    author_pda_vec = cmp_df["author_PDA"].to_numpy()

    rho_panel, p_panel = spearmanr(counts, panel_pda_vec, alternative="less")
    rho_author, p_author = spearmanr(counts, author_pda_vec, alternative="less")

    rng = np.random.default_rng(SEED)
    n = len(counts)
    def bootstrap_rho(y):
        out = []
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for _ in range(BOOTSTRAP_N):
                idx = rng.integers(0, n, size=n)
                if len(set(idx.tolist())) < 3:
                    continue
                # spearmanr undefined when either array is constant
                if len(set(y[idx].tolist())) < 2 or len(set(counts[idx].tolist())) < 2:
                    continue
                r, _ = spearmanr(counts[idx], y[idx])
                if not np.isnan(r):
                    out.append(r)
        if not out:
            return float("nan"), float("nan"), 0
        a = np.asarray(out)
        return float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)), len(a)

    ci_panel_lo, ci_panel_hi, n_panel_valid = bootstrap_rho(panel_pda_vec)
    ci_author_lo, ci_author_hi, n_author_valid = bootstrap_rho(author_pda_vec)

    panel_falsified = bool(rho_panel >= 0 or p_panel >= 0.05)
    author_falsified = bool(rho_author >= 0 or p_author >= 0.05)

    h2_rerun = {
        "n_formats": int(n),
        "alpha_one_sided": 0.05,
        "bootstrap_n": BOOTSTRAP_N,
        "bootstrap_seed": SEED,
        "author_pda": {
            "rho": float(rho_author),
            "p_one_sided_less": float(p_author),
            "ci_95": [ci_author_lo, ci_author_hi],
            "bootstrap_valid": n_author_valid,
            "falsified_at_alpha_0.05": author_falsified,
        },
        "panel_pda": {
            "rho": float(rho_panel),
            "p_one_sided_less": float(p_panel),
            "ci_95": [ci_panel_lo, ci_panel_hi],
            "bootstrap_valid": n_panel_valid,
            "falsified_at_alpha_0.05": panel_falsified,
        },
        "delta_rho_panel_minus_author": float(rho_panel - rho_author),
    }
    (RESULTS / "h2_rerun.json").write_text(json.dumps(h2_rerun, indent=2))
    log(f"H2 re-run: author rho={rho_author:.3f} (p={p_author:.3f}); panel rho={rho_panel:.3f} (p={p_panel:.3f})")

    # ---- Metadata + limitations ----
    total_elapsed = sum(c["elapsed_s"] for c in call_log)
    meta = {
        "started_at_utc": started_at,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "raters": [{"id": r["id"], "label": r["label"], "cmd": shlex.join(r["cmd"])} for r in RATERS],
        "total_calls": len(call_log),
        "total_wall_seconds": round(total_elapsed, 1),
        "parse_retries": parse_retries,
        "failed_cells": failures,
        "python_version": sys.version,
        "scipy_version": __import__("scipy").__version__,
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
    }
    (RESULTS / "run_metadata.json").write_text(json.dumps(meta, indent=2))

    lim = ["# AMSM Multi-Model Run Limitations", ""]
    lim.append(f"Snapshot: {started_at}")
    lim.append(f"- Calls: {len(call_log)} / 24 expected ({len(rater_ids)} raters x {len(format_order)} formats)")
    lim.append(f"- JSON parse retries: {parse_retries}")
    lim.append(f"- Failed cells (missing scores): {len(failures)}")
    if failures:
        lim.append("")
        lim.append("## Failures")
        for f in failures:
            lim.append(f"- `{f}`")
    lim.append("")
    lim.append("## Panel composition deviation")
    lim.append("- Original protocol nominated GPT-5 as R3. Substituted with Gemini 2.5 Pro because OPENAI_API_KEY is not configured in this environment. Cross-vendor diversity preserved (2 Anthropic + 1 Google).")
    (RESULTS / "limitations.md").write_text("\n".join(lim) + "\n")

    (RESULTS / "run.log").write_text("\n".join(log_lines) + "\n")
    log("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
