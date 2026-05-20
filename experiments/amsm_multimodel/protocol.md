# AMSM Multi-Model Panel — Locked Protocol

**Pre-registered**: 2026-05-21
**Reason for existing**: The AMSM 5-dimension 1-5 scores in `papers/framework/paper/main.tex` were LLM-assisted (per author's confirmation, 2026-05-21). The H2 bibliometric test (`experiments/h2_misallocation/`) correlated paper counts against those same LLM-assisted scores, creating a single-author × single-model dependency in the experimental chain. This protocol regenerates the AMSM scores under a 3-model panel and re-runs H2 against panel-mean PDA to factor out single-model judgment.

**Source of truth**: this file. Any deviation must be logged in `planning/decisions.md` before re-running.

---

## Panel composition

The original protocol proposed (Opus 4.7, Sonnet 4.6, GPT-5). GPT-5 access is unavailable from this environment (no `OPENAI_API_KEY` configured). Substituted with Gemini 2.5 Pro to preserve cross-vendor diversity.

| Rater | Identifier | Invocation |
|---|---|---|
| R1 | Claude Opus 4.7 | `claude --print --model claude-opus-4-7 --max-budget-usd 5` |
| R2 | Claude Sonnet 4.6 | `claude --print --model sonnet --max-budget-usd 5` |
| R3 | Gemini 2.5 Pro | `gemini -m gemini-2.5-pro -p ...` |

Temperature 0 / default decoding. Each rater receives the identical prompt for each of the 8 formats. Raters do not see each other's outputs.

## Contamination guards

The prompt does **not** include:
- The paper's existing AMSM 1-5 scores
- The text of H2 or any other hypothesis from the paper
- The string "Production-Detection Paradox" or "Production-Detection Asymmetry"
- Per-format paper counts from the OpenAlex H2 run
- Any reference to the paper itself or its expected findings

The prompt **does** include:
- Abstract 1-5 rubric for each of the 5 AMSM dimensions, with concrete anchor descriptions for 1, 3, 5
- Format name + neutral 1-2 sentence description

This separates dimension *definition* (load-bearing for the framework) from *expected scoring* (the variable we want to measure).

## Per-format prompt structure

See `prompts.json` for the locked 8 format descriptions. The prompt template is in `prompt_template.txt`.

Each model produces, per format, a JSON object:
```json
{"PCA": <int 1-5>, "DDI": <int 1-5>, "EDP": <int 1-5>, "AAS": <int 1-5>, "RCG": <int 1-5>, "rationale": "<2-3 sentences>"}
```

3 raters × 8 formats = 24 LLM calls total. 5 scores per call = 120 individual scores.

## Inter-rater agreement statistics

1. **Krippendorff's α** (ordinal level) computed over the full 3 × 40 (raters × cells) matrix. α ≥ 0.667 = acceptable, α ≥ 0.80 = good.
2. **Per-dimension Krippendorff α** for each of PCA, DDI, EDP, AAS, RCG separately (3 raters × 8 formats matrix).
3. **Pairwise Pearson correlation** between rater scores treating 1-5 as interval, all 40 cells, for each pair (R1↔R2, R1↔R3, R2↔R3).
4. **Per-cell variance** across raters: how often do raters disagree by ≥ 2 points?

Computed with a hand-rolled Krippendorff implementation (numpy only) since `krippendorff` PyPI package is not assumed available.

## Panel-mean AMSM

Per (format, dimension): mean of the 3 raters' scores, rounded to 1 decimal place (the original paper uses integer 1-5 but the mean is genuinely continuous).

Panel-mean PDA per format = mean(panel-mean PCA, panel-mean DDI).

The original (author-assigned, LLM-assisted) PDA scores are retained for comparison in `results/pda_comparison.csv`.

## H2 re-run

Using the cached OpenAlex paper counts from `experiments/h2_misallocation/results/paper_counts.csv` (unchanged — they do not depend on AMSM scoring):

- Spearman's ρ between paper counts and panel-mean PDA, one-sided `alternative='less'`, α = 0.05
- Bootstrap 95% CI with the same seed `20260521` and `BOOTSTRAP_N = 10000`
- Compare side-by-side with the original H2 (author-PDA) result: ρ = −0.497, p = 0.105

Reported as a clean before/after.

## Reproducibility

- Each model's raw text output cached to `results/raw/<rater>_<format>.txt`
- Each parsed JSON cached to `results/raw/<rater>_<format>.json`
- Each native CLI envelope (when `run.py` is invoked fresh) cached to `results/raw/<rater>_<format>.meta.json` with per-call `input_tokens`, `output_tokens`, `cache_*_tokens`, `total_cost_usd`, `duration_ms`, `duration_api_ms`
- All scores aggregated to `results/scores_raw.csv`
- Panel mean to `results/panel_mean.csv`
- IRR statistics to `results/irr_stats.json`
- H2 re-run statistics to `results/h2_rerun.json`
- Run metadata (timestamps, CLI versions, model identifiers) to `results/run_metadata.json`

## Observability (first-class experimental variables)

Per-call wall time, input/output tokens, and USD cost are first-class experimental variables. `run.py` invokes each rater with structured-JSON output (`claude --output-format json` and `gemini -o json`) and persists the native envelope in `.meta.json` per cell. Aggregates are written to:

- `results/metrics.csv` — per-call rows with `wall_s`, `input_tokens`, `output_tokens`, `total_cost_usd`, `duration_ms`, `duration_api_ms`
- `results/cost_summary.json` — per-rater totals (calls, native cost, wall time)
- `results/observability_findings.md` — narrative findings including the calibration result that retrofit `chars/4` token estimates undercount the true Anthropic-billed cost by roughly an order of magnitude because Claude Code's CLI scaffolding dominates the bill via `cache_creation_input_tokens`

For the original run that pre-dated native capture, the retrofit lives in `results/metrics_retrofit.csv` + `results/cost_summary.json` (estimates) and `results/run_full.log` (preserved per-call wall times). The calibration that quantifies the retrofit/native gap is in `results/calibration/`.

## Failure modes

1. **JSON parse failure for a rater's output**: 1 retry with appended "STRICT JSON ONLY, NO PROSE" instruction. If still failing, log to `results/limitations.md` and skip that (rater, format) cell. Krippendorff α handles missing data gracefully.
2. **Rate-limit / API error**: 3 retries with exponential backoff (5s, 25s, 125s). If still failing, halt and report.
3. **Model output reports refusal or off-scale value (e.g., 0 or 6)**: log as invalid, retry once, then mark as missing.
4. **Krippendorff α < 0.4 (low agreement)**: the panel-mean is still computed and H2 is still re-run, but interpretation is qualified — low agreement means the AMSM scaffold itself is poorly operationalized, which is a finding (and a more serious one than the H2 result).

## What this protocol does NOT do

- Does not validate that the 5 AMSM dimensions are the *correct* dimensions (that is a higher-level theoretical question).
- Does not generate new format definitions — the 8 formats are fixed from the paper.
- Does not change the OpenAlex bibliometric data (cached from prior H2 run).
- Does not include human raters.
- Does not test for prompt-order or wording bias (a single locked prompt is used for all calls).
