# 연구 방향 D: 플랫폼 알고리즘과 AI 슬롭 인과성
## "Platform Algorithms and AI Slop Causality"

> 작성일: 2026-03-28 | 문서 유형: 구체적 연구 제안서 (Actionable Research Proposal)
> 핵심 논제: "플랫폼 추천 알고리즘은 AI 슬롭의 중립적 유통자가 아니다 — 인게이지먼트 최적화 피드백 루프를 통해 능동적으로 증폭한다. 문제는: 알고리즘이 슬롭 확산을 야기하는가, 아니면 슬롭이 알고리즘을 착취하는가?"

---

## 1. 연구 질문 (Research Questions)

### RQ1. 추천 알고리즘은 AI 생성 슬롭 콘텐츠를 불균형적으로 촉진하는가?

**구체적 질문:**
- 유튜브 쇼츠 추천 알고리즘은 AI 슬롭 콘텐츠에 대해 체계적 편향(systematic bias)을 보이는가?
- 동일한 주제/메타데이터를 가진 AI 생성 콘텐츠와 인간 생성 콘텐츠 간 추천 빈도 차이가 존재하는가?
- cold start 상태(신규 계정)에서 AI 슬롭 노출 비율이 왜 유의미하게 높은가(Kapwing 연구: 21-33%)?

**현재 근거:**
- Kapwing(2025.10) 15,000개 트렌딩 채널 분석: 신규 유저에게 추천되는 쇼츠의 21%가 순수 AI 슬롭, 33%가 브레인롯(brainrot)
- NYT(2026.03): 어린이 추천 영상 중 약 40%가 AI 슬롭
- 278개 AI 슬롭 전용 채널이 누적 630억 뷰, 2.21억 구독자, 연간 추정 광고 수익 $117M
- Techloy 분석: "AI slop is taking over YouTube, and the algorithm is doing exactly what it was built to do" — 알고리즘이 설계 목적대로 작동한 결과 슬롭이 증폭됨

### RQ2. AI 슬롭은 어떤 인게이지먼트 지표를 최적화하는가?

**구체적 질문:**
- AI 슬롭이 높은 성과를 보이는 구체적 지표는 무엇인가? (시청 시간, CTR, 완료율, 공유율, 댓글 수)
- 인간 제작 콘텐츠 대비 AI 슬롭의 인게이지먼트 프로필은 어떻게 다른가?
- 알고리즘이 최적화하는 지표 중 AI 슬롭에 유리한 것은 무엇이며, 불리한 것은 무엇인가?

**현재 근거:**
- Bynder 연구: AI 생성 콘텐츠는 좋아요/도달/노출에서 유사 성과를 보이나, 인간 콘텐츠가 댓글/해시태그 노출에서 우세
- AI 이미지 평균 41 좋아요 vs 인간 이미지 평균 66 좋아요 (인간 콘텐츠 61% 우세)
- 인간 제작 콘텐츠: 5개월간 5.44배 더 많은 트래픽, 41% 더 긴 세션 시간
- 하이브리드(AI+인간) 콘텐츠가 순수 AI보다 높은 인게이지먼트, 순수 인간과 대등한 성과
- 핵심 모순: **소비자 56%는 AI 콘텐츠 선호(블라인드 테스트)** vs **52%는 AI 의심 시 디스인게이지** — 알고리즘은 전자를 학습하고, 후자는 포착하지 못함
- Search Engine Journal: 추천 시스템이 시청 시간(watch time)과 호기심 갭(curiosity-gap) 클릭을 우선시하여, AI 영상의 고빈도/고자극 특성에 자연스럽게 편향

### RQ3. 피드백 루프가 존재하는가? (알고리즘 → 슬롭 촉진 → 더 많은 슬롭 생산 → 알고리즘 학습 강화)

**구체적 질문:**
- 알고리즘-슬롭 간 양의 피드백 루프(positive feedback loop)가 실증적으로 입증 가능한가?
- 이 피드백 루프의 주기(cycle time)는 얼마나 빠른가?
- 루프를 끊는 개입(intervention)의 효과는 무엇인가?

**현재 근거:**
- arXiv(2207.01616): 추천 시스템의 피드백 루프가 추천 품질을 저하하고 사용자 행동을 동질화함. "피드백 과정에서 추천 시스템이 이후 업데이트에 사용되는 사용자 행동 데이터를 영향하여, 윤리적/성능적 우려를 야기하는 피드백 루프를 생성"
- 체계적 문헌리뷰(arXiv:2509.00109): 347편 스크리닝, 24편 1차 연구(2019-2025). AI 피드백 루프가 시간이 지남에 따라 편향을 증폭하고 공정성을 저하. **대부분의 편향 완화 기법이 정적 분할에서만 테스트되어, 다중 재훈련 라운드의 장기 효과는 불명확**
- Baumann et al.(arXiv:2503.20231, EPJ Data Science 2026): TikTok 봇 감사 → 관심사 부합 콘텐츠의 강한 증폭, **처음 200개 영상 시청 내 급속 강화(rapid reinforcement)**. 증폭과 탐색 간 강한 음의 상관: 증폭 ↑ → 콘텐츠 다양성 ↓
- Lasser et al.(Annals of the New York Academy of Sciences, 2025): 사회적 선을 위한 추천 알고리즘 설계 필요성 — 현재 최적화 목표가 인게이지먼트에 편중되어 콘텐츠 다양성/품질 저하 야기

**인과 방향성 쟁점:**
이것이 이 연구의 핵심 딜레마다. 두 가지 경쟁 가설이 존재한다:
- **가설 A (알고리즘 원인론):** 알고리즘의 인게이지먼트 최적화가 AI 슬롭에 체계적으로 유리한 환경을 조성 → 생산자가 합리적으로 슬롭 생산에 진입 → 더 많은 슬롭 → 알고리즘 학습 데이터가 슬롭에 오염
- **가설 B (슬롭 착취론):** AI 슬롭 생산자가 알고리즘의 약점(engagement proxy, cold start popularity bias)을 의도적으로 착취 → 고빈도 업로드와 클릭베이트로 지표 조작 → 알고리즘은 사후적으로 이를 반영
- **가설 C (공진화):** 알고리즘과 슬롭이 상호 강화하는 공진화(co-evolution) 관계. 어느 한쪽이 원인이라기보다 시스템 수준의 창발적 현상(emergent phenomenon)

**현실적 판단:** 가설 C(공진화)가 가장 개연성이 높다. arXiv(2602.06437)의 주의 경제 공진화 모델이 이를 수학적으로 지지: "청중의 콘텐츠 품질 구별 능력이 약할 때, 선택적 주의와 고품질 생산이 동시에 사라지며, 정보적 붕괴(informational collapse)로 이어진다." 그러나 학술적 기여를 위해서는 이 공진화의 메커니즘, 시간적 역학, 개입 가능성을 구체적으로 밝혀야 한다.

### RQ4. 알고리즘 변경은 슬롭 유행에 어떤 영향을 미치는가?

**구체적 질문:**
- 유튜브의 "does this feel like AI slop?" 사용자 피드백 시스템(2026.03)은 슬롭 노출 비율을 실질적으로 감소시키는가?
- 인스타그램의 합성 콘텐츠 페널티(2026.01)는 AI 슬롭 도달률에 얼마나 영향을 미치는가?
- 유튜브의 AI 슬롭 채널 수익 정지/삭제 조치의 생태계 수준 효과는 무엇인가?
- 한국의 AI 라벨링 의무제(2026.01 시행)는 슬롭 생산/소비 행태를 변화시키는가?
- Sora 서비스 종료(2026.03.24)는 AI 영상 슬롭 생산량에 영향을 미치는가?

**각 자연실험의 상세 정보:**

| 자연실험 | 시기 | 유형 | 데이터 가용성 | RDD/DiD 적합성 |
|----------|------|------|--------------|----------------|
| YouTube "AI slop?" 피드백 | 2026.03 | 플랫폼 개입 | 외부 관측 가능 (sock puppet) | DiD 가능 |
| Instagram 합성 콘텐츠 페널티 | 2026.01 | 알고리즘 변경 | 크리에이터 도달 데이터 | DiD 가능 |
| YouTube 슬롭 채널 삭제/수익정지 | 2025.07-2026.01 | 집행 조치 | Social Blade, YouTube API | 이벤트 스터디 |
| 한국 AI 라벨링 의무제 | 2026.01.22 | 법적 규제 | 플랫폼 표시 데이터 | RDD 가능 |
| Sora 서비스 종료 | 2026.03.24 | 도구 소멸 | 업로드 패턴 분석 | DiD 가능 |
| YouTube 수익화 정책 변경 | 2025.07.15 | 경제적 인센티브 | Social Blade | 이벤트 스터디 |

### RQ5. 플랫폼의 경제 모델(광고 수익 분배)이 슬롭에 대한 구조적 인센티브를 만드는가?

**구체적 질문:**
- 조회수 기반 광고 수익 분배 모델은 AI 슬롭 생산을 경제적으로 합리적인 행위로 만드는가?
- 슬롭 채널의 CPM/RPM 구조와 진성 크리에이터의 그것은 어떻게 다른가?
- 수익 정지/삭제 조치가 슬롭 생산의 경제적 인센티브를 실질적으로 제거하는가?

**현재 근거:**
- 278개 AI 슬롭 채널 추정 연간 광고 수익: $117M (~1,600억원)
- 한국 AI 슬롭 채널 추정 연간 수익: ~1,700억원
- YouTube 수익화 정책: RPM $0.25~$4.00 범위, 슬롭의 대량 생산 구조에서 낮은 RPM도 총량으로 상쇄
- Social Blade의 수익 추정 정확도 한계: +/-50%, CPM이 니치/국가/기기/시즌에 따라 10배 이상 변동
- 2026년 초 유튜브 16개 대형 AI 채널 삭제 → 3,500만 구독자, 47억 뷰 소멸, 연간 추정 $10M 수익 증발
- Madsen & Puyt(2026): "수익화 프로그램이 가치(value) 대신 볼륨(volume)을 적극적으로 보상하는 구조가 핵심 문제"

---

## 2. 인과관계 분석 프레임워크 (Causal Inference Framework)

### 2-1. 핵심 인과 도전: "블랙박스 문제"

플랫폼 알고리즘 연구의 근본적 한계를 직시해야 한다.

**Casper et al.(FAccT 2024): "Black-Box Access is Insufficient for Rigorous AI Audits"**
- "유한한 수의 쿼리로 블랙박스 시스템에 대한 보증을 하는 것은 추가 가정 없이 불가능하다"
- "부실한(예: 블랙박스) 감사는 역효과를 낳을 수 있다: 거짓된 근거로 대중/규제 기관의 신뢰를 높여, 적절한 수준의 외부 감시를 방해한다"
- 화이트박스/아웃사이드-더-박스 접근이 블랙박스 단독보다 본질적으로 더 많은 정밀 조사를 허용

**이것이 우리 연구에 의미하는 바:**
플랫폼 내부 접근 없이 알고리즘-슬롭 간 **엄밀한 인과관계**를 확립하는 것은 원칙적으로 불가능하다. 그러나 이것이 연구를 포기할 이유는 되지 않는다. 세 가지 이유:
1. **관측적/준실험적 증거도 정책 결정에 충분히 유용하다.** 흡연-폐암 연구도 최초에는 관측 연구였다.
2. **자연실험이 풍부한 시기다.** 2025-2026년에 유례없이 많은 알고리즘 변경/규제 시행이 동시다발적으로 발생하여, 준실험적 설계의 기회가 풍부하다.
3. **블랙박스 한계를 투명하게 인정하는 것 자체가 학술적 기여다.** 무엇을 알 수 있고 무엇을 알 수 없는지를 명확히 하는 것은 이 분야에 필요한 인식론적 정직성이다.

### 2-2. 인과 추론 방법론 도구 세트

본 연구에 적용 가능한 인과 추론 방법론을 다층적으로 구성한다:

#### (1) 알고리즘 감사 (Algorithm Audit) — Sock Puppet 방법론

**방법:** 프로그래밍된 봇 계정(sock puppet)을 플랫폼에 배치하여, 알고리즘이 다양한 페르소나에 어떻게 반응하는지 관측

**선행 연구 기반:**
- Baumann et al.(2025/2026): TikTok 봇 감사 → 200개 영상 내 급속 강화 발견 (EPJ Data Science)
- arXiv:2501.15048: 유튜브 감정 편향 감사 → 분노/불만 등 부정 감정 증폭 발견 (Emotionally-Agentic Sock Puppets)
- FAccT 2025: X(트위터) 120개 sock puppet 계정으로 정치적 노출 편향 감사 → 우파 성향 계정의 최고 불평등 발견
- Springer(2024): "Auditing the audits" — 소셜 미디어 추천 시스템 감사 방법론 자체의 체계적 평가

**구체적 실험 설계:**
```
실험군: AI 슬롭 콘텐츠에 인게이지먼트(좋아요, 시청 완료)를 보이는 봇
대조군 1: AI 슬롭과 유사 주제의 인간 콘텐츠에 인게이지먼트를 보이는 봇
대조군 2: 인게이지먼트 없이 패시브하게 시청만 하는 봇
대조군 3: 완전 새 계정(cold start, 아무 인게이지먼트 없음)

측정 변수:
- AI 슬롭 추천 비율 (전체 추천 중 AI 슬롭의 비율)
- 추천 다양성 지수 (Shannon entropy)
- 증폭 속도 (첫 200개 영상 내 AI 슬롭 비율의 시계열 변화)
- 탐색-착취 비율 (새 해시태그/채널 vs 기존 해시태그/채널)
```

**이 방법의 강점과 한계:**
| 강점 | 한계 |
|------|------|
| 통제된 실험 설계 가능 | 봇 탐지에 의한 추방 리스크 |
| 플랫폼 협조 불필요 | 실제 사용자 경험과 차이 가능 |
| 반복 가능(replicable) | TOS 위반 윤리 논쟁 |
| 인과적 추론에 근접 | 알고리즘 업데이트 시 결과 무효화 가능 |

#### (2) 이중차분법 (Difference-in-Differences, DiD)

**원리:** 처리(treatment) 전후, 처리군과 대조군의 결과 변수 차이의 차이를 추정하여 인과 효과를 식별

**적용 가능한 자연실험:**

**(a) Instagram 합성 콘텐츠 페널티 (2026.01)**
```
처리군: AI 생성/합성 콘텐츠를 주로 게시하는 계정
대조군: 인간 제작 콘텐츠를 주로 게시하는 계정
처리 시점: 2026년 1월 (알고리즘 페널티 시행)
결과 변수: 도달률(reach), 인게이지먼트율, 팔로워 증가율
데이터 소스: Meta Content Library API (학술 연구자 접근 가능)
```

**(b) YouTube 슬롭 채널 수익정지 (2025.07)**
```
처리군: AI 슬롭 채널이 활동하던 장르/카테고리
대조군: AI 슬롭이 상대적으로 적은 장르/카테고리
처리 시점: 2025년 7월 15일 (수익화 정책 변경)
결과 변수: 장르별 평균 조회수 분포, 진성 크리에이터 성과 변화
데이터 소스: Social Blade, YouTube Data API
```

**(c) Sora 서비스 종료 (2026.03.24)**
```
처리군: AI 영상 생성 도구 의존도가 높은 콘텐츠 카테고리
대조군: AI 영상 생성 도구와 무관한 카테고리
처리 시점: 2026년 3월 24일
결과 변수: 신규 AI 슬롭 영상 업로드 빈도, AI 슬롭 추천 비율
주의: Sora 외 대안 도구(Runway, Pika, Kling AI) 존재로 인해 효과 약화 예상
```

**DiD의 핵심 가정 — 평행 추세(parallel trends):**
평행 추세 가정의 검증이 필수적이다. 처리 전 기간(pre-treatment period)의 처리군과 대조군 추세가 평행했음을 입증해야 한다. 이것이 위반되면 인과 추론은 무효화된다. 방법론적으로 Difference-in-Discontinuities(DiDC) 설계를 혼합하여 평행 추세 가정의 불확실성에 대한 백업으로 활용 가능 (Albright, 2024).

#### (3) 회귀불연속설계 (Regression Discontinuity Design, RDD)

**적용 가능한 자연실험:**

**(a) 한국 AI 라벨링 의무제 (2026.01.22 시행)**
```
불연속점: 2026년 1월 22일 (AI 기본법 시행일)
처리: "현실과 구분이 어려운 합성 음성/이미지/영상"에 AI 생성 표시 의무
결과 변수:
  - AI 슬롭 업로드 빈도 변화
  - 한국 발 AI 슬롭 콘텐츠의 라벨 부착 비율
  - 라벨 부착 콘텐츠 vs 미부착 콘텐츠의 인게이지먼트 차이
데이터: YouTube Data API (한국어 콘텐츠 필터링), 플랫폼 표시 데이터
```

**(b) YouTube 수익화 정책 변경 (2025.07.15)**
```
불연속점: 2025년 7월 15일
처리: "AI 슬롭" 타겟 수익 정지/삭제 시작
결과 변수: 채널 수준 수익/조회수 변화
데이터: Social Blade 일별 데이터
```

#### (4) 이벤트 스터디 (Event Study) / 합성 통제법 (Synthetic Control Method)

**대규모 이벤트 분석:**
- YouTube의 16개 대형 AI 채널 삭제(2026.01) 이벤트를 활용
- 3,500만 구독자, 47억 뷰 소멸이라는 외생적 충격(exogenous shock)
- 해당 채널이 활동하던 장르에서 진성 크리에이터의 성과 변화를 합성 통제법으로 추정
- "슬롭이 없어지면 진성 콘텐츠가 부활하는가?" → 그레셤의 법칙 역전 검증

#### (5) 도구변수법 (Instrumental Variables, IV)

**잠재적 도구변수:**
- AI 영상 생성 도구의 가용성 변화 (Sora 출시/종료)를 도구변수로 활용 가능
- 논리: Sora 가용성 → AI 슬롭 생산량(관련성) / Sora 가용성 → 알고리즘 추천(배제 제약 — 직접 영향 없음)
- 한계: 배제 제약(exclusion restriction) 위반 가능성 — Sora가 알고리즘 자체에 영향을 미칠 경로 존재

### 2-3. 통합적 인과 추론 전략

단일 방법론으로는 블랙박스 문제를 극복할 수 없다. **삼각측량(triangulation)** 전략을 채택한다:

```
                    [인과 추론 삼각측량]

           Sock Puppet 감사 (실험적)
                /              \
               /                \
              /   인과 추론의    \
             /    수렴적 증거    \
            /    (convergent     \
           /      evidence)      \
          /                       \
 DiD/RDD 자연실험 ────────── 이론적 모델링
 (준실험적)                    (시뮬레이션)
```

- **Sock puppet 감사:** 알고리즘의 AI 슬롭 편향을 직접 측정 (가장 인과적)
- **DiD/RDD 자연실험:** 알고리즘/규제 변경의 인과 효과를 추정 (준실험적)
- **이론적 모델링:** 피드백 루프의 수학적 모델 구축 (arXiv:2602.06437의 주의 경제 공진화 모델을 확장)

세 가지 접근의 결과가 수렴하면, 블랙박스에도 불구하고 강건한(robust) 인과적 증거를 구축할 수 있다.

---

## 3. 실증 가능성 (Empirical Feasibility) — 솔직한 평가

### 3-1. Sock Puppet 감사

**선례:**
| 연구 | 플랫폼 | 봇 수 | 주요 발견 | 방법론적 시사점 |
|------|--------|-------|-----------|----------------|
| Kapwing(2025) | YouTube | 관측 연구 | 21-33% AI 슬롭 | 대규모 트렌딩 분석 |
| Baumann et al.(2026) | TikTok | 다수 봇 | 200영상 내 급속 강화 | 시계열 + Markov 모델 |
| arXiv:2501.15048 | YouTube | 감정 봇 | 부정 감정 증폭 | 감정-봉입 sock puppet |
| FAccT 2025 | X (Twitter) | 120개 | 정치 성향 편향 | 4개 페르소나 설계 |
| Mozilla Rally | 다중 | 크라우드소싱 | 추천 데이터 수집 | 실사용자 참여 |
| Algorithm Watch | YouTube | 다수 | 추천 편향 | 독립 감사 기관 |

**실행 가능성 평가:**
- 기술적 난이도: **중** (Selenium/Playwright 기반 자동화, YouTube API 보조)
- 비용: **낮음** (클라우드 서버 비용 + 개발 인력)
- 시간: **2-3개월** (봇 배치 + 데이터 수집)
- 윤리적 리스크: **높음** (TOS 위반 가능성, IRB 심의 필요)
- 탐지 리스크: **중-높음** (YouTube의 봇 탐지 정교화 추세)

**실행 가이드:**
1. IRB 심의 시 "공익적 알고리즘 감사" 목적 명시
2. 수집 데이터를 개인 식별이 불가능한 수준으로 집계
3. Springer(2024) "Auditing the audits" 논문의 방법론적 권고 준수
4. 한국 유튜브 특화: 한국어 콘텐츠, 한국 IP, 한국어 인터페이스 설정

### 3-2. 자연실험 활용

**2025-2026년은 자연실험의 황금기다.**

| 이벤트 | 날짜 | DiD 실행 가능성 | 데이터 접근성 | 독립 연구자 실현 가능성 |
|--------|------|-----------------|--------------|------------------------|
| YouTube 수익화 정책 변경 | 2025.07.15 | **높음** | Social Blade | **높음** |
| Instagram 합성 콘텐츠 페널티 | 2026.01 | **높음** | MCL API | **중** (학술 접근 필요) |
| 한국 AI 기본법 시행 | 2026.01.22 | **높음** | 다중 소스 | **높음** |
| YouTube "AI slop?" 피드백 | 2026.03 | **중** | sock puppet | **중** |
| Sora 서비스 종료 | 2026.03.24 | **중** | 업로드 패턴 | **중** (대안 도구 존재) |
| YouTube 16개 대형 채널 삭제 | 2026.01 | **높음** | Social Blade | **높음** |

**가장 실현 가능한 자연실험 우선순위:**
1. **YouTube 수익화 정책 변경 + 대형 채널 삭제** — 데이터 접근성 최상, Social Blade 무료/유료 데이터 활용 가능, 사전-사후 비교 명확
2. **한국 AI 기본법 시행** — 명확한 법적 불연속점, 한국 특화 연구의 차별성, 정책 함의 직접적
3. **Instagram 합성 콘텐츠 페널티** — Meta Content Library API 접근이 관건

### 3-3. API 접근성 — 현실적 평가

**YouTube Data API v3:**
- **일일 쿼터:** 기본 10,000 유닛/프로젝트 (대규모 연구에 부족)
- **핵심 제약 (arXiv:2506.11727, "Forgetful by Design?"):**
  - 동영상 발견 가능성의 심각한 시간적 감쇠: 게시 20-60일 내 검색 가능 영상 수 급감
  - 검색 결과 비일관성: 동일 쿼리가 시간에 따라 다른 영상 세트 반환
  - 누락 데이터: 영상 트랜스크립트 불가, 쇼츠 식별 플래그 부재, 수익화 여부 불명, 채널/영상 삭제 사유 불명
- **연구자 프로그램:** 검증된 프로젝트에 확장 접근 제공, 그러나 범위 제한적이고 플랫폼 검증 프로세스 필요

**Tandfonline(Information, Communication & Society, 2025)** "Forgetful by design?" 논문의 핵심 경고:
> YouTube 검색 API가 학술 연구에 구조적으로 부적합하며, 이 한계를 인식하지 못한 연구는 타당성에 심각한 문제를 가질 수 있다.

**Meta Content Library API:**
- CrowdTangle 종료(2024.08.14) 이후의 대체 도구
- **접근 자격:** 학술 기관 또는 비영리 연구 기관 소속 필수
- **보안 환경:** Meta Secure Research Environment 또는 SOMAR Virtual Data Enclave에서만 접근
- R/Python 프로그래밍 필요
- Instagram Reels 데이터 포함 — 합성 콘텐츠 페널티 연구에 활용 가능

**Social Blade:**
- 채널 수준 일별 구독자/조회수 데이터 접근 가능
- 수익 추정 정확도: **+/-50%** — RPM $0.25-$4.00 범위의 단순 모델
- "CPM이 니치, 시청자 국가, 기기, 시즌, 영상 길이, 광고 형태, 청중 참여에 따라 10배 이상 변동"
- **연구 활용 시 주의:** 수익 추정은 상대적 비교 용도로만 사용하고, 절대값으로 보고하지 말 것

### 3-4. 수익 데이터 — 피드백 루프의 경제적 차원

**측정 가능한 것:**
- Social Blade: 채널별 조회수 추세, 구독자 추세 (일별)
- YouTube API: 영상별 조회수, 좋아요, 댓글 수
- Kapwing 보고서: 슬롭 채널 식별 + 추정 수익 ($117M/년)

**측정 불가능한 것:**
- 실제 CPM/RPM (플랫폼 내부 데이터)
- 스폰서십, 멤버십, 슈퍼챗 수익 (Social Blade 추정에 미포함)
- 광고주의 AI 슬롭 채널 이탈률 (브랜드 안전성 데이터)

**피드백 루프 측정에 필요한 데이터:**
```
이상적 데이터셋:
1. 시계열 추천 데이터: 특정 계정이 t시점에 받은 추천 목록 (sock puppet으로 수집 가능)
2. 콘텐츠 분류: 각 추천 영상의 AI 슬롭 여부 (분류기 개발 필요)
3. 인게이지먼트 반응: 봇의 시청/좋아요/스킵 행동 (실험 설계로 통제)
4. 후속 추천 변화: 인게이지먼트 후 추천 패턴 변화 (시계열 추적)
5. 생산자 반응: 신규 AI 슬롭 업로드 빈도 변화 (YouTube API/크롤링)
6. 경제적 피드백: 채널 수익 변화와 생산량 변화의 관계 (Social Blade)
```

**현실적으로 수집 가능한 데이터:** 1, 3, 4, 5, 6 (부분적)
**핵심 병목:** 2 (AI 슬롭 분류기의 정확도가 전체 연구의 타당성을 좌우)

---

## 4. 기존 연구 분석 (Literature Review)

### 4-1. 알고리즘 증폭 연구

| 연구 | 핵심 발견 | 우리 연구와의 관계 |
|------|-----------|-------------------|
| Baumann et al. (2025/2026) "Dynamics of Algorithmic Content Amplification on TikTok" | 200영상 내 급속 강화, 증폭-탐색 간 음의 상관, 지속적 콘텐츠 강화와 다양성 점진적 감소 | **직접 참조 모델.** 동일 sock puppet 방법론을 YouTube에 적용하되, AI 슬롭 특화 분석 추가 |
| arXiv:2501.15048 "YouTube Recommendations Reinforce Negative Emotions" | 유튜브가 분노/불만 등 부정 감정을 증폭, 감정-봉입(emotionally-agentic) 봇 방법론 | AI 슬롭의 감정 자극 특성과 연결. 감정적 인게이지먼트가 슬롭 증폭의 매개변수일 수 있음 |
| FAccT 2025 "Auditing Political Exposure Bias" | X에서 120개 sock puppet으로 정치적 편향 감사, 고인기 사용자에 대한 노출 편중 | 방법론적 템플릿 제공. 동일 설계를 AI 슬롭 맥락에 적용 가능 |
| Springer(2024) "Auditing the audits" | 소셜 미디어 추천 시스템 감사 방법론 자체의 체계적 평가 | 방법론적 타당성 확보를 위한 필수 참조 |
| Raymond(2025) "The Market Effects of Algorithms" | 알고리즘이 사용자 주의 할당을 통해 경쟁 생산자 간 경제적 가치를 재분배 | 슬롭의 경제적 영향 분석 프레임워크 |

### 4-2. 주의 경제 및 콘텐츠 품질 저하 연구

| 연구 | 핵심 발견 | 우리 연구와의 관계 |
|------|-----------|-------------------|
| arXiv:2602.06437 "An attention economy model of co-evolution between content quality and audience selectivity" | 청중의 품질 구별 능력이 약하면 선택적 주의와 고품질 생산이 동시에 사라져 정보적 붕괴로 이어짐 | **핵심 이론 모델.** 피드백 루프의 수학적 기초 제공. "건전한 정보 생태계 유지에는 적절한 청중 변별력과 충분한 고노력 창작 인센티브가 필요" |
| Madsen & Puyt (2026) "7Vs of AI Slop" | 7차원 분류 체계, "산업적 슬롭 농장" 개념, Visibility(알고리즘 증폭) 차원 강조 | 슬롭의 알고리즘적 증폭을 이론적으로 체계화. Visibility 차원의 실증적 검증이 우리 연구의 핵심 기여 |
| arXiv:2509.00109 "Bias Mitigation for AI-Feedback Loops in Recommender Systems" | 347편 스크리닝, 24편 분석. 대부분 정적 분할 테스트, 다중 재훈련 장기 효과 불명확 | 피드백 루프의 장기 편향 축적에 대한 실증 공백 확인 |
| Cambridge Core "Algorithmic Attention Rents" | 알고리즘이 사용자 주의 할당에서 "주의 지대(attention rents)"를 추출하여 시장 지배력 행사 | 플랫폼 경제학적 프레임워크. 슬롭 증폭이 플랫폼의 경제적 이해와 구조적으로 정렬됨을 설명 |
| Lasser et al. (2025) "Designing social media content recommendation algorithms for societal good" | 인게이지먼트 편중 최적화가 콘텐츠 다양성/품질 저하 야기. 사회적 선을 위한 설계 필요 | 규범적(normative) 차원. 알고리즘 재설계에 대한 정책 함의 |

### 4-3. 플랫폼 경제학 및 그레셤의 법칙 연구

| 연구/이론 | 핵심 주장 | 적용 |
|-----------|-----------|------|
| arXiv:2410.13101 "Impact of GenAI on Content Platforms: Two-Sided Market Analysis" | GenAI가 기술적 품질과 가격 하락을 통해 소비자 잉여를 향상하나, 스킬 기반 인적 인컴번트를 대체하고 시장 집중을 심화 | 양면시장 관점에서 슬롭의 구조적 역할 분석. 소비자 단기 이익 vs 생태계 장기 피해 |
| PMC: "Engagement, user satisfaction, and the amplification of divisive content on social media" | 인게이지먼트 기반 알고리즘이 사용자가 직접 평가하면 선호하지 않는 콘텐츠를 증폭 | **핵심 발견.** 인게이지먼트 ≠ 사용자 만족. 알고리즘은 "클릭은 했지만 후회하는" 콘텐츠를 증폭. 이것이 AI 슬롭 증폭의 핵심 메커니즘일 수 있음 |
| FourWeekMBA "The Attention Economy Collapse" | AI가 자체 생성 콘텐츠를 다시 소비하는 재귀적 루프 → 각 반복마다 정보 품질 저하 | 이론적 극한 시나리오. 슬롭의 장기적 귀결 |
| Gresham's Law for content (Medium/학술) | 알고리즘이 깊은 콘텐츠와 피상적 콘텐츠에 동등한 "가치"(인게이지먼트)를 부여하면, 생산자는 저비용 생산에 인센티브 | 슬롭이 진성 콘텐츠를 구축하는 메커니즘의 경제학적 설명 |

### 4-4. 알고리즘 게이트키핑 이론

| 연구 | 핵심 주장 | 적용 |
|------|-----------|------|
| Gorwa et al.(2020) "Algorithmic content moderation" | 콘텐츠 모더레이션은 커뮤니티 참여를 구조화하는 거버넌스 메커니즘 | AI 슬롭 대응이 콘텐츠 모더레이션의 새로운 전선임을 이론화 |
| Bruns(2025) "Algorithmic gatewatching" | 알고리즘 게이트워칭 개념 — 알고리즘이 게이트키퍼 역할을 하는 것을 감시하는 외부자의 역할 | 우리 연구의 메타적 위치 정의: 알고리즘 게이트키퍼에 대한 게이트워칭 |
| MDPI(2025) "Reconceptualizing Gatekeeping in the Age of AI" | AI 시대 게이트키핑 재개념화 — 의제 설정, 프레이밍 이론과 알고리즘 추천 통합 | "인게이지먼트 튜닝 → 주의 끌기 콘텐츠 게이트키핑" — 슬롭이 게이트를 통과하는 이유 |
| Liang et al.(2025) "Content Creation within the Algorithmic Environment" | 알고리즘 환경 내 콘텐츠 창작의 체계적 리뷰 | 생산자가 알고리즘에 적응하여 콘텐츠를 변형하는 메커니즘 — 슬롭 생산의 합리적 선택 측면 |

---

## 5. 이론적 프레임워크 (Theoretical Framework)

### 5-1. 통합 이론 모델: "알고리즘-슬롭 공진화 모델(Algorithm-Slop Co-evolution Model)"

본 연구는 6개의 이론을 통합하여 알고리즘과 AI 슬롭 간의 인과적 역학을 다층적으로 분석한다:

```
[거시 수준: 생태계]
┌─────────────────────────────────────────────────────┐
│  주의 경제학 (Simon, 1971; Wu, 2017)                │
│  "정보의 풍요 = 주의의 빈곤"                         │
│  → 유한한 주의 자원을 두고 슬롭과 진성 콘텐츠 경쟁  │
│                                                     │
│  그레셤의 법칙 for Content (Grimmelmann)             │
│  "나쁜 콘텐츠가 좋은 콘텐츠를 구축한다"              │
│  → 인게이지먼트가 동일하면 저비용 생산이 합리적      │
│                                                     │
│  공유재의 비극 (Hardin, 1968)                        │
│  → 개별 슬롭 생산자의 합리적 선택이                 │
│    정보 생태계 전체를 오염시키는 외부성              │
└────────────────────────┬────────────────────────────┘
                         │
[중범위 수준: 플랫폼]     │
┌────────────────────────┴────────────────────────────┐
│  플랫폼 경제학 (양면시장: Rochet & Tirole, 2003)     │
│  → 플랫폼은 사용자 주의를 광고주에 판매              │
│  → 인게이지먼트 최대화 = 수익 최대화                │
│  → 슬롭 억제와 수익 극대화 간 구조적 갈등           │
│                                                     │
│  알고리즘 게이트키핑 (Napoli, 2014; Bruns, 2025)     │
│  → 알고리즘이 가시성(visibility)의 배분자            │
│  → "인게이지먼트 최적화 = 슬롭 게이트 개방"          │
│                                                     │
│  피드백 루프 이론 (arXiv:2207.01616)                 │
│  → 알고리즘 추천 → 사용자 행동 → 재훈련 → 편향 증폭│
└────────────────────────┬────────────────────────────┘
                         │
[미시 수준: 개인]         │
┌────────────────────────┴────────────────────────────┐
│  주의 경제 공진화 모델 (arXiv:2602.06437, 2026)      │
│  → 청중 변별력(audience discriminability)이 약하면   │
│    고품질 생산과 선택적 주의가 동시에 사라짐          │
│  → 숏폼의 구조적 제약이 변별력을 약화시킴            │
│                                                     │
│  인게이지먼트 ≠ 만족 괴리 (PMC, 2025)               │
│  → 사용자는 클릭했지만 후회하는 콘텐츠를             │
│    알고리즘은 "선호"로 학습                          │
│  → AI 슬롭의 "표면적 역량"이 이 괴리를 착취         │
└─────────────────────────────────────────────────────┘
```

### 5-2. 핵심 이론별 상세 적용

#### (1) 주의 경제학 (Attention Economy)

**원천:** Simon(1971), Goldhaber(1997), Wu(2017)

**AI 슬롭 맥락 적용:**
- Simon: "정보의 풍요는 주의의 빈곤을 의미한다" → AI 생성형 도구가 콘텐츠 생산의 한계비용을 제로에 근접하게 만들면서 정보 풍요가 극한으로 치닫고, 주의 빈곤이 심화
- Wu(2017): 주의력의 상품화(commodification of attention) → 플랫폼이 사용자 주의를 광고주에게 판매하는 비즈니스 모델에서, AI 슬롭은 주의력 추출에 최적화된 "주의력 해킹" 도구
- arXiv(2602.06437): 주의 경제의 공진화 모델 → **"건전한 정보 생태계 유지에는 적절한 청중 변별력(audience discriminability)과 충분한 고노력 창작 인센티브가 필요"** — 현재 두 조건 모두 약화되고 있음

**측정 가능 변수:**
- 주의 시간 배분: AI 슬롭 vs 진성 콘텐츠에 할당되는 시청 시간 비율
- 주의의 질: 완료율, 되감기, 반복 시청 등 깊은 인게이지먼트 지표
- 주의 이동: 슬롭 시청 후 다음 선택 패턴

#### (2) 플랫폼 경제학 (Platform Economics)

**원천:** Rochet & Tirole(2003), Parker, Van Alstyne & Choudary(2016)

**AI 슬롭 맥락 적용:**
- 양면시장(two-sided market): 플랫폼은 콘텐츠 생산자와 소비자를 연결하되, 실질적 고객은 광고주
- 교차 네트워크 효과(cross-side network effects): 더 많은 콘텐츠 → 더 많은 시청자 → 더 많은 광고 수익 → 더 많은 생산 인센티브. AI 슬롭은 이 사이클의 "양" 측면을 극대화하되 "질"은 무시
- 승자 독식(winner-take-all): 알고리즘적 가시성이 극소수 콘텐츠에 집중 → 조회수의 멱법칙(power law) 분포 → 슬롭이 이 소수에 진입하면 막대한 수익
- **구조적 갈등:** 플랫폼의 단기 이익(인게이지먼트/광고 수익 극대화) vs 장기 이익(사용자 신뢰/플랫폼 품질) → 슬롭 억제는 단기 수익 감소를 수반

**Cambridge Core "Algorithmic Attention Rents"(2025):**
> 알고리즘이 사용자 주의 할당에서 "주의 지대(attention rents)"를 추출하여 시장 지배력을 행사한다.

이는 플랫폼이 슬롭 증폭에서 경제적 이해를 가진다는 것을 의미한다 — 슬롭이 인게이지먼트를 생성하는 한, 플랫폼은 이를 억제할 경제적 동기가 약하다. 2026년의 anti-slop 조치는 이 갈등이 장기 이익(사용자 이탈 방지, 브랜드 안전성) 쪽으로 기울어진 결과일 수 있다.

#### (3) 디지털 콘텐츠의 그레셤의 법칙 (Gresham's Law for Digital Content)

**원천:** Gresham's Law(경제학), Grimmelmann(디지털 적용)

**AI 슬롭 맥락 적용:**
원래의 그레셤의 법칙: 액면가가 동일하면 사람들은 금화를 비축하고 구리 동전을 유통시킨다 → "나쁜 화폐가 좋은 화폐를 구축한다."

디지털 콘텐츠 적용:
- "인게이지먼트"라는 화폐가 깊은 콘텐츠와 피상적 콘텐츠에 동등한 "액면가"를 부여
- 생산자는 합리적으로 저비용(AI 슬롭) 생산을 선택
- 고비용(인간 제작) 콘텐츠는 경제적으로 불리해져 "비축"(생산 축소)

**경제학적 메커니즘:**
```
AI 슬롭의 한계비용 ≈ 0 (전기비 + API 비용)
인간 콘텐츠의 한계비용 = 시간 + 기술 + 장비 + 노동

인게이지먼트 단위당 수익이 동일하다면:
→ AI 슬롭의 ROI >>> 인간 콘텐츠의 ROI
→ 합리적 행위자는 AI 슬롭 생산을 선택
→ 시장에 AI 슬롭이 범람 → 전체 콘텐츠 품질 하락
```

**실증 검증 방안:**
- H3a(기존 프레임워크): AI 슬롭 채널 시장점유율 증가 → 동일 장르 진성 크리에이터 수익 감소 (부의 관계)
- 이벤트 스터디: YouTube 16개 대형 AI 채널 삭제 후 해당 장르 진성 크리에이터 성과 변화 → "슬롭 제거 시 그레셤의 법칙이 역전되는가?"

#### (4) 알고리즘 게이트키핑 이론 (Algorithmic Gatekeeping Theory)

**원천:** Napoli(2014), Bruns(2025), MDPI(2025)

**AI 슬롭 맥락 적용:**
- 전통적 게이트키핑: 편집자가 "뉴스 가치"에 따라 콘텐츠를 선별
- 알고리즘 게이트키핑: 알고리즘이 "인게이지먼트 잠재력"에 따라 콘텐츠를 선별
- MDPI(2025): "알고리즘이 인게이지먼트에 튜닝되면, 저널리즘적 중요성이나 전문적 편집 판단에 따른 콘텐츠를 거의 우선시하지 않는다"
- **AI 슬롭의 게이트 통과:** 슬롭은 인게이지먼트 최적화 게이트키핑 기준을 정확히 충족하도록 설계됨 — 클릭베이트 썸네일, 감정 유발, 호기심 갭

**Bruns(2025)의 "알고리즘 게이트워칭" 개념:**
우리 연구의 메타적 위치를 정의한다. 알고리즘이 게이트키퍼 역할을 하는 것을 외부에서 감시하는 행위 자체가 학술적/민주적 기능이다. Sock puppet 감사는 이 게이트워칭의 구체적 방법론이다.

#### (5) 피드백 루프 / 양의 되먹임 역학 (Positive Feedback Dynamics)

**원천:** arXiv:2207.01616, arXiv:2509.00109, Baumann et al.(2026)

**AI 슬롭에 적용한 피드백 루프 모델:**

```
[피드백 루프 단계]

1단계: 초기 추천 (cold start)
  알고리즘 → 인기도 기반 추천 → AI 슬롭의 높은 조회수가 인기도 지표에 반영
  → 신규 사용자에게 AI 슬롭이 불균형적으로 추천 (21-33%, Kapwing)

2단계: 인게이지먼트 학습
  사용자 → 슬롭에 클릭/시청/좋아요 (표면적 역량에 의한 주변 경로 반응)
  → 알고리즘: "이 사용자는 이 유형의 콘텐츠를 선호한다"

3단계: 증폭 (amplification)
  알고리즘 → 유사 슬롭 추천 강화 (Baumann et al.: 200영상 내 급속 강화)
  → 탐색(exploration) 감소, 필터 버블 형성

4단계: 생산 인센티브
  슬롭 생산자 → 높은 조회수/수익 관측 → 더 많은 슬롭 생산
  → 한계비용 ≈ 0이므로 대량 생산 합리적

5단계: 데이터 오염
  더 많은 슬롭 → 훈련 데이터에 슬롭 비율 증가
  → 알고리즘 재훈련 시 슬롭 친화적 패턴 학습
  → 1단계로 회귀 (루프 완성)

루프 속도: 4단계까지 수일~수주 (대량 생산자), 5단계는 알고리즘 업데이트 주기에 의존
```

**루프 파괴 메커니즘 (Loop Breaking):**
- **사용자 측:** 의식적 회피, AI 리터러시, "AI slop?" 피드백
- **플랫폼 측:** 알고리즘 변경, 수익 정지, 채널 삭제
- **규제 측:** 라벨링 의무, 징벌적 배상
- **도구 측:** 생산 도구 소멸 (Sora 종료)

#### (6) 공유재의 비극 (Tragedy of the Commons)

**원천:** Hardin(1968)

**AI 슬롭 맥락 적용:**
- 공유재 = 플랫폼의 콘텐츠 품질 / 사용자의 집합적 주의
- 개별 슬롭 생산자: 슬롭 생산의 사적 이익(수익) > 생태계 오염의 사적 비용(거의 영)
- 모든 생산자가 합리적으로 행동하면 → 공유재(콘텐츠 품질)가 고갈
- 외부성(externality): 슬롭 1개의 추가 비용은 생산자가 아닌 전체 생태계가 부담

**정책 함의:**
- 공유재의 비극 해법은 (1) 사유화, (2) 규제, (3) 공동체 거버넌스
- 현재 시도: 규제(라벨링 의무), 플랫폼 거버넌스(수익 정지), 커뮤니티(사용자 피드백)
- 미시도: 슬롭 생산의 외부성 내부화 (탄소세와 유사한 "슬롭세" 개념)

---

## 6. 약점 및 리스크 — 솔직한 평가

### 6-1. 블랙박스 문제: 이 연구는 가능한가?

**솔직한 답변: 엄밀한 인과관계 확립은 플랫폼 협력 없이 불가능하다. 그러나 강건한 준인과적 증거 구축은 가능하다.**

| 연구 목표 | 블랙박스 하에서의 달성 가능성 | 대안 |
|-----------|------------------------------|------|
| "알고리즘이 AI 슬롭을 증폭한다" 인과 증명 | **불가능** (내부 추천 로직 불가시) | sock puppet으로 증폭 패턴 관측 (상관 + 시간적 선행성) |
| "알고리즘 변경이 슬롭 노출을 감소시킨다" 인과 추정 | **가능** (DiD/RDD로 추정) | 자연실험 활용 |
| "피드백 루프가 존재한다" 증명 | **부분적 가능** (시계열 패턴으로 시사) | Granger 인과, 시계열 분석 |
| "플랫폼 경제 모델이 슬롭을 인센티브화한다" 분석 | **가능** (구조적 분석) | 경제학적 모델링 + Social Blade 데이터 |

**Casper et al.(FAccT 2024)의 경고를 내재화해야 한다:**
"부실한 감사가 역효과를 낳을 수 있다." 따라서:
- 인과적 주장의 범위를 방법론적 한계에 맞게 신중하게 제한
- "알고리즘이 슬롭을 촉진한다"(인과적) 대신 "알고리즘 환경에서 슬롭이 체계적으로 높은 가시성을 얻는다"(관측적)로 표현
- 블랙박스 한계를 논문에 명시적으로 기술하는 것 자체가 학술적 기여

### 6-2. 상관 ≠ 인과 문제

**핵심 딜레마:** AI 슬롭이 추천받기도 하고 높은 인게이지먼트를 갖기도 하는데, 무엇이 원인이고 무엇이 결과인가?

```
경로 A: 알고리즘이 슬롭 추천 → 슬롭에 노출 증가 → 인게이지먼트 발생
경로 B: 슬롭이 본질적으로 높은 인게이지먼트 → 알고리즘이 이를 학습 → 추천
경로 C: 둘 다 동시에 (공진화)
```

**분리 전략:**
1. **Sock puppet 실험:** 초기 cold start 상태에서의 추천 패턴 관측 → 사용자 인게이지먼트 이전에 알고리즘이 슬롭을 추천하는지 확인 (경로 A의 시간적 선행성 테스트)
2. **인게이지먼트 통제 실험:** 동일 주제의 AI 슬롭과 인간 콘텐츠에 동일한 인게이지먼트를 의도적으로 부여한 후 후속 추천 비교 (인게이지먼트를 통제한 상태에서의 알고리즘 편향 측정)
3. **자연실험:** 알고리즘 변경(외생적 충격) 전후의 슬롭 노출 변화 측정 → 알고리즘의 인과적 역할 추정

### 6-3. 시간적 유효성 (Temporal Validity) 리스크

**문제:** 알고리즘은 끊임없이 변화한다. 연구 수행 시점의 결과가 출판 시점에는 이미 무효화될 수 있다.

**완화 전략:**
- 특정 알고리즘 버전이 아닌, **구조적 메커니즘(인게이지먼트 최적화 → 슬롭 증폭)**에 초점
- 다중 시점 데이터 수집으로 변화 추적 (2025.07 → 2026.01 → 2026.03)
- 자연실험 설계는 특정 시점의 변화를 포착하므로 시간적 유효성이 높음
- 메타 수준의 질문: "알고리즘이 바뀌어도 같은 패턴이 반복되는가?" → 구조적 문제 vs 일시적 결함 구분

### 6-4. 플랫폼의 능동적 감사 저항

**현실적 리스크:**
- 유튜브 봇 탐지 정교화 → sock puppet 실험 방해
- API 쿼터 제한 → 대규모 데이터 수집 어려움
- TOS 위반 → 법적/윤리적 리스크
- "Forgetful by design" (arXiv:2506.11727) — YouTube 검색 API가 학술 연구에 구조적으로 부적합

**대응:**
- 법적: Ada Lovelace Institute(2025)의 "Technical methods for regulatory inspection" 보고서의 프레임워크 활용
- 윤리적: IRB 심의, 공익적 감사 목적 명시
- 기술적: 봇 탐지 회피가 아닌, 탐지될 수 있다는 한계를 인정하고 설계에 반영
- 대안적: 크라우드소싱(Mozilla Rally 모델) — 실제 사용자 자발적 참여로 추천 데이터 수집

### 6-5. 독립 연구자의 실현 가능성

**솔직한 답변: 제한적이지만 가능하다.**

| 자원 | 필요 수준 | 독립 연구자 접근 가능성 |
|------|-----------|------------------------|
| 플랫폼 내부 데이터 | 필수 (이상적) | **불가능** |
| YouTube Data API | 기본 쿼터 | **가능** (제한적) |
| Meta Content Library | 학술 기관 소속 | **조건부 가능** |
| Social Blade 유료 | 월 $100-500 | **가능** |
| 클라우드 컴퓨팅 (sock puppet) | 월 $200-500 | **가능** |
| AI 슬롭 분류기 개발 | ML 역량 필요 | **가능** (사전 훈련 모델 활용) |
| 대규모 서베이 (N=1,000+) | $5,000-10,000 | **연구비 필요** |

**최소 가능 연구(Minimum Viable Research):**
연구비 $0 기준으로:
1. YouTube Data API (무료) + Social Blade (무료 티어) → 채널 수준 분석
2. Selenium/Playwright 기반 sock puppet (개인 서버) → 소규모 추천 감사
3. 2025.07 수익화 정책 변경의 DiD 분석 → Social Blade 사전-사후 데이터
4. 한국 AI 기본법(2026.01.22) 시행 전후 RDD → YouTube API 한국어 필터링

이것만으로도 ICWSM 또는 CSCW 수준의 논문이 가능하다.

### 6-6. AI 슬롭 분류기 — 전체 연구의 병목

**문제:** 모든 분석의 전제는 "이 콘텐츠가 AI 슬롭인지 아닌지"를 판별하는 것인데, 이것 자체가 연구 문제다.

**현재 접근법:**
- Shaib et al.(arXiv:2509.19163): 텍스트 슬롭 측정 프레임워크 (정보 품질, 정보 효용, 문체 품질)
- Kapwing: 수동 분류 (연구자가 직접 시청/판단)
- 자동화 도구: AI 생성 텍스트 탐지기(GPTZero 등)의 한계 — false positive/negative 비율 높음

**우리의 전략:**
1. 1차: Kapwing 방식의 수동 분류로 골드 스탠다드 데이터셋 구축 (500-1,000개 영상)
2. 2차: 골드 스탠다드 기반 자동 분류기 훈련 (시각적/청각적 특징 + 메타데이터)
3. 3차: 분류기 정확도를 투명하게 보고하고, 민감도 분석(sensitivity analysis)으로 분류 오류의 영향 평가
4. 한계 인정: "완벽한 분류가 불가능하다"는 것을 명시하고, 분류 불확실성을 결과 해석에 반영

---

## 7. 학술적 임팩트 예측

### 7-1. 타겟 학술지/학회

| 학회/저널 | 분야 | 적합도 | 마감일 | 수락률 | 비고 |
|-----------|------|--------|--------|--------|------|
| **ICWSM 2026** | 웹/소셜 미디어 | **최적** | 2026.01 (지남) / 차기 | ~25% | 알고리즘 감사 + 대규모 데이터 분석 |
| **CSCW 2026** | 컴퓨터 지원 협력/사회 컴퓨팅 | **최적** | 롤링 (2025.05+) | ~25% | sock puppet + 사용자 경험 |
| **CHI 2027** | 인간-컴퓨터 상호작용 | **높음** | 2026.09 (예상) | ~25% | 사용자 인식/행동 실험 포함 시 |
| **FAccT 2027** | 공정성/책임/투명성 | **높음** | 2026 하반기 | ~25% | 알고리즘 감사 + 정책 함의 |
| **New Media & Society** | 미디어/커뮤니케이션 | **높음** | 수시 | 다양 | 이론적 프레임워크 + 실증 |
| **Information, Communication & Society** | 정보사회 | **높음** | 수시 | 다양 | YouTube API 한계 논문 게재 이력 |
| **EPJ Data Science** | 계산사회과학 | **높음** | 수시 | 다양 | Baumann et al. TikTok 논문 게재 |
| **AI & Society (Springer)** | AI/사회 | **높음** | 수시 | 다양 | Madsen & Puyt 7Vs 논문 게재 |

**전략적 투고 계획:**
1. **1차 타겟: ICWSM 2027 (2026 하반기 마감)** — sock puppet 감사 + DiD 자연실험 결과
2. **2차 타겟: CSCW 2027** — 한국 특화 분석 + 사용자 인식 데이터
3. **저널 옵션: New Media & Society** — 이론적 프레임워크 중심 + 정책 함의

### 7-2. 학술적 기여 (예상)

**기여 1: 알고리즘-슬롭 공진화의 최초 실증적 분석**
- 기존 연구: 알고리즘 증폭 연구(정치/감정 편향)와 AI 슬롭 연구(현황/분류)가 분리
- 본 연구: 알고리즘 증폭의 대상으로 AI 슬롭을 최초로 체계적 분석
- "플랫폼 알고리즘이 AI 슬롭을 어떻게 증폭하는가?"에 대한 최초의 실증적 답변 시도

**기여 2: 자연실험의 황금기를 활용한 준인과적 증거**
- 2025-2026년의 유례없는 다중 자연실험(6개 이상)을 체계적으로 활용
- DiD/RDD/이벤트스터디의 삼각측량으로 블랙박스 한계를 부분적 극복
- 방법론적 템플릿: 향후 알고리즘-콘텐츠 품질 연구에 재사용 가능

**기여 3: 한국 사례의 글로벌 학술적 가치**
- 한국 = AI 슬롭 소비 세계 1위 (84.5억 뷰) — 극단적 사례(extreme case)
- 동시에 세계 최초 종합 AI 법률(AI 기본법) 시행 → 규제 효과 연구의 최적 사례
- 한국 사례를 통해 글로벌 현상의 메커니즘을 밝히는 "극단적 사례 연구(extreme case study)" 전략

**기여 4: 블랙박스 한계의 투명한 인정이라는 인식론적 기여**
- "무엇을 알 수 있고 무엇을 알 수 없는가"를 명확히 하는 것
- Casper et al.(2024)의 경고를 내재화한 연구 설계
- 플랫폼 연구의 인식론적 정직성에 대한 방법론적 논의 촉진

### 7-3. 정책 함의 (Policy Implications)

**규제 기관 대상:**
- 알고리즘 투명성 의무화의 근거 제시: 슬롭 증폭이 알고리즘의 구조적 특성이라면, 블랙박스를 열어야 한다
- 한국 AI 기본법의 실효성 평가 데이터 제공
- EU DSA(디지털 서비스법)의 추천 시스템 투명성 요건과 연결

**플랫폼 대상:**
- 인게이지먼트 최적화의 부작용에 대한 실증적 증거
- "사용자 만족 ≠ 인게이지먼트"라는 연구 결과의 정책적 함의 — 새로운 최적화 지표 필요
- 슬롭 대응 조치의 실효성 데이터 → 더 나은 대응 설계

**산업 대상 (Trust & Safety):**
- AI 슬롭이 브랜드 안전성(brand safety)에 미치는 위험
- eMarketer(2026): "YouTube's AI slop surge risks brand safety and viewer trust"
- 미국 성인 49%가 AI 콘텐츠 증가 시 소셜 플랫폼 사용을 줄이거나 중단하겠다고 응답

### 7-4. 최종 판단: 이 연구는 할 가치가 있는가?

**예. 확실히 가치가 있다. 이유는 다음과 같다:**

1. **타이밍이 최적이다.** 2025-2026년은 알고리즘 변경, 규제 시행, 도구 소멸(Sora)이 동시에 발생하는 유례없는 자연실험의 창(window of opportunity)이다. 이 데이터는 지금 수집하지 않으면 영구히 소실된다.

2. **블랙박스가 이유가 아니라 논점이다.** "플랫폼 알고리즘을 외부에서 연구할 수 없다"는 것은 연구 포기의 이유가 아니라, 연구해야 할 문제 자체다. 알고리즘 투명성 요구의 근거가 된다.

3. **한국의 극단적 사례 가치는 대체 불가능하다.** 세계 1위 AI 슬롭 소비국 + 최초 종합 AI 법률. 이 조합은 다른 어떤 연구 맥락에서도 재현 불가능하다.

4. **"불완전한 답변"도 "답변 부재"보다 낫다.** 블랙박스 하에서의 관측적/준실험적 증거는 완벽한 인과적 증거가 아니지만, 정책 결정과 학술 논의를 진전시키기에 충분하다.

5. **리스크는 관리 가능하다.** 최소 가능 연구(YouTube API + Social Blade + 소규모 sock puppet)로도 ICWSM/CSCW 수준의 논문이 가능하며, 비용은 거의 영이다.

**가장 큰 리스크는 이 연구를 하지 않는 것이다.**

---

## 부록: 연구 실행 로드맵

### Phase 1: 데이터 인프라 구축 (2026 Q2, 4-6주)

- [ ] YouTube Data API 연구용 쿼터 신청
- [ ] Meta Content Library 학술 접근 신청
- [ ] Social Blade 유료 계정 설정
- [ ] AI 슬롭 분류기 v1 개발 (수동 분류 500개 영상 → 자동화)
- [ ] Sock puppet 인프라 구축 (Playwright/Selenium + 클라우드 서버)
- [ ] IRB 심의 제출

### Phase 2: Sock Puppet 감사 + 기초 데이터 수집 (2026 Q2-Q3, 8-12주)

- [ ] 4개 실험군 봇 배치 (실험군 + 대조군 3개)
- [ ] 2,000-5,000개 추천 영상 데이터 수집
- [ ] AI 슬롭 비율, 증폭 속도, 다양성 지수 측정
- [ ] Social Blade 역사적 데이터 수집 (2025.01-2026.03)

### Phase 3: 자연실험 분석 (2026 Q3, 4-6주)

- [ ] DiD 분석: YouTube 수익화 정책 변경(2025.07) 전후
- [ ] RDD 분석: 한국 AI 기본법(2026.01.22) 시행 전후
- [ ] 이벤트 스터디: YouTube 16개 대형 채널 삭제(2026.01) 효과
- [ ] (가능 시) DiD 분석: Instagram 합성 콘텐츠 페널티(2026.01) 전후

### Phase 4: 통합 분석 + 논문 집필 (2026 Q3-Q4, 8-12주)

- [ ] 삼각측량: sock puppet + DiD/RDD + 이론적 모델의 수렴 여부 판단
- [ ] 피드백 루프 시계열 분석 (Granger 인과 + Markov 모델)
- [ ] 그레셤의 법칙 검증: 슬롭 제거 후 진성 크리에이터 성과 변화
- [ ] 논문 집필: ICWSM 2027 또는 CSCW 2027 타겟

### Phase 5: 투고 및 확장 (2026 Q4 - 2027 Q1)

- [ ] 1차 타겟 학회 투고
- [ ] 리비전 대응
- [ ] 한국어 버전: 한국언론학보 또는 정보사회와 미디어 투고
- [ ] 정책 브리프: 방송통신위원회/과학기술정보통신부 대상

---

## Sources

### 핵심 참조 논문
- [Baumann et al. (2025/2026) "Dynamics of Algorithmic Content Amplification on TikTok"](https://arxiv.org/abs/2503.20231) — EPJ Data Science
- [arXiv:2501.15048 "YouTube Recommendations Reinforce Negative Emotions"](https://arxiv.org/abs/2501.15048)
- [FAccT 2025 "Auditing Political Exposure Bias"](https://facctconference.org/static/docs/facct2025-206archivalpdfs/facct2025-final1290-acmpaginated.pdf)
- [Springer(2024) "Auditing the audits"](https://link.springer.com/article/10.1007/s41109-024-00668-6)
- [Casper et al. (FAccT 2024) "Black-Box Access is Insufficient for Rigorous AI Audits"](https://dl.acm.org/doi/10.1145/3630106.3659037)
- [arXiv:2602.06437 "An attention economy model of co-evolution"](https://arxiv.org/abs/2602.06437)
- [arXiv:2207.01616 "Breaking Feedback Loops in Recommender Systems"](https://arxiv.org/abs/2207.01616)
- [arXiv:2509.00109 "Bias Mitigation for AI-Feedback Loops"](https://arxiv.org/html/2509.00109)
- [arXiv:2410.13101 "Impact of GenAI on Content Platforms: Two-Sided Market Analysis"](https://arxiv.org/html/2410.13101v2)
- [Lasser et al. (2025) "Designing social media content recommendation algorithms for societal good"](https://nyaspubs.onlinelibrary.wiley.com/doi/full/10.1111/nyas.15359)

### 알고리즘 게이트키핑 이론
- [Bruns (2025) "Algorithmic gatewatching"](https://journals.sagepub.com/doi/10.1177/29768640251336597)
- [MDPI (2025) "Reconceptualizing Gatekeeping in the Age of AI"](https://www.mdpi.com/2673-5172/6/2/68)
- [Liang et al. (2025) "Content Creation within the Algorithmic Environment"](https://journals.sagepub.com/doi/10.1177/09500170251325784)
- [Frontiers (2025) "Algorithmic influence and media legitimacy"](https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2025.1667471/full)
- [Cambridge Core "Algorithmic Attention Rents"](https://www.cambridge.org/core/journals/data-and-policy/article/algorithmic-attention-rents-a-theory-of-digital-platform-market-power/D85FE41F6CF99FC57DDFB2B2B63491C5)

### 플랫폼 대응 및 자연실험
- [YouTube "AI slop?" 사용자 피드백 테스트](https://www.ghacks.net/2026/03/23/youtube-is-testing-pop-up-surveys-asking-users-to-rate-videos-as-ai-slop/)
- [YouTube Algorithm Updates 2026](https://outlierkit.com/resources/youtube-algorithm-updates/)
- [Instagram Algorithm Updates 2026](https://clippie.ai/blog/instagram-algorithm-updates-2026-creators-guide)
- [YouTube AI Demonetization 2026](https://fliki.ai/blog/youtube-ai-demonetization)
- [YouTube 16개 AI 채널 삭제](https://perplexityaimagazine.com/ai-news/youtube-deletes-ai-slop-channels-crackdown/)

### 한국 AI 규제
- [한국 AI 기본법 분석 (IAPP)](https://iapp.org/news/a/analyzing-south-korea-s-framework-act-on-the-development-of-ai)
- [한국 AI 기본법 (OneTrust)](https://www.onetrust.com/blog/south-koreas-new-ai-law-what-it-means-for-organizations-and-how-to-prepare/)
- [한국 AI 콘텐츠 라벨링 의무 (BABL AI)](https://babl.ai/south-koreas-revised-ai-basic-act-to-take-effect-january-22-with-new-oversight-watermarking-rules/)
- [한국 AI 광고 라벨링 (PBS)](https://www.pbs.org/newshour/world/south-korea-to-require-advertisers-to-label-ai-generated-ads)

### Sora 종료
- [NPR: Sora 레거시](https://www.npr.org/2026/03/25/nx-s1-5759931/openais-sora-app-may-be-going-away-but-its-legacy-will-be-the-spread-ai-video-slop)
- [CNN: Sora 종료](https://www.cnn.com/2026/03/24/tech/openai-sora-video-app-shutting-down)
- [Euronews: Sora 종료](https://www.euronews.com/next/2026/03/25/openai-to-abruptly-close-sora-video-app-following-backlash-over-deepfakes-and-ai-slop)

### API 접근 및 데이터
- [arXiv:2506.11727 "Forgetful by Design?" YouTube API 한계](https://arxiv.org/html/2506.11727)
- [Tandfonline: YouTube Search API 학술 연구 비판](https://www.tandfonline.com/doi/full/10.1080/1369118X.2025.2591767)
- [Meta Content Library](https://transparency.meta.com/researchtools/meta-content-library/)
- [CrowdTangle 종료 (CJR)](https://www.cjr.org/tow_center/meta-is-getting-rid-of-crowdtangle.php)
- [Social Blade 정확도 분석](https://tuberanker.com/blog/how-accurate-is-socialblade)

### AI vs 인간 콘텐츠 인게이지먼트
- [Bynder: AI vs Human Content 인게이지먼트](https://www.bynder.com/en/press-media/ai-vs-human-made-content-study/)
- [ResearchGate: AI vs Human Content on Instagram](https://www.researchgate.net/publication/398844461_AI_versus_Human_Content_Creation_on_Instagram_Engagement_Outcomes_and_Consumer_Perceptions)
- [Springer: AI-generated and human-generated content engagement](https://innovation-entrepreneurship.springeropen.com/articles/10.1186/s13731-025-00529-1)

### 인과 추론 방법론
- [Ada Lovelace Institute: Technical methods for regulatory inspection](https://www.adalovelaceinstitute.org/report/technical-methods-regulatory-inspection/)
- [Frontiers: AI-driven disinformation policy](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1569115/full)
- [PMC: Cascading falsehoods in algorithmic environments](https://link.springer.com/article/10.1007/s00146-025-02575-5)
- [Difference-in-Discontinuities Design](https://arxiv.org/html/2405.18531v2)
