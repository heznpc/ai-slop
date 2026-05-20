#!/usr/bin/env python3
"""
AMSM Panel — Native Metrics Calibration (3 calls)
==================================================

Validates the retrofit token/cost estimates by issuing a single fresh call to
each rater (format=video) with native JSON output capture, and comparing the
CLI-reported usage/cost against the chars/4 + published-pricing retrofit.

Does NOT touch the main panel cache. Writes only under results/calibration/.
"""

from __future__ import annotations
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
RESULTS = HERE / "results"
CAL = RESULTS / "calibration"
CAL.mkdir(parents=True, exist_ok=True)

PRICING_PER_M = {
    "opus47":      {"input": 15.00, "output": 75.00},
    "sonnet46":    {"input":  3.00, "output": 15.00},
    "gemini25pro": {"input":  1.25, "output":  5.00},
}
CHARS_PER_TOKEN = 4.0


def run(cmd, prompt, uses_stdin):
    t0 = time.time()
    if uses_stdin:
        proc = subprocess.run(cmd, input=prompt, text=True, capture_output=True, timeout=300)
    else:
        proc = subprocess.run(cmd + [prompt], text=True, capture_output=True, timeout=300)
    return proc.stdout or "", time.time() - t0, proc.returncode


def main() -> int:
    cfg = json.loads((HERE / "prompts.json").read_text())
    template = (HERE / "prompt_template.txt").read_text()
    video_fmt = next(f for f in cfg["formats"] if f["name"] == "video")
    prompt = template.replace("{format_name}", video_fmt["name"]).replace("{format_description}", video_fmt["description"])
    input_chars = len(prompt)

    targets = [
        {"id": "opus47", "label": "Claude Opus 4.7", "family": "claude",
         "cmd": ["claude", "--print", "--no-session-persistence", "--output-format", "json", "--model", "claude-opus-4-7", "--max-budget-usd", "5"],
         "uses_stdin": True},
        {"id": "sonnet46", "label": "Claude Sonnet 4.6", "family": "claude",
         "cmd": ["claude", "--print", "--no-session-persistence", "--output-format", "json", "--model", "sonnet", "--max-budget-usd", "5"],
         "uses_stdin": True},
        {"id": "gemini25pro", "label": "Gemini 2.5 Pro", "family": "gemini",
         "cmd": ["gemini", "-m", "gemini-2.5-pro", "-o", "json", "-p"],
         "uses_stdin": False},
    ]

    rows = []
    for t in targets:
        print(f"calibrating {t['id']}...", flush=True)
        out, wall_s, rc = run(t["cmd"], prompt, t["uses_stdin"])
        (CAL / f"{t['id']}_video_envelope.json").write_text(out)
        if t["family"] == "claude":
            env = json.loads(out)
            usage = env.get("usage") or {}
            native_in = usage.get("input_tokens")
            native_out = usage.get("output_tokens")
            native_cache_read = usage.get("cache_read_input_tokens")
            native_cache_create = usage.get("cache_creation_input_tokens")
            native_cost = env.get("total_cost_usd")
            native_duration_ms = env.get("duration_ms")
            model_text = env.get("result", "")
        else:
            env = json.loads(out)
            stats_models = (env.get("stats") or {}).get("models") or {}
            first_key = next(iter(stats_models))
            m = stats_models[first_key]
            tokens = m.get("tokens") or {}
            api = m.get("api") or {}
            native_in = tokens.get("input")
            native_out = tokens.get("candidates")
            native_cache_read = tokens.get("cached")
            native_cache_create = None
            native_cost = None  # gemini CLI doesn't report cost
            native_duration_ms = api.get("totalLatencyMs")
            model_text = env.get("response", "")

        output_chars = len(model_text)
        retrofit_in_tok = int(round(input_chars / CHARS_PER_TOKEN))
        retrofit_out_tok = int(round(output_chars / CHARS_PER_TOKEN))
        price = PRICING_PER_M[t["id"]]
        retrofit_cost = (retrofit_in_tok * price["input"] + retrofit_out_tok * price["output"]) / 1_000_000.0

        row = {
            "rater": t["id"],
            "rater_label": t["label"],
            "wall_s": round(wall_s, 2),
            "input_chars": input_chars,
            "output_chars": output_chars,
            "native_input_tokens": native_in,
            "retrofit_input_tokens": retrofit_in_tok,
            "input_token_ratio_native_over_retrofit": (round(native_in / retrofit_in_tok, 3) if native_in and retrofit_in_tok else None),
            "native_output_tokens": native_out,
            "retrofit_output_tokens": retrofit_out_tok,
            "output_token_ratio_native_over_retrofit": (round(native_out / retrofit_out_tok, 3) if native_out and retrofit_out_tok else None),
            "native_cache_read_tokens": native_cache_read,
            "native_cache_creation_tokens": native_cache_create,
            "native_cost_usd": native_cost,
            "retrofit_cost_usd": round(retrofit_cost, 6),
            "native_duration_ms": native_duration_ms,
        }
        rows.append(row)
        (CAL / f"{t['id']}_video_summary.json").write_text(json.dumps(row, indent=2))

    # Aggregate
    header = list(rows[0].keys())
    csv_lines = [",".join(header)]
    for r in rows:
        csv_lines.append(",".join("" if r.get(k) is None else str(r.get(k)) for k in header))
    (CAL / "summary.csv").write_text("\n".join(csv_lines) + "\n")

    print("=== calibration summary ===")
    for r in rows:
        ir = r["input_token_ratio_native_over_retrofit"]
        orr = r["output_token_ratio_native_over_retrofit"]
        nc = r["native_cost_usd"]
        rc = r["retrofit_cost_usd"]
        print(f"  {r['rater_label']:20s}  in_ratio={ir}  out_ratio={orr}  native_cost=${nc} retrofit_cost=${rc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
