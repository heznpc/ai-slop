# ai-slop-paper — Review (2026-04-11)

## 1. 커밋 톤이 주장을 일관되게 지지하는가?

**판정: 매우 일관됨 (3 commits, 2026-03-28 → 04-04).**

```
303b349 Initial commit: AI slop multi-format research papers       (2026-03-28)
bd3c841 feat: restructure into framework/perspectives tracks       (2026-03-30)
25454c0 feat: consolidate ai-slop repos into monorepo              (2026-04-04)
```

진화 패턴:
- **t=0 (3/28)**: research notes 10개(약 5,737줄) + Paper A/B v2 draft가 동시에 들어옴 — 사전에 외부에서 작성된 자료가 한 번에 import됨.
- **t+2 (3/30)**: research/ 디렉토리 *전체 삭제* + framework/perspectives 2-track 구조로 재편 + draft_final.md 두 개 추가. *연구 노트를 흡수해 최종본으로 압축*하는 결정.
- **t+7 (4/4)**: LaTeX 컴파일 가능 형태(main.tex 665줄/428줄, references.bib 402줄) + draft_v1.md(이전 단계 보존). 외부 작업물의 monorepo 통합.

톤의 일관성:
- 모든 단계에서 핵심 주장 두 가지가 변하지 않음: ① "video-centric framing이 잘못됐다", ② AMSM 5차원 모델로 cross-format 비교가 가능하다.
- 새로 발견된 사실로 핵심 가설을 흔들지 않고 *부속 수치만 보강*. 학술적으로 건강한 진화.
- `FACTCHECK_CORRECTIONS.md`(2026-03-28)가 첫 commit에 함께 존재 — **자기 비판/팩트체크가 commit history의 첫 단계부터 제도화**돼 있음. 11개 critical/moderate error를 stage별로 분류하고 수정 우선순위까지 매김. 이는 working paper로서 매우 드문 자기교정 인프라.
- 단점: 4월 4일 이후 1주 동안 추가 commit 없음. fact-check correction이 main.tex에 *반영됐는지* 확인이 안 된다 — references.bib에 `BenderThompson2026`이 명시적으로 "Removed" 코멘트로 표시된 정도만 확인 가능.

## 2. 부가 서비스 품질

**판정: 부가 서비스 0개 — 그러나 TODO.md에 5개 실험이 명시되어 있음.**

레포 구성:
- `framework/` Big Data & Society 논문(665줄 LaTeX, 402줄 bib, 4개 draft + outline + cover_letter)
- `perspectives/` CACM Viewpoints 논문(428줄 LaTeX, 4개 draft + outline + cover_letter)
- `shared/` 11개 리서치 노트(약 350KB) + FACTCHECK_CORRECTIONS.md
- `.gitignore`가 LaTeX 산출물(`*.aux`, `*.bbl`, `*.log` 등) 제외 처리 → CI 빌드 가능 형태

코드, 데이터셋, 노트북, 데모 사이트, 탐지기, 벤치마크 — *전무*. 카드뉴스 탐지기 부재가 가장 큰 갭(논문 본문에서 "no published detection study exists"라고 자신이 인정).

TODO.md(2026-04-04)에 명시된 5개 실험은 모두 **proposal 상태** — 데이터 수집·코드·노트북 모두 0%. 즉 *제안 인프라*조차 없다.

## 3. 고도화 가능 파트

높은 우선순위:
1. **카드뉴스 탐지 모델 (실험 #4)** — Korean Naver/Instagram carousel 1,000~2,000개 데이터셋 + CLIP 기반 multimodal encoder. 논문이 핵심 약점으로 지목하는 *그* 갭을 본인이 채울 기회. 한국어/한국 시장 데이터는 글로벌 경쟁자가 거의 없어 *first-mover prize* 명확.
2. **다형식 탐지 벤치마크 (실험 #1)** — GPTZero / Turnitin / Copyleaks / OpenAI classifier 비교. AMSM의 DDI(Detection Difficulty Index) 차원을 *실제 측정값*으로 채울 수 있음. 현재는 모든 DDI 점수가 expert judgment.
3. **fact-check 결과의 main.tex 반영** — 11개 항목 중 몇 개가 적용됐는지 확인 commit이 필요. `git diff bd3c841 25454c0 -- references.bib`로 추적.
4. **2-paper 분리 전략의 일관성 점검** — perspectives는 ~3,000 단어, framework는 ~9,500 단어. 자기인용 `\parencite{author2026amsm}`/`\parencite{author2026pda}` 양방향 cross-reference가 *동시 출간 시점에* 작동하는지 확인.
5. **AMSM 5차원의 quantitative scoring 개선** — 현재 1-5 점수가 expert judgment. 각 차원을 *측정 가능한 metric*으로 operationalize하면 reviewer pushback이 크게 줄어듦. 예: PCA(Production Cost Asymmetry) = log(human-hours/AI-cost)로 정의.

중간 우선순위:
6. 6개 자연실험(중국 2025.9, EU 2026.8, 한국 2026.1 시행) 시점 전후의 *실제* 슬롭 비율 측정 → 실험 #5. 시점 데이터가 휘발성이라 지금이 적기.
7. 한국 데이터(8.45B Kapwing views, 9,000 books/year, Naver 카드뉴스)가 풍부 — *Korea-as-canary* 서브 페이퍼 1편 추가 가능. 한국 특화 deep dive로 ACM CHI/CSCW에 별도 트랙 가능.
8. AMSM 모델을 Streamlit/Jupyter calculator로 공개 → 콘텐츠 폼 입력 시 자동 점수화. 정책 담당자에게 어필.
9. README의 "Status" 체크리스트 업데이트(현재 4월 4일 기준 TODO 상태가 아직 "Final proofreading").

낮은 우선순위:
10. arXiv 동시 투고용 PDF build (tectonic + GitHub Actions).
11. 한/영 양쪽 abstract.

## 4. 학술적 / 시장 가치 (글로벌, 2026-04-11 기준)

### 학술적 가치: **상위권 (working paper 기준 상위 ~10%)**

타이밍이 거의 완벽:
- Sora 셧다운(2026-03-24) 4일 후 첫 commit → 시의성 가장 높은 시점 진입.
- Merriam-Webster "slop" Word of Year 2025, YouTube CEO 발언, Mosseri Instagram 발언 — 모두 2025 12월 ~ 2026 3월의 *직전* 이벤트.
- 직접 경쟁 학술논문은 단 1편: Shaib et al.(2025) "Measuring AI Slop in Text" — text only. **multi-format framework는 빈 슬롯**.

차별점:
- AMSM 5차원(PCA/DDI/EDP/AAS/RCG)이라는 명확한 새로운 분석 단위. 인용 가능한 framework 명칭이 있다는 것은 학술적 mileage가 길다.
- "Production-Detection Paradox" — 1줄 요약 가능한 명제. 토픽 글에서 인용되기 좋은 형태.
- "Algorithm-Slop Co-evolution Model" — 알고리즘과 슬롭의 상호 진화. CHI/CSCW에서 강한 반응 예상.
- *2-paper strategy* (long framework + short commentary) — Ross & Wagner 식 dual deployment. 인용 surface area가 2배.
- **FACTCHECK_CORRECTIONS.md의 존재 자체가 reviewer 신뢰도를 +1 단계 올림.** 특히 independent researcher라는 약점을 자기 검증으로 메움.

게재 전망:
- *Big Data & Society* (framework, 9,500 words, 6개월 review): **realistic, 60-70%**. 인터디시플리너리 framework 페이퍼를 환영하는 저널. cover_letter도 적합도 강조 잘 함.
- *Communications of the ACM* Viewpoints (perspectives, 3,000 words): **competitive, 30-40%**. 시의성과 명확한 정책 함의가 강점이지만 CACM Viewpoints는 invitation-driven 비중이 높음.
- 대안 트랙: *First Monday*, *Internet Policy Review*, *AoIR*, *New Media & Society* — 모두 적합도 매우 높음.

위험 요소:
- **Independent researcher 단독 저자** — 일부 reviewer는 이를 negative signal로 봄. cover_letter에서 약점을 강점(practitioner perspective)으로 전환했지만 reviewer 운에 좌우.
- **Empirical contribution 0** — AMSM 적용 사례가 모두 secondary citation. 작은 detection benchmark 1개만 추가해도 reject 위험이 크게 줄어듦.
- **fact-check 11개 중 main.tex 반영 확인 불가** — submission 전 반드시 점검 필요. 발견된 critical error(71% image stat, StealthRL 수치, 22% CS 저널명 등)가 그대로 남아있다면 reviewer가 첫 페이지에서 reject 가능.
- 카드뉴스 detection이 *0편*이라는 주장이 6개월 후에도 유효할지 — Korean/Chinese 그룹 중 누군가 빠르게 1편 낼 가능성 있음.

### 시장 가치: **상위권 (정책·플랫폼 영역에서 즉시 사용 가능)**

- **YouTube/Meta/TikTok Trust & Safety 팀**: AMSM의 5차원 score는 risk prioritization framework로 그대로 사용 가능. 컨설팅/자문 수요 명확.
- **EU AI Act / 한국 AI 기본법 / 중국 CAC** 시행 직전 timing — AI 라벨링 정책의 cross-format 적용 가이드라인으로 인용 가능. 정책 think-tank 가치 매우 높음.
- **DoubleVerify / Originality.AI / GPTZero** 같은 detection vendor에게는 "어디에 투자해야 하는가"의 답을 제시 → 카드뉴스/리뷰/북 시장 진입 정당화.
- **언론**: NYT, WIRED, The Verge가 사용할 만한 1줄 명제(Production-Detection Paradox)가 있음. 미디어 픽업 가능성 매우 높음.
- **한국 시장 특화 가치**: 한국 데이터의 풍부함(8.45B Kapwing views, 9,000 books, 카드뉴스 격발지) → KISDI, KCC, 방통위 자문 직결.

### 종합 평점 (2026-04-11)

| 축 | 점수 | 코멘트 |
|---|---|---|
| Originality of framing | 9/10 | AMSM, PDP, ASCM 세 framework 모두 인용 가능 |
| Literature integration | 8/10 | 16+편 정리, but Shaib 외엔 직접 cf 부족 |
| Empirical contribution | 2/10 | 0개. TODO에만 5개 |
| Self-correction discipline | 9/10 | FACTCHECK 문서가 보기 드물게 정직 |
| Repo health (commits, structure) | 7/10 | 3 commits, 2-track 구조 깔끔, but 1주 update 정체 |
| Timing | 10/10 | Sora shutdown 4일 후 진입 |
| Submission readiness | 6/10 | LaTeX 빌드 가능, cover letter 완성, but fact-check 반영 미확인 |
| **Overall (working paper)** | **7.5/10** | "투고 직전" 상태. 카드뉴스 detector 1개만 추가하면 8.5+ |

핵심 격언: **"두 논문이 출간 전에 카드뉴스 detector 데모 1개와 fact-check 반영 commit 1개가 더 들어오면 임팩트가 1단계 비약."** 한국 데이터 우위는 글로벌에서 누구도 못 따라온다.
