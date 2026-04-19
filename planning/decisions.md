# Research Decisions Log

Records non-obvious choices with rationale. Append-only; don't rewrite history.

Format: `## YYYY-MM-DD -- <short title>` with **Context**, **Decision**, **Why**.

---

## 2026-04-19 -- Repository restructure to umbrella multi-paper DDD-style layout

**Context**: Root had framework/ and perspectives/ as two sibling paper directories, plus shared/ (11 research notes) and TODO/review at top level. Each paper directory already had paper/main.tex + drafts/ + cover_letter.md internally -- a reasonable sub-structure.

**Decision**: Group both papers under papers/ (framework -> papers/framework, perspectives -> papers/perspectives). Preserve each paper's internal paper/drafts/cover_letter.md layout. Keep shared/ at top level (it is cross-paper, not external). Move TODO, review to planning/. Add literature/ for supplementary external reading notes.

**Why**: Matches the umbrella pattern established in emergence-paradox. The papers/<id>/ grouping signals "program with multiple papers" without flattening the existing per-paper sub-structure.
