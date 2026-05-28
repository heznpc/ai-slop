#!/usr/bin/env python3
"""
H-CoEv3: Cycle Velocity by Production Cost Asymmetry — Publication Growth Proxy
================================================================================

Hypothesis (Framework Co-evolution §5.4):
  H-CoEv3: The co-evolution cycle velocity -- time from production to economic
  validation -- is faster for formats with lower Production Cost Asymmetry.
  Text and card news slop should complete the cycle faster than video slop.

Original pre-registered method was 'Cross-format comparison of growth
trajectories for new slop channels/accounts'. That data is in platform
custody. This run substitutes a publication-velocity proxy: per-format
OpenAlex detection-paper counts BY YEAR, fitted to a linear growth slope.

This is a research-velocity proxy, not a production-velocity measurement.
The interpretation is: formats whose detection research is growing fastest
are presumably formats where the underlying slop production is also
growing fastest, prompting the research response. This is an indirect
signal with documented limitations.

Input: cached OpenAlex envelopes from experiments/h2_misallocation/results/raw/
       (already-fetched 2020-2026 paper data with publication_year fields).

Output: results/h_coev3_stats.json
        results/per_format_by_year.csv
"""

from __future__ import annotations
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.stats import linregress, spearmanr

HERE = Path(__file__).parent
RESULTS = HERE / "results"
RESULTS.mkdir(exist_ok=True)

H2_RAW = HERE.parent / "h2_misallocation" / "results" / "raw"

# PDA per format from AMSM matrix (author-assigned, from H2 protocol)
PDA = {
    "video": 2.5,
    "audio": 2.5,
    "image": 3.5,
    "text": 4.5,
    "hybrid_card_news": 5.0,
    "fake_reviews": 4.5,
    "academic_papers": 4.0,
    "news_articles": 3.5,
}

YEAR_MIN, YEAR_MAX = 2020, 2026


def main() -> int:
    log_lines: list[str] = []
    def log(msg: str) -> None:
        t = datetime.now(timezone.utc).strftime("%H:%M:%S")
        line = f"[{t}] {msg}"
        print(line, flush=True)
        log_lines.append(line)

    # Per format, union all 3 queries' raw pages and dedup by Work ID, then
    # count by publication_year.
    per_format_by_year: dict[str, Counter] = {}
    for fmt in PDA.keys():
        seen_ids: set[str] = set()
        year_counts: Counter = Counter()
        for q_idx in range(3):
            cache_path = H2_RAW / f"{fmt}_{q_idx}.json"
            if not cache_path.exists():
                continue
            payload = json.loads(cache_path.read_text())
            for page in payload.get("pages", []):
                for r in (page.get("results") or []):
                    wid = r.get("id")
                    yr = r.get("publication_year")
                    if not wid or wid in seen_ids:
                        continue
                    seen_ids.add(wid)
                    if isinstance(yr, int) and YEAR_MIN <= yr <= YEAR_MAX:
                        year_counts[yr] += 1
        per_format_by_year[fmt] = year_counts
        log(f"  {fmt}: total={sum(year_counts.values())}  by year={dict(sorted(year_counts.items()))}")

    # Write CSV
    years = list(range(YEAR_MIN, YEAR_MAX + 1))
    header = ["format", "pda"] + [str(y) for y in years] + ["slope_per_year", "intercept", "r_squared"]
    rows = []
    slopes = {}
    for fmt, ycounts in per_format_by_year.items():
        ys = [ycounts.get(y, 0) for y in years]
        if sum(ys) == 0:
            slope, intercept, r2 = 0.0, 0.0, 0.0
        else:
            # OLS slope: counts vs year
            res = linregress(years, ys)
            slope, intercept, r2 = float(res.slope), float(res.intercept), float(res.rvalue ** 2)
        slopes[fmt] = slope
        rows.append([fmt, PDA[fmt]] + ys + [round(slope, 3), round(intercept, 3), round(r2, 3)])
    with (RESULTS / "per_format_by_year.csv").open("w") as f:
        f.write(",".join(header) + "\n")
        for r in rows:
            f.write(",".join(str(x) for x in r) + "\n")

    # H-CoEv3 predicts: higher PDA -> faster slope (more recent acceleration)
    # because higher-PDA formats have *lower* cost barriers, so the production
    # explosion is steeper. Test: Spearman(PDA, slope) should be POSITIVE.
    fmts = sorted(slopes.keys())
    pdas = np.array([PDA[f] for f in fmts])
    slps = np.array([slopes[f] for f in fmts])
    if len(set(slps.tolist())) >= 2:
        rho, p = spearmanr(pdas, slps, alternative="greater")
    else:
        rho, p = float("nan"), float("nan")
    log(f"Spearman(PDA, slope) = {rho:.3f}  one-sided greater p = {p:.4f}")

    # Sanity check: a lower-PDA format like video should have steady or
    # decreasing late-window slope; high-PDA formats should peak late.
    # Compute year-of-peak per format.
    year_of_peak = {}
    for fmt, ycounts in per_format_by_year.items():
        if not ycounts:
            year_of_peak[fmt] = None
            continue
        year_of_peak[fmt] = int(max(ycounts.items(), key=lambda kv: kv[1])[0])
    log(f"year_of_peak: {year_of_peak}")
    rho_peak, p_peak = float("nan"), float("nan")
    peak_years_valid = {f: y for f, y in year_of_peak.items() if y is not None}
    if len(peak_years_valid) >= 4:
        f_v = list(peak_years_valid.keys())
        p_v = np.array([PDA[f] for f in f_v])
        py = np.array([peak_years_valid[f] for f in f_v])
        if len(set(py.tolist())) >= 2:
            rho_peak, p_peak = spearmanr(p_v, py, alternative="greater")
        log(f"Spearman(PDA, peak_year) = {rho_peak:.3f}  one-sided p = {p_peak:.4f}")

    falsified = (rho <= 0) or (p >= 0.05) if not np.isnan(p) else True
    decision = "consistent with H-CoEv3 (high PDA -> steeper growth slope)" if not falsified else (
        "H-CoEv3 not supported under the publication-velocity proxy"
    )
    log(f"decision: {decision}")

    out = {
        "method": "publication-velocity proxy from cached OpenAlex H2 data",
        "n_formats": len(slopes),
        "years": years,
        "pda_per_format": PDA,
        "slope_per_format_papers_per_year": {f: round(slopes[f], 3) for f in fmts},
        "year_of_peak_per_format": year_of_peak,
        "primary_spearman_pda_vs_slope": {
            "rho": float(rho) if not np.isnan(rho) else None,
            "p_one_sided_greater": float(p) if not np.isnan(p) else None,
            "alpha": 0.05,
        },
        "secondary_spearman_pda_vs_peak_year": {
            "rho": float(rho_peak) if not np.isnan(rho_peak) else None,
            "p_one_sided_greater": float(p_peak) if not np.isnan(p_peak) else None,
        },
        "decision": decision,
        "h_coev3_supported": (not falsified) if not np.isnan(p) else False,
        "limitations": [
            "Publication-velocity is a research proxy, not a production-velocity measurement.",
            "Higher per-format research volume may simply reflect more detection-research interest, not faster slop production.",
            "Video research is mature pre-2020 (FaceForensics++ 2019, DFDC 2020); the 2020-2026 window may under-capture its earlier acceleration.",
            "Card news has zero published detection research in the window (per H2), so its slope is 0 by construction; this skews the direction of the test.",
            "n=8 formats is the same Spearman-power-ceiling structure as H2 (n=8 critical |rho| >= 0.643 at alpha=0.05).",
        ],
        "snapshot_utc": datetime.now(timezone.utc).isoformat(),
    }
    (RESULTS / "h_coev3_stats.json").write_text(json.dumps(out, indent=2))
    (RESULTS / "run.log").write_text("\n".join(log_lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
