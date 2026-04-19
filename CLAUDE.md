# CLAUDE.md -- Project Context for ai-slop-paper

## What This Is

Two-paper research program challenging the video-centric bias in AI-slop research.

- **Perspectives** (CACM Viewpoints, ~3,000 words): "Beyond the Video Frame: The Production-Detection Asymmetry in Multi-Format AI Slop"
- **Framework** (Big Data & Society, ~9,500 words): "Beyond Video Slop: A Multi-Format Framework for Understanding AI-Generated Content Pollution" -- introduces the AI-Generated Multi-Format Slop Model (AMSM)

## Repository layout (umbrella / multi-paper)

```
papers/                       Papers in the program (each keeps its own sub-DDD)
  perspectives/
    paper/main.tex
    drafts/                   draft_v1, draft_v2, draft_final, outline
    cover_letter.md           Submission-specific
  framework/
    paper/main.tex
    drafts/
    cover_letter.md
shared/                       Cross-paper research notes (11 files)
                              Literature + proposal drafts + factcheck audit
literature/                   Reading notes (supplementary to shared/)
planning/                     Program-level meta
  TODO.md, review.md, decisions.md
  drafts/
```

## Key Findings

- **Card news/carousel** scores highest threat (4.6/5) across AMSM dimensions -- zero detection research exists
- **Text slop** is more pervasive than video (74.2% of new web pages vs 21-33% of Shorts) but far less studied
- Research investment is **inversely correlated** with actual threat (Production-Detection Paradox)

## Conventions

- Commits: author and committer are `heznpc` only. No Co-Authored-By trailers.
- Each paper under `papers/` keeps its own sub-structure (paper/, drafts/, cover_letter).
- `shared/` holds cross-paper resources; don't duplicate into per-paper directories.
- Single source of truth per paper: `papers/<id>/paper/main.tex`.
