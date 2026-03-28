# AI Slop 핵심 논문 심층 분석
> 작성일: 2026-03-28 | 논문 8편 + 추가 발굴 논문 분석

---

## 논문 1: "The 7Vs of AI Slop: A Typology of Generative Waste"

**저자**: Dag Oivind Madsen & Richard W. Puyt
**출처**: SSRN (Working Paper) + AI & Society (Springer, 2026)
**DOI**: 10.2139/ssrn.5558018
**발표일**: 2025년 10월 2일 (SSRN), 2026년 Springer 게재

### 핵심 주장 (Core Argument)
AI 슬롭은 일시적 현상이 아닌 현대 미디어 생태계의 **구조적 특성(structural feature)**이다. 플랫폼 자본주의, 정보 과부하, 인식론적 오염(epistemic pollution) 이론에 근거하여, TikTok, YouTube, Meta, X 등 주요 플랫폼을 **"산업적 슬롭 농장(industrial slop farms)"**으로 규정한다. 수익화 프로그램이 가치(value) 대신 볼륨(volume)을 적극적으로 보상하는 구조가 핵심 문제이다.

### 방법론 (Methodology)
- **유형**: 개념적/이론적 논문 (Conceptual Paper)
- **방법**: 기존 문헌의 체계적 종합 및 유형학(typology) 구축
- **데이터**: 플랫폼 사례 연구, 기존 연구 메타분석, 산업 보고서 종합
- 생성형 AI 콘텐츠의 범람 현상을 7가지 차원으로 체계적으로 분류하는 프레임워크 개발

### 주요 발견 (Key Findings)

**7Vs 프레임워크:**

| 차원 | 핵심 내용 | 상세 설명 |
|------|-----------|-----------|
| **Volume** | 생산 규모 | 제로 한계비용에 가까운 대량 생산. 일반 에세이, 클릭베이트 블로그, 합성 영상 등이 플랫폼을 포화 |
| **Velocity** | 생성/유통 속도 | 실시간 생산과 즉각적 배포. 인간 창작의 시간적 제약을 완전히 초월 |
| **Variety** | 형태/장르의 범위 | 텍스트, 이미지, 영상, 음악, 딥페이크 포르노까지 전 장르를 아우르는 범용성 |
| **Value** | 문화적/인식론적 가치 침식 | 고품질 콘텐츠를 경제적으로 구축(crowd out). 문화적 다양성과 지식 인프라 약화 |
| **Verification** | 진실성/신뢰 문제 | 사실 확인 불가능한 콘텐츠의 양적 증가. 진위 판별 비용의 소비자 전가 |
| **Visibility** | 알고리즘적 증폭 | 참여도(engagement) 기반 추천 알고리즘이 슬롭을 우선 노출 |
| **Virality** | 밈적 확산 | 바이럴 최적화된 구조. 공유와 확산에 최적화된 콘텐츠 설계 |

### 이론적 프레임워크 (Theoretical Framework)
- **플랫폼 자본주의(Platform Capitalism)**: 플랫폼의 수익 구조가 슬롭 생산을 체계적으로 인센티브화
- **정보 과부하(Information Overload)**: 인지적 처리 한계를 초과하는 콘텐츠 양이 의사결정 품질을 저하
- **인식론적 오염(Epistemic Pollution)**: 지식 생태계의 체계적 오염으로 민주적 공론장 훼손
- **주의 경제(Attention Economy)**: 제한된 주의 자원을 두고 슬롭이 진성 콘텐츠를 압도

### 한계점 (Limitations)
- 이론적/개념적 논문으로 **자체 실증 데이터 부재**
- 7Vs 각 차원 간 상호작용(interaction effects) 분석 미흡
- 플랫폼별, 문화권별 차이 미분석
- 슬롭의 경계 설정(boundary conditions)이 모호 -- 모든 AI 생성 콘텐츠가 슬롭인가?
- 시간적 변화(temporal dynamics) 미반영

### 우리 연구와의 연결 (Connection to Our Research)
- 한국 맥락에서 7Vs 각 차원의 **구체적 수치를 실증적으로 측정** 가능
- 특히 **Visibility(알고리즘 증폭)** 차원에서 한국 유튜브 추천 알고리즘의 AI 슬롭 노출 비율을 정량화하는 연구 설계 가능
- 한국이 Volume과 Visibility에서 세계 1위라는 점을 이 프레임워크로 설명 가능
- **"산업적 슬롭 농장"** 개념을 한국 쇼츠 생태계에 적용하여 수익 구조 분석 가능

### 인용 가능한 핵심 문장
> "TikTok, YouTube, Meta, and X function as 'industrial slop farms,' where monetization programs actively reward volume over value."

> "AI slop is not a passing nuisance but a structural feature of contemporary media ecologies."

---

## 논문 2: "Measuring AI 'Slop' in Text"

**저자**: Chantal Shaib, Tuhin Chakrabarty, Diego Garcia-Olano, Byron C. Wallace
**출처**: arXiv 2509.19163 [cs.CL] (프리프린트, 리뷰 중)
**발표일**: 2025년 9월 23일 (초판), 2026년 1월 24일 (개정판)

### 핵심 주장 (Core Argument)
"AI 슬롭"은 일상적으로 널리 사용되는 용어이지만 **합의된 정의도, 측정 수단도 없다**. 이 연구는 전문가 인터뷰를 통해 슬롭의 분류 체계(taxonomy)를 개발하고, 해석 가능한 평가 차원(interpretable assessment dimensions)을 제안하여 텍스트에서의 슬롭을 체계적으로 측정하는 최초의 프레임워크를 구축한다.

### 방법론 (Methodology)
- **1단계 -- 전문가 인터뷰**: NLP 연구자, 전문 작가, 철학자를 대상으로 구조화된 인터뷰 수행. "슬롭이란 무엇인가?"에 대한 다학제적 정의 도출
- **2단계 -- 분류 체계 구축**: 인터뷰 결과를 종합하여 슬롭의 핵심 차원 도출
- **3단계 -- 크라우드소싱 주석(Annotation)**: 구체적 가이드라인에 따라 텍스트 샘플의 **스팬 레벨(span-level) 주석** 수행
- **4단계 -- 계산적 분석**: 언어학적 마커와 인간 판단 간 상관관계 분석
- **적용 영역**: 뉴스 기사, 질의응답(QA) 텍스트 등 다양한 도메인

### 주요 발견 (Key Findings)

**슬롭의 핵심 평가 차원:**

| 상위 차원 | 하위 코드 | 설명 |
|-----------|-----------|------|
| **Information Quality (정보 품질)** | 사실 오류, 편향된 언어, 관련성 부족 | 정보의 정확성과 신뢰성 |
| **Information Utility (정보 효용)** | 중복성, 주제 이탈, 깊이 부족 | 독자에게 실질적 가치 제공 여부 |
| **Style Quality (문체 품질)** | 장황함(verbosity), 아첨/부자연스러움(flattery), 어색함(awkwardness), 일반성(genericity) | 표현의 자연스러움과 고유성 |

**도메인별 슬롭 특성 차이:**
- **뉴스 기사**: "장황하고, 주제에서 벗어나며, 어조/프레이밍에 문제가 있는" 텍스트가 슬롭으로 판정
- **질의응답**: 사실성(factuality)과 구조적 문제가 슬롭의 가장 강력한 예측 변수
- 모든 도메인 공통: **관련성 부족과 정보 결여, 사실 오류, 편향된 언어**가 일관되게 슬롭 판정과 상관

**주석자 간 신뢰도:**
- 이진적 슬롭 판단은 "다소 주관적(somewhat subjective)"
- 그러나 이러한 판단은 **일관성(coherence)과 관련성(relevance) 같은 잠재적 차원과 유의미하게 상관**
- 완전히 주관적이지 않으며, 측정 가능한 언어적 차원으로 부분적 객관화 가능

### 이론적 프레임워크 (Theoretical Framework)
- **정보 품질(Information Quality) 문헌**: 전통적 가독성 지표(Gunning, Flesch-Kincaid)를 확장
- AI 특화 품질 문제를 포착하기 위해 **기존 가독성 개념을 넘어서는 새로운 평가 체계** 제안
- 텍스트의 "기술적 유창함(technical fluency)"과 "실질적 품질(substantive quality)"을 분리

### 한계점 (Limitations)
- 주로 **영어 텍스트**에 한정 -- 한국어 등 다른 언어에 대한 적용 미검증
- 초기 분석의 도메인 한정 (뉴스, QA)
- 크라우드소싱 주석의 고유한 변동성
- AI 모델 능력의 급격한 변화로 인해 **결과의 시간적 유효성(temporal validity)** 제한
- 슬롭의 맥락 의존성(context dependency) 완전 반영 어려움

### 우리 연구와의 연결 (Connection to Our Research)
- **한국어 텍스트 슬롭 측정 프레임워크 개발의 직접적 기반** -- 이 논문의 분류 체계를 한국어에 적용/수정하는 연구 설계 가능
- 네이버 블로그, 한국어 유튜브 자막, 커뮤니티 글 등에서 **한국어 특화 슬롭 지표** 개발
- Information Quality / Information Utility / Style Quality 3축 프레임워크를 한국어 맥락에서 재검증
- 한국어 LLM(HyperCLOVA X 등)이 생성하는 텍스트의 슬롭 특성 분석

### 인용 가능한 핵심 문장
> "AI 'slop' is an increasingly popular term used to describe low-quality AI-generated text, but there is currently no agreed upon definition of this term nor a means to measure its occurrence."

> "Binary 'slop' judgments are (somewhat) subjective, but such determinations nonetheless correlate with latent dimensions such as coherence and relevance."

> "Text lacking relevance and information, or containing factual errors or biased language, is consistently labeled as slop across domains."

---

## 논문 3: "AI-Generated 'Slop' in Online Biomedical Science Educational Videos"

**저자**: Eric M. Jones, Jane D. Newman, Boyun Kim, Emily J. Fogle
**출처**: JMIR Medical Education, Vol. 11, e80084 (2025)
**DOI**: 10.2196/80084
**PMID**: 41264860 | **PMC**: PMC12634010
**발표일**: 2025년 11월 20일

### 핵심 주장 (Core Argument)
AI 슬롭은 학술 문헌에서 최초로 공식 정의를 부여받아야 하는 현상이다. 슬롭은 **"생성형 AI에 의해 대부분 또는 전적으로 만들어진 자료로, 정확성, 유창성, 유용성에 대한 인간의 주의(care)가 거의 또는 전혀 없는 것"**으로 정의된다. 교육 맥락에서 이는 학습자에게 "이해의 환상(illusion of understanding)"을 만들어내며, 특히 혼란 상태에 있는 학습자가 가장 취약하다.

### 방법론 (Methodology)
- **설계**: 혼합 방법론(Mixed Methods Study)
- **검색 전략**: 2025년 2-3월, 10개 주제별 검색어로 YouTube와 TikTok 체계적 검색
- **표본**: 총 **1,082개** 전임상 생의학 교육 영상 (YouTube 814개, TikTok 268개)
- **3단계 평가**:
  - 1차: 초기 스크리닝
  - 2차: 다수 리뷰어에 의한 검증
  - 3차: 질적 내용 분석
- **분석**: 2단계 질적 분석 (귀납적 코딩 후 "부주의한 발화" 특성과 매핑)
- **정량 분석**: 순열 검정(permutation testing)을 통한 시청 지표 비교
- **주목**: AI 탐지 도구의 알려진 불신뢰성으로 인해 **AI 탐지 도구 미사용**

### 주요 발견 (Key Findings)

**유병률(Prevalence):**
- 전체 AI 슬롭 비율: **5.3%** (1,082개 중 57개)
- YouTube: **5.8%** (814개 중 47개)
- TikTok: **3.7%** (268개 중 10개)
- YouTube Shorts에 슬롭 집중: YouTube 슬롭의 **78.7%**가 Shorts (전체 YouTube 영상 중 Shorts는 34.3%에 불과)

**참여 지표(Engagement Metrics):**
- YouTube 슬롭은 전체 평균 대비 약 **10배 낮은** 참여도
- YouTube 슬롭의 **21.3%**가 좋아요 0개
- YouTube 슬롭의 **78.7%**가 댓글 0개
- 그러나 통계적으로는 유의하지 않음 (조회율 P=.11, TikTok 수집률 P=.87)
- **핵심 발견**: "슬롭의 존재와 유의미하게 상관하는 지표는 없었다" -- 시청 데이터만으로는 슬롭 식별 불가

**질적 분석 -- 16개 문제 코드 (3개 범주):**

| 범주 | 코드 수 | 구체적 문제 |
|------|---------|-------------|
| **내용 기반 문제** | 5개 | 사실 오류/환각, 핵심 맥락 누락, 과잉 일반화/단순화, 부적절한 깊이, 오해 유발 비유 |
| **구조적 문제** | 5개 | 저품질 그래픽/애니메이션, 저품질 오디오, 문법/어휘 오류, 부자연스러운 발화 패턴/발음 오류, 편집/시퀀싱 오류 |
| **내용-구조 복합 문제** | 6개 | 과도한 수식어/클리셰, 오디오-비주얼 불일치, 주제 이탈, 무의미한 그래픽, 텍스트 깨짐, 주제 비조직화 |

**주목할 사례:**
- 영상 679: 니코틴 아세틸콜린 수용체를 "벌집 출입구"에, 아세틸콜린을 "일벌"에 비유 -- 구조적으로 비일관적 유추
- 영상 1088: 생화학이 "해가 뜨고 지게 한다"고 주장 -- 명백한 사실 오류
- 영상 643: 전자전달계를 설명하면서 "Barney & Friends" 영상 위에 "Yankee Doodle" 음악 배치
- 영상 712: 대사 경로 다이어그램에 "깨진 텍스트(garbled text)"와 무의미한 비주얼

### 이론적 프레임워크 (Theoretical Framework)
- **부주의한 발화(Careless Speech)**: AI 출력물이 훈련 데이터와 상관하지만 **외부 현실과의 직접적 연결이 없는** 발화
- **인지 부하 이론(Cognitive Load Theory)**: 슬롭이 외적 인지 부하(extraneous cognitive load)를 증가시켜 학습 방해
- **멀티미디어 학습 원리**: 관련 없는 시각/청각 조합이 학습 원리를 체계적으로 위반
- **이해의 환상(Illusion of Understanding)**: 그럴듯하게 들리지만 부정확한 비유가 피상적 이해를 촉진

### 한계점 (Limitations)
- 정의가 **교육적 맥락에 특화** -- 다른 맥락으로의 일반화 제한
- 탐지 방법이 **명백하고 저품질인 AI 출력물에 편향** -- 고품질 슬롭 탐지 불가
- 전임상 생의학 주제에 **범위 한정**
- 편향(bias) 분석이 코드 A2(불완전성) 이상으로 확장되지 않음
- 슬롭의 **윤리적 차원** 미충분 논의
- 고품질 슬롭이 탐지를 회피할 수 있다는 경고 제시

### 우리 연구와의 연결 (Connection to Our Research)
- **한국어 교육 영상에 동일 방법론 적용 가능**: 한국 유튜브의 의학/과학 교육 영상에서 슬롭 유병률 조사
- 16개 문제 코드 체계를 **한국어 콘텐츠에 맞게 수정/확장**
- "부주의한 발화" 프레임워크를 한국어 TTS 기반 콘텐츠 분석에 적용
- **YouTube Shorts 집중 현상**이 한국에서도 동일한지 검증 (한국이 세계 1위 소비국이므로 특히 중요)
- 슬롭의 교육적 위험이 한국 학습자에게 어떻게 나타나는지 조사

### 인용 가능한 핵심 문장
> "Slop is any material, created mostly or entirely by generative AI, with little or no apparent human care toward the accuracy, fluency, or helpfulness of the material."

> "None of the metrics we collected correlates significantly with the presence of slop."

> "Creators face 'no risk of consequence' for low-quality material, particularly on anonymized platforms, creating asymmetric incentives for proliferation."

> "[Slop represents] a 'small but nonnegligible' portion of accessible educational video content."

---

## 논문 4: "The Impact of Generative AI on Social Media: An Experimental Study"

**저자**: Anders Giovanni Moller, Daniel M. Romero, David Jurgens, Luca Maria Aiello
**출처**: Nature Scientific Reports, Vol. 16, Article 9376 (2026)
**DOI**: 10.1038/s41598-026-40110-8
**PMID**: 41699054
**발표일**: 2026년 2월 17일

### 핵심 주장 (Core Argument)
생성형 AI 도구는 소셜 미디어에서 **"복잡한 이중성(complex duality)"**을 만들어낸다. 일부 AI 도구는 사용자 참여도와 콘텐츠 생산량을 증가시키지만, **동시에** 토론의 인지된 품질과 진정성(authenticity)을 저하시키며, 대화 전반에 **부정적 파급 효과(negative spill-over effect)**를 초래한다.

### 방법론 (Methodology)
- **설계**: 통제된 실험(Controlled Experiment)
- **참가자**: 미국 대표 표본 **680명**
- **환경**: 현실적 소셜 미디어 환경을 구현한 실험 플랫폼
- **집단 구성**: 5인 1조 토론 그룹, 무작위 배정
- **5가지 실험 조건**:
  1. **대조군(Control)**: AI 도구 없음
  2. **Chat 지원**: AI 챗봇 활용 가능
  3. **대화 시작(Conversation Starters)**: AI가 토론 주제 제안
  4. **피드백(Feedback)**: AI가 댓글 초안에 피드백 제공
  5. **답변 제안(Reply Suggestions)**: AI가 답변 옵션 제시
- **논문 분량**: 48페이지, 12개 그림

### 주요 발견 (Key Findings)

**핵심 이중성(Duality):**
| 긍정적 효과 | 부정적 효과 |
|-------------|-------------|
| 사용자 참여도 증가 | 인지된 품질(perceived quality) 저하 |
| 콘텐츠 생산량 증가 | 진정성(authenticity) 감소 |
| 활발한 토론 촉진 | 부정적 파급 효과 발생 |

**구체적 발견:**
- AI 도구 사용 시 콘텐츠 **양(volume)은 증가**하나 **깊이(depth)는 감소**
- 참여자들이 AI 지원 토론을 **덜 진정성 있다고 인식**
- **부정적 파급 효과**: AI가 개입한 대화가 AI를 사용하지 않는 참여자의 대화 품질에도 영향
- 이 파급 효과는 AI 슬롭 문제의 핵심 -- 소수의 AI 사용이 전체 담론 환경을 오염

### 이론적 프레임워크 (Theoretical Framework)
- **인간-컴퓨터 상호작용(HCI)**: AI 도구가 사용자 행동을 어떻게 변형하는가
- **참여-품질 트레이드오프**: 양적 참여와 질적 담론 사이의 근본적 긴장
- **4가지 윤리적 AI 통합 설계 원칙**:
  1. AI 생성 콘텐츠의 투명한 공개(Transparent Disclosure)
  2. 사용자 중심 개인화(User-focused Personalization)
  3. 맥락 민감성(Context-sensitivity) -- 주제와 사용자 의도 고려
  4. 직관적 사용자 인터페이스(Intuitive UI)

### 한계점 (Limitations)
- **실험실 환경** -- 실제 소셜 미디어 플랫폼의 복잡성(알고리즘, 네트워크 효과 등) 미반영
- 미국 참가자 한정 -- **문화적 차이** 미검증
- 5인 소그룹 토론 -- 대규모 온라인 커뮤니티 동학과 다를 수 있음
- 단기 실험 -- **장기적 적응 효과** 미측정
- 4가지 AI 개입 유형만 테스트 -- 실제 플랫폼의 다양한 AI 기능 미포함
- 특정 주제 영역에 한정된 토론

### 우리 연구와의 연결 (Connection to Our Research)
- **한국 참가자 대상 동일 실험 설계 가능**: 한국 소셜 미디어 맥락에서 AI 도구의 이중성 검증
- "부정적 파급 효과"가 한국의 **높은 AI 슬롭 소비율**과 연결되는지 조사
- 한국 특유의 **빠른 기술 수용(fast adoption)** 문화가 이중성의 균형을 어떻게 변화시키는지 분석
- 네이버 카페, DC인사이드, 에브리타임 등 한국 커뮤니티에서의 AI 개입 효과 연구
- **"참여도 증가 vs 품질 저하" 트레이드오프**가 한국 플랫폼에서 어떻게 나타나는지 실증

### 인용 가능한 핵심 문장
> "Some AI-tools increase user engagement and volume of generated content, but at the same time decrease the perceived quality and authenticity of discussion, and introduce a negative spill-over effect on conversations."

---

## 논문 5: "AI Slop in Academic Publishing: History, Characteristics, Manifestations, Causes, and Mitigation Strategies"

**저자**: 미상 (Taylor & Francis 게재)
**출처**: Internet Reference Services Quarterly (2026)
**DOI**: 10.1080/10875301.2026.2637526
**발표일**: 2026년 3월 3일 (온라인)

### 핵심 주장 (Core Argument)
AI 슬롭은 학술 출판에서 **"체계적 위협(systemic threat)"**으로, "인간 감독 없이 대량 생산된 저품질 합성 콘텐츠(low-quality, mass-produced synthetic content lacking human oversight)"로 정의된다. 이는 **SDG 4(양질의 교육)과 SDG 16(평화, 정의, 강한 제도)**에 직접적 위험을 가한다.

### 방법론 (Methodology)
- **유형**: 문헌 분석 및 개념적 프레임워크 논문
- **접근**: 학술 출판에서 AI 슬롭의 역사적 진화, 특성, 발현, 원인, 완화 전략을 체계적으로 분석
- **핵심 분석 도구**: SLOP 해부학(SLOP Anatomy) 프레임워크

### 주요 발견 (Key Findings)

**SLOP 해부학 프레임워크:**
| 요소 | 의미 | 학술 출판에서의 발현 |
|------|------|---------------------|
| **S**hallow | 피상적 | 깊이 없는 분석, 표면적 문헌 검토 |
| **L**ow-quality | 저품질 | 방법론적 결함, 논리적 비일관성 |
| **O**vergeneralized | 과잉 일반화 | 근거 없는 광범위한 주장 |
| **P**oorly-sourced | 빈약한 출처 | **환각 인용(hallucinated citations)**, 허구 저널 참조 |

**학술 출판에서의 구체적 발현:**
- **환각 인용(Fabricated Citations)**: AI가 그럴듯하지만 실제로 존재하지 않는 논문을 인용하는 현상
- **시각적 사기(Visual Fraud)**: AI 생성 이미지/그래프의 조작
- **가짜 동료 심사(Synthetic Peer Review)**: AI에 의한 형식적 리뷰
- Scientific American(2026) 보도: AI 슬롭이 **존재하지 않는 저널에 대한 기록적 요청**을 유발
- NeurIPS에서 환각 인용 문제 보고

**완화 전략(Multi-level Mitigation):**
- **저자 수준**: AI 생성 참조 미인용, LLM 사용 공개
- **편집자 수준**: 제작 스크리닝 절차 강화, 허위 인용 탐지 기술 도입
- **리뷰어 수준**: AI 생성 콘텐츠와 허위 참조에 대한 경계 강화
- **기관 수준**: 견고한 편집 정책과 인간 감독 체계 구축

### 이론적 프레임워크 (Theoretical Framework)
- **학술 무결성(Scholarly Integrity)**: 동료 심사 기반 지식 생산 체계의 신뢰성
- **UN SDGs 프레임워크**: SDG 4(교육)와 SDG 16(제도적 신뢰)에 대한 위협으로 프레이밍
- **제도적 신뢰(Institutional Trust)**: 학술 출판 시스템에 대한 공공 신뢰의 침식

### 한계점 (Limitations)
- 문헌 분석 중심으로 **자체 실증 연구 미수행**
- 학술 출판이라는 **특정 영역에 한정** -- 일반 콘텐츠 생태계로의 확장 미논의
- 완화 전략의 **실제 효과에 대한 검증 부재**
- 학문 분야별 차이(STEM vs. 인문사회) 미분석
- 글로벌 남반구(Global South) 학술 생태계의 특수성 미고려

### 우리 연구와의 연결 (Connection to Our Research)
- 한국 학술 출판(KCI 등재 학술지)에서의 **AI 슬롭 침투 실태** 조사로 확장 가능
- 한국 연구재단(NRF) 등재 논문에서 **환각 인용 빈도** 분석
- SLOP 해부학 프레임워크를 한국 학술 맥락에 적용
- **SDG 프레이밍**은 한국 정부/정책 대상 연구에서 설득력 높은 접근

### 인용 가능한 핵심 문장
> "AI slop -- low-quality, mass-produced synthetic content lacking human oversight -- poses a systemic threat to scholarly integrity."

---

## 논문 6: Kapwing AI Slop Report

**출처**: Kapwing 블로그 (산업 보고서)
**URL**: https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/
**발표일**: 2025년 10월 (데이터 기준)

### 핵심 주장 (Core Argument)
유튜브 피드의 **21~33%가 AI 슬롭 또는 브레인롯(brainrot) 영상**으로 구성되어 있으며, 이는 전 세계적으로 수십억 회 조회되고 수억 달러의 광고 수익을 창출하는 **산업적 현상**이다. 한국은 조회수 기준 세계 1위 AI 슬롭 소비국이다.

### 방법론 (Methodology)
- **데이터 수집**:
  - playboard.co를 활용하여 **국가별 상위 100개 트렌딩 채널** 분석
  - socialblade.com으로 조회수, 구독자수, 수익 추정치 수집
  - 데이터 기준: 2025년 10월
- **실험**: 신규 YouTube 계정 생성 후 알고리즘 노출 실험
  - 첫 500개 Shorts 중 AI 생성 비율 및 브레인롯 비율 측정
- **분석 단위**: 15,000개 트렌딩 채널 중 슬롭 채널 분류

### 주요 발견 (Key Findings)

**글로벌 규모:**
| 지표 | 수치 |
|------|------|
| 트렌딩 채널 중 AI 슬롭 채널 | **278개** (15,000개 중) |
| 누적 조회수 | **630억 회** |
| 총 구독자 | **2.21억 명** |
| 추정 연간 광고 수익 | **$117M (~1,600억 원)** |

**국가별 조회수 순위:**
| 순위 | 국가 | 조회수 | 채널 수 |
|------|------|--------|---------|
| **1** | **한국** | **84.5억 회** | 11개 |
| 2 | 파키스탄 | 53.4억 회 | - |
| 3 | 미국 | 33.9억 회 | 9개 |

**국가별 구독자 순위:**
| 순위 | 국가 | 구독자 | 채널 수 |
|------|------|--------|---------|
| 1 | 스페인 | 2,022만 | 8개 |
| 3 | 미국 | 1,447만 | 9개 |

**글로벌 탑 채널:**
- 인도 *Bandar Apna Dost*: **20.7억 조회, 연간 $4,251,500** 추정
- 한국 *삼분의지혜(Three Minutes Wisdom)*: **20.2억 조회, 연간 $4,036,500** 추정

**알고리즘 노출 실험:**
- 신규 계정 첫 500개 Shorts 중 **21%가 AI 생성**
- **33%가 브레인롯**으로 분류
- 처음 16개 영상에는 노출되지 않다가 이후 급격히 증가 -- **알고리즘적 증폭의 증거**

### 이론적 프레임워크 (Theoretical Framework)
- 산업 보고서로 명시적 이론 프레임워크 없음
- 그러나 암묵적으로:
  - **주의 경제(Attention Economy)**: 조회수/광고 수익 중심 분석
  - **알고리즘적 증폭**: 플랫폼 추천 시스템의 슬롭 우대 구조
  - **환상적 진실 효과(Illusory Truth Effect)**: 반복 노출이 허위 정보 신뢰도를 높이는 심리적 메커니즘 언급

### 한계점 (Limitations)
- **동료 심사 미경과** -- 산업 보고서로서 학술적 엄밀성 제한
- playboard.co/socialblade.com 데이터의 **정확성/신뢰성 미검증**
- 슬롭 채널 분류 기준의 **객관성/재현성** 불명확
- "트렌딩 채널 상위 100개"라는 표본의 **대표성** 문제
- 수익 추정치의 **불확실성** (YouTube 공식 데이터 아님)
- **신규 계정 1개**에 대한 알고리즘 실험 -- 일반화 제한

### 우리 연구와의 연결 (Connection to Our Research)
- **한국 1위 데이터가 우리 연구의 핵심 동기(motivation)** -- 왜 한국인가? 에 대한 실증적 근거
- Kapwing의 방법론을 **더 엄밀하게 확장**: 더 많은 신규 계정으로 알고리즘 실험 반복, 한국 IP vs 해외 IP 비교
- 한국 트렌딩 11개 채널의 **콘텐츠 유형, 언어, 대상 청중** 심층 분석
- **한국 특화 슬롭 생태계 지도(ecosystem mapping)** 구축 가능
- 연간 수익 데이터를 활용하여 **한국 크리에이터 경제에 대한 슬롭의 경제적 영향** 분석

### 인용 가능한 핵심 문장
> "21-33% of YouTube's feed may consist of AI slop or brainrot videos."

> "South Korea dominates with 8.45 billion total views across 11 trending [AI slop] channels."

---

## 논문 7: MINT Lab "AI Slop: Definitions and Normative Status"

**저자**: Cody Kommers 외 (Alan Turing Institute, Purdue, Duke, U of Chicago, UIUC, Cornell)
**출처**: MINT Research Lab 보고서 + arXiv "Why Slop Matters" (2601.06060)
**URL**: https://mintresearch.org/reports/ai-slop/
**발표일**: 2025-2026

### 핵심 주장 (Core Argument)
AI 슬롭은 단순한 디지털 오염이 아니라 **진지한 학술적 연구가 필요한 현상**이다. 기술적(descriptive) 차원과 규범적(normative) 차원을 엄격히 구분해야 하며, 슬롭은 (1) 진정한 **사회적 기능**을 수행하고 (2) **미학적 정당성**을 보유할 수 있다는 주장을 포함한다.

### 방법론 (Methodology)
- **유형**: 철학적/개념적 분석 (Philosophical Analysis)
- **접근**: 기존 정의들의 체계적 비교 분석 + 규범적 평가 프레임워크 구축
- Eaton의 포르노그래피 논쟁 방법론 차용: 대상 범주, 인과적 해악 가설, 적절한 대응을 체계적으로 분리
- 가족 유사성(family resemblance) 논리 활용

### 주요 발견 (Key Findings)

**세 가지 핵심 정의 비교:**

| 정의 유형 | 출처 | 핵심 | 강조점 |
|-----------|------|------|--------|
| **일상적(Vernacular)** | Simon Willison | "무분별하게 생성되어 요청하지 않은 사람에게 강제된 콘텐츠" | 비동의적 배포 |
| **사전적(Lexicographic)** | Merriam-Webster | "AI에 의해 대량 생산된 저품질 디지털 콘텐츠" | 품질 기준과 규모 |
| **학술적(Academic)** | Kommers et al. | 3가지 원형적 속성 기반 | 구조적 특성 |

**3가지 원형적 속성(Prototypical Properties):**
1. **표면적 역량(Superficial Competence)**: 전문가 수준의 출력 품질("좋은 문법") 뒤에 실질이나 진정한 소통 의도가 부재
2. **비대칭적 노력(Asymmetric Effort)**: 전통적 창작 대비 극히 적은 프롬프트 기반 노력으로 생산
3. **대량 생산 가능성(Mass Producibility)**: 대규모 생성과 소비가 가능한 디지털 생태계에 최적화

**3가지 변이 차원(Dimensions of Variation):**
1. **도구적 효용(Instrumental Utility)**: 특정 목적을 위한 의도적 생성
2. **개인화(Personalization)**: 개인 맞춤형 콘텐츠 생성 가능성
3. **초현실주의(Surrealism)**: 환각적/비현실적 미학적 특성

**4가지 규범적 반론(Normative Objections):**
| 반론 | 내용 | 이론적 기반 |
|------|------|-------------|
| **인식론적 오염(Epistemic Pollution)** | 정보 생태계 저하, 가용 지식 축소, "인식론적 게으름" 유도 | Coeckelbergh (2026) |
| **자동화 편향(Automation Bias)** | 유창함이 비신뢰성을 가리지만 사람들이 체계적으로 AI에 과의존 | Cummings (2004), Danry et al. (2024) |
| **부당한 이유 제공(Illegitimate Reason-Giving)** | 진정한 인식론적 지위나 책임 없이 권위적 증언으로 자처 | Enoch (2012) |
| **비동의적 부과(Nonconsensual Imposition)** | 검토되지 않은 콘텐츠 배포가 수신자에게 무급 평가 노동 강제 | Doctorow (2026) |

**슬롭의 사회적 기능:**
- "AI 슬롭은 문화적/경제적 수요의 다양한 문제에 대한 **공급 측 해결책**"
- 인간이 경제적으로 생산할 수 없는 **니치 콘텐츠 갭(niche content gap)** 충족
- 역사적 선례: Tin Pan Alley, Norman Rockwell 등 처음에 "키치"로 폄하된 대중 문화 형식의 재평가

### 이론적 프레임워크 (Theoretical Framework)
- **가족 유사성(Family Resemblance)** 논리: Wittgenstein에서 차용
- **Eaton의 방법론**: 대상 범주/인과적 해악/적절한 대응의 체계적 분리
- **인식론적 환경(Epistemic Environment)**: 개별 콘텐츠가 아닌 시스템 수준의 구조적 해악 강조
- **최적 제품 다양성(Optimum Product Diversity)**: 경제학적 관점에서 슬롭의 시장 충족 기능 분석

**제안된 작업 정의:**
- *기술적(Descriptive)*: 겉보기 역량은 있으나 실제로는 비신뢰적(사실적 불확실, 개념적 일반성, 공허한 응답성)인 모델 생성 콘텐츠, 참여 최적화 배포 경로를 통해 저비용으로 대량 생산
- *규범적(Normative)*: 소음 축적, 신뢰 신호 침식, 품질 대안 대체, 자동화 편향을 통해 인식론적 환경을 예측 가능하게 저하시킬 때 반론 제기 가능

### 한계점 (Limitations)
- 철학적 분석 중심으로 **실증적 검증 부재**
- "누적 노출 효과에 대한 자연적 연구가 대부분 부재"라고 저자들이 직접 인정
- 경계 사례(hobbyist AI 이미지 공유, AI 보조 저널리즘, 학생 초안 작성) 처리 어려움
- 딥페이크와 슬롭의 관계 미완전 해결 -- 설득력 있는 고품질 콘텐츠는 슬롭과 다름
- 글로벌 남반구, 비영어권 맥락 미고려

### 우리 연구와의 연결 (Connection to Our Research)
- **한국 맥락에서 4가지 규범적 반론을 실증적으로 검증**하는 연구 설계 가능
- 특히 한국의 "빠른 기술 수용" 문화에서 **자동화 편향**이 어떻게 나타나는지 조사
- **한국어 AI 슬롭의 사회적 기능** 분석: 실제로 니치 수요를 충족하는가, 아니면 기존 진성 콘텐츠를 대체하는가?
- "비동의적 부과" 프레임워크를 한국 유튜브 추천 알고리즘에 적용
- MINT Lab의 "실증 연구 부재" 갭을 한국 데이터로 채우는 것이 높은 학술적 기여 가능

### 인용 가능한 핵심 문장
> "AI Slop offers a supply-side solution to a variety of problems in cultural and economic demand."

> "The strongest normative framing emphasizes system-level structural harms over individual content quality."

> "The empirical research agenda remains underdeveloped; naturalistic studies of cumulative exposure effects are largely absent."

> "Content is 'mindlessly generated and thrust upon someone who didn't ask for it.'" (Simon Willison)

---

## 논문 8: KR Institute "AI Slop: Pollution in Our Communication Environment"

**출처**: Khazanah Research Institute (KRI) 리서치 브리프
**URL**: https://www.krinstitute.org/publications/ai-slop-i-pollution-in-our-communication-environment
**발표일**: 2025-2026 (시리즈 1편)

### 핵심 주장 (Core Argument)
AI 슬롭은 **커뮤니케이션 환경의 오염(pollution in our communication environment)**으로 프레이밍해야 한다. 전통적 품질 보증 메커니즘(인간 편집자, 큐레이터)이 콘텐츠 생성 속도를 따라잡을 수 없으며, 진정한(authentic) 콘텐츠가 더 저렴한 대안에 의해 경제적으로 축출(crowded out)되고 있다. 이는 민주적 참여와 문화적 진정성에 체계적 위협이다.

### 방법론 (Methodology)
- **유형**: 정책 리서치 브리프 (Policy Research Brief)
- **접근**: 다중 부문(multi-sector) 증거 수집 및 사례 분석
- **데이터**: Spotify, Amazon, 학술 출판, 문학 잡지 등 다양한 플랫폼의 슬롭 사례 종합
- 시리즈 구성: 1편은 용어 정의와 유병률 증거 확립, 후속편에서 소비자 영향과 체계적 결과 분석 예정

### 주요 발견 (Key Findings)

**다중 부문 증거:**
| 부문 | 구체적 사례 | 수치 |
|------|------------|------|
| **음악** | Spotify 연간 스팸 트랙 제거 | **7,500만 트랙** |
| **출판** | Amazon AI 생성 전자책 범람 대응 | 저자당 일일 **3권** 출판 제한 도입 |
| **학술** | 과학 문헌에서 LLM 사용 증가 | 연구 제출물에서 LLM 포함 증가 |
| **문학** | 문학 잡지 AI 생성 소설 투고 급증 | 투고량 급증으로 일부 잡지 투고 중단 |
| **검색** | AI 콘텐츠 팜의 검색 결과 지배 | 한 기업가가 1,800 AI 페이지로 합법 경쟁자에서 **360만 뷰** 탈취 |

**플랫폼 대응 비교:**
| 플랫폼 | 대응 | 성격 |
|--------|------|------|
| Spotify | 스팸 트랙 대량 제거 | 사후적(reactive) |
| Amazon | 일일 출판 제한 도입 | 수량 규제 |
| Meta | AI 생성 콘텐츠 확장 명시적 지지 | 확대 방향 |
| Deezer | 합성 트랙 라벨링 + 알고리즘 추천 제한 | 차별화 전략 |

### 이론적 프레임워크 (Theoretical Framework)
- **커뮤니케이션 환경 오염(Communication Environment Pollution)**: 물리적 환경 오염과의 체계적 유추
  - 전통적 품질 보증 기제의 붕괴
  - 플랫폼이 글로벌 수용성의 사실상의(de facto) 중재자로 기능
  - 진정한 콘텐츠의 경제적 축출
- **"부주의한 발화(Careless Speech)"**: 의도적 허위정보와 구분 -- 오류가 명시적이 아닌 미묘하게 존재
- **모델 붕괴(Model Collapse)**: 저하된 데이터셋으로 훈련 시 발생하는 재귀적 품질 저하

### 한계점 (Limitations)
- **시리즈 1편**으로 용어 정의와 증거 확립에 한정 -- 소비자 영향과 체계적 결과 분석은 후속편으로 이월
- 동남아시아/말레이시아 맥락 중심 -- 다른 지역으로의 일반화 제한
- 정책 브리프로서 **학술적 방법론적 엄밀성** 부족
- 제시된 증거가 사례 중심(case-based)으로 **체계적 실증 분석 미포함**
- 해결책 제시보다 **문제 진단에 치중**

### 우리 연구와의 연결 (Connection to Our Research)
- **"오염" 프레이밍**을 한국 맥락에 적용: 한국 디지털 생태계의 "오염도" 측정
- Spotify의 7,500만 스팸 트랙 제거 사례처럼, **한국 플랫폼(멜론, 지니 등)에서의 AI 음악 슬롭** 조사
- Amazon 사례의 한국 대응물: **리디북스, 예스24 등에서 AI 전자책** 현황 분석
- **"모델 붕괴" 관점**: 한국어 AI 모델이 한국어 AI 생성 콘텐츠로 훈련될 때의 품질 저하 연구
- 한국의 AI 기본법(2026.01.22 시행) 워터마크 의무와 연결하여 정책 효과 분석 가능

### 인용 가능한 핵심 문장
> "[Traditional] quality assurance mechanisms cannot match content generation velocity."

> "Authentic content becomes economically crowded out by cheaper alternatives."

> "[AI slop threatens] informed citizenship and authentic human expression foundational to democratic and cultural health."

---

## 추가 발굴 논문 및 연구

### 추가 1: "Why Slop Matters" (Kommers et al., 2025)
- **출처**: arXiv 2601.06060
- **핵심**: 슬롭은 비난이 아닌 연구 대상. "최적 제품 다양성" 관점에서 AI 슬롭이 니치 콘텐츠 수요 충족
- **우리 연구 연결**: 한국의 슬롭 소비가 실제로 니치 수요 충족인지, 품질 대안 대체인지 실증적 구분 필요

### 추가 2: "Resisting AI Slop" (H. Holden Thorp, Science, 2026.01.01)
- **출처**: Science 편집장 에디토리얼, DOI: 10.1126/science.aee8267
- **핵심**: Science 저널이 "시간의 시험을 견딜, 인간이 큐레이션한 연구 문헌에 기여"할 것. AI가 오류 포착에 도움을 주지만 "더 적은 인간 노력이 아니라 더 많은 인간 노력을 요구"
- **수치**: 2021-2024 발표 논문 2,680편 중 69%가 데이터 공유 준수
- **우리 연구 연결**: 한국 학술지 편집 정책의 AI 슬롭 대응 현황 조사

### 추가 3: "The Economics of Information Pollution in the Age of AI" (arXiv 2509.13729, 2025.09/2026.01)
- **핵심**: AI가 저품질 콘텐츠 생산의 한계비용을 비대칭적으로 붕괴시킴. 고품질 생산은 여전히 비용이 높아 정보 오염을 체계적으로 인센티브화
- **방법론**: 독점 플랫폼, 이윤 극대화 생산자, 효용 극대화 소비자 간 3단계 게임 모델
- **핵심 개념**: 정보 오염 지수(Information Pollution Index, IPI) -- 사회 후생과 엄격히 부(-)의 상관
- **수치**: AI는 저품질 생산에서 노동의 대체재(σ_L > 1), 고품질 생산에서 보완재(σ_H < 1)
- **우리 연구 연결**: 한국 콘텐츠 시장의 IPI 측정, 한국 크리에이터 생태계의 경제적 영향 분석

### 추가 4: "Generative AI, Academic Deepfakes, and Epistemic Pollution" (Acquier & Cossey, 2026)
- **출처**: Business & Society, SAGE, DOI: 10.1177/00076503251406457
- **핵심**: 인식론적 오염(epistemic pollution)을 "지식 생태계의 저품질, 오해 유발, 또는 조작된 정보에 의한 저하"로 정의. 생성형 AI가 학술 딥페이크를 "더 저렴하고, 접근 가능하며, 탐지하기 어렵게" 만듦

### 추가 5: 한국 관련 핵심 데이터

**한국의 AI 슬롭 소비 구조적 요인 (Korea Herald, 2026.01):**
- 2025년 상반기 한국 생성형 AI 사용률: **25.9%** -> 하반기: **30.7%** (4.8%p 증가, 세계 최대폭)
- Microsoft AI 확산 보고서: 한국 AI 채택 순위 25위 -> 18위로 상승
- 전문가 분석 (임준호, ETRI): "한국 사회는 1997년 이래 끊임없이 변화를 강요받았다. 빠르게 적응하지 않으면 뒤처진다는 기본 심리가 형성"
- 전문가 분석 (Billy Choi, 고려대): "한국은 예외적으로 높은 문해율, 광범위한 5G 스마트폰, 최고 수준의 네트워크 품질"

**한국 정부 규제 (2026.01.22 시행):**
- **인공지능기본법**: AI 생성 콘텐츠에 가시적 워터마크 필수
- 딥페이크 영상: 처음부터 끝까지 AI 생성물 표시 의무
- 비가시적 워터마크의 경우에도 1회 이상 고지 의무
- 최소 1년 규제 유예 기간 부여
- 예술적/창의적 표현물 예외 조항 (예: 영화 엔딩 크레딧)

### 추가 6: Dead Internet Theory와 봇 트래픽 (2025-2026)
- 2024년 기준 자동화 트래픽(봇, 스크래퍼, AI 에이전트)이 **전체 웹 트래픽의 51%** 초과 -- 10년 만에 처음
- 신규 발행 웹페이지의 **74.2%**가 AI 생성 콘텐츠 포함
- Google 상위 20개 검색 결과 중 AI 작성 페이지: 2024.05 11.11% -> 2025.07 **19.56%**
- Reddit 공동창립자 Alexis Ohanian: "Dead Internet Theory에 오래 전부터 공감했으며, 이제 현실"

### 추가 7: 모델 붕괴(Model Collapse) 연구
- **Nature (2024.07)**: Shumailov et al. (Google DeepMind) -- LLM, VAE, GMM이 이전 세대 출력물로 훈련 시 비가역적 결함 발생
- **핵심 메커니즘**: 모델의 현실 관점이 좁아지고, 희귀 사건이 먼저 소실, 출력물이 "밋밋한 중앙 경향성과 이상한 이상치"로 수렴
- **CACM (2026.02)**: 모델 붕괴가 이론적 미래 위험이 아닌 현재 생산 시스템에서 발생 중
- **대응**: 원본 데이터 보존을 통한 미세조정이 성능 저하를 경미하게 유지

### 추가 8: 소비자 심리 연구 (2025-2026)
- AI 기업/AI 자체 신뢰도: 각각 **21%, 20%** (Sprout Social, 2025)
- AI 생성 라벨링 시 소비자 반응: 더 비판적 평가, 덜 자연스럽고 유용하지 않다고 인식 (NIM, 2025)
- AI 인플루언서: 인간 인플루언서 대비 인지된 진정성과 브랜드 신뢰 **유의하게 감소**
- AI 리터러시가 높을수록 부정적 반응이 약해지는 조절 효과
- 맥락 효과: 커피 광고에서는 AI 이미지 선호, 의료/공익 광고에서는 인간 이미지 선호

---

## 종합 분석: 연구 지형도 (Research Landscape Map)

### 이론적 접근별 분류

| 접근 | 논문/연구 | 핵심 개념 |
|------|-----------|-----------|
| **유형학적(Typological)** | Madsen & Puyt (7Vs), MINT Lab (3 속성) | 현상의 체계적 분류 |
| **측정론적(Measurement)** | Shaib et al. | 텍스트 슬롭의 정량적 측정 |
| **실증적(Empirical)** | Jones et al. (PMC), Kapwing, Moller et al. (Nature) | 데이터 기반 유병률/영향 분석 |
| **규범적/철학적(Normative)** | MINT Lab, KRI | 슬롭의 윤리적/인식론적 문제 |
| **경제학적(Economic)** | arXiv 2509.13729 | 정보 오염의 경제적 모델링 |
| **영역 특화(Domain-specific)** | Taylor & Francis (학술), Jones et al. (교육) | 특정 분야에서의 슬롭 영향 |

### 공통 연구 갭

1. **비영어권 실증 연구 부재**: 거의 모든 논문이 영어 중심. 한국어, 중국어, 아랍어 등 비영어 콘텐츠의 슬롭 측정/분석 거의 전무
2. **누적 노출 효과의 종단 연구 부재**: MINT Lab이 직접 인정한 바와 같이, "naturalistic studies of cumulative exposure effects are largely absent"
3. **한국 특화 연구의 완전한 공백**: 한국이 세계 1위 AI 슬롭 소비국임에도 한국 기반 학술 연구 전무
4. **플랫폼 알고리즘의 인과적 역할 미검증**: 상관관계는 시사되나 인과적 메커니즘 미확립
5. **정책 효과 평가 부재**: 한국 AI 기본법, EU AI Act 등 규제의 실효성 사전/사후 비교 연구 전무

### 한국 중심 연구를 위한 전략적 포지셔닝

**왜 한국인가?**
1. AI 슬롭 조회수 세계 1위 (84.5억 회)
2. 생성형 AI 채택 증가율 세계 1위 (4.8%p)
3. 세계 최고 수준의 디지털 인프라 (5G, 문해율)
4. AI 기본법 시행 (2026.01.22) -- 워터마크 의무화
5. "빠른 적응" 문화와 기술 수용성
6. **학술적 공백**: 글로벌 1위 현상에 대한 학술 연구 완전 부재

**가능한 연구 설계:**
- Shaib et al.의 슬롭 분류 체계를 한국어에 적용하여 **한국어 AI 슬롭 측정 프레임워크** 개발
- Jones et al.의 교육 영상 분석 방법론을 한국 유튜브에 적용
- Moller et al.의 실험 설계를 한국 참가자로 재현
- Madsen & Puyt의 7Vs를 한국 데이터로 실증적 검증
- MINT Lab의 4가지 규범적 반론을 한국 맥락에서 검증
- 한국 AI 기본법 워터마크 의무의 정책 효과 분석 (정책 시행 전후 비교)

---

## Sources

### 분석 대상 논문 (8편)
- [SSRN: The 7Vs of AI Slop](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5558018)
- [arXiv: Measuring AI Slop in Text](https://arxiv.org/abs/2509.19163)
- [PMC: AI Slop in Biomedical Videos](https://pmc.ncbi.nlm.nih.gov/articles/PMC12634010/)
- [Nature: Impact of Generative AI on Social Media](https://www.nature.com/articles/s41598-026-40110-8)
- [Taylor & Francis: AI Slop in Academic Publishing](https://www.tandfonline.com/doi/full/10.1080/10875301.2026.2637526)
- [Kapwing AI Slop Report](https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/)
- [MINT Lab: AI Slop Definitions](https://mintresearch.org/reports/ai-slop/)
- [KR Institute: AI Slop Pollution](https://www.krinstitute.org/publications/ai-slop-i-pollution-in-our-communication-environment)

### 추가 발굴 논문
- [arXiv: Why Slop Matters (Kommers et al.)](https://arxiv.org/html/2601.06060v1)
- [Science: Resisting AI Slop (Thorp, 2026)](https://www.science.org/doi/10.1126/science.aee8267)
- [arXiv: Economics of Information Pollution](https://arxiv.org/abs/2509.13729)
- [SAGE: Generative AI, Academic Deepfakes, Epistemic Pollution](https://journals.sagepub.com/doi/10.1177/00076503251406457)
- [Springer: When AI Turns Culture into Slop](https://link.springer.com/article/10.1007/s00146-025-02630-1)
- [Nature: AI Models Collapse (Shumailov et al., 2024)](https://www.nature.com/articles/s41586-024-07566-y)

### 한국 관련 출처
- [Korea Herald: Korea tops AI slop consumption](https://www.koreaherald.com/article/10669855)
- [Korea Herald: Korea ranks No. 1 in AI slop views](https://www.koreaherald.com/article/10629996)
- [정책브리핑: AI기본법 시행](https://www.korea.kr/news/policyNewsView.do?newsId=148958380)
- [AI타임스: 유튜브 추천 20% AI 슬롭](https://www.aitimes.com/news/articleView.html?idxno=205149)
- [한국일보: AI 제작 저질 영상 한국 1위](https://www.hankookilbo.com/news/article/amp/A2025122815090000257)

### 소비자 심리 연구
- [Springer: Consumer Perceptions of AI Marketing Content](https://link.springer.com/rwe/10.1007/978-3-031-75316-9_94-1)
- [NIM: Consumer Attitudes toward AI Content](https://www.nim.org/en/publications/detail/transparency-without-trust)
- [JMSR: AI Influencer Impact on Brand Trust](https://www.jmsr-online.com/article/influence-of-ai-generated-influencer-content-on-brand-trust-and-authenticity-perceptions-438/)

### 플랫폼 알고리즘 연구
- [Wiley: Designing Social Media Recommendation Algorithms](https://nyaspubs.onlinelibrary.wiley.com/doi/full/10.1111/nyas.15359)
- [ScienceDirect: Algorithm Awareness and Personalized Content](https://www.sciencedirect.com/science/article/pii/S0001691825006961)
