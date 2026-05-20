# H2 Bibliometric Misallocation — Locked Protocol

**Pre-registered**: 2026-05-21
**Source of truth**: this file. Both `papers/perspectives/paper/main.tex` H2 paragraph and `papers/framework/paper/main.tex` `\S 4.2` reference this protocol.
**Author commitment**: any deviation from the parameters below MUST be logged in `planning/decisions.md` *before* re-running, not after seeing results.

---

## Hypothesis (verbatim from paper)

> H2: The number of published detection studies per format is inversely correlated with the production-detection asymmetry of that format.

## Falsification rule

Reject H2 if Spearman's $\rho$ between per-format paper counts and per-format PDA composite scores satisfies $\rho \ge 0$ at $\alpha = 0.05$, one-sided test (alternative: $\rho < 0$).

## Data source

- **OpenAlex Works API** (`https://api.openalex.org/works`).
- Polite-pool access via `mailto=wantcongz@gmail.com` query parameter. No API key required, no payment.
- Original protocol (Semantic Scholar Academic Graph) was unusable from this IP — every request returned 429 with no results. Pivoted before any data was observed; rationale in `planning/decisions.md` (2026-05-21 entry).
- Snapshot date: the date the script is executed. Recorded in `results/run_metadata.json`.

## Time window

`year >= 2020 AND year <= 2026` — fixed.

## Per-format keyword sets

Eight formats. For each, queries are run in three independent forms; results are unioned then deduplicated on Semantic Scholar `paperId`.

| Format | Query strings (OR-unioned) |
|---|---|
| **video** | `"deepfake detection"`, `"AI-generated video detection"`, `"synthetic video detection"` |
| **audio** | `"audio deepfake detection"`, `"synthetic speech detection"`, `"voice spoofing detection"` |
| **image** | `"AI-generated image detection"`, `"synthetic image detection"`, `"GAN image detection"` |
| **text** | `"AI-generated text detection"`, `"machine-generated text detection"`, `"LLM-generated text detection"` |
| **hybrid (card news / carousel)** | `"AI-generated infographic detection"`, `"AI-generated carousel detection"`, `"card news detection"` |
| **fake reviews** | `"fake review detection"`, `"AI-generated review detection"`, `"synthetic review detection"` |
| **academic papers** | `"AI-generated academic paper detection"`, `"AI-generated abstract detection"`, `"GPT generated paper detection"` |
| **news articles** | `"AI-generated news detection"`, `"AI-generated news article detection"`, `"synthetic news detection"` |

Queries are case-insensitive on Semantic Scholar's side; exact-phrase quoting is preserved in the API request.

## Dedup

Per format: union over the three queries, then deduplicate on OpenAlex Work `id`. A paper appearing in multiple format-queries (e.g., both text and academic) is counted once per format it appears in — this is intentional, because misallocation is measured per modality, not per paper.

## PDA composite

Per format, `PDA = mean(PCA, DDI)` using the values published in `papers/framework/paper/main.tex` AMSM matrix:

| Format | PCA | DDI | PDA |
|---|---|---|---|
| Video | 3 | 2 | 2.5 |
| Audio | 3 | 2 | 2.5 |
| Image | 4 | 3 | 3.5 |
| Text (Blog/SEO) | 5 | 4 | 4.5 |
| Hybrid (Card News) | 5 | 5 | 5.0 |
| Fake Reviews | 5 | 4 | 4.5 |
| Academic Papers | 4 | 4 | 4.0 |
| News Articles | 4 | 3 | 3.5 |

If the AMSM matrix is later revised in the paper, this table must be updated and the experiment re-run.

## Primary statistic

`scipy.stats.spearmanr(paper_counts, pda_scores, alternative='less')` — one-sided, alternative is negative correlation.

Report: $\rho$, $p$, 95% bootstrap CI (10,000 resamples, fixed `numpy` seed `20260521`).

## Secondary descriptives (no formal test)

- Per-format paper count
- Mean paper count for PDA $\le 3$ vs. PDA $\ge 4$
- Per-format paper title / abstract spot-check on 5 random papers — to verify queries returned topical results, not noise.

## Sample size / power

This is a population census of Semantic Scholar over 8 formats, not a sample. Power analysis is not applicable in the classical sense. The 8-format scaffold gives a fixed degrees-of-freedom for the Spearman test ($n=8$, df=6). With $n=8$, a Spearman $\rho \le -0.643$ is significant at $\alpha=0.05$ one-sided. This is a high bar — small-$n$ Spearman is well-known to require large effect sizes for significance, which is appropriate here.

## Reproducibility

- Python 3.13, `requests`, `scipy`, `numpy`, `pandas` only.
- Random seed for bootstrap: `20260521`.
- Raw API responses cached to `results/raw/<format>_<query_idx>.json` (one file per query, full concatenated JSON).
- Final tally to `results/paper_counts.csv`.
- Statistical output to `results/stats.json`.
- Run metadata (OpenAlex polite-pool email, snapshot date, total API calls) to `results/run_metadata.json`.

## Failure modes and fallback

1. **API rate-limit (HTTP 429)**: protocol allows up to 3 retries per page with exponential backoff. If still failing, the experiment halts and reports the failed query; no fallback to web scraping.
2. **API returns < 5 results for a format with high PDA**: this is a *finding*, not a failure — report as-is.
3. **Query returns clearly off-topic results in spot-check**: log to `results/limitations.md`; do not silently change the keyword set. If the spot-check shows the methodology is broken, halt and revise the protocol via `planning/decisions.md`.
4. **Pagination cap (5000 results per query) reached for high-volume formats (e.g., video)**: documented in `results/limitations.md`. Rank ordering is preserved as long as capped formats are the higher-count ones, which is the direction H2 predicts.

## What this protocol does NOT do

- Does not claim each Semantic Scholar paper is unique — the same arXiv preprint and a later venue publication may both be counted. Acknowledged limitation.
- Does not weight by citations, venue prestige, or recency — raw paper count only.
- Does not measure non-English-language literature outside Semantic Scholar's index.
- Does not test H1, H3, H4 from the Perspectives paper or H-Gap through H-Spill from the Framework agenda — those are separate experiments.
