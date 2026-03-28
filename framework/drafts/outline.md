# Paper Outline: "Beyond Video Slop"

## Target Journal

**Recommended: Big Data & Society (SAGE)**

**Justification:**
- Open-access journal (Gold OA) indexed in SSCI (IF ~6.5), Scopus, and Web of Science
- Explicitly welcomes interdisciplinary work on digital culture, platform economies, and algorithmic governance
- Accepts conceptual/framework papers alongside empirical studies
- Published by SAGE with no requirement for traditional academic affiliation -- independent researchers regularly publish here
- Audience includes media scholars, platform researchers, STS scholars, and policymakers -- the exact readership this paper needs
- Recent publications on algorithmic amplification, content moderation, and generative AI demonstrate strong topical fit
- Turnaround time: typically 8-16 weeks for initial decision

**Alternatives considered:**
- First Monday: Open access, no APC, accepts non-traditional authors. However, lower impact and less visibility among platform/AI researchers.
- New Media & Society: Higher IF (~8.0) but more empirically oriented; a pure framework paper may face resistance.
- Internet Policy Review: Strong policy audience but narrower scope, primarily European regulatory focus.

---

## Word Count Target

**8,000-9,000 words** (excluding references and figure/table captions)

This sits in the sweet spot for Big Data & Society's "Original Research Article" format, which permits up to 10,000 words. The paper needs enough length to develop AMSM rigorously but should not pad with unnecessary elaboration.

---

## Section-by-Section Outline

### 1. Introduction (~1,000 words)

**Opening hook:** The shutdown of OpenAI's Sora app on March 24, 2026 -- the symbolic endpoint of the "generate anything" era -- and Merriam-Webster naming "slop" the 2025 word of the year.

**Problem statement:** The dominant discourse on AI slop is video-centric. The Kapwing report (2025), YouTube CEO's anti-slop declaration (2026), children's content contamination (NYT, 40% AI slop) -- all focus on video. But the phenomenon is far broader:
- 74.2% of new web pages contain AI-generated content (Ahrefs, 2025)
- 54%+ of LinkedIn long-form posts are AI-generated
- 1,265 pink-slime news sites now outnumber US daily newspapers
- 75 million spam tracks removed from Spotify in 12 months
- 11,300 academic papers retracted from Wiley/Hindawi alone
- Card news/carousel posts have zero detection research despite highest engagement rates

**The gap:** No existing framework compares AI slop across content formats on unified dimensions. Video-centrism in both research and regulation creates blind spots where the most damaging forms of slop proliferate undetected.

**Contribution:** This paper proposes the AI-Generated Multi-Format Slop Model (AMSM) -- a five-dimensional framework for analyzing slop across all content formats. It introduces two novel concepts: the Production-Detection Paradox and the Algorithm-Slop Co-evolution Model. It concludes with a concrete research agenda of testable hypotheses.

**Positionality statement:** The author is an independent developer with direct experience in content automation pipelines, giving practitioner insight into production economics that pure academic analysis often lacks.

---

### 2. Literature Review (~1,500 words)

**2.1 Definitional Work**
- 7Vs typology (Madsen & Puyt, 2025/2026): Volume, Velocity, Variety, Value, Verification, Visibility, Virality -- structural feature of contemporary media ecologies
- SLOP Anatomy (Internet Reference Services Quarterly, 2026): Shallow, Low-quality, Overgeneralized, Poorly-sourced -- academic publishing context
- Three prototypical properties (Kommers et al., 2025/2026): Superficial competence, Asymmetric effort, Mass producibility
- Vernacular definition (Willison): "mindlessly generated and thrust upon someone who didn't ask for it"
- Text-specific dimensions (Shaib et al., 2025): Information Quality, Information Utility, Style Quality

**2.2 Empirical Studies**
- Kapwing (2025): 15,000 channels, 278 slop channels, 63B views, $117M revenue, 21-33% of new user feeds
- PMC biomedical study (Jones et al., 2025): 1,082 videos, 5.3% slop, 78.7% concentrated in Shorts
- Nature experimental study (Moller et al., 2026): 680 participants, AI tools increase volume but decrease quality, negative spillover effect
- Raptive survey (2025): ~50% trust decline on AI detection, creator preference drops from 60% to 26%

**2.3 Detection Research**
- Video: FaceForensics++ (AUROC 87-98%), Sora 2 detection (85-93%), physical grounding violations
- Audio: ASVspoof 5 (98%+ accuracy, EER 0.0013), Resemble AI DETECT-2B (94-98%)
- Text: GPTZero (88-95% baseline, 60-70% after paraphrase), StealthRL attack (AUROC drops to 0.27), 61.3% false positive for ESL writers (Stanford HAI)
- KatFishNet (ACL 2025): Korean text detection, +19.78% AUROC over baselines
- Image+Text hybrid: NO detection research exists -- complete gap

**2.4 Platform and Regulatory Responses**
- YouTube: "Does this feel like AI slop?" feedback (2026.03), CEO priority declaration (2026.01)
- Instagram: synthetic content algorithm penalty (2026.01)
- Reddit: human verification via passkeys (2026.03)
- Sora shutdown (2026.03.24), Disney $1B deal collapse
- China AI labeling law (2025.09): strongest enforcement (37,000 videos purged)
- EU AI Act Art.50 transparency (2026.08 expected)
- Korea AI Basic Act (2026.01): labeling mandate + 5x punitive damages

**2.5 Identifying the Gap**
Three systematic blind spots:
1. Video-centrism: The vast majority of slop research and platform action targets video, despite text formats having higher penetration rates
2. No cross-format comparison: Each format is studied in isolation; no framework unifies them
3. Hybrid-format neglect: Card news, infographics, and carousel posts are completely unstudied despite dominating engagement metrics

---

### 3. The AMSM Framework (~2,000 words) -- CORE CONTRIBUTION

**3.1 Framework Design Rationale**
- Extends 7Vs (Madsen & Puyt) from description to operationalization
- Format-agnostic: dimensions apply equally to video, text, audio, image, and hybrid formats
- Practitioner-informed: production cost estimates derived from direct experience with automation tools

**3.2 Five Dimensions**

**(a) Production Cost Asymmetry (PCA)**
- Definition: The ratio of cost/effort to produce slop vs. equivalent human-made content
- Operationalization: Time (seconds to hours), monetary cost, expertise required
- Scale: 1 (near-zero marginal cost) to 5 (significant compute/expertise)
- Format comparison with evidence for each rating

**(b) Detection Difficulty Index (DDI)**
- Definition: How resistant is this format's slop to identification by both automated tools and human judgment?
- Operationalization: Best available AUROC, false positive rates, adversarial robustness
- Scale: 1 (easily detected) to 5 (virtually undetectable)
- Key insight: text under adversarial attack drops to AUROC 0.27; hybrid formats have never been evaluated

**(c) Ecosystem Damage Potential (EDP)**
- Definition: The downstream harm inflicted by slop in this format
- Operationalization: Categories of harm (financial, epistemic, democratic, health, developmental)
- Scale: 1 (attention waste) to 5 (direct material/epistemic harm)
- Argument that video slop is primarily an attention/time drain (EDP ~2) while fake reviews cause financial harm (EDP ~4) and academic slop threatens knowledge integrity (EDP ~5)

**(d) Algorithmic Amplification Susceptibility (AAS)**
- Definition: How much does the dominant platform algorithm for this format boost slop?
- Operationalization: Engagement rate differentials, cold-start exposure rates, algorithmic feed dependence
- Scale: 1 (low amplification) to 5 (extreme amplification)
- Evidence: carousel/card news achieves ~10% engagement (highest of any format), Shorts driven by algorithmic feed, blog/SEO dependent on search algorithm

**(e) Regulatory Coverage Gap (RCG)**
- Definition: How well do current laws and platform policies address slop in this format?
- Operationalization: Existence of specific regulations, enforcement history, coverage breadth
- Scale: 1 (well-covered) to 5 (no coverage)
- Comparative analysis across China, EU, Korea, US for each format

**3.3 The AMSM Comparison Table (Table 1 -- centerpiece)**

Full matrix: rows = 8 content formats (Video/Shorts, Text/Blog/SEO, Card News/Carousel, Fake Reviews, Academic Papers, News Articles, Audio/Podcast, AI Books); columns = 5 AMSM dimensions + composite threat score.

Each cell contains a numerical rating (1-5) with a brief evidence note. Composite score = weighted average (weights discussed).

**3.4 Key Findings from the AMSM Matrix**
- Formats with highest composite threat scores are NOT the most-studied ones
- Text-based formats cluster in high-PCA, high-DDI, high-EDP territory
- Card news occupies a unique position: low PCA, unknown DDI, high AAS, high RCG
- Video occupies the most favorable position from a defense perspective: moderate PCA, moderate DDI, low-to-moderate EDP

---

### 4. The Production-Detection Paradox (~1,000 words)

**4.1 Defining the Paradox**
Research investment is inversely correlated with the actual threat level:
- Video: most studied, most detectable, moderate damage -- gets the most attention
- Text: least studied (as slop specifically), hardest to detect under attack, most pervasive -- gets least attention
- Card news/hybrid: completely unstudied, detection never evaluated, highest engagement amplification -- invisible to researchers

**4.2 Quantifying the Paradox**
- Research density metric: approximate count of academic papers focused on detection in each modality
- Threat metric: composite AMSM score
- Demonstrate the inverse correlation with Figure 1

**4.3 Explaining the Paradox**
Three hypotheses for why this paradox exists:
1. Visibility bias: video slop is visually dramatic and easy to demonstrate in media coverage
2. Methodological path dependence: deepfake detection research predates the slop era, creating established benchmarks and datasets
3. Platform disclosure asymmetry: platforms publish video data more readily than text/engagement data

**4.4 Implications**
- Research funding and attention should be reallocated toward high-DDI, high-EDP formats
- Detection researchers should prioritize adversarial-robust text detection and hybrid-format detection
- Policymakers should not equate "most visible" with "most harmful"

**Figure 1: Production-Detection Paradox Visualization**
- Scatter plot: X-axis = Detection Difficulty (DDI), Y-axis = Research Investment (paper count)
- Each point = one content format, sized by Ecosystem Damage Potential
- Expected pattern: negative correlation -- high DDI formats have low research investment
- Visual emphasis on the "danger zone" (upper-left quadrant: high DDI, low research)

---

### 5. The Algorithm-Slop Co-evolution Model (~1,000 words)

**5.1 Beyond Distribution: Co-evolution**
Algorithms do not merely distribute slop -- they co-evolve with it. Drawing on:
- Attention economy theory (Simon, 1971; Wu, 2017)
- Gresham's Law 2.0 (Grimmelmann): bad content drives out good
- Platform capitalism (Madsen & Puyt, 2026): monetization programs reward volume over value
- Feedback loop evidence (arXiv:2207.01616; Baumann et al., 2026; Lasser et al., 2025)

**5.2 The Co-evolution Feedback Loop (Figure 2)**
Four-stage cycle:
1. **Production**: Near-zero marginal cost enables mass slop production
2. **Algorithmic Selection**: Engagement-optimized algorithms systematically favor slop (high CTR, curiosity gap, completion rate)
3. **Consumption Reinforcement**: User engagement with slop trains the algorithm to recommend more slop (rapid reinforcement within first 200 videos -- Baumann et al.)
4. **Economic Validation**: Ad revenue flows to slop channels ($117M/year globally, ~170B KRW in Korea) reinforcing production incentives
5. **Return to Stage 1**: Increased production at larger scale

**5.3 Natural Experiments Testing the Model**
- Instagram synthetic content penalty (2026.01): Did breaking the loop at Stage 2 reduce slop?
- YouTube "AI slop?" feedback (2026.03): Does user input disrupt Stage 3?
- Sora shutdown (2026.03.24): Does removing a production tool disrupt Stage 1?
- Korea AI labeling mandate (2026.01): Does transparency regulation disrupt Stage 3/4?
- YouTube channel deletions (2025-2026): Does enforcement disrupt Stage 4?

**5.4 Testable Hypotheses**
- H1: Engagement-optimized algorithms produce a measurable bias toward AI slop content, all else being equal (sock puppet audit methodology)
- H2: Platform interventions targeting one stage of the co-evolution cycle produce temporary disruption followed by adaptation (regulatory adaptation theory -- Lessig, 2006)
- H3: The co-evolution cycle accelerates faster in formats with lower Production Cost Asymmetry (text > video)

**Figure 2: Algorithm-Slop Co-evolution Feedback Loop Diagram**
- Circular diagram with 4 stages, arrows showing reinforcement
- Annotated with natural experiments that test disruption at each stage
- Side annotation showing acceleration gradient by format (text fastest, video slowest)

---

### 6. Research Agenda (~1,500 words)

**6.1 Priority Hypotheses with Methodologies**

| # | Hypothesis | Format Focus | Method | Feasibility | Impact |
|---|-----------|-------------|--------|-------------|--------|
| H1 | Text slop penetration exceeds video slop penetration in absolute volume | Text vs. Video | Web crawl + AI detection tool comparison | High | High |
| H2 | Detection accuracy for text drops below chance under adversarial conditions while video detection remains above 70% | Text, Video | Benchmark evaluation with StealthRL-style attacks | High | Very High |
| H3 | Card news/carousel formats have ZERO existing detection capability | Hybrid | Build and test first hybrid detection pipeline | Medium | Very High |
| H4 | AI slop engagement metrics differ systematically from human content metrics across formats | All | Platform data analysis, controlled upload experiments | Medium | High |
| H5 | Platform algorithm interventions produce <6 month disruption before slop producers adapt | Video, Image | DiD analysis of Instagram penalty, YouTube feedback | High | High |
| H6 | The economic displacement (Gresham's Law 2.0) effect is measurable in creator revenue data | Video, Text | Social Blade data + creator surveys | Medium | Very High |
| H7 | Cross-format spillover exists: academic AI papers become AI news articles become AI blog posts | Text (multi) | Citation/content tracing analysis | Medium | High |

**6.2 What Independent Researchers CAN Do**
- Algorithm audits via sock puppet methodology (no platform cooperation needed)
- Web crawl-based text slop prevalence studies
- Cross-tool detection benchmarking
- Card news detection gap documentation
- Creator economy impact surveys
- Natural experiment analysis (publicly observable events)

**6.3 What Requires Platform Cooperation**
- Internal engagement metric comparison (AI vs. human content)
- Algorithmic recommendation data (true exposure rates)
- Content moderation outcome data (removal rates by format)
- A/B testing of intervention effectiveness

**6.4 Critical Format-Specific Gaps**
1. **Card news/infographic**: No detection research, no prevalence data, no quality benchmark
2. **Fake reviews (non-English)**: Korean/Asian language detection tools absent
3. **Academic papers (Korean KCI)**: No tortured phrase analysis or LLM marker tracking
4. **Cross-format contamination**: The pipeline from AI paper to AI news to AI blog is entirely untracked

**Table 2: Research Agenda Summary**
Columns: Hypothesis, Format, Method, Feasibility (High/Med/Low), Impact (High/Med/Low), Requires Platform Data (Yes/No), Priority Rank

---

### 7. Implications (~500 words)

**7.1 For Platforms**
- Content moderation must become format-aware; video-focused moderation misses the majority of slop
- Engagement optimization creates structural incentives for slop; alternative objective functions needed
- Cold-start algorithms are particularly vulnerable and should be audited specifically

**7.2 For Regulators**
- AI labeling mandates (Korea AI Basic Act, EU AI Act Art.50) are disproportionately focused on visual/video content
- Text-based slop (reviews, blog posts, news) falls through regulatory gaps
- Format-specific enforcement mechanisms needed: FTC fake review rules are a model but enforcement is weak
- Detection tool accuracy claims should be independently verified before regulatory reliance

**7.3 For Researchers**
- Stop studying only Shorts: text and hybrid formats deserve equal or greater attention
- Cross-format comparison studies are urgently needed
- Adversarial robustness should be standard in detection evaluations
- Non-English and non-video detection benchmarks are critically absent

**7.4 For the Public**
- Media literacy must expand beyond deepfake video awareness to include AI text, reviews, and card news
- "Your AI slop bores me" is only the beginning -- most slop is invisible, not boring

---

### 8. Conclusion (~500 words)

- Recap of AMSM framework and its key findings
- The Production-Detection Paradox as a call to action for research reallocation
- The Algorithm-Slop Co-evolution Model as a lens for understanding platform dynamics
- The urgency of the moment: 2025-2026 offers unprecedented natural experiments
- Closing: AI slop is not a video problem. It is an information ecosystem problem. The framework proposed here offers a map of the full terrain.

---

## Key Figures and Tables

| Item | Type | Content | Purpose |
|------|------|---------|---------|
| Table 1 | Table | AMSM Multi-Format Comparison Matrix (8 formats x 5 dimensions + composite) | Centerpiece of the paper |
| Figure 1 | Scatter plot | Production-Detection Paradox (DDI vs. Research Investment, sized by EDP) | Visualize the inverse correlation |
| Figure 2 | Circular diagram | Algorithm-Slop Co-evolution Feedback Loop (4 stages + natural experiments) | Conceptualize the dynamic model |
| Table 2 | Table | Research Agenda (7 hypotheses, methods, feasibility, impact) | Actionable takeaway |

---

## References Strategy

**Core citations (~25-30 sources):**
- All 8 key papers from the deep analysis (7Vs, Shaib et al., PMC biomedical, Nature experimental, Academic publishing SLOP, Kapwing report, MINT Lab Kommers et al., KR Institute)
- Detection research: FaceForensics++, ASVspoof, KatFishNet, StealthRL/adversarial paraphrase NeurIPS 2025
- Platform economics: Simon (1971) attention economy, Grimmelmann Gresham's Law 2.0, Lessig (2006) regulatory adaptation
- Empirical data: Originality.AI studies, Ahrefs analysis, NewsGuard, Retraction Watch, Imperva bot report
- Cultural/theoretical: Hofstede cultural dimensions, Petty & Cacioppo ELM, Postman media ecology
- News/policy sources: NPR Sora, CNN anti-AI marketing, FTC fake review rule, Korea AI Basic Act

**Citation format:** Author-year in-text (Author, Year), full reference list at end following APA 7th or SAGE house style.

**Strategy for non-peer-reviewed sources:**
- Industry reports (Kapwing, Originality.AI, Imperva) are cited as industry evidence with appropriate caveats about methodological limitations
- News sources (NPR, CNN, NYT) are cited for specific events/dates, not for analytical claims
- Platform announcements are cited directly (YouTube CEO statement, Instagram algorithm change)

---

## Writing Notes

- Tone: Rigorous but accessible. This should read like a manifesto for a new research direction.
- The practitioner perspective is a strength: production cost estimates and automation pipeline knowledge come from direct experience.
- AMSM table is the star -- it must be detailed, evidence-based, and visually clear.
- Every claim about a format's rating must be supported by specific data from the research base.
- Acknowledge limitations of the framework (ratings are partially subjective, data quality varies, evolving landscape).
