#!/usr/bin/env python3
"""
H-Prev: Text vs Video Penetration — Structured Meta-Analysis
============================================================

Hypothesis (Framework Research Agenda, row 3):
  H-Prev: AI text penetration exceeds AI video penetration by >= 2x.

Original pre-registered method was "Web crawl + video feed audit", which
requires data sources unavailable in the Claude Code environment. This run
substitutes a structured meta-analysis that triangulates three classes of
prevalence indicator:

  (P1) Research-volume proxy: per-format Semantic Scholar / OpenAlex
       paper counts (cached from H2 at experiments/h2_misallocation/).
       Inversion intended: more *research* per format proxies a perceived
       prevalence floor; it does *not* measure content penetration.

  (P2) Cited content-prevalence values from the paper itself:
       - Ahrefs (2025): 74.2% of newly published web pages contain
         AI-generated text content.
       - Kapwing (2025): 21-33% of YouTube Shorts recommended to new
         users are AI slop.
       - LinkedIn / Originality.AI (2025): 54%+ of LinkedIn posts
         contain AI-generated text.
       - Buffer (2026): carousel engagement 6.90%, Reels 3.31%.

  (P3) Ratio test: under multiple paired interpretations, compute the
       text/video penetration ratio and check whether it meets the
       hypothesis threshold of >= 2x.

This is a meta-analysis, not a primary measurement. The hypothesis can be
provisionally supported or refuted only conditional on the validity of the
cited industry numbers.

Output:
  results/h_prev_meta.json   triangulated ratios + decision
  results/run.log
"""

from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
RESULTS = HERE / "results"
RESULTS.mkdir(exist_ok=True)

THRESHOLD = 2.0


def main() -> int:
    log_lines: list[str] = []
    def log(msg: str) -> None:
        t = datetime.now(timezone.utc).strftime("%H:%M:%S")
        line = f"[{t}] {msg}"
        print(line, flush=True)
        log_lines.append(line)

    # ---- P1: research-volume proxy from cached H2 ----
    h2_csv = HERE.parent / "h2_misallocation" / "results" / "paper_counts.csv"
    research_counts = {}
    if h2_csv.exists():
        for line in h2_csv.read_text().splitlines()[1:]:
            parts = line.split(",")
            if len(parts) >= 5:
                research_counts[parts[0]] = int(parts[4])
    log(f"P1 research counts (OpenAlex, 2020-2026): {research_counts}")

    # ---- P2: cited content-prevalence values ----
    cited = {
        "ahrefs_text_web_pages_pct": {
            "value": 0.742,
            "source": "Ahrefs 2025 (cited in Perspectives [ahrefs2025])",
            "note": "74.2% of newly published web pages contain AI-generated text",
        },
        "kapwing_shorts_ai_slop_mid_pct": {
            "value": 0.27,
            "range": [0.21, 0.33],
            "source": "Kapwing 2025 (cited in [kapwing2025])",
            "note": "21-33% of YouTube Shorts recommended to new users are AI slop; midpoint 27%",
        },
        "originalityai_linkedin_text_pct": {
            "value": 0.54,
            "source": "Originality.AI 2025 (cited in Perspectives)",
            "note": "54%+ LinkedIn posts contain AI text",
        },
        "imperva_bot_traffic_pct": {
            "value": 0.51,
            "source": "Imperva 2025 (cited in [imperva2025])",
            "note": "51% of internet traffic is automated (bots); upper bound on AI-text saturation",
        },
        "graphite_articles_pct": {
            "value": 0.52,
            "source": "Graphite 2025 (cited as 'See also' in Perspectives [ahrefs2025])",
            "note": "52% of analyzed English articles show AI involvement",
        },
    }

    # ---- P3: ratio tests ----
    # Build pairwise penetration ratios using triangulation:
    #   text proxy:  max(Ahrefs 74.2%, Graphite 52%, Originality 54%) = Ahrefs 74.2%
    #   text proxy floor: min = Graphite 52%
    #   video proxy: Kapwing 27% (midpoint), 21% floor, 33% ceiling
    text_high = cited["ahrefs_text_web_pages_pct"]["value"]
    text_floor = cited["graphite_articles_pct"]["value"]
    video_mid = cited["kapwing_shorts_ai_slop_mid_pct"]["value"]
    video_floor = cited["kapwing_shorts_ai_slop_mid_pct"]["range"][0]
    video_ceil = cited["kapwing_shorts_ai_slop_mid_pct"]["range"][1]

    ratios = {
        "text_high_over_video_mid": round(text_high / video_mid, 3),
        "text_high_over_video_ceil": round(text_high / video_ceil, 3),
        "text_high_over_video_floor": round(text_high / video_floor, 3),
        "text_floor_over_video_mid": round(text_floor / video_mid, 3),
        "text_floor_over_video_ceil": round(text_floor / video_ceil, 3),
        "text_floor_over_video_floor": round(text_floor / video_floor, 3),
    }
    log(f"ratios: {ratios}")
    n_meet_threshold = sum(1 for r in ratios.values() if r >= THRESHOLD)
    log(f"ratios meeting >= {THRESHOLD}x: {n_meet_threshold}/{len(ratios)}")

    # ---- Research-volume cross-check (note: opposite direction expected) ----
    # Hypothesis is about CONTENT penetration, not research volume.
    # H2 already showed research volume INVERSE-correlates with PDA. So the
    # research-volume ratio is the wrong-direction signal and is reported
    # here for completeness only.
    if "text" in research_counts and "video" in research_counts:
        rv_text = research_counts["text"]
        rv_video = research_counts["video"]
        rv_ratio = round(rv_text / rv_video, 3) if rv_video else None
        log(f"  research-volume text/video ratio (NOT a penetration measure): {rv_ratio}")
    else:
        rv_text = rv_video = rv_ratio = None

    # ---- Decision ----
    # Hypothesis supported if MAJORITY of content-prevalence ratios meet threshold.
    fraction_meeting = n_meet_threshold / len(ratios)
    supported = fraction_meeting >= 0.5
    decision = (
        f"supported (>=50% of triangulated content-prevalence ratios meet 2x threshold)"
        if supported else
        f"not supported (only {fraction_meeting:.0%} of ratios meet 2x threshold)"
    )
    log(f"decision: {decision}")

    out = {
        "method": "structured meta-analysis (no primary measurement)",
        "threshold": THRESHOLD,
        "P1_research_volume_proxy": {
            "counts": research_counts,
            "text_video_ratio": rv_ratio,
            "interpretation": "NOT a content-penetration measure; reported for completeness. Research counts inversely relate to PDA per H2; cannot test H-Prev directly.",
        },
        "P2_cited_prevalence_values": cited,
        "P3_pairwise_ratios": ratios,
        "P3_ratios_meeting_threshold": n_meet_threshold,
        "P3_total_ratios": len(ratios),
        "P3_fraction_meeting": round(fraction_meeting, 3),
        "decision": decision,
        "h_prev_supported": bool(supported),
        "limitations": [
            "Triangulated from cited industry sources, not a primary measurement.",
            "Kapwing 'AI slop in Shorts recommended to new users' is an algorithm-amplified slice, not a population prevalence. True video AI-content prevalence may be higher in the long tail.",
            "Ahrefs 'AI text on new web pages' includes any AI involvement, including light editing; raw fully-AI text prevalence may be lower.",
            "Single-vendor estimates from Kapwing and Ahrefs have not been independently replicated.",
        ],
        "snapshot_utc": datetime.now(timezone.utc).isoformat(),
    }
    (RESULTS / "h_prev_meta.json").write_text(json.dumps(out, indent=2))
    (RESULTS / "run.log").write_text("\n".join(log_lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
