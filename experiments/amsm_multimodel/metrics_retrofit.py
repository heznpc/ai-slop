#!/usr/bin/env python3
"""
AMSM Multi-Model Panel — Metrics Retrofit
==========================================

Reconstructs per-call observability metrics from the already-cached run
artifacts (run.log + raw/<rater>_<format>.txt). This addresses the gap that
the original run.py only persisted aggregate wall time and did not record
per-call input/output tokens or USD cost.

Reads:
    results/run.log                  per-call timestamps + elapsed seconds
    results/raw/<rater>_<format>.txt cached model output text
    prompts.json                     format descriptions
    prompt_template.txt              prompt template

Writes:
    results/metrics_retrofit.csv     per-call: rater, format, elapsed_s,
                                     input_chars, output_chars, input_tokens_est,
                                     output_tokens_est, cost_usd_est
    results/cost_summary.json        per-rater aggregate + grand total

Caveats (documented in output and in results/limitations.md):
    - Token counts are estimated as ceil(chars/4); actual tokenization differs
      slightly per model. Cross-checked against Anthropic's published rule of
      thumb (~4 chars/token for English).
    - Cost is computed from published per-million-token pricing as of 2026-05-21;
      actual billing reconciliation requires API-side records.
    - For Gemini 2.5 Pro the basic-tier per-M pricing is applied; if the call
      exceeded any context threshold, true cost may be higher.
    - This is a retrofit. Going forward, run.py captures these natively via
      `--output-format json` (Claude) and `-o json` (Gemini).
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

HERE = Path(__file__).parent
RESULTS = HERE / "results"
RAW = RESULTS / "raw"

# Published per-million-token pricing as of 2026-05-21.
# These are estimates for retrofit purposes; native capture (run.py) records exact billing.
PRICING_PER_M = {
    "opus47":      {"input": 15.00, "output": 75.00},   # Claude Opus 4.7
    "sonnet46":    {"input":  3.00, "output": 15.00},   # Claude Sonnet 4.6
    "gemini25pro": {"input":  1.25, "output":  5.00},   # Gemini 2.5 Pro (basic tier)
}

CHARS_PER_TOKEN = 4.0  # English approximation; documented as estimate


def estimate_tokens(text: str) -> int:
    return int(math.ceil(len(text) / CHARS_PER_TOKEN))


def parse_run_log(log_path: Path) -> dict[tuple[str, str], float]:
    """Parse a run log file for per-call elapsed_s.

    Lines we care about:
      [HH:MM:SS] call <rater>/<format>
      [HH:MM:SS]   ok: {...} (N.Ns)
    Skip lines do not yield a timing (the cell was cached).
    """
    if not log_path.exists():
        return {}
    text = log_path.read_text()
    timings: dict[tuple[str, str], float] = {}
    current: tuple[str, str] | None = None
    for line in text.splitlines():
        m_call = re.search(r"\] call (\w+)/(\w+)$", line)
        if m_call:
            current = (m_call.group(1), m_call.group(2))
            continue
        m_ok = re.search(r"\]   ok: \{.*\} \(([\d.]+)s\)$", line)
        if m_ok and current is not None:
            timings[current] = float(m_ok.group(1))
            current = None
            continue
    return timings


def merged_timings() -> dict[tuple[str, str], float]:
    """Merge timings from all available log sources.

    Priority order (later wins): results/run.log, results/run_full.log,
    and a manual seed of known timings recovered from the live bash output
    history that wasn't preserved in any saved log.
    """
    merged: dict[tuple[str, str], float] = {}
    for fname in ("run.log", "run_full.log"):
        merged.update(parse_run_log(RESULTS / fname))
    # Manual recovery of timings present only in transcript not on disk:
    manual = {
        ("opus47", "video"): 7.3,   # observed in task b6hco0mul output
    }
    for k, v in manual.items():
        merged.setdefault(k, v)
    return merged


def main() -> int:
    cfg = json.loads((HERE / "prompts.json").read_text())
    template = (HERE / "prompt_template.txt").read_text()

    # Build per-call input text reconstructions
    formats = cfg["formats"]
    raters = ["opus47", "sonnet46", "gemini25pro"]
    rater_labels = {
        "opus47": "Claude Opus 4.7",
        "sonnet46": "Claude Sonnet 4.6",
        "gemini25pro": "Gemini 2.5 Pro",
    }

    timings = merged_timings()

    rows = []
    for rater in raters:
        for fmt in formats:
            name = fmt["name"]
            prompt = template.replace("{format_name}", name).replace("{format_description}", fmt["description"])
            input_chars = len(prompt)
            out_path = RAW / f"{rater}_{name}.txt"
            output_chars = len(out_path.read_text()) if out_path.exists() else 0
            elapsed = timings.get((rater, name))
            input_tokens_est = estimate_tokens(prompt)
            output_tokens_est = estimate_tokens(out_path.read_text() if out_path.exists() else "")
            price = PRICING_PER_M[rater]
            cost_usd_est = (input_tokens_est * price["input"] + output_tokens_est * price["output"]) / 1_000_000.0
            rows.append({
                "rater": rater,
                "rater_label": rater_labels[rater],
                "format": name,
                "elapsed_s": elapsed if elapsed is not None else "",
                "input_chars": input_chars,
                "output_chars": output_chars,
                "input_tokens_est": input_tokens_est,
                "output_tokens_est": output_tokens_est,
                "cost_usd_est": round(cost_usd_est, 6),
            })

    # Write CSV by hand to avoid pandas dependency in retrofit
    csv_path = RESULTS / "metrics_retrofit.csv"
    header = ["rater","rater_label","format","elapsed_s","input_chars","output_chars","input_tokens_est","output_tokens_est","cost_usd_est"]
    with csv_path.open("w") as f:
        f.write(",".join(header) + "\n")
        for r in rows:
            f.write(",".join(str(r[k]) for k in header) + "\n")

    # Aggregate per-rater
    summary = {
        "_method": "retrofit from cached outputs + run.log (estimates; see metrics_retrofit.py docstring)",
        "chars_per_token_assumed": CHARS_PER_TOKEN,
        "pricing_per_million_tokens_usd": PRICING_PER_M,
        "raters": {},
        "grand_total": {},
    }
    grand_input_tok = 0
    grand_output_tok = 0
    grand_cost = 0.0
    grand_wall = 0.0
    for rater in raters:
        rs = [r for r in rows if r["rater"] == rater]
        wall_times = [r["elapsed_s"] for r in rs if isinstance(r["elapsed_s"], float)]
        in_tok = sum(r["input_tokens_est"] for r in rs)
        out_tok = sum(r["output_tokens_est"] for r in rs)
        cost = sum(r["cost_usd_est"] for r in rs)
        wall = sum(wall_times)
        summary["raters"][rater] = {
            "label": rater_labels[rater],
            "calls": len(rs),
            "calls_with_timing": len(wall_times),
            "wall_s_total": round(wall, 2),
            "wall_s_mean": round(wall / max(1, len(wall_times)), 2) if wall_times else None,
            "wall_s_min": round(min(wall_times), 2) if wall_times else None,
            "wall_s_max": round(max(wall_times), 2) if wall_times else None,
            "input_tokens_total_est": in_tok,
            "output_tokens_total_est": out_tok,
            "cost_usd_total_est": round(cost, 4),
        }
        grand_input_tok += in_tok
        grand_output_tok += out_tok
        grand_cost += cost
        grand_wall += wall
    summary["grand_total"] = {
        "calls": len(rows),
        "wall_s_total_across_raters": round(grand_wall, 2),
        "input_tokens_total_est": grand_input_tok,
        "output_tokens_total_est": grand_output_tok,
        "cost_usd_total_est": round(grand_cost, 4),
    }
    (RESULTS / "cost_summary.json").write_text(json.dumps(summary, indent=2))
    print(f"metrics_retrofit.csv: {len(rows)} rows")
    print(f"cost_summary.json: grand total est ${grand_cost:.4f}, wall {grand_wall:.1f}s")
    for rater in raters:
        s = summary["raters"][rater]
        print(f"  {rater_labels[rater]:20s}  calls={s['calls']}  wall_mean={s['wall_s_mean']}s  est_cost=${s['cost_usd_total_est']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
