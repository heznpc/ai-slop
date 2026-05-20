# Research Decisions Log

Records non-obvious choices with rationale. Append-only; don't rewrite history.

Format: `## YYYY-MM-DD -- <short title>` with **Context**, **Decision**, **Why**.

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
