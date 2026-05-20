#!/usr/bin/env python3
"""
H2 Bibliometric Misallocation — Locked Runner (OpenAlex)
=========================================================

Pre-registered protocol: ./protocol.md (locked 2026-05-21; data source pivoted
to OpenAlex same day, see planning/decisions.md).
Hypothesis source: papers/perspectives/paper/main.tex (H2 paragraph).

Tests Spearman rank correlation between OpenAlex Works counts per format
(AI-content detection literature, 2020-2026) and the AMSM PDA composite scores
published in the Framework paper. Falsification rule: rho >= 0 at alpha=0.05,
one-sided.

Outputs:
    results/raw/<format>_<query_idx>.json            raw API responses
    results/paper_counts.csv                         per-format final tally
    results/stats.json                               Spearman rho, p, CI
    results/run_metadata.json                        snapshot, api calls, version
    results/limitations.md                           any deviations / failures
    results/run.log                                  per-event log
"""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from scipy.stats import spearmanr

HERE = Path(__file__).parent
RESULTS = HERE / "results"
RAW = RESULTS / "raw"
RESULTS.mkdir(exist_ok=True)
RAW.mkdir(exist_ok=True)

API = "https://api.openalex.org/works"
POLITE_EMAIL = "wantcongz@gmail.com"
PER_PAGE = 200
MAX_PAGE = 25            # 25 * 200 = 5000 per query cap
RATE_SLEEP = 0.15        # polite pool: ~10 RPS allowed
MAX_RETRIES = 4
BOOTSTRAP_N = 10000
SEED = 20260521

USER_AGENT = f"ai-slop-paper-h2-misallocation/1.0 (mailto:{POLITE_EMAIL})"


def fetch_query(query: str, year_min: int, year_max: int, log) -> tuple[set[str], int, list[dict]]:
    """Fetch all matching OpenAlex Work IDs for one query, paginating up to MAX_PAGE.

    Returns (work_ids_set, reported_total, raw_pages_list).
    """
    work_ids: set[str] = set()
    raw_pages: list[dict] = []
    reported_total = 0

    for page in range(1, MAX_PAGE + 1):
        params = {
            "search": query,
            "filter": f"publication_year:{year_min}-{year_max}",
            "per-page": PER_PAGE,
            "page": page,
            "mailto": POLITE_EMAIL,
            "select": "id,title,publication_year",
        }
        for attempt in range(MAX_RETRIES):
            try:
                resp = requests.get(API, params=params, headers={"User-Agent": USER_AGENT}, timeout=30)
                if resp.status_code == 429:
                    backoff = 2 ** attempt
                    log(f"  429 rate-limit, sleeping {backoff}s (attempt {attempt+1}/{MAX_RETRIES})")
                    time.sleep(backoff)
                    continue
                if resp.status_code in (500, 502, 503, 504):
                    backoff = 2 ** attempt
                    log(f"  {resp.status_code}, sleeping {backoff}s (attempt {attempt+1}/{MAX_RETRIES})")
                    time.sleep(backoff)
                    continue
                resp.raise_for_status()
                data = resp.json()
                break
            except (requests.RequestException, ValueError) as e:
                backoff = 2 ** attempt
                log(f"  error {e!r}, sleeping {backoff}s (attempt {attempt+1}/{MAX_RETRIES})")
                time.sleep(backoff)
        else:
            raise RuntimeError(f"Query failed after {MAX_RETRIES} retries: {query!r} page={page}")

        raw_pages.append(data)
        meta = data.get("meta") or {}
        if page == 1:
            reported_total = int(meta.get("count", 0))
            log(f"    page 1: total reported={reported_total}")
        results = data.get("results") or []
        if not results:
            break
        for r in results:
            wid = r.get("id")
            if wid:
                work_ids.add(wid)
        if len(results) < PER_PAGE:
            break
        time.sleep(RATE_SLEEP)

    return work_ids, reported_total, raw_pages


def main() -> int:
    log_lines: list[str] = []

    def log(msg: str) -> None:
        ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
        line = f"[{ts}] {msg}"
        print(line, flush=True)
        log_lines.append(line)

    cfg = json.loads((HERE / "queries.json").read_text())
    year_min = cfg["year_min"]
    year_max = cfg["year_max"]

    started_at = datetime.now(timezone.utc).isoformat()
    log(f"H2 runner start (OpenAlex). snapshot={started_at} window={year_min}-{year_max}")

    rows: list[dict] = []
    api_calls = 0
    failures: list[str] = []
    spot_check: dict[str, list[dict]] = {}

    rng_spot = np.random.default_rng(SEED)

    for fmt in cfg["formats"]:
        name = fmt["name"]
        union_ids: set[str] = set()
        per_query_total: list[int] = []
        per_query_returned: list[int] = []
        all_sample_titles: list[dict] = []
        log(f"format={name} pda={fmt['pda']}")

        for q_idx, q in enumerate(fmt["queries"]):
            log(f"  query[{q_idx}]: {q}")
            try:
                ids, total, raw_pages = fetch_query(q, year_min, year_max, log)
            except RuntimeError as e:
                failures.append(f"{name}/{q_idx}: {e}")
                log(f"  FAIL: {e}")
                continue
            (RAW / f"{name}_{q_idx}.json").write_text(json.dumps({
                "query": q,
                "pages": raw_pages,
            }, indent=2))
            log(f"    returned={len(ids)} reported_total={total} pages={len(raw_pages)}")
            per_query_total.append(total)
            per_query_returned.append(len(ids))
            union_ids |= ids
            api_calls += len(raw_pages)
            # Capture sample titles for spot-check
            for raw_page in raw_pages[:1]:
                for r in (raw_page.get("results") or [])[:10]:
                    all_sample_titles.append({
                        "query": q,
                        "id": r.get("id"),
                        "title": r.get("title"),
                        "year": r.get("publication_year"),
                    })

        # Random 5 spot-check
        if all_sample_titles:
            k = min(5, len(all_sample_titles))
            picks = rng_spot.choice(len(all_sample_titles), size=k, replace=False)
            spot_check[name] = [all_sample_titles[i] for i in picks]

        rows.append({
            "format": name,
            "pca": fmt["pca"],
            "ddi": fmt["ddi"],
            "pda": fmt["pda"],
            "queries_total_reported": per_query_total,
            "queries_returned": per_query_returned,
            "deduped_count": len(union_ids),
            "any_query_capped": any(t > MAX_PAGE * PER_PAGE for t in per_query_total),
        })

    df = pd.DataFrame(rows)
    df_out = df[["format", "pca", "ddi", "pda", "deduped_count", "any_query_capped"]].copy()
    df_out.to_csv(RESULTS / "paper_counts.csv", index=False)
    log("paper_counts.csv written")

    counts = df["deduped_count"].to_numpy()
    pdas = df["pda"].to_numpy()
    rho, p_one_sided = spearmanr(counts, pdas, alternative="less")

    rng = np.random.default_rng(SEED)
    n = len(counts)
    bs_rhos = []
    for _ in range(BOOTSTRAP_N):
        idx = rng.integers(0, n, size=n)
        if len(set(idx.tolist())) < 3:
            continue
        bs_rho, _ = spearmanr(counts[idx], pdas[idx])
        if not np.isnan(bs_rho):
            bs_rhos.append(bs_rho)
    bs_rhos_arr = np.asarray(bs_rhos)
    ci_lo, ci_hi = np.percentile(bs_rhos_arr, [2.5, 97.5])

    falsified = bool(rho >= 0 or p_one_sided >= 0.05)
    stats = {
        "n_formats": int(n),
        "spearman_rho": float(rho),
        "p_one_sided_less": float(p_one_sided),
        "bootstrap_n": BOOTSTRAP_N,
        "bootstrap_seed": SEED,
        "bootstrap_ci_95": [float(ci_lo), float(ci_hi)],
        "bootstrap_valid_samples": int(len(bs_rhos_arr)),
        "alpha": 0.05,
        "decision": "H2 not supported (falsified at alpha=0.05)" if falsified else "consistent with H2 at alpha=0.05",
        "falsified": falsified,
    }
    (RESULTS / "stats.json").write_text(json.dumps(stats, indent=2))
    log(f"spearman rho={rho:.4f} p_one_sided={p_one_sided:.4f} ci95=[{ci_lo:.3f}, {ci_hi:.3f}] decision={stats['decision']}")

    meta = {
        "started_at_utc": started_at,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "api": API,
        "user_agent": USER_AGENT,
        "polite_email": POLITE_EMAIL,
        "per_page": PER_PAGE,
        "max_page": MAX_PAGE,
        "rate_sleep_seconds": RATE_SLEEP,
        "year_window": [year_min, year_max],
        "api_call_count": api_calls,
        "python_version": sys.version,
        "scipy_version": __import__("scipy").__version__,
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "requests_version": requests.__version__,
        "failed_queries": failures,
    }
    (RESULTS / "run_metadata.json").write_text(json.dumps(meta, indent=2))
    (RESULTS / "spot_check.json").write_text(json.dumps(spot_check, indent=2))
    log(f"run_metadata.json + spot_check.json written; api_calls={api_calls} failures={len(failures)}")

    caps = df_out[df_out["any_query_capped"]]["format"].tolist()
    lim = [
        "# H2 Run Limitations",
        "",
        f"Snapshot: {started_at}",
        f"Data source: OpenAlex Works API (polite pool, mailto={POLITE_EMAIL})",
        "",
        f"- API call count: {api_calls}",
        f"- Failed queries: {len(failures)}",
    ]
    if failures:
        lim.append("")
        lim.append("## Failed queries")
        for f in failures:
            lim.append(f"- `{f}`")
    if caps:
        lim.append("")
        lim.append("## Formats with at least one query whose reported_total exceeded the 5000-result page-paginated cap")
        lim.append("")
        for c in caps:
            lim.append(f"- **{c}** — actual count for those queries may be undercounted; first 5000 results retrieved per query and deduped across queries.")
        lim.append("")
        lim.append("Rank ordering of formats by deduped_count is preserved as long as capped formats are the higher-count ones, which is the direction H2 predicts.")
    lim.append("")
    lim.append("## Spot-check")
    lim.append("")
    lim.append(f"5 random sample titles per format are recorded in `spot_check.json` to verify queries returned topical results, not noise.")
    (RESULTS / "limitations.md").write_text("\n".join(lim) + "\n")
    log("limitations.md written")

    (RESULTS / "run.log").write_text("\n".join(log_lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
