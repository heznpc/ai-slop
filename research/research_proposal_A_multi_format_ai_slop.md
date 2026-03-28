# 연구 방향 A: "다중 포맷 AI 슬롭 생태계" 구체화 연구 제안서

> 작성일: 2026-03-28 | 문서 유형: 실행 가능한(Actionable) 연구 제안서
> 핵심 테제: "AI 슬롭은 영상만의 문제가 아니다 — 블로그, 카드뉴스, 리뷰, 댓글, 학술 논문, 도서, 팟캐스트, 미술까지 전 포맷에 걸쳐 있다. 기존 연구에는 영상 중심 맹점(video-centric blind spot)이 존재한다."

---

## 1. 연구 질문 (Research Questions)

### RQ1. 콘텐츠 포맷별 AI 슬롭의 상대적 규모는 어떠한가?

현재까지 확보된 데이터를 종합하면, 포맷별 AI 슬롭 침투율은 다음과 같이 추정된다:

| 포맷 | AI 생성 비율 추정 | 데이터 출처 | 데이터 신뢰도 |
|------|------------------|------------|-------------|
| **웹 텍스트/블로그** | 신규 페이지의 74.2%에 AI 포함 (순수 AI 2.5%) | Ahrefs 900K 페이지 분석 (2025.04) | 높음 |
| **영상 (쇼츠/릴스)** | 유튜브 추천 중 5.3~40% (대상에 따라) | PMC; NYT (2026.03) | 중간 |
| **리뷰** | Amazon 상위 리뷰 중 5~6%, Zillow 에이전트 리뷰 23.7% | Originality.AI; Zillow 분석 | 중간 |
| **학술 논문** | PubMed 인덱싱 논문의 13.5%, CS 프리프린트 20%+ | Bulletin of Atomic Scientists | 높음 |
| **도서/전자책** | Amazon "성공" 자기계발 장르의 77% | 2025 연구 (844권 분석) | 중간 (단일 장르) |
| **음악/오디오** | Spotify 업로드의 28%, 스트림의 0.5% | Spotify 공식 발표 | 높음 |
| **소셜미디어 이미지** | 소셜미디어 이미지의 약 71% | 2025 복수 보고서 | 낮음 (추정치) |
| **댓글/봇 참여** | 전체 인터넷 트래픽 중 봇 51%, 플랫폼별 15~20% | Imperva; Meta (Q1 2025 10억 계정 조치) | 중간 |
| **학술 피어리뷰** | ICLR 피어리뷰의 21% 완전 AI 생성 | 2025 연구 | 높음 |

**핵심 발견**: 텍스트 포맷(블로그, 학술논문, 리뷰)의 AI 침투율이 영상보다 훨씬 높다. 그런데 학술적 관심은 영상에 집중되어 있다. 이것이 바로 이 연구의 존재 이유다.

### RQ2. 어떤 포맷에서 생산-탐지 비대칭(production-to-detection asymmetry)이 가장 큰가?

| 포맷 | 생산 비용/시간 | 탐지 정확도 | 비대칭 수준 | 비고 |
|------|-------------|-----------|-----------|------|
| **텍스트 (블로그/SEO)** | 극저 (몇 초) | 65~90% (도구별 편차 큼) | **매우 높음** | FTC 경고: 탐지 도구 정확도 과장 광고 주의 |
| **학술 논문** | 저 (분~시간) | 낮음 (LLM 편집 감지 어려움) | **극도로 높음** | "tortured phrases" 방식은 7,500개+ 패턴 필요 |
| **리뷰** | 극저 (몇 초) | 낮음~중간 | **매우 높음** | 짧은 텍스트로 통계적 탐지 어려움 |
| **댓글/봇** | 극저 (자동화) | 낮음 (Botometer 실패 사례) | **극도로 높음** | 봇이 인간 행동 모방에 점점 정교해짐 |
| **도서** | 저 (시간~일) | 중간 | **높음** | 장문이라 탐지 기회 더 많으나, 편집 후 탐지 곤란 |
| **음악** | 중 (분~시간) | 중간~높음 | **중간** | 음향 분석 기법 발전 중 |
| **이미지/카드뉴스** | 저 (초~분) | 중간 | **높음** | 인포그래픽 내 오류(무의미한 텍스트 등)로 식별 가능한 경우 있음 |
| **영상** | 중~고 (분~시간) | 중간~높음 | **중간** | 시각적 아티팩트 탐지 가장 연구됨 |

**핵심 발견**: 생산-탐지 비대칭이 가장 큰 포맷은 텍스트 기반(학술논문, 리뷰, 댓글)이다. 영상은 오히려 비대칭이 상대적으로 낮은 편이다 (시각적 아티팩트가 여전히 존재하고, 생산 비용도 더 높음). 연구 자원이 비대칭이 낮은 곳(영상)에 집중되고, 비대칭이 높은 곳(텍스트)에는 부족하다는 역설이 존재한다.

### RQ3. 포맷별 경제적 유인은 어떻게 다른가?

| 포맷 | 주요 수익 모델 | 수익 규모 | 진입 장벽 |
|------|-------------|----------|----------|
| **블로그/SEO** | 광고 수익 (AdSense, 네이버 애드포스트), 제휴 마케팅 | 건당 미미, 대량 생산으로 월 수백만 원 가능 | 극저 |
| **리뷰** | 판매자 대행 수수료, 자체 제품 순위 조작 | 가짜 리뷰로 인한 소비자 피해 연간 $770.7B (2025) | 극저 |
| **학술 논문** | 논문 공장(paper mill) 수수료, 저자 이력 부풀리기 | 건당 $500~수천 달러 | 중간 |
| **도서** | KDP 로열티, 대량 출판으로 롱테일 수익 | 한국: 1개 출판사 연 9,000권 출간 | 저 |
| **음악** | 스트리밍 수익 (가짜 스트림 포함) | Spotify 스팸 트랙 7,500만 개 삭제 | 중간 |
| **댓글/봇** | 인플루언서 마케팅 사기, 가짜 참여 판매 | 인플루언서 가짜 팔로워 시장 15~20% | 극저 |
| **영상** | YouTube 광고 수익, 쇼츠 기금 | AI 슬롭 채널 연 약 1,700억 원 (한국) | 중간 |

### RQ4. 포맷 간 파급 효과(cross-format spillover)는 어떠한가?

이 질문이 이 연구의 가장 독창적인 기여가 될 수 있다. 가설적 파급 경로:

1. **학술 논문 → 뉴스 → 블로그**: AI 생성 논문이 보도자료로 변환되어 AI 생성 뉴스 기사가 되고, 다시 AI 블로그로 재가공
2. **리뷰 → 구매 결정 → 반품 비용**: 가짜 리뷰가 소비자 오도 → 반품 → 물류 비용 → 환경 비용
3. **댓글/봇 → 알고리즘 증폭 → 도달 범위 왜곡**: 봇 댓글이 참여도 지표를 부풀려서 저품질 콘텐츠의 알고리즘 노출을 증폭
4. **도서 → 인용 → 지식 오염**: AI 생성 도서가 다른 AI 시스템의 훈련 데이터가 되는 순환적 오염 (model collapse)
5. **음악 → 추천 알고리즘 → 진성 아티스트 수익 잠식**: AI 스팸 트랙이 추천 슬롯을 차지하여 실제 음악가 수익 감소

---

## 2. 실증 가능성 평가 (Feasibility Assessment)

### 2-1. 포맷별 측정 가능성, 데이터 소스, 탐지 도구, 현실적 표본 규모

#### (1) 영상 (YouTube Shorts, TikTok, Reels) — 기준선(Baseline)

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 높음. 이미 연구 선례 다수 |
| **데이터 소스** | YouTube Data API, TikTok Research API, CrowdTangle (Meta) |
| **탐지 도구** | Hive Moderation, Sensity AI, 수동 코딩 (PMC 연구 사례) |
| **현실적 표본** | 1,000~5,000건 (PMC 연구는 1,082건 스크리닝) |
| **난이도** | 중간. API 접근 제한이 주요 장벽 |

#### (2) 텍스트 (블로그, SEO, 뉴스 기사)

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 높음. 텍스트 분석은 NLP 분야 핵심 역량 |
| **데이터 소스** | Common Crawl, Google Search API, 네이버 검색 API, Ahrefs/SEMrush 데이터 |
| **탐지 도구** | GPTZero (정확도 85~99.3% 자체 주장), Originality.ai (99% 자체 주장), GLTR, DetectGPT, watermark 탐지 |
| **현실적 표본** | 10,000~100,000건 (웹 크롤링으로 대규모 수집 가능) |
| **난이도** | 낮음~중간. 탐지 도구 정확도의 신뢰성이 핵심 문제 (FTC 경고 존재) |
| **주의사항** | 탐지 도구별 정확도 주장이 상충 (GPTZero vs Originality.ai 벤치마크 전쟁). 복수 도구 교차 검증 필수 |

#### (3) 이미지+텍스트 하이브리드 (카드뉴스, 인포그래픽, 캐러셀)

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 중간. 이미지와 텍스트를 모두 분석해야 함 |
| **데이터 소스** | Instagram API (제한적), 수동 수집, CrowdTangle |
| **탐지 도구** | 이미지: Hive Moderation, C2PA 메타데이터 검사. 텍스트: OCR + 텍스트 탐지 도구 조합 |
| **현실적 표본** | 500~2,000건 (수동 수집 병행 시) |
| **난이도** | 높음. 멀티모달 분석 필요, 표준화된 방법론 부재 |
| **참고** | AI 인포그래픽의 "무의미한 텍스트" 문제가 보고됨 — 오히려 탐지 단서가 될 수 있음 |

#### (4) 리뷰 (제품 리뷰, 음식점 리뷰)

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 높음. 구조화된 데이터, 대규모 수집 용이 |
| **데이터 소스** | Amazon Product API, Google Maps/Places API, 네이버 플레이스, Yelp Dataset |
| **탐지 도구** | Originality.ai, Fakespot, ReviewMeta, 자체 분류기 학습 가능 |
| **현실적 표본** | 10,000~50,000건 |
| **난이도** | 중간. 짧은 텍스트(리뷰)의 AI 탐지 정확도가 장문보다 낮은 것이 문제 |
| **기존 연구** | Originality.AI의 Amazon 리뷰 분석, MDPI 논문 (AI 생성 리뷰 분류) 존재 |

#### (5) 댓글/인게이지먼트 (봇 댓글, 가짜 참여)

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 중간~낮음. 봇 탐지 자체가 난제 |
| **데이터 소스** | YouTube Comments API, Reddit API (Pushshift 대안), X/Twitter API ($$$) |
| **탐지 도구** | Botometer (정확도 한계 보고됨), BotDMM (Springer 2025), ISBT 모델 |
| **현실적 표본** | 50,000~200,000건 (API 기반 대량 수집) |
| **난이도** | 높음. LLM 기반 봇이 기존 탐지 도구를 무력화하는 추세 |
| **핵심 문제** | Botometer가 AI 에이전트와 인간 계정을 구분하지 못한다는 연구 결과 존재 |

#### (6) 학술 논문

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 중간~높음. Retraction Watch 등 체계적 데이터베이스 존재 |
| **데이터 소스** | PubMed, arXiv, Retraction Watch, Crossref, Dimensions |
| **탐지 도구** | Problematic Paper Screener (tortured phrases 7,500+), Scholarcy, 자체 LLM 탐지기 |
| **현실적 표본** | 1,000~10,000건 (특정 저널/분야 한정 시) |
| **난이도** | 중간. "완전 AI 생성"과 "AI 보조 편집"의 경계 설정이 어려움 |
| **기존 연구** | 상당량 존재 — Retraction Watch, Nature, Science 모두 다루고 있음 |

#### (7) 도서/전자책

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 중간. 전문(全文) 접근이 가장 큰 장벽 |
| **데이터 소스** | Amazon KDP 메타데이터, Google Books API (제한적), 도서 샘플(Look Inside) |
| **탐지 도구** | GPTZero, Originality.ai (장문 분석), 자체 분류기 |
| **현실적 표본** | 500~2,000건 (메타데이터 기반) + 100~300건 (전문 분석) |
| **난이도** | 높음. 저작권 문제로 전문 접근 제한, 샘플 기반 분석의 대표성 문제 |
| **참고** | Amazon "Success" 장르 77% AI 연구(2025)가 방법론적 선례 |

#### (8) 오디오 (팟캐스트, 음악)

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 낮음~중간 (팟캐스트), 중간 (음악) |
| **데이터 소스** | Spotify API, Apple Podcasts 메타데이터, Podchaser, Chartable |
| **탐지 도구** | Resemble AI, audio deepfake detection (학술 모델), C2PA 메타데이터 |
| **현실적 표본** | 500~2,000건 (메타데이터), 100~500건 (음향 분석) |
| **난이도** | 높음. 오디오 처리 파이프라인 구축 필요, out-of-domain 일반화 문제 |
| **핵심 문제** | "AI가 생성한 팟캐스트"의 정의 자체가 모호 (TTS만 사용? 스크립트도 AI?) |

#### (9) 미술/일러스트레이션 (DeviantArt, 웹툰)

| 항목 | 평가 |
|------|------|
| **측정 가능성** | 중간. 시각적 특성으로 탐지 가능하나 급격한 품질 향상 |
| **데이터 소스** | DeviantArt API, ArtStation 공개 갤러리, 네이버 웹툰 |
| **탐지 도구** | Hive Moderation, Illuminarty, GLAZE/Nightshade (방어용), C2PA |
| **현실적 표본** | 2,000~5,000건 |
| **난이도** | 중간~높음. AI 이미지 생성 품질이 빠르게 향상 중 |
| **참고** | AI 생성 코믹/웹툰 시장 $1.52B→$2.01B (2025→2026, CAGR 32.1%) |

### 2-2. 실증 가능성 종합 판정

```
실증 용이                                              실증 곤란
  |========|========|========|========|========|========|
  텍스트    리뷰    학술논문   영상    도서    이미지+텍스트  오디오
  (블로그)                                 (카드뉴스)    (팟캐스트)
                                댓글/봇
                                미술/일러스트
```

**결론**: 텍스트, 리뷰, 학술논문은 실증 가능성이 높고 데이터 접근도 용이하다. 반면 오디오, 카드뉴스 하이브리드, 댓글/봇은 방법론적 도전이 크다.

---

## 3. 방법론 (Methodology)

### 3-1. 통합 분류 프레임워크 (Unified Classification Framework)

기존 7Vs 프레임워크(Madsen & Puyt, 2025)를 확장하되, **포맷-불가지론적(format-agnostic)** 분류 체계를 구축한다:

**제안: AI 슬롭 다중 포맷 분류 매트릭스 (AMSM: AI Slop Multi-format Matrix)**

| 분류 축 | 측정 지표 | 적용 가능 포맷 |
|---------|----------|-------------|
| **1. AI 개입 수준** | (a) 완전 AI 생성, (b) AI 보조 (구조/초안), (c) AI 편집/교정, (d) AI 배포 자동화만 | 전 포맷 |
| **2. 생산 비용** | 시간(초/분/시간), 금전적 비용, 필요 전문성 | 전 포맷 |
| **3. 탐지 난이도** | 최상위 탐지 도구의 F1-score, 인간 판별 정확도 | 전 포맷 |
| **4. 경제적 유인** | 건당 기대 수익, 확장성(scalability), 적발 시 비용 | 전 포맷 |
| **5. 사회적 피해** | 정보 오염 심각도, 경제적 피해, 신뢰 훼손 | 전 포맷 |
| **6. 탐지 연구 성숙도** | 해당 포맷 관련 학술 논문 수, 도구 수, 벤치마크 유무 | 전 포맷 |

이 매트릭스를 통해 포맷 간 직접 비교가 가능해지며, "연구 공백 매핑(research gap mapping)"을 수행할 수 있다.

### 3-2. 포맷 간 비교 지표 (Cross-format Comparison Metrics)

1. **슬롭 침투율 (Slop Penetration Rate, SPR)**: 특정 포맷/플랫폼에서 AI 슬롭이 차지하는 비율
2. **생산-탐지 비율 (Production-Detection Ratio, PDR)**: 생산 용이성 대비 탐지 정확도의 비율. PDR이 높을수록 위험
3. **경제적 비대칭 지수 (Economic Asymmetry Index, EAI)**: (슬롭 생산자 기대수익) / (탐지/제거 비용)
4. **연구 관심 격차 (Research Attention Gap, RAG)**: (포맷별 슬롭 규모) / (포맷별 학술 논문 수). RAG가 높으면 연구 사각지대

### 3-3. 데이터 수집 전략

**Phase 1: 메타 분석 + 기존 데이터 종합 (1~2개월)**
- 포맷별 기존 연구, 산업 보고서, 플랫폼 공식 발표 데이터를 체계적으로 수집
- 체계적 문헌 검토 (Systematic Literature Review) 수행
- 각 포맷별 SPR, PDR, EAI, RAG 초기 추정치 산출

**Phase 2: 1차 실증 — 고실현가능성 포맷 집중 (2~4개월)**
- 텍스트(블로그/SEO): 웹 크롤링 + 복수 탐지 도구 교차 검증 (N=10,000+)
- 리뷰: Amazon/네이버 리뷰 수집 + 탐지 (N=10,000+)
- 학술논문: 특정 분야 논문 표본 + tortured phrases 스크리닝 (N=1,000+)

**Phase 3: 2차 실증 — 중간 난이도 포맷 (3~5개월)**
- 도서: KDP 메타데이터 + 샘플 텍스트 분석 (N=500+)
- 음악: Spotify 메타데이터 + 음향 특성 분석 (N=500+)
- 영상: 기존 방법론 재현 + 비교 기준선 확립 (N=1,000+)

**Phase 4: 통합 분석 + 포맷 간 비교 (2~3개월)**
- AMSM 매트릭스 완성
- 포맷 간 파급 효과 사례 분석
- 정책 함의 도출

---

## 4. 기존 연구와의 차별점 (Novelty Assessment)

### 4-1. 기존 연구 지형도

웹 검색을 통해 확인한 2025~2026년 AI 슬롭 관련 주요 학술 연구:

| 연구 | 포맷 | 접근 | 한계 |
|------|------|------|------|
| Madsen & Puyt (2025) "7Vs of AI Slop" | 전체 (개념적) | 유형학/이론적 | **실증 데이터 없음**, 포맷별 비교 없음 |
| PMC (2026) "AI Slop in Biomedical Videos" | 영상 (교육) | 혼합연구 (N=1,082) | 단일 포맷(영상), 단일 분야(바이오의학) |
| Kommers et al. (2026) AI slop 정의 논문 | 전체 (개념적) | 개념 정의 | 실증 없음, 포맷별 분석 없음 |
| Bingbing Zhang (2025-2026) 아이오와대 | 전체 (소비자 인식) | "Folk theories" 질적 연구 | 생산/탐지 측면보다 소비자 인식 중심 |
| KRI (말레이시아) "AI Slop I" | 커뮤니케이션 전반 | 정보 오염 프레임 | 단일 국가, 포맷별 정량 비교 없음 |
| arxiv (2025) "AI-Generated Content in Cross-Domain Applications" | 멀티모달 | 서베이 논문 | **탐지 기술 중심**, 사회과학적 분석 부재 |
| SSRN "When AI turns culture into slop" | 문화 전반 | 문화비평 | 실증 없음 |

### 4-2. 진정으로 새로운 것은 무엇인가?

**기존 연구에 없는 것:**

1. **포맷 간 정량적 직접 비교**: 동일한 분류 체계를 사용하여 9개 포맷의 AI 슬롭을 비교한 연구는 **존재하지 않는다**. 7Vs 논문조차 개념적 수준에서 "Variety"를 언급할 뿐, 포맷별 수치를 제시하지 않는다.

2. **생산-탐지 비대칭의 포맷별 정량화**: 어떤 포맷이 가장 "방어하기 어려운지"를 비교한 연구가 없다. 이는 정책 입안에 직접적 함의를 갖는다.

3. **포맷 간 파급 효과(spillover) 분석**: 학술논문→뉴스→블로그→리뷰 등의 연쇄적 오염 경로를 추적한 연구가 없다.

4. **"연구 관심 격차(RAG)" 메타 분석**: AI 슬롭의 실제 규모와 학술적 관심의 불일치를 체계적으로 문서화한 연구가 없다.

**기존 연구에 있는 것 (차별화 불필요):**
- AI 슬롭의 개념 정의 → Kommers et al. (2026), 7Vs (2025)
- 영상 슬롭의 실증 → PMC (2026), Kapwing (2025)
- 개별 포맷의 탐지 기술 → 각 분야별 풍부한 문헌

**결론**: 이 연구의 독창성은 "개별 포맷을 연구하는 것"이 아니라, **"포맷 간 비교와 생태계적 시각을 제공하는 것"**에 있다. 이는 진정한 연구 공백이다.

---

## 5. 약점 및 리스크 (Weaknesses & Risks)

### 5-1. 치명적 약점: "너무 넓다" 문제

**진단**: 이 연구의 가장 큰 리스크는 **"1마일 넓이에 1인치 깊이(mile wide, inch deep)"** 비판이다. 9개 포맷을 모두 실증적으로 다루면:
- 각 포맷당 할당 가능한 지면/분석 깊이가 부족
- 리뷰어가 "아무것도 제대로 안 했다"고 판단할 위험
- 포맷별 전문성 부족 노출

**이것은 실제 치명적 약점인가?**: **Yes, 관리하지 않으면 치명적이다.**

### 5-2. 축소(Scoping Down) 전략 — 핵심을 잃지 않는 최소 버전

#### 옵션 A: "전체 조감도 + 3개 포맷 심층" (권장)
- **Paper 1** (Framework Paper): 9개 포맷의 메타분석/기존 데이터 종합으로 AMSM 매트릭스 제시 → RAG(연구 관심 격차) 정량화
- **Paper 2** (Empirical Paper): 가장 연구 격차가 큰 3개 포맷(텍스트/블로그, 리뷰, 학술논문)에 대한 심층 실증
- **장점**: 프레임워크 논문으로 학술적 기여를 확보하고, 실증 논문으로 깊이를 보완
- **단점**: 2편 논문 작성 부담

#### 옵션 B: "비대칭 분석 특화" (차선)
- 연구 질문을 "생산-탐지 비대칭"으로 좁힘
- 9개 포맷에 대해 PDR만 측정/비교
- **장점**: 단일 논문으로 완결, 명확한 기여
- **단점**: 파급 효과, 경제적 유인 등 풍부한 분석 축 상실

#### 옵션 C: "Minimum Viable Paper" (최소)
- 기존 데이터와 문헌만으로 9개 포맷의 SPR, PDR, RAG를 추정
- 순수 메타분석/리뷰 논문
- **장점**: 빠르게 출판 가능 (3~4개월), 새로운 실증 불필요
- **단점**: "그래서 새로 밝혀낸 것이 무엇인가?"라는 비판에 취약

**권장**: 옵션 A. Framework Paper를 먼저 내고, 이것이 받아들여지면 실증 논문으로 확장.

### 5-3. 출판 리스크 (Publication Risk)

| 리스크 | 심각도 | 완화 전략 |
|--------|--------|----------|
| "너무 넓어서 피상적" | **높음** | 옵션 A로 분할, 프레임워크 논문은 넓이를 강점으로 전환 |
| "새로운 실증 없음" (옵션 C의 경우) | **높음** | 최소 2~3개 포맷에서 자체 데이터 수집 |
| 탐지 도구 정확도 논쟁 | **중간** | 복수 도구 교차 검증 + 정확도 한계 명시적 논의 |
| 포맷 정의의 경계 모호 | **중간** | AMSM 매트릭스에서 명확한 조작적 정의 제시 |
| 빠르게 변하는 환경 (데이터 진부화) | **중간** | 데이터 수집 시점 명시, "스냅샷 연구"로 포지셔닝 |
| 이미 누군가 같은 논문을 쓰고 있을 가능성 | **중간** | 빠른 출판이 핵심. 옵션 C를 선투자하는 전략도 고려 |

### 5-4. 방법론적 리스크

**가장 심각한 문제: 탐지 도구의 신뢰성**

- GPTZero는 자체 벤치마크에서 99.3% 정확도를 주장하나, 독립 테스트에서는 85~90%
- Originality.ai는 99%를 주장하나, GPTZero의 벤치마크에서는 83%
- FTC가 AI 탐지 도구의 과장 광고에 경고를 발한 상태
- **함의**: 이 연구의 모든 "AI 생성 비율" 추정치는 탐지 도구의 한계를 반영한 불확실 구간(confidence interval)으로 제시해야 한다

**포맷별 "AI 슬롭"의 정의 문제**:
- 텍스트: "AI 보조 편집"은 슬롭인가? → Kommers et al.의 3가지 원형적 속성(superficial competence, asymmetric effort, mass producibility) 적용 가능하나, 임계값 설정이 주관적
- 음악: 28%의 Spotify 업로드가 AI이지만 스트림은 0.5% → 공급 측면 슬롭 vs 수요 측면 영향의 괴리
- 학술: 13.5%가 LLM 처리됨 → "처리(processed)"와 "생성(generated)"의 구분 필요

---

## 6. 학술적 임팩트 예측 (Academic Impact Projection)

### 6-1. 적합한 저널

#### Tier 1: 최적 타겟

| 저널 | 분야 | IF | 적합 이유 | 수용 가능성 |
|------|------|-----|----------|-----------|
| **New Media & Society** | 미디어/커뮤니케이션 | ~8.5 | AI 슬롭 담론의 핵심 저널, 7Vs 논문도 이 궤도 | **높음** (프레임워크 논문) |
| **Information, Communication & Society** | 정보사회 | ~5.5 | 디지털 콘텐츠 생태계 연구의 핵심 무대 | **높음** |
| **Journal of Computer-Mediated Communication** | CMC | ~7.0 | 다중 플랫폼/다중 포맷 비교에 적합 | **중간~높음** |
| **AI & Society** (Springer) | AI/사회 | ~3.5 | 7Vs 논문 게재지, AI 슬롭 주제에 호의적 | **높음** |

#### Tier 2: 차선 타겟

| 저널 | 적합 이유 |
|------|----------|
| **Big Data & Society** | 대규모 데이터 분석 + 사회적 함의 |
| **Social Media + Society** | 소셜미디어 중심 분석 시 |
| **Science** (Perspective/Policy Forum) | "Resisting AI Slop" 이미 게재 → 짧은 관점 논문 가능 |
| **Nature Human Behaviour** | 포맷 간 행동적 차이 분석 포함 시 |

#### 학회 발표 우선 타겟
- **ICA (International Communication Association)** — 2027 제출 → 최신성 유지 가능
- **AAAI (Defactify Workshop)** — AI 탐지 기술적 측면
- **ACM CHI** — 사용자 인식/행동 측면 포함 시
- **한국언론학회** — 한국 맥락 특화 버전

### 6-2. 인용 잠재력 (Citation Potential)

**긍정적 요인:**
1. "AI slop"이 2025 올해의 단어 → 학술적 관심 폭증 중, 지금이 최적 타이밍
2. 포맷 간 비교 프레임워크를 최초로 제시하면, 후속 연구가 이 프레임워크를 인용해야 함
3. 7Vs 논문(개념적)에 대한 실증적 대응물로 포지셔닝 가능
4. 정책 입안자에게 "어디에 자원을 집중할 것인가"에 대한 근거 제공 → 정책 보고서 인용

**부정적 요인:**
1. 분야가 너무 빠르게 변해서 2~3년 후 데이터가 구식이 될 수 있음
2. "AI slop"이라는 용어 자체의 학술적 수명이 불확실
3. 포맷별 전문 연구자들이 "우리 분야를 피상적으로 다뤘다"고 비판할 가능성

**인용 예측**: 프레임워크 논문이 top-tier 저널에 게재될 경우, 출판 후 3년간 **50~150회** 인용 가능 (AI slop 연구가 현재 급성장 중이므로). 중간 저널이라도 **20~50회** 예상.

### 6-3. 새로운 연구 어젠다를 열 수 있는가?

**Yes.** 이 연구가 성공적으로 출판되면 다음 후속 연구가 가능하다:

1. **포맷별 심층 연구 시리즈**: AMSM 매트릭스의 각 셀을 채우는 개별 논문 (예: "한국 네이버 블로그 생태계의 AI 슬롭")
2. **종단 연구**: 시간에 따른 SPR, PDR 변화 추적
3. **국가 간 비교 연구**: 한국, 미국, 인도 등 포맷별 침투율 비교
4. **정책 효과 연구**: C2PA, 라벨링 의무제 등의 포맷별 효과 차이
5. **파급 효과 네트워크 분석**: 포맷 간 오염 전파 경로의 네트워크 모델링

이는 단발성(one-off) 연구가 아니라, **연구 프로그램(research program)의 출발점**이 될 수 있다.

---

## 7. 최종 판정: 이 방향은 추진할 가치가 있는가?

### 솔직한 평가

| 평가 기준 | 점수 (5점 만점) | 근거 |
|----------|---------------|------|
| **독창성** | ★★★★☆ (4/5) | 포맷 간 비교 프레임워크는 진정한 공백. 단, 개별 포맷 연구는 이미 존재 |
| **실현 가능성** | ★★★☆☆ (3/5) | 텍스트/리뷰/학술은 실현 가능, 전체 9개 포맷은 매우 야심적 |
| **시의성** | ★★★★★ (5/5) | "AI slop"이 2025 올해의 단어, 학술적 관심 폭증. 2026년 출판이 최적 타이밍 |
| **학술적 영향력** | ★★★★☆ (4/5) | 프레임워크 논문으로 새 연구 어젠다 개척 가능 |
| **출판 가능성** | ★★★☆☆ (3/5) | 스코핑을 잘 하면 높음, 못 하면 "피상적" 비판에 취약 |
| **총합** | **19/25** | **추진할 가치 있음, 단 스코핑이 관건** |

### 치명적 결함(Fatal Flaw)이 있는가?

**No.** 치명적 결함은 없다. 다만 관리해야 할 핵심 리스크가 있다:

1. **스코핑 실패 리스크**: 옵션 A(프레임워크 + 실증 분할)로 관리 가능
2. **탐지 도구 신뢰성 리스크**: 복수 도구 교차 검증 + 불확실 구간 명시로 관리 가능
3. **타이밍 리스크**: 빠르게 움직이지 않으면 누군가 비슷한 프레임워크를 먼저 출판할 수 있음

### 권장 실행 계획

1. **즉시 (1~2주)**: 옵션 C(최소 버전) — 기존 데이터만으로 9개 포맷의 SPR, PDR, RAG 추정. 짧은 perspectives/commentary 형태로 Science 또는 Nature에 투고 시도. 이것이 "깃발 꽂기(flag planting)"
2. **단기 (1~3개월)**: 옵션 A의 Paper 1 — AMSM 프레임워크 논문 작성. New Media & Society 또는 JCMC 타겟
3. **중기 (3~6개월)**: 옵션 A의 Paper 2 — 3개 포맷(텍스트, 리뷰, 학술논문) 심층 실증

---

## Sources

- [AI slop's meteoric rise - Digital Watch Observatory](https://dig.watch/updates/ai-slop-content-social-media)
- [AI slop - Wikipedia](https://en.wikipedia.org/wiki/AI_slop)
- [The 7Vs of AI Slop - SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5558018)
- [Resisting AI slop - Science](https://www.science.org/doi/10.1126/science.aee8267)
- [AI-Generated Slop in Biomedical Videos - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12634010/)
- [UI researcher investigates AI slop - Daily Iowan](https://dailyiowan.com/2026/03/22/ui-researcher-investigates-mass-produced-ai-generated-contents-effects/)
- [KRI: AI Slop I - Pollution in Communication](https://www.krinstitute.org/publications/ai-slop-i-pollution-in-our-communication-environment)
- [From Transparency to Explainability - HUMAN Security](https://www.humansecurity.com/learn/blog/cutting-through-the-noise-of-ai-slopin-2026/)
- [2025 was the year AI slop went mainstream - Euronews](https://www.euronews.com/next/2025/12/28/2025-was-the-year-ai-slop-went-mainstream-is-the-internet-ready-to-grow-up-now)
- [GPTZero vs Copyleaks vs Originality accuracy](https://gptzero.me/news/gptzero-vs-copyleaks-vs-originality/)
- [AI Detection Accuracy Meta-Analysis - Originality.AI](https://originality.ai/blog/ai-detection-studies-round-up)
- [Are AI Detectors Accurate in 2026?](https://walterwrites.ai/are-ai-detectors-accurate/)
- [Can we trust academic AI detective? - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12331776/)
- [Fake Review Statistics 2025 - Capital One Shopping](https://capitaloneshopping.com/research/fake-review-statistics/)
- [AI Content in Amazon Reviews - Originality.AI](https://originality.ai/blog/amazon-ai-generated-reviews)
- [Classification of AI Product Reviews on Amazon - MDPI](https://www.mdpi.com/2673-4591/92/1/17)
- [Dissecting AI-related Paper Retraction - Preprints.org](https://www.preprints.org/manuscript/202601.0314)
- [AI in retraction spotlight - Frontiers](https://www.frontiersin.org/journals/research-metrics-and-analytics/articles/10.3389/frma.2025.1737168/full)
- [GenAI-fueled research fraud bibliography - Sharon Kabel](http://sharonkabel.com/genai-fraud/)
- [Low-quality papers flooding cancer literature - Nature](https://www.nature.com/articles/d41586-025-02906-y)
- [How AI use threatens scholarly publishing - Bulletin of Atomic Scientists](https://thebulletin.org/premium/2026-03/how-ai-use-in-scholarly-publishing-threatens-research-integrity-lessens-trust-and-invites-misinformation/)
- [Amazon Is Filled with AI Book Slop - Rolling Stone](https://www.rollingstone.com/culture/culture-features/amazon-ai-book-knockoffs-1235450690/)
- [Majority of Amazon Success books likely AI-written](https://san.com/cc/majority-of-books-in-amazons-success-self-help-genre-likely-written-by-ai-study/)
- [AI Slop Is Flooding Streaming - Time](https://time.com/article/2026/03/26/ai-slop-is-threatening-musicians-can-tech-companies-stem-the-tide-/)
- [Spotify reveals AI music measures - Music Ally](https://musically.com/2025/09/25/spotify-reveals-its-latest-measures-to-handle-ai-music/)
- [Spotify tests tool to stop AI slop - TechCrunch](https://techcrunch.com/2026/03/24/spotify-tests-new-tool-to-stop-ai-slop-from-being-attributed-to-real-artists/)
- [AI slop infographics warning - Colecandoo](https://colecandoo.com/2026/02/07/stop-making-ai-slop-for-social-media-clout/)
- [Dissecting social bot powered by generative AI - Springer](https://link.springer.com/article/10.1007/s13278-025-01410-5)
- [BotDMM: Dual-channel multi-modal bot detection - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1566253525008206)
- [AI-Generated Content in Cross-Domain Applications - arXiv](https://arxiv.org/html/2509.11151v1)
- [March 2026 Spam Update - LinkDoctor](https://linkdoctor.io/march-2026-spam-update/)
- [74% of New Webpages Include AI Content - Ahrefs](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/)
- [AI Now Writes Half of the Internet - eWeek](https://www.eweek.com/news/ai-writes-half-internet/)
- [When Is Self-Disclosure Optimal? AI Content - arXiv](https://arxiv.org/html/2601.18654v1)
- [C2PA State of Content Authenticity 2026](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026)
- [C2PA Specification](https://c2pa.org/)
- [AI slop quietly conquering the internet - Reuters Institute](https://reutersinstitute.politics.ox.ac.uk/news/ai-generated-slop-quietly-conquering-internet-it-threat-journalism-or-problem-will-fix-itself)
