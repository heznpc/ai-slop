# Research Decisions Log

Records non-obvious choices with rationale. Append-only; don't rewrite history.

Format: `## YYYY-MM-DD -- <short title>` with **Context**, **Decision**, **Why**.

---

## 2026-05-21 -- H-Spill Judge B swap: Gemini 2.5 Pro -> Gemini 2.5 Flash (mid-run, partial-result)

**Context**: During execution of `experiments/h_spill/run.py`, Judge B (Gemini 2.5 Pro) returned `TerminalQuotaError: You have exhausted your capacity on this model. Your quota will reset after 9h6m38s.` after completing 21 of 80 planned Gemini calls. Judge A (Claude Opus 4.7) completed all 80 calls successfully. Continuing would require either (a) a 9-hour wait, (b) mixing Gemini 2.5 Pro and Gemini 2.5 Flash judgments within the same Judge B slot (methodologically inconsistent), or (c) swapping the entire Judge B slot to a different model.

**Decision**: Archive the 21 partial Gemini 2.5 Pro judgments under `experiments/h_spill/results/judgments/_gemini25pro_archived/` (preserved for inspection, not used in final analysis). Re-run all 80 Gemini judgments with **Gemini 2.5 Flash** (`gemini -m gemini-2.5-flash -o json -p`). Update `run.py` rater config accordingly.

**Why not wait 9h**: The user explicitly asked to continue. Waiting blocks the experiment for nearly a full day with no methodological gain; Gemini 2.5 Flash is a documented, generally-available model from the same vendor in the same family, preserving cross-vendor diversity vs. the all-Anthropic alternative.

**Why not Sonnet 4.6 instead**: Using Sonnet 4.6 as Judge B would produce a 2-Anthropic panel, eliminating cross-vendor diversity -- which was the explicit rationale for substituting Gemini for GPT-5 in the original AMSM panel (\S 2026-05-21 AMSM entry below).

**Why pre-result and not post-result**: This decision is logged BEFORE the swapped re-run produces any new data. The 21 archived Gemini 2.5 Pro judgments are not used in the final H-Spill statistics; only Opus 4.7 + Gemini 2.5 Flash judgments are used. This preserves the pre-registration discipline.

**What is preserved**: hypothesis (verbatim), 20-seed corpus, generation chain (Sonnet 4.6, 60 calls already completed), Judge A (Opus 4.7, 80 calls already completed), prompt template, falsification rule, statistical procedure.

**Cost impact**: Gemini 2.5 Flash is free under the polite-pool quota (separate quota bucket from 2.5 Pro), so total Anthropic billing is unchanged (~$25-30 for the full run).

---

## 2026-05-21 -- AMSM multi-model panel + H2 supplementary re-run

**Context**: The H2 bibliometric test (`experiments/h2_misallocation/`) correlated OpenAlex paper counts against AMSM PDA scores that were originally LLM-assisted by a single author. This creates a single-judge dependency in the experimental chain. To factor that out, AMSM scores were regenerated under a 3-model panel and H2 was re-run against the panel-mean PDA.

**Panel composition**: Claude Opus 4.7 + Claude Sonnet 4.6 + Gemini 2.5 Pro. Original protocol nominated GPT-5 but `OPENAI_API_KEY` is not configured in this environment; Gemini 2.5 Pro substituted to preserve cross-vendor diversity. Rationale logged in `experiments/amsm_multimodel/protocol.md` and `results/limitations.md`.

**Method**: Identical zero-shot prompt to each rater, asking for an integer 1-5 score on each of the 5 AMSM dimensions (PCA, DDI, EDP, AAS, RCG) for each of the 8 formats. Prompt does not include the paper's existing scores, H2 hypothesis, or any reference to the paper. 24 LLM calls total (3 raters x 8 formats).

**Inter-rater agreement (Krippendorff alpha, ordinal)**:
- Overall (40 cells): 0.621 -- borderline acceptable, below the conventional >=0.667 threshold
- Per dimension: AAS=0.659 (best), DDI=0.403, RCG=0.251, PCA=0.179 (worst), EDP=0.154
- Pairwise Pearson r: Opus<->Sonnet 0.774, Opus<->Gemini 0.684, Sonnet<->Gemini 0.606

The low alpha on PCA reflects a ceiling effect: in 2026 nearly all formats receive a 5 from raters (AI cost <= 1/100 human cost), so PCA discriminates poorly between formats at the 1-5 scale. EDP and RCG also show low agreement, indicating the rubrics for those dimensions are under-operationalized. AAS is the only dimension with meaningful cross-rater consistency.

**H2 re-run results** (Spearman, one-sided, alpha=0.05):
- Author-PDA: rho = -0.497, p = 0.105 (original)
- Panel-mean PDA: rho = -0.610, p = 0.054 (this experiment)
- Delta rho = -0.113 (panel produces a larger effect size)

Direction is preserved and effect size strengthens, but the result remains formally "not supported" under the pre-registered alpha=0.05 falsification rule, now at the borderline (p just above alpha). With n=8 the Spearman ceiling at alpha=0.05 one-sided is |rho| >= 0.643.

**Format-level reassessment by the panel** (panel - author PDA):
- video: +1.00 (panel sees 2026-era Sora video as harder to detect than author rated)
- audio: +1.83 (largest delta -- panel rates audio detection gap much wider)
- text: -0.50 (panel sees text as more actively studied -- matches OpenAlex 1926 count)
- hybrid_card_news: -0.33 (panel slightly lowered the maximum format)
- others: between -0.33 and +0.67

**Decision**: Treat the panel-mean PDA result as supplementary evidence to be reported alongside the author-PDA result, not as a replacement. The paper's H2 paragraph and Limitations should note (a) the panel-mean rho = -0.610, p = 0.054 result, (b) the Krippendorff alpha = 0.621 caveat, and (c) the specific finding that PCA exhibits a ceiling effect at the 1-5 scale and warrants future logarithmic or USD-grounded re-operationalization. No changes to the pre-registered author-PDA falsification rule.

**What this experiment does NOT do**: It does not change the OpenAlex bibliometric counts (those are cached from the prior H2 run). It does not introduce human raters. It does not test for prompt-order or wording sensitivity.

---

## 2026-05-21 -- H2 data source pivot: Semantic Scholar -> OpenAlex (pre-result, no data observed)

**Context**: First execution of `experiments/h2_misallocation/run.py` against Semantic Scholar Academic Graph API. Every API request from the runner's IP returned HTTP 429 (rate limit) on the very first call, and exhausted all 3 retries with exponential backoff for both queries attempted before the run was stopped. No paper data was returned for any format. The unauthenticated tier appears to be effectively unusable from this IP at this time. Free API key issuance requires email verification with multi-day turnaround per the Semantic Scholar API page.

**Decision**: Switch the locked data source from Semantic Scholar Academic Graph API to **OpenAlex Works API** (`https://api.openalex.org/works`). The hypothesis, formats, keyword sets, time window, dedup procedure, primary statistic, falsification threshold, and bootstrap seed are all preserved. Only the source endpoint and dedup key change.

Specifically:
- Endpoint: `https://api.openalex.org/works`
- Authentication: polite-pool via `mailto=wantcongz@gmail.com` parameter (no API key required, no payment)
- Per-page: 200 (OpenAlex max)
- Pagination: page-based (`page=1..25`), capping at 5000 results per query (analogous to Semantic Scholar's effective 1000-cap; OpenAlex itself supports cursor pagination for >10K but 5K per query is sufficient for the scale we expect)
- Dedup key: OpenAlex `id` (canonical Work ID), replacing Semantic Scholar `paperId`
- Rate-limit: 10 RPS in polite pool → `RATE_SLEEP=0.15s`

**Why now (pre-result)**: This pivot is logged *before* any per-format counts have been observed. The original protocol stipulated "any deviation MUST be logged before re-running, not after seeing results." Compliance is exact: the failed run produced no decision-relevant data; only the operational signal that the chosen data source is unreachable.

**Why OpenAlex specifically**: (1) Free, no payment, no key required — preserves the project's no-paid-API constraint. (2) Designed for bibliometric workloads (founded 2022 as a replacement for the discontinued Microsoft Academic Graph). (3) Polite-pool rate limit (10 RPS) is two orders of magnitude more generous than Semantic Scholar's basic tier (~1 RPS). (4) Coverage of arXiv preprints and conference papers is comparable to Semantic Scholar for the CS / detection-research domain we're querying. (5) Reproducible — the OpenAlex Work ID is a canonical permalink, so future replications can verify our raw cached results match.

**What is preserved**: keyword sets (8 formats × 3 queries), 2020-2026 year window, Spearman one-sided alternative='less' against PDA composite, alpha=0.05, bootstrap seed 20260521 with 10,000 resamples, and the falsification rule rho >= 0.

**What changes in paper**: The H2 paragraph in `papers/perspectives/paper/main.tex` is updated to reference OpenAlex instead of Semantic Scholar. The `experiments/h2_misallocation/protocol.md` and `queries.json` are updated correspondingly.

---

## 2026-05-21 -- Pre-experiment design hardening (Critical: C1, C2)

**Context**: In a pre-flight review of the two papers' design, two Critical issues were identified that would invalidate any H2 bibliometric experiment if left in place. (1) `papers/framework/paper/main.tex` Section "Quantifying the Paradox" claimed the y-axis of Figure `fig:paradox` was "approximated by the number of academic papers and dedicated benchmarks in each modality" while supplying no count, citation, or methodology -- the y-axis values were sole-author expert judgment presented as if data-derived. (2) `papers/perspectives/paper/main.tex` H2 statement was falsifiable in principle but specified neither database, keyword set, time window, dedup procedure, primary statistic, nor falsification threshold -- making it impossible to claim that any specific experiment run "tests the paper's H2" rather than a post-hoc methodological variant.

**Decision**:

1. Soften Framework Section 4.2 (`fig:paradox`): explicitly mark Research Investment Gap y-axis values as "preliminary expert estimates pending bibliometric validation under H2", in both prose (\S\ref{sec:paradox}) and figure caption. The figure is now presented as an organizing hypothesis, not a measurement result.

2. Pin Perspectives H2 method in the paper body itself: Semantic Scholar Academic Graph API; per-format fixed keyword set; time window 2020-01-01 to 2026-05-21; dedup on Semantic Scholar paper-ID; primary statistic Spearman's $\rho$ between per-format paper counts and AMSM PDA composite (PDA $\equiv$ mean of PCA and DDI); falsification threshold $\rho \ge 0$ at $\alpha=0.05$, one-sided. Protocol, query strings, and raw paper-IDs archived under `experiments/h2_misallocation/`.

3. Create `experiments/h2_misallocation/` with locked protocol so the pinned methodology has a single source of truth referenced from both the paper and the run scripts.

**Why**: A framework paper that runs its own predicted experiment to populate its own figure is only credible if (a) the figure does not pretend to be the result before the experiment exists, and (b) the experiment's method is specified ex ante so post-hoc methodological wiggle room is closed. Both Critical fixes are pre-conditions for the H2 run to count as a genuine test of the paper's hypothesis rather than a self-supporting exhibit.

---

## 2026-04-19 -- Repository restructure to umbrella multi-paper DDD-style layout

**Context**: Root had framework/ and perspectives/ as two sibling paper directories, plus shared/ (11 research notes) and TODO/review at top level. Each paper directory already had paper/main.tex + drafts/ + cover_letter.md internally -- a reasonable sub-structure.

**Decision**: Group both papers under papers/ (framework -> papers/framework, perspectives -> papers/perspectives). Preserve each paper's internal paper/drafts/cover_letter.md layout. Keep shared/ at top level (it is cross-paper, not external). Move TODO, review to planning/. Add literature/ for supplementary external reading notes.

**Why**: Matches the umbrella pattern established in emergence-paradox. The papers/<id>/ grouping signals "program with multiple papers" without flattening the existing per-paper sub-structure.
