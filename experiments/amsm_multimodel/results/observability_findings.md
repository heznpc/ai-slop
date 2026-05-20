# Observability Findings (2026-05-21)

The original `run.py` for this experiment persisted only aggregate wall time and per-call decision logs. Token usage, per-call duration, and USD cost were not recorded as first-class experimental variables. This document records what we reconstructed after the fact and what the calibration revealed.

## Three artefacts now exist

| File | Source | Reliability |
|---|---|---|
| `metrics_retrofit.csv` + `cost_summary.json` (retrofit) | Parsed from `results/run_full.log` (preserves the timing from the live run) and `chars/4` token + published-pricing estimates over the cached raw outputs | **Approximate; biased low by an order of magnitude — see below** |
| `calibration/summary.csv` | 3 fresh calls (one per rater, format=video) with `claude --output-format json` and `gemini -o json`, capturing CLI-native usage envelopes | **Ground truth, n=3** |
| `metrics.csv` (when produced by re-running `run.py`) | Native CLI envelopes for every call when run.py is invoked fresh | **Ground truth, full panel** (requires cache invalidation for existing runs) |

## What the calibration revealed

| Rater | native input tokens | retrofit input tokens (chars/4) | native / retrofit | native output tokens | output ratio | native cost (1 call) | retrofit cost (1 call) | cost ratio |
|---|---|---|---|---|---|---|---|---|
| Claude Opus 4.7 | 5 | 727 | **0.007** | 247 | 1.625 | **$0.2714** | $0.0223 | **12.2 ×** |
| Claude Sonnet 4.6 | 2 | 727 | 0.003 | 173 | 1.113 | **$0.0391** | $0.0048 | **8.1 ×** |
| Gemini 2.5 Pro | 6{,}336 | 727 | 8.717 | 145 | 0.964 | (CLI does not report) | $0.0015 | unknown |

Two distinct mechanisms explain the discrepancy:

**For Claude CLI (Opus 4.7, Sonnet 4.6).** The Claude Code agentic CLI loads a substantial system prompt, tool catalogue, and project context before delivering the user prompt. This bulk content is delivered through Anthropic prompt caching: `cache_read_input_tokens` and `cache_creation_input_tokens` dominate the bill, not the `input_tokens` of the actual prompt. The calibration for opus47/video shows `input_tokens = 5`, `cache_read = 15{,}605`, `cache_creation = 12{,}232`. Cost is dominated by cache creation. The naive `chars/4` retrofit was therefore measuring the wrong quantity entirely.

**For Gemini CLI.** The reverse: Gemini's `tokens.input` field reports ~6{,}400 tokens for a prompt whose own character count maps to ~700 tokens via chars/4. The CLI is injecting ~5{,}700 tokens of additional system context before issuing the call. The retrofit is again measuring the wrong quantity, but in the opposite direction.

## Extrapolated true cost of the 24-call panel run

Applying calibration multipliers to the 8 calls per rater (treating the calibration value as representative; per-call variance is real but small over short prompts):

| Rater | calibration cost | × 8 calls | total |
|---|---|---|---|
| Claude Opus 4.7 | $0.271 | × 8 | **$2.17** |
| Claude Sonnet 4.6 | $0.039 | × 8 | **$0.31** |
| Gemini 2.5 Pro | not CLI-reported | × 8 | unknown (small, free-tier likely) |
| **Total** | | | **~ $2.50** (Anthropic-billed) |

The retrofit's `cost_usd_total_est = $0.234` is therefore an underestimate by roughly an order of magnitude. The true Anthropic-billed cost of this experiment was on the order of $2.50.

## Methodological consequence

When LLM-as-judge experiments are run through agentic CLIs (Claude Code, Gemini CLI), the **cost is dominated by CLI scaffolding, not by the experimental prompt itself**. Char-count retrofits underestimate by ~10× because they treat the experimental prompt as the whole input. Reproducible LLM-as-judge accounting therefore requires:

1. Capturing the CLI's native usage envelope at run time (`--output-format json` for Claude, `-o json` for Gemini), or
2. Bypassing the CLI entirely and using the raw SDK (`anthropic`, `google.generativeai`) where the input is exactly the prompt you supplied.

For this paper's reported AMSM panel run, the scores are the authoritative deliverable; the cost figures are now accurate to within a calibration multiplier. The protocol going forward (per the updated `run.py`) writes per-call `.meta.json` files alongside each cached score so that any future replication has native usage on disk per cell, not just an aggregate.

## What's not in this repo

- A full-panel re-run with native capture would cost ~$2.50 to re-execute, which would also re-roll the 24 model outputs (potentially producing slightly different scores at the same nominal temperature 0). Not done in this turn to preserve the published scores. If the future Delphi or replication run is performed, it should always start from a clean cache and use the updated `run.py`.
