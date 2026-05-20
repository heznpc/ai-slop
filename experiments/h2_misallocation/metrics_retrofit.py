#!/usr/bin/env python3
"""
H2 Bibliometric — Metrics Retrofit
==================================

Reconstructs per-query observability metrics from the cached run artifacts.
OpenAlex is free, so cost is N/A; this retrofit captures per-query wall
time, page count, and reported_total for each (format, query) pair to
support replication-cost forecasting.

Reads:
    results/raw/<format>_<query_idx>.json   cached OpenAlex page sequences
    results/paper_counts.csv                deduped counts per format

Writes:
    results/metrics_retrofit.csv            per-query: format, query_idx,
                                            pages, reported_total, returned_ids
    results/metrics_summary.json            aggregate: total pages, mean pages
                                            per query, per-format breakdown
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).parent
RESULTS = HERE / "results"
RAW = RESULTS / "raw"


def main() -> int:
    cfg = json.loads((HERE / "queries.json").read_text())
    rows = []
    for fmt in cfg["formats"]:
        for q_idx, query in enumerate(fmt["queries"]):
            cache_path = RAW / f"{fmt['name']}_{q_idx}.json"
            if not cache_path.exists():
                rows.append({"format": fmt["name"], "query_idx": q_idx, "query": query, "pages": "", "reported_total": "", "returned_ids": ""})
                continue
            payload = json.loads(cache_path.read_text())
            pages = payload.get("pages") or []
            if pages:
                reported_total = pages[0].get("meta", {}).get("count", 0)
            else:
                reported_total = 0
            returned_ids = set()
            for page in pages:
                for r in (page.get("results") or []):
                    if r.get("id"):
                        returned_ids.add(r["id"])
            rows.append({
                "format": fmt["name"],
                "query_idx": q_idx,
                "query": query,
                "pages": len(pages),
                "reported_total": reported_total,
                "returned_ids": len(returned_ids),
            })

    header = ["format", "query_idx", "query", "pages", "reported_total", "returned_ids"]
    csv_path = RESULTS / "metrics_retrofit.csv"
    with csv_path.open("w") as f:
        f.write(",".join(header) + "\n")
        for r in rows:
            # Quote query to avoid comma issues
            q = '"' + str(r["query"]).replace('"', '""') + '"'
            line = f"{r['format']},{r['query_idx']},{q},{r['pages']},{r['reported_total']},{r['returned_ids']}\n"
            f.write(line)

    total_pages = sum(r["pages"] for r in rows if isinstance(r["pages"], int))
    by_format = {}
    for r in rows:
        f = r["format"]
        by_format.setdefault(f, {"pages": 0, "reported_total_max": 0, "returned_ids_union_size": 0})
        if isinstance(r["pages"], int):
            by_format[f]["pages"] += r["pages"]
            by_format[f]["reported_total_max"] = max(by_format[f]["reported_total_max"], r["reported_total"] or 0)

    summary = {
        "_method": "retrofit from cached results/raw/*.json — counts pages and reported_total from OpenAlex envelopes",
        "_note": "OpenAlex is free; cost is N/A. Per-query wall time was not persisted on the original run; only the aggregate api_call_count=80 (in run_metadata.json) is available.",
        "total_pages": total_pages,
        "total_queries": len(rows),
        "by_format": by_format,
    }
    (RESULTS / "metrics_summary.json").write_text(json.dumps(summary, indent=2))
    print(f"H2 retrofit: {len(rows)} queries, {total_pages} total pages")
    for f, s in by_format.items():
        print(f"  {f:20s}  pages={s['pages']:>3}  reported_total_max={s['reported_total_max']:>5}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
