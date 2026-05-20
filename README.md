Research Program: 5 (Synthetic Content and Measurement)
Status: Submission-ready drafts — CACM Viewpoints (Perspectives, ~3,000 words) + Big Data & Society (Framework, ~9,500 words)
Relationship to other work: Anchor for Program 5; companion papers include ai-bubble, emergence-paradox, aichemist, babel

---

# Beyond Video Slop: Multi-Format AI Content Pollution

**Thesis.** Public and scholarly discourse on AI "slop" is overwhelmingly video-centric — Sora's shutdown, YouTube's anti-slop campaign, deepfake benchmarks — yet video is neither the most pervasive nor the most damaging format. As of early 2026, 74.2% of new web pages contain AI-generated text and card-news/carousel formats have zero published detection research, while only 21–33% of YouTube Shorts to new users are AI slop. Research investment is *inversely* correlated with actual threat: the most-studied format (video) is the most detectable; the least-studied formats (text, hybrid card news) are the hardest to detect and cause the greatest ecosystem damage. This umbrella program names that gap the **Production–Detection Paradox** and introduces the **AI-Generated Multi-Format Slop Model (AMSM)** to systematize cross-format analysis.

## Papers

### Paper A — Perspectives (CACM Viewpoints, ~3,000 words)
**"Beyond the Video Frame: The Production-Detection Asymmetry in Multi-Format AI Slop"**
- Core concept: Production–Detection Asymmetry (PDA)
- Argument: video-centric detection benchmarks (FaceForensics++, DFDC, ASVspoof) have created a gravitational pull that concentrates funding on the format where detection already works
- 5 testable hypotheses

### Paper B — Framework (Big Data & Society, ~9,500 words)
**"Beyond Video Slop: A Multi-Format Framework for Understanding AI-Generated Content Pollution"**
- Core contribution: AI-Generated Multi-Format Slop Model (AMSM)
- 5 dimensions: Production Cost Asymmetry (PCA), Detection Difficulty Index (DDI), Ecosystem Damage Potential (EDP), Algorithmic Amplification Susceptibility (AAS), Regulatory Coverage Gap (RCG)
- Algorithm–Slop Co-evolution Model (four-stage feedback loop)
- 7 testable hypotheses with prioritized research agenda

## Currently implemented

- Two complete LaTeX drafts: `papers/perspectives/paper/main.tex`, `papers/framework/paper/main.tex`
- Per-paper draft history under `papers/<id>/drafts/`
- Per-paper submission cover letters under `papers/<id>/cover_letter.md`
- 11 cross-paper research notes in `shared/` (comparative country data, factcheck audit, four research-direction proposals)
- Decisions log: `planning/decisions.md`

## Planned

- Submission to CACM Viewpoints (Perspectives) and Big Data & Society (Framework)
- Five experiment tracks listed in `planning/TODO.md`: multi-format detection benchmark, platform algorithm amplification study, cross-format conversion detection loss, Korean card-news detection model, regulatory effectiveness comparison (CN/EU/KR)

## Design intent

- **Two papers, one program.** A short Viewpoints piece names the problem so the community sees it; a full framework paper gives the analytical machinery. The split is deliberate — Perspectives points to the Framework via footnote, it is not a substitute.
- **Umbrella DDD-style layout** (`papers/<id>/paper/{drafts,cover_letter}` + top-level `shared/`, `literature/`, `planning/`) follows the pattern established in `emergence-paradox`. Each paper keeps its sub-structure; cross-paper material lives once in `shared/`.
- **Single source of truth per paper:** `papers/<id>/paper/main.tex`. Drafts are history, not parallel forks.

## Non-goals

- No detection model is built in this repo. The Framework paper's contribution is a measurement framework and research agenda, not a classifier.
- Not a survey paper. Existing literature is cited only where it bears on the asymmetry claim.
- No video-only treatment. The whole point of the program is that video-centric scoping is the problem.

## Key findings

- Card news / carousel scores the highest threat (4.6/5) across AMSM dimensions — and has zero published detection research
- Text slop is more pervasive than video (74.2% of new web pages vs 21–33% of Shorts) but far less studied
- Research investment is inversely correlated with actual threat → Production–Detection Paradox
- 2025–2026 provides six natural experiments (regulatory rollouts, platform policy shifts) for testing the Algorithm–Slop Co-evolution Model

## Repository layout

```
papers/
  perspectives/           Paper A — CACM Viewpoints
    paper/main.tex
    drafts/               draft_v1, draft_v2, draft_final, outline
    cover_letter.md
  framework/              Paper B — Big Data & Society
    paper/main.tex
    drafts/
    cover_letter.md
shared/                   Cross-paper research notes (11 files)
literature/               Supplementary external reading notes
planning/                 TODO.md, review.md, decisions.md, drafts/
```

## License

All rights reserved. Pre-publication research.
