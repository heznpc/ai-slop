# Outline: "Beyond the Video Frame: The Production-Detection Asymmetry in Multi-Format AI Slop"

## Target Journal

**Communications of the ACM (CACM) -- Viewpoints Section**

### Justification

1. **Audience fit**: CACM Viewpoints reaches both CS researchers and technology practitioners. The paper's core argument -- that detection research is misallocated across content modalities -- requires an audience that understands both the technical detection landscape and the platform ecosystem. Nature and Science commentary sections are narrower (natural science focus) and would require framing AI slop primarily as a societal phenomenon rather than a computational/systems problem. CACM lets us do both.

2. **Practitioner perspective as strength**: CACM Viewpoints explicitly welcomes "practitioner-informed perspectives" and opinion pieces that challenge field assumptions. The author's independent developer background maps directly to the "trusted voice from the field" slot that CACM Viewpoints reserves.

3. **Format alignment**: CACM Viewpoints accepts 2,000-3,000 word commentary pieces with figures/tables. This matches the scope of the argument: tight enough to be provocative, long enough to present the production-detection asymmetry framework with data.

4. **Precedent**: CACM has published recent viewpoints on AI-generated content moderation, platform governance, and information ecosystem integrity. This paper sits directly in that conversation.

5. **Impact**: CACM Viewpoints articles are widely cited in both CS and policy communities. A well-placed piece here would set the agenda for detection research resource allocation.

**Alternative considered**: Nature Perspectives (higher prestige, but the argument is fundamentally about misallocated research effort in detection -- a CS problem. Nature would require diluting the technical specificity that makes the argument sharp.)

---

## Word Count Target

**2,500 words** (within CACM Viewpoints 2,000-3,000 range)

- Tight enough to enforce discipline on every sentence
- Long enough to include the production-detection asymmetry framework with data

---

## Section-by-Section Outline

### 1. Opening Hook (250 words)
**Title concept**: "Beyond the Video Frame: The Production-Detection Asymmetry in Multi-Format AI Slop"

**Opening**: The shutdown of OpenAI's Sora app on March 24, 2026 -- coming just months after it peaked at 3.3 million monthly downloads -- was widely celebrated as the climax of the AI slop backlash. But Sora's closure addresses only one format of AI slop: video. Meanwhile, the text-based and hybrid-format slop that saturates search results, product reviews, academic journals, and social media carousels continues to grow unchecked. Merriam-Webster named "slop" the 2025 Word of the Year based almost entirely on video content. The field's attention followed the dictionary.

**Key data points for hook**:
- Sora timeline: peak 3.3M downloads (Nov 2025) -> shutdown (Mar 2026)
- 52%+ of new English web content is AI-generated (Ahrefs, 2025)
- But existing research overwhelmingly studies video

**Tone**: Direct, provocative. "We are studying the wrong problem."

### 2. The Video-Centrism Problem (350 words)
**Argument**: Current AI slop research has a systematic bias toward video content.

**Evidence of bias**:
- Kapwing's 15,000-channel study: video-only (YouTube Shorts)
- PMC biomedical study (Jones et al., 2025): 1,082 educational videos
- Nature Scientific Reports (Moller et al., 2026): social media experiment focused on content production volume
- YouTube CEO declares slop reduction a 2026 priority -- video only
- Instagram, TikTok, Reddit responses: all video/visual focused
- Detection research: FaceForensics++, DFDC, ASVspoof -- all video/audio benchmarks

**The gap**:
- Shaib et al. (2025) "Measuring AI Slop in Text" is effectively the only direct study of text-based slop
- Zero published studies on AI-generated infographic/card news detection
- The 7Vs framework (Madsen & Puyt, 2026) and SLOP Anatomy framework both acknowledge multi-format existence but provide no format-differentiated analysis

**Practitioner observation**: As a developer who builds content systems, the author observes the gap daily -- automated blog pipelines produce orders of magnitude more content than video pipelines, at a fraction of the cost, with zero detection infrastructure.

### 3. The Multi-Format Landscape (400 words)
**Argument**: AI slop is a multi-format ecosystem. A brief map of the terrain with scale data.

**Format-by-format data table**:

| Format | Scale Indicator | Source |
|--------|----------------|--------|
| Web text/blogs | 74.2% of new pages contain AI content | Ahrefs (2025) |
| Search results | 17-19% of top-20 Google results are AI | Originality.AI |
| Academic papers | 22% of CS preprints, 13.5% of PubMed abstracts | Science; Bulletin of Atomic Scientists |
| Product reviews | 3% of Amazon bestseller reviews, 23.7% of Zillow agent reviews | Originality.AI |
| Books | 77% of Amazon "Success" genre, 9,000 titles/year from single Korean publisher | 2025 study; Korea Times |
| Music/audio | 75M tracks removed by Spotify in 12 months | Spotify (2025) |
| Video (Shorts) | 21-33% of new user recommendations | Kapwing (2025) |
| Social images | ~71% of social media images AI-generated | Multiple reports (2025) |
| News | 1,265 pink-slime sites (exceeding US dailies) | NewsGuard |
| Comments/bots | 51% of web traffic is bots | Imperva (2025) |
| Card news/carousels | No prevalence data exists | -- |

**Key point**: Text formats dominate by volume. Video gets the attention. This is a resource misallocation problem.

### 4. The Production-Detection Asymmetry (500 words) -- CORE CONTRIBUTION
**Argument**: The key variable the field should focus on is not the prevalence of AI slop per format, but the production-detection asymmetry -- the gap between how easy it is to produce AI slop in a given format and how hard it is to detect it.

**Framework**: Introduce the Production-Detection Asymmetry (PDA) concept.

**Production cost axis**:
- Near-zero: text (blogs, reviews, comments) -- ChatGPT + seconds
- Low: card news/infographics (Canva Bulk Create: 100 cards in 5 minutes)
- Low-medium: academic papers, books
- Medium: audio (TTS), images
- Medium-high: video (still requires rendering time, GPU)

**Detection accuracy axis** (cite specific numbers from research):
- Video: AUROC 85-98% (benchmark), 70-90% real-world, visual artifacts persist
- Audio: AUROC 94-99% (benchmark), acoustic signatures detectable
- Image: AUROC 88-97% (benchmark), but 15-35% accuracy drop on social media
- Text: AUROC 88-99% (self-reported) / 65-90% (independent), drops to **AUROC 0.27 under adversarial paraphrasing** (StealthRL, 2026)
- Card news/hybrid: **No evaluation exists** -- complete research void

**The asymmetry matrix** (Figure 1 concept):
- Highest PDA (most dangerous): text, card news, reviews -- cheap to produce, hard to detect
- Moderate PDA: images, academic papers
- Lowest PDA (most studied): video, audio -- more expensive to produce, more detectable

**Key finding**: Research resources are inversely correlated with the production-detection asymmetry. The most-studied formats (video) have the lowest asymmetry. The least-studied formats (text, hybrid) have the highest asymmetry.

### 5. The Card News Blind Spot (300 words)
**Argument**: Card news / image+text carousels represent a uniquely dangerous blind spot.

**Evidence**:
- Zero published detection research for AI-generated infographics/carousels
- Card news is a dominant format in Korean digital media (originated 2014, SBS)
- Instagram carousels achieve 6.90% engagement rate vs 3.31% for Reels (Buffer, 2026: 52M+ posts)
- Production cost: 100 cards in 5 minutes via ChatGPT + Canva Bulk Create
- Detection is structurally difficult: template-based (no visual artifacts), short text per card (low AI text detection accuracy), no temporal analysis (static images), multimodal analysis required but no tools exist
- Already weaponized: fake hotel reviews, fake travel recommendations, health misinformation via AI-generated card news documented in Korean media

**Why this matters globally**: While "card news" is a Korean term, the Instagram carousel format is global. The detection void applies everywhere.

### 6. Testable Hypotheses (250 words)
**Five specific hypotheses the field should test**:

**H1 (Format-Detection Inequality)**: Across standardized benchmarks, AI content detection accuracy follows the order: video > audio > image > text > image+text hybrid. The gap between video and text detection exceeds 30 percentage points under adversarial conditions.

**H2 (Research Misallocation)**: The number of published detection studies per format is inversely correlated with the production-detection asymmetry of that format. Formats with the highest asymmetry receive the least research attention.

**H3 (Cross-Format Spillover)**: AI slop in one format amplifies slop in others through content transformation pipelines (e.g., AI academic paper -> AI news article -> AI blog post -> AI social carousel). Measuring the spillover coefficient across formats would quantify information ecosystem contamination.

**H4 (Engagement-Detection Tradeoff)**: Formats with higher user engagement rates (carousels: 6.9%) and lower detection capability (hybrid: no tools) will exhibit higher sustained AI slop prevalence than formats with lower engagement and better detection (video).

**H5 (Adversarial Asymmetry)**: The effectiveness of adversarial evasion techniques varies dramatically by modality. Text-based evasion (paraphrasing) reduces detection AUROC by >60 percentage points, while video-based evasion achieves <20 percentage point reduction, due to the presence/absence of physical grounding constraints.

### 7. Implications for Platform Governance and Regulation (300 words)
**Argument**: Current regulatory frameworks (EU AI Act, Korean AI Basic Act) and platform policies are video-biased and must be reformed for multi-format coverage.

**Key points**:
- EU AI Act Article 50 transparency provisions: machine-readable marking requirement applies to all synthetic content but enforcement is focused on deepfakes (video/audio)
- Korean AI Basic Act (Jan 2026): labeling mandate covers "synthetic voice/image/video that is difficult to distinguish from reality" -- text is not explicitly covered
- Platform responses mirror the bias: YouTube "does this feel like AI slop?" feedback (video only); Instagram synthetic content penalty (image/video); Reddit passkey verification (bot accounts, not content)
- No platform has deployed multi-format slop detection at scale
- China is the only country with comprehensive multi-format enforcement (37,000 videos removed, 543,000 content pieces deleted after Sep 2025 labeling law) -- but this comes with authoritarian information control tradeoffs

**Recommendations**:
1. Detection research funding should be allocated proportional to the production-detection asymmetry, not proportional to media attention
2. Regulatory frameworks must explicitly cover text and hybrid formats
3. Platforms should develop multimodal detection pipelines rather than format-siloed approaches
4. The field needs a cross-format AI slop detection benchmark (analogous to FaceForensics++ for video)

### 8. Conclusion (150 words)
**Closing**: Sora's shutdown is not the end of AI slop -- it is barely the beginning of the real problem. The formats that matter most are the ones we are not studying. The production-detection asymmetry framework provides a compass for where detection research, platform governance, and regulatory attention should be directed. Every day we spend fixated on video is a day the text, carousel, and hybrid slop ecosystem grows unchecked.

---

## Key Figures/Tables

### Figure 1: The Production-Detection Asymmetry Matrix
- **Type**: 2x2 scatter plot with format labels
- **X-axis**: Production cost (log scale: seconds -> hours)
- **Y-axis**: Detection accuracy (AUROC or equivalent, 0-1.0)
- **Bubble size**: Estimated scale (volume of AI content in that format)
- **Color**: Research density (number of published detection studies)
- **Key insight**: The upper-left quadrant (low production cost, low detection accuracy) is where research investment should concentrate, but most current research clusters in the lower-right quadrant (higher production cost, higher detection accuracy)

### Table 1: Multi-Format AI Slop Landscape
- Format | Scale indicator | Production cost | Detection AUROC (benchmark) | Detection AUROC (adversarial) | Published detection studies | Research gap severity
- All 10 formats listed with data from research files

### Table 2 (optional, if space permits): Platform/Regulatory Response by Format
- Platform/Regulation | Video | Image | Text | Audio | Hybrid
- Shows the format-bias in current responses

---

## References Strategy

### Core citations (must include):
1. **Kapwing AI Slop Report** (2025) -- 15,000-channel video study, establishes video-centrism baseline
2. **Shaib et al.** (2025) "Measuring AI Slop in Text" -- only direct text slop study, arXiv:2509.19163
3. **Madsen & Puyt** (2026) "The 7Vs of AI Slop" -- conceptual framework, SSRN/AI & Society
4. **Jones et al.** (2025) PMC biomedical video study -- video-focused detection methodology
5. **Moller et al.** (2026) Nature Scientific Reports -- AI impact on social media
6. **StealthRL** (2026) -- adversarial text detection evasion, AUROC drop to 0.27
7. **KatFishNet** (ACL 2025) -- Korean text detection, AUROC +19.78%
8. **Ahrefs** (2025) -- 74.2% of new web pages contain AI content
9. **Originality.AI** -- multiple studies on AI in search, reviews, LinkedIn
10. **Imperva Bad Bot Report** (2025) -- 51% bot traffic
11. **Buffer** (2026) -- carousel vs Reels engagement rates (52M+ posts)
12. **NewsGuard** -- 1,265+ pink-slime news sites
13. **NPR** (2026) -- Sora shutdown and legacy
14. **Kommers et al.** (2026) -- "superficial competence, asymmetric effort, mass producibility"
15. **FTC** (2024) -- fake review regulation, $51,744 per violation

### Secondary citations (include if space):
- Retraction Watch: Hindawi 11,300 retractions
- Spotify: 75M track removals
- Korea Times: single publisher 9,000 books/year
- Pew Research: Korean AI concern at 16% (lowest globally)
- NYT (2026): 40% of children's recommendations are AI slop
- Instagram Mosseri: "authenticity is becoming infinitely reproducible"
- Casper et al. (FAccT 2024): black-box audit limitations

### Citation format:
- CACM Viewpoints uses numbered references in ACM format
- Target: 25-35 references (within CACM norms for viewpoints)
- Mix of peer-reviewed (60%), industry reports (25%), news (15%)

---

## Writing Notes

- Lead with the Sora shutdown as a shared cultural reference point, then pivot immediately to the blind spot
- Use the practitioner voice explicitly: "As a developer building content systems, I observe..."
- The production-detection asymmetry is the novel conceptual contribution -- devote the most space to it
- Keep the multi-format landscape section tight (table carries the weight, prose provides interpretation)
- The card news section serves as a concrete case study of the blind spot -- avoid making it feel Korea-specific by linking to the global carousel format
- Every claim has a citation from the research files -- no hand-waving
- End with urgency, not hedging
