# Beyond the Video Frame: The Production-Detection Asymmetry in Multi-Format AI Slop

---

**[Perspectives/Commentary -- submitted to Communications of the ACM, Viewpoints]**

---

On March 24, 2026, OpenAI shut down Sora, the AI video generator that had peaked at 3.3 million monthly downloads just four months earlier [1]. The closure was widely framed as the climax of the AI slop backlash -- the definitive moment when the industry acknowledged that mass-produced, low-quality AI content had gone too far. Merriam-Webster had named "slop" its 2025 Word of the Year [2]. YouTube's CEO declared slop reduction a top priority [3]. Instagram's head announced intent to prioritize authentic content over synthetic material [4]. The message seemed clear: the problem was being addressed.

It was not. Sora's shutdown addressed one format of AI slop -- video -- while the formats that are more pervasive, harder to detect, and more damaging to the information ecosystem continued to grow unchecked. As of early 2026, 74.2% of new web pages contain some AI-generated text [5], and 22.5% of sentences in computer science paper abstracts show evidence of LLM modification [6]. The number of partisan-funded "pink slime" news websites (1,265), alongside a separate 3,006 AI content farm sites, now exceeds the number of actual US daily newspapers (1,213) [7]. Bots generate 51% of all internet traffic [8]. None of this is video.

The field has a video-centrism problem. And that problem is hiding the real crisis.

## The Video-Centrism of AI Slop Research

The most-cited empirical work on AI slop is overwhelmingly video-focused. Kapwing's landmark study analyzed 15,000 trending YouTube channels and found that 21-33% of Shorts recommended to new users were AI slop [9]. Jones et al. screened 1,082 biomedical educational videos on YouTube and TikTok, finding 5.3% were AI slop, with 78.7% concentrated in Shorts [10]. Moller et al.'s Nature Scientific Reports experiment examined how AI tools affect social media discussions, finding that AI-assisted content increases volume while decreasing perceived quality [11]. The 7Vs framework proposed by Madsen and Puyt -- Volume, Velocity, Variety, Value, Verification, Visibility, Virality -- acknowledges that AI slop spans multiple formats, but the empirical referents are overwhelmingly video and social media [12].

Detection research follows the same pattern. The field's major benchmarks -- FaceForensics++, the Deepfake Detection Challenge, ASVspoof -- are all built around video and audio [13]. These benchmarks have driven real progress: deepfake video detection now achieves AUROC of 91-97% in-domain, degrading to approximately 70-87% cross-dataset (DFDC) [13]. But they have also created a gravitational pull that concentrates research talent, funding, and attention on formats where detection is already comparatively effective.

Meanwhile, text-based AI slop -- the format with the largest scale and lowest detection reliability -- has received almost no direct research attention. Shaib et al.'s "Measuring AI Slop in Text" (2025) is effectively the only published study that directly addresses text slop as a phenomenon, proposing a taxonomy of Information Quality, Information Utility, and Style Quality dimensions through expert interviews [14]. For image-text hybrid content such as infographics and social media carousels, the situation is starker: no published detection study exists at all. Searches of ACM Digital Library, IEEE Xplore, arXiv, and Google Scholar as of March 2026 returned no results for AI-generated carousel or card news detection [15].

As a developer who builds content pipelines, this asymmetry is visible daily. An automated blog generation system can produce hundreds of SEO-optimized posts per day at the cost of a $20/month ChatGPT subscription. A Canva Bulk Create workflow can output 100 social media card-news graphics in five minutes [16]. These pipelines operate at industrial scale with zero detection infrastructure. Video generation, by contrast, still requires meaningful compute resources and produces artifacts -- temporal inconsistencies, physics violations, anatomical errors -- that detection systems can exploit.

## The Multi-Format Landscape

AI slop is not a single-format problem. It is a multi-format ecosystem where each content type has its own production economics, detection characteristics, and information ecosystem impacts. Table 1 maps the terrain.

**Table 1. The Multi-Format AI Slop Landscape (2025-2026)**

| Format | Scale Indicator | Source |
|--------|----------------|--------|
| Web text / blogs | 74.2% of new pages contain AI content; 17-19% of Google top-20 results | Ahrefs [5]; Originality.AI [17] |
| Academic papers | 22.5% of CS abstract sentences LLM-modified; 13.5% of PubMed abstracts; 11,300 retractions at Wiley/Hindawi | Nature Human Behaviour [6]; Retraction Watch [18] |
| Product reviews | 3% of Amazon bestseller reviews; FTC $51,744/violation penalty | Originality.AI [19]; FTC [20] |
| News websites | 1,265 partisan-funded pink-slime sites + 3,006 AI content farm sites exceeding US dailies | NewsGuard [7] |
| Books | 77% of Amazon "Success" genre; 9,000 titles/year from single Korean publisher | [21]; Korea Times [22] |
| Music / audio | 75M "spammy tracks" removed by Spotify in 12 months | Spotify [23] |
| Video (Shorts) | 21-33% of new-user recommendations; ~40% of children's recommendations | Kapwing [9]; NYT [24] |
| Comments / bots | 51% of all web traffic; 12-15% of YouTube comments | Imperva [8]; Factcheck.by [25] |
| Card news / carousels | No prevalence data exists | -- |

Two patterns emerge. First, text-based formats dominate by volume. The 74.2% AI content rate for new web pages [5] dwarfs the 5-33% range reported for video. Second, the formats with the largest scale and the most severe information ecosystem consequences -- search results, academic literature, product reviews -- have received the least detection research attention. This is not a gap in our knowledge. It is a systematic misallocation of research resources.

## The Production-Detection Asymmetry

I propose that the key variable the field should organize around is not the prevalence of AI slop per format, but the **production-detection asymmetry (PDA)** -- the gap between how cheaply a format can be produced and how reliably it can be detected.

For video, production cost is moderate (rendering time, GPU resources, $20-200/month for tools) and detection is relatively effective (AUROC 91-97% in-domain, approximately 70-87% cross-dataset, with exploitable physical artifacts) [13]. For text, production cost approaches zero (a single API call, seconds of generation time) while detection accuracy is fragile: independent evaluations put real-world accuracy at 65-90%, and adversarial paraphrasing reduces AUROC catastrophically. StealthRL, a 2026 reinforcement-learning attack framework, reduces text detector AUROC from 0.79 to 0.43 and achieves a 97.6% attack success rate -- and these attacks transfer to detectors not seen during training [26]. The NeurIPS 2025 adversarial paraphrasing framework reduces true positive rates at 1% false-positive rate by an average of 87.88% [27]. Text detection faces a structural vulnerability that video detection does not: text has no physical grounding. There are no laws of physics to violate, no anatomical constraints to break. Detection relies entirely on statistical distribution differences that converge toward human text as language models improve.

For image-text hybrids -- carousels, infographics, card news -- the asymmetry is at its most extreme. Production is trivial: ChatGPT generates the text, Canva renders the design, Bulk Create scales it to hundreds of units in minutes [16]. Detection has never been evaluated. Existing image detectors ignore embedded text; text detectors cannot process images; no multimodal detection pipeline has been built or benchmarked for this format [15]. The detection accuracy for AI-generated carousels is, at present, entirely unknown.

Figure 1 (concept) plots this asymmetry. The x-axis represents production cost (log scale, from seconds to hours). The y-axis represents detection reliability (AUROC, from 0 to 1.0). Bubble size encodes estimated content volume. The result is striking: the upper-left quadrant -- low production cost, low detection reliability, large volume -- is populated by text, reviews, and hybrid formats. The lower-right quadrant -- higher production cost, higher detection reliability -- is where video sits. Research investment is concentrated in the lower-right. The upper-left is almost empty of published work.

**This is the fundamental misallocation.** We are spending our detection research budget on the formats where detection already works best, while the formats where detection is weakest and production is cheapest receive almost nothing.

One might argue that video-centrism is justified: video is the most consumed format, children are disproportionately affected, and deepfakes pose the most immediate threat to public trust. These points have merit. But they do not justify the near-total neglect of text and hybrid formats. The question is not whether video detection matters -- it does -- but whether the current allocation, which directs the vast majority of resources to the format with the strongest existing defenses, represents a rational response to the actual threat landscape.

## The Card News Blind Spot

The Instagram carousel -- the highest-engagement format on the platform at 6.90% versus 3.31% for Reels (Buffer, 2026) [28] -- has zero detection research. The image-text hybrid format deserves particular attention because it combines the worst of both worlds: near-zero production cost, high engagement, and zero detection infrastructure. In South Korea, a culturally distinct variant called "card news" originated in 2014 as a journalistic innovation [29], and AI-generated carousels have already been documented spreading fabricated hotel reviews, non-existent travel destinations, and unverified health claims [16].

This is not a Korea-specific problem. Carousels are the highest-engagement format on Instagram globally, based on Buffer's analysis of over 52 million posts [28]. They are also the format with no detection research whatsoever.

Why is carousel detection structurally difficult? Five reasons. First, carousels use platform-native templates (Canva, Piktochart), making AI-generated and human-generated outputs visually identical. Second, each card contains only 3-5 lines of text -- too short for reliable AI text detection, where accuracy drops sharply on short passages [14]. Third, static images cannot be analyzed for temporal inconsistencies the way video frames can. Fourth, multimodal analysis (evaluating image-text consistency) is required but no tools exist for this purpose in the detection context. Fifth, C2PA watermarking metadata is stripped trivially via screenshot or re-upload.

This format is not a niche concern. It is the highest-engagement content type on the world's largest image-sharing platform, with no detection capability at any level -- automated, platform-level, or regulatory.

## Hypotheses for the Field

The production-detection asymmetry framework generates specific, testable predictions that the field should prioritize:

**H1 (Format-Detection Hierarchy):** Under standardized adversarial evaluation, AI content detection accuracy follows the order video > audio > image > text > image-text hybrid. The gap between video and text detection under adversarial conditions exceeds 30 AUROC percentage points.

**H2 (Research Misallocation):** The number of published detection studies per format is inversely correlated with the production-detection asymmetry of that format. A bibliometric analysis comparing detection paper counts against PDA scores would quantify the magnitude of the misallocation.

**H3 (Cross-Format Contamination):** AI slop propagates across formats through content transformation pipelines -- AI-generated academic paper becomes AI-generated news article becomes AI-generated blog post becomes AI-generated social carousel. Each transformation reduces the statistical signal available to format-specific detectors. Measuring this cross-format spillover coefficient is essential for understanding information ecosystem contamination.

**H4 (Engagement-Detection Inversion):** Formats with higher user engagement rates and lower detection capability will exhibit higher sustained AI slop prevalence than formats with lower engagement and better detection. Carousel-format slop (6.9% engagement, no detection) will persist longer and reach more users than video-format slop (3.3% engagement, 85%+ detection) on the same platform.

**H5 (Adversarial Asymmetry):** The effectiveness of adversarial evasion varies dramatically by modality due to the presence or absence of physical grounding constraints. Text-based evasion (paraphrasing) achieves AUROC reductions exceeding 35 percentage points [26], while video-based evasion is constrained by physics simulation requirements and achieves substantially smaller reductions.

## Implications for Governance and Regulation

Current regulatory frameworks reproduce the video-centrism of the research community. The EU AI Act's Article 50 transparency provisions require machine-readable marking of synthetic content, but enforcement attention and compliance guidance focus overwhelmingly on deepfakes -- a video/audio phenomenon [30]. South Korea's AI Basic Act (effective January 2026) mandates labeling for "synthetic voice, image, and video that is difficult to distinguish from reality" -- text is not explicitly covered [31]. Platform responses mirror this bias: YouTube's "does this feel like AI slop?" feedback system targets video [3]; Instagram's synthetic content penalty targets images and video [4]; Reddit's passkey verification targets bot accounts rather than AI-generated content [32].

China stands alone in enforcing multi-format AI content labeling, having deleted 37,000 non-compliant videos, suspended 3,400 accounts, and applied labels to 600,000 videos since its September 2025 labeling law took effect [33]. Whatever its governance tradeoffs, China's approach demonstrates that multi-format enforcement is technically feasible.

Three reforms are needed. First, detection research funding should be allocated proportional to the production-detection asymmetry, not proportional to current research volume or media attention. The upper-left quadrant of the PDA matrix -- text, hybrid formats, reviews -- needs an order-of-magnitude increase in research investment. Second, regulatory frameworks must explicitly cover text-based and hybrid-format AI content. A labeling mandate that covers video but not the blog posts, product reviews, and social carousels where most AI slop lives is performative, not protective. Third, the field needs a cross-format AI slop detection benchmark -- analogous to what FaceForensics++ did for video -- that enables systematic comparison of detection performance across modalities and drives research toward the formats where detection is weakest.

## Conclusion

Sora's shutdown was not the end of the AI slop crisis. It was a distraction from the real one. The formats that matter most -- text, hybrid carousels, product reviews, academic papers -- are the ones we are not studying, not detecting, and not regulating. The production-detection asymmetry tells us exactly where to look: wherever production is cheapest and detection is weakest, that is where slop accumulates fastest and causes the most damage.

Every month the field spends fixated on video is a month the text and hybrid slop ecosystem grows without scrutiny. The data is clear. The framework is ready. The only question is whether the research community will redirect its attention before the information ecosystem is saturated beyond recovery.

---

## References

[1] NPR. "OpenAI pulls the plug on Sora." March 25, 2026.

[2] Merriam-Webster. "Word of the Year 2025: Slop." December 2025.

[3] Dexerto. "YouTube is asking users if videos feel like AI slop." March 2026.

[4] Clippie.AI. "Instagram Algorithm Updates 2026." January 2026; Musically. "Instagram boss: authenticity is becoming infinitely reproducible." January 2026.

[5] Graphite. Analysis of ~65,000 English articles (52% show AI involvement). 2025; Ahrefs. Analysis of 900,000 newly published web pages. April 2025. (74.2% contain AI content; pure AI 2.5%, human-AI mix 71.7%).

[6] Liang, W. et al. "Monitoring AI-Modified Content at Scale." Nature Human Behaviour, 2025. (22.5% of sentences in CS paper abstracts show evidence of LLM modification); Bao, Z. et al. "AI-generated text in PubMed abstracts." Science Advances, 2025. (1/7 of biomedical abstracts).

[7] NewsGuard. Unreliable news sites tracking. 2024-2025. (1,265 partisan-funded "pink slime" sites categorized separately from 3,006 AI content farm sites.)

[8] Imperva. "2025 Bad Bot Report." 2025. (51% of web traffic is automated).

[9] Kapwing. "AI Slop Report: The Global Rise of Low-Quality AI Videos." October 2025.

[10] Jones, E.M. et al. "AI-Generated 'Slop' in Online Biomedical Science Educational Videos." JMIR Medical Education 11, e80084. 2025.

[11] Moller, A.G. et al. "The impact of generative AI on social media: An Experimental Study." Nature Scientific Reports 16, 9376. 2026.

[12] Madsen, D.O. and Puyt, R.W. "The 7Vs of AI Slop: A Typology of Generative Waste." AI & Society (Springer), 2026.

[13] FaceForensics++ (Rossler et al., 2019); Deepfake Detection Challenge (Dolhansky et al., 2020); ASVspoof 5 (2025-2026, best challenge EER of 2.59%). Video detection AUROC ranges 91-97% in-domain (FF++), degrading to ~70-87% cross-dataset (DFDC).

[14] Shaib, C. et al. "Measuring AI 'Slop' in Text." arXiv:2509.19163. 2025.

[15] No published study on AI-generated infographic, card news, or carousel detection was identified in searches of ACM Digital Library, IEEE Xplore, arXiv, and Google Scholar as of March 2026.

[16] JacktheReviewer.com. "ChatGPT + Canva: 100 Instagram card news in 5 minutes." 2026; BizhankookMedia. "AI programs making blogs effortlessly -- junk information overflows." 2025.

[17] Originality.AI. "AI Content in Google Search Results." 2019-2025 longitudinal tracking.

[18] Retraction Watch. Hindawi/Wiley mass retraction tracking. 11,300+ retractions, 19 journals closed, 2023-2024.

[19] Originality.AI. "AI Content in Amazon Reviews." 2025.

[20] Federal Trade Commission. "Consumer Reviews Rule." Final rule effective October 21, 2024. $51,744 civil penalty per violation.

[21] Analysis of Amazon KDP "Success" genre. 844 titles examined, 77% identified as AI-generated. 2025.

[22] Korea Times. Reporting on single Korean publisher producing 9,000 AI-generated titles in one year. 2025.

[23] Spotify. "Spotify Strengthens AI Protections." September 25, 2025. (75M+ spammy tracks removed).

[24] New York Times. Investigation finding ~40% of children's recommended videos are AI slop. March 2026.

[25] Factcheck.by. "YouTube Botnet Study." March 2025. (12% of comments on political videos are bots).

[26] StealthRL. RL-based paraphrasing policy. 2026. Reduces average TPR@1%FPR, AUROC from 0.79 to 0.43, attack success rate 97.6%. Transfers to unseen detectors.

[27] Adversarial Paraphrasing framework. NeurIPS 2025. Training-free attack reducing TPR@1%FPR by average 87.88%.

[28] Buffer. "State of Social Media 2026." Analysis of 52M+ posts. Carousel engagement: 6.90%; Reels: 3.31%. CreatorsJet 2025 (10,000 posts): Mixed carousels 2.33% vs Reels 1.23%.

[29] CivicNews. "Card news is a uniquely Korean news format." 2018; Bae, J.G. "Card news as the first 'mainstream' multimedia format in Korean journalism history." 2018.

[30] EU AI Act, Article 50. Effective August 2, 2026. Machine-readable marking and deepfake disclosure requirements.

[31] Republic of Korea. AI Basic Act. Effective January 22, 2026. Labeling mandate for synthetic voice/image/video.

[32] WinBuzzer. "Reddit Human Verification: Bot Detection via Passkeys and Biometrics." March 25, 2026.

[33] Sixth Tone; MLex. Reporting on China's AI content labeling enforcement. September 2025 onward. 37,000 non-compliant videos removed, 3,400 accounts suspended, 600,000 videos labeled.

---

**About the Author:** The author is an independent developer working at the intersection of content systems and AI tooling. This perspective draws on direct experience building and observing automated content production pipelines -- the infrastructure that AI slop research studies from the outside.

---

*Word count: ~2,700*
