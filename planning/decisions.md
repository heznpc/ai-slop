# Research Decisions Log

Records non-obvious choices with rationale. Append-only; don't rewrite history.

Format: `## YYYY-MM-DD -- <short title>` with **Context**, **Decision**, **Why**.

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
