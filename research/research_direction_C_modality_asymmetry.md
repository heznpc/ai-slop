# 연구 방향 C: AI 슬롭 탐지의 모달리티 비대칭성 (Modality Asymmetry in AI Slop Detection)

> 작성일: 2026-03-28 | 문서 유형: 구체화된 연구 제안서
> 핵심 테제: AI 슬롭 탐지 난이도는 모달리티에 따라 극적으로 다르며, 이 비대칭성은 플랫폼 콘텐츠 모더레이션의 구조적 사각지대를 만든다.

---

## 0. 솔직한 사전 평가 (Honest Pre-Assessment)

**이 연구의 본질적 성격부터 명확히 하자.**

이 방향은 본질적으로 **CS/ML 기술 논문**이다. 학제간(interdisciplinary) 연구로 포장할 수는 있으나, 핵심 기여(contribution)는 크로스-모달리티 탐지 벤치마크와 성능 비교라는 기술적 작업에 있다. 이것은 약점이 아니라 명확한 포지셔닝의 문제이다.

다만, 단순 벤치마크 논문(survey/benchmark paper)으로 끝나면 임팩트가 제한적이다. **"비대칭성의 존재를 보여주는 것"에서 그치지 않고, "비대칭성이 실제 플랫폼 모더레이션에 미치는 영향의 정량적 추정"까지 나아가야** 학술적 기여가 성립한다.

**결론: 순수 CS 논문으로 쓰되, Trust & Safety 실무 함의를 강조하는 하이브리드 포지셔닝이 최적이다.**

---

## 1. 연구 질문 (Research Questions)

### RQ1 (핵심): 모달리티별 AI 슬롭 탐지 정확도는 어떻게 다른가?

> "AI 생성 콘텐츠 탐지 정확도는 비디오, 오디오, 텍스트, 이미지, 이미지+텍스트 하이브리드 모달리티에 걸쳐 어떤 체계적 차이를 보이며, 이 차이의 크기는 얼마인가?"

**조작적 정의:**
- 탐지 정확도 = AUROC, F1, TPR@1%FPR (표준화된 지표)
- 모달리티 = {비디오, 오디오, 텍스트, 이미지, 이미지+텍스트 하이브리드}
- AI 슬롭 = AI로 생성되었으며 대량 생산/저품질/클릭베이트 특성을 갖는 콘텐츠

### RQ2 (메커니즘): 각 모달리티를 탐지하기 쉽거나 어렵게 만드는 구체적 특성(feature)은 무엇인가?

**가설적 프레임워크:**
- **고탐지율 모달리티**: 물리 법칙 위반(비디오), 음성 합성 패턴(오디오) 등 "물리적 그라운딩"이 있는 모달리티
- **저탐지율 모달리티**: 의미적/문체적 판단에 의존하는 모달리티(텍스트), 복수 모달리티가 결합되어 단일 탐지기로 커버 불가능한 하이브리드(카드뉴스, 인포그래픽)

### RQ3 (실무): 현존 탐지 도구들은 각 모달리티에 적절한가?

> 상용 탐지 도구(GPTZero, Hive, Sensity 등)와 학술 모델의 실제 성능을 모달리티별로 비교

### RQ4 (동적): 모달리티별 탐지-회피 군비경쟁(detection-evasion arms race)의 현재 상태는 어떠한가?

> 적대적 공격(adversarial attack)에 대한 탐지기의 강건성이 모달리티마다 어떻게 다른가?

### RQ5 (함의): 이 비대칭성은 플랫폼 모더레이션의 실효성에 어떤 영향을 미치는가?

> 탐지가 어려운 모달리티의 AI 슬롭이 플랫폼에서 더 오래 생존하고, 더 많이 확산되는가?

---

## 2. 기술적 현황: 모달리티별 탐지 성능 종합 (2025-2026)

### 2-1. 비디오 탐지 (Video Detection) -- 상대적 고탐지율

**벤치마크 성능:**
| 벤치마크 | 최고 AUROC | 비고 |
|----------|-----------|------|
| FaceForensics++ | 98.3% (Capsule Network) | 통제된 조건, 과대평가 우려 |
| CDFv2 | 96.62% | 크로스-데이터셋 |
| DFDC | 87.15% | 현실적 조건, 성능 하락 두드러짐 |
| FFIW | 91.52% | |
| DSv1 | 92.01% | |

**AI 생성 비디오 (Sora, Runway, Kling) 탐지:**
- 현재 탐지율: **85-94%** (모델/도구에 따라 편차)
- Sora 2 비디오: 85-93% 탐지율
- 모델별 고유 시그니처: Sora 2의 모션 블러 패턴, Runway Gen-4의 엣지 렌더링, Kling의 물리 시뮬레이션 이상
- **95%의 사람은 고품질 AI 생성 비디오를 구별하지 못함** -- 자동 탐지의 필요성 강조

**핵심 약점:**
- **일반화 실패**: 특정 생성 파이프라인에서 훈련된 탐지기는 미지의 생성 모델에 대해 **20-60%p 성능 하락**
- Transformer 기반 아키텍처가 CNN 대비 크로스-데이터셋 일반화에서 우수 (성능 하락 11.33% vs 15%+)
- 생성 모델이 월 단위로 업데이트되므로 탐지기의 지속적 재훈련 필요

**탐지가 상대적으로 쉬운 이유:**
- 비디오는 물리적 세계의 법칙(중력, 관성, 광학)을 시뮬레이션해야 하므로 **물리적 그라운딩 위반**이 탐지 단서가 됨
- 시간적 일관성(temporal consistency) 요구로 인해 아티팩트가 프레임 간에 누적
- 얼굴/신체의 해부학적 정확성이 강력한 탐지 피처

---

### 2-2. 오디오 탐지 (Audio Detection) -- 고탐지율, 단 일반화 취약

**벤치마크 성능:**
| 시스템 | 정확도/EER | 벤치마크 |
|--------|-----------|----------|
| ASVspoof 5 최고 모델 | 98%+ 정확도, EER 0.0013 | ASVspoof 5 |
| Resemble AI DETECT-2B | 94-98% | 30+ 언어, 압축/노이즈 환경 |
| Sensity | 95-98% | 상용 도구 |
| 음악 탐지 (CNN + spectrogram) | 99%+ | 폐쇄 조건 |

**ASVspoof 5 (2025-2026):**
- 역대 최대 규모의 음성 위조 탐지 챌린지
- 크라우드소싱 데이터로 현실적 시나리오 시뮬레이션
- TTS + VC(Voice Conversion) + 적대적 공격 포함

**핵심 약점:**
- 높은 정확도에도 불구하고 **형식적 강건성 보증(formal robustness guarantee) 부재**
- 미지의 생성 기법에 대한 일반화 취약
- 현실 환경(전화 통화, 소셜 미디어 압축, 배경 소음)에서 성능 하락
- **한국어 TTS 탐지**: KatFishNet이 한국어 텍스트 탐지를 다루고 있으나, 한국어 음성 합성 탐지에 대한 전문 벤치마크는 사실상 **부재**

**탐지가 상대적으로 쉬운 이유:**
- 음성은 고유한 음향 시그니처(acoustic signature)를 가지며, 합성 음성은 이를 완벽히 복제하기 어려움
- 주파수 스펙트럼 분석으로 합성 아티팩트 검출 가능
- 단, 최신 TTS(ElevenLabs, XTTS 등)의 품질 향상으로 이 이점이 점차 약화 중

---

### 2-3. 텍스트 탐지 (Text Detection) -- 저탐지율, 적대적 공격에 극도로 취약

**벤치마크 성능:**
| 도구 | 원본 AI 텍스트 정확도 | 패러프레이즈 후 정확도 | FPR | 비고 |
|------|---------------------|---------------------|-----|------|
| GPTZero v4.1b | 98.78% (자체 벤치마크) | 60-70% (독립 테스트) | 자체 0%, 독립 1-2% | 비원어민 텍스트 FPR 25-35% |
| Originality.ai | 99% (자체 주장) | 미공개 | 미공개 | |
| ZeroGPT | 65-85% | 크게 하락 | 높음 | |
| 전반적 범위 | 88-95% | **60-80%** | 도구마다 편차 | |

**적대적 공격의 파괴력 -- 이것이 핵심 문제:**
- **Adversarial Paraphrasing (NeurIPS 2025)**: 훈련 불필요(training-free) 공격 프레임워크. 탐지기 안내 하에 LLM이 AI 텍스트를 "인간화". **TPR@1%FPR을 평균 87.88% 감소**시킴
- **StealthRL (2026)**: RL 기반 패러프레이즈 정책. **평균 TPR@1%FPR을 0.001까지 감소, AUROC를 0.74에서 0.27로 하락, 공격 성공률 99.9%**
- 이 공격들은 **학습 시 보지 못한 탐지기에도 전이(transfer)**됨 -- 탐지기별 취약성이 아닌 구조적 취약성

**한국어 텍스트 탐지 -- KatFishNet (ACL 2025 Main):**
- 한국어 AI 텍스트 탐지 최초의 벤치마크 데이터셋 + 전용 탐지기
- 한국어 고유 언어적 특성(띄어쓰기 패턴, 품사 다양성, 쉼표 사용) 활용
- 기존 최고 영어 중심 탐지기 대비 **AUROC 19.78%p 향상**
- 그러나: 4개 LLM x 3개 장르로 규모 제한적, 적대적 공격 환경 미평가

**오탐(False Positive) 문제 -- 텍스트 탐지의 아킬레스건:**
- 비원어민 영어 작성자의 글이 AI로 오탐되는 비율 **25-35%** (학술 연구)
- 정형화된(formulaic) 학술 글쓰기도 높은 오탐
- 이 문제는 윤리적으로 심각: 비원어민 학생의 과제가 AI 표절로 오판될 위험

**탐지가 어려운 근본적 이유:**
- 텍스트에는 **물리적 그라운딩이 없음**: 문법적으로 올바르고 의미적으로 타당한 텍스트를 "자연 법칙 위반"으로 탐지할 수 없음
- 탐지는 **통계적 분포 차이**(perplexity, burstiness 등)에 의존하나, LLM이 고도화될수록 인간 텍스트의 통계적 분포에 수렴
- 패러프레이즈 공격이 본질적으로 쉬움: LLM 자체가 최적의 패러프레이즈 도구
- **적대적 방어의 확장성 한계**: 가능한 패러프레이즈 전략의 공간이 방대하여, 어떤 단일 탐지기도 모든 공격에 강건할 수 없음

---

### 2-4. 이미지 탐지 (Image Detection) -- 중간 수준, C2PA 의존적

**벤치마크 성능:**
| 접근법 | 정확도 | 비고 |
|--------|--------|------|
| 전통 CNN | 78-92% | |
| CNN + Transformer 하이브리드 | 88-95% | |
| 다중 스케일 텍스처/주파수 | 92-97% | |
| Hive Moderation (상용) | 94% | 혼합 소스 테스트 |
| Illuminarty (상용) | 91% | 히트맵 제공 |
| AI Image Detector V2 | 95%+ | DALL-E 3, Midjourney v6, SD3, Flux, Imagen 3 |

**현실 환경에서의 성능 저하:**
- 리사이징, 압축, 스크린샷, 색상 필터, 크롭 등 **실제 소셜 미디어 유통 과정에서 15-35% 정확도 하락**
- 이 갭이 벤치마크와 실전 사이의 가장 큰 괴리

**C2PA 워터마킹 -- 보완적이지만 불완전:**
- 업계 채택 가속 중: Adobe, Google, NTB 등이 통합
- ISO 국제 표준 채택 예정 (2025년)
- **한계**: 워터마크는 동시에 강건하고(robust), 위조 불가능하며(unforgeable), 공개 검증 가능(publicly detectable)할 수 없음
- 공격자가 **프로비넌스 메타데이터 변조, 워터마크 제거/위조, 디지털 핑거프린트 모방** 가능
- Bruce Schneier: "워터마킹 단독으로는 생성형 AI의 도전에 대응할 수 없다"
- **핵심 문제**: C2PA는 참여하는 생태계 내에서만 작동. 미참여 생성 도구(오픈소스 SD, 로컬 실행 모델)의 결과물에는 적용 불가

**인간 탐지 성능 -- 매우 낮음:**
- AI 생성 이미지에 대한 인간 정확도: **49-61%** (거의 동전 던지기 수준)
- 자동 탐지 도구가 인간을 압도적으로 능가하는 모달리티

---

### 2-5. 이미지+텍스트 하이브리드 (카드뉴스, 인포그래픽) -- 탐지 사각지대

**현황: 사실상 연구 공백**

웹 서치 결과, "AI 생성 인포그래픽/카드뉴스의 자동 탐지"를 주제로 한 학술 연구는 **사실상 발견되지 않았다**. 이것 자체가 이 연구의 존재 이유이다.

**왜 사각지대인가:**

1. **모달리티 간 의미적 상호작용**: 이미지와 텍스트가 결합될 때 의미는 개별 모달리티의 합이 아님. CLIP, LLaVA 등 멀티모달 모델이 이를 해석할 수 있으나 탐지 정확도 개선은 **10-15%** 수준에 불과하며 컴퓨팅 비용이 높음
2. **기존 탐지기의 설계 한계**: 이미지 탐지기는 텍스트를 무시하고, 텍스트 탐지기는 이미지를 무시함. 파이프라인을 연결해도(이미지 탐지 + OCR + 텍스트 탐지) 모달리티 간 일관성(cross-modal consistency)은 평가하지 못함
3. **생성의 용이성**: Canva AI, Piktochart AI 등으로 수 초 만에 "전문적" 인포그래픽 생성 가능. 완전 자동화 가능한 파이프라인 존재
4. **유통량의 폭증**: 인스타그램/페이스북의 캐러셀이 알고리즘적으로 우대. AI 생성 콘텐츠가 인간 생성 콘텐츠를 처음으로 총량 기준 추월 (2025년 말)
5. **그라운드 트루스 확보 난이도**: "이 인포그래픽이 AI로 만들어졌는가?"를 판정하는 것 자체가 어려움. 부분 AI 사용(텍스트만 AI, 이미지만 AI, 레이아웃만 AI)의 경우 이진 라벨링이 부적절

**한국 맥락의 특수성:**
- 카드뉴스는 한국 디지털 미디어의 **지배적 포맷** (네이버 뉴스, 인스타그램, 페이스북)
- 정보 전달형 카드뉴스 + AI 생성의 결합이 이미 광범위
- 그러나 이에 대한 탐지 연구는 전무

---

### 2-6. 모달리티별 탐지 성능 종합 비교표

| 모달리티 | 벤치마크 AUROC/정확도 | 현실환경 추정 정확도 | 적대적 공격 후 | 인간 탐지 | 탐지 도구 성숙도 | 연구 밀도 |
|----------|---------------------|-------------------|--------------|----------|----------------|----------|
| **비디오 (딥페이크)** | 87-98% | 75-90% | 60-80% | 낮음 (동전 던지기 이하) | 높음 | 매우 높음 |
| **비디오 (AI 생성)** | 85-94% | 70-85% | 미평가 | 매우 낮음 (5%만 구별) | 중간 | 중간 |
| **오디오 (TTS/VC)** | 94-99% | 80-95% | 불명 | 중간 | 높음 | 높음 |
| **오디오 (AI 음악)** | 99% (폐쇄조건) | 60-80% (추정) | 미평가 | 불명 | 낮음 | 낮음 |
| **이미지** | 88-97% | 65-82% | 미체계적 평가 | 매우 낮음 (49-61%) | 중-높음 | 높음 |
| **텍스트** | 88-99% (자체) / 65-90% (독립) | 60-80% | **0.1-27%** (AUROC) | 낮음 | 중간 | 높음 |
| **이미지+텍스트 하이브리드** | **평가된 적 없음** | **평가된 적 없음** | **평가된 적 없음** | 불명 | **사실상 부재** | **거의 없음** |

**이 표가 말해주는 것:**
- 벤치마크 → 현실환경으로 갈 때 **모든 모달리티에서 10-25%p 하락**
- 적대적 공격은 텍스트에서 **파괴적** (AUROC 0.27까지 하락)
- 이미지+텍스트 하이브리드는 **평가 자체가 부재**하여 "높다/낮다"를 말할 수조차 없음
- 연구의 관심과 탐지의 필요성 사이에 **역(inverse) 관계**: 가장 많이 연구된 모달리티(비디오)가 이미 상대적으로 탐지 가능하고, 가장 적게 연구된 모달리티(하이브리드)가 가장 탐지가 어려울 가능성이 높음

---

## 3. 실증 가능성 평가 (Feasibility Assessment)

### 3-1. 크로스-모달리티 벤치마크 데이터셋 구축

**가능한가? -- 조건부 Yes.**

**구축 전략:**
```
동일 "슬롭 캠페인" 시뮬레이션:
  주제 선정 (예: 건강 미신, 투자 사기, 음모론)
  → 텍스트 생성 (GPT-4o, Claude, Gemini로 기사/블로그)
  → 이미지 생성 (DALL-E 3, Midjourney v6, SD3로 삽화)
  → 비디오 생성 (Sora 2, Runway Gen-4, Kling으로 숏폼)
  → 오디오 생성 (ElevenLabs, XTTS로 나레이션)
  → 하이브리드 생성 (Canva AI, Piktochart로 카드뉴스/인포그래픽)
  → 대조군: 동일 주제의 인간 생성 콘텐츠 수집
```

**규모 추정:**
- 주제 10개 x 생성 모델 3-4개/모달리티 x 모달리티 5개 x 샘플 50개 = **~7,500-10,000개 샘플**
- 하이브리드 모달리티는 추가로 **부분 AI 사용** 변형 포함 (텍스트만 AI, 이미지만 AI, 전체 AI)
- 인간 대조군: 모달리티당 500+ 샘플 (기존 데이터셋 활용 가능)

**비용/자원:**
- 생성 API 비용: 약 $2,000-5,000 (대부분의 생성 모델이 유료 API 제공)
- 인간 주석(annotation): 크라우드소싱 필요, 약 $3,000-8,000
- 컴퓨팅: 탐지 모델 실행을 위한 GPU -- A100 1대로 충분 (대부분 추론만 수행)
- **총 추정 비용: $10,000-20,000** -- 대학원 연구 예산으로 충분히 가능

**기존 데이터셋 활용:**
- 비디오: FaceForensics++, DFDC, GenVideo(arXiv 2601.11035)
- 오디오: ASVspoof 5, WaveFake
- 텍스트: KatFish(한국어), HC3, M4
- 이미지: GenImage, DiffusionDB
- 하이브리드: **없음** -- 직접 구축 필수 (이것이 기여점)

### 3-2. 탐지 도구 크로스-모달리티 테스트

**가능한가? -- Yes.**

| 모달리티 | 테스트 가능한 탐지 도구 | 접근성 |
|----------|---------------------|--------|
| 비디오 | Sensity, AI Video Detector, Faux Lens | API/웹 |
| 오디오 | Resemble AI Detect, Pindrop | API |
| 텍스트 | GPTZero, Originality.ai, Turnitin, KatFishNet | API/오픈소스 |
| 이미지 | Hive, Illuminarty, AI Photo Check | API/웹 |
| 하이브리드 | **없음** -- 파이프라인 직접 구축 | 직접 구현 |

**하이브리드 탐지 파이프라인 구축:**
```
카드뉴스/인포그래픽 입력
  → 이미지 탐지기 적용 (전체 이미지로)
  → OCR로 텍스트 추출
  → 텍스트 탐지기 적용
  → 레이아웃/디자인 패턴 분석 (Canva 템플릿 탐지 등)
  → 크로스-모달 일관성 평가 (텍스트-이미지 정합성)
  → 앙상블 판정
```

### 3-3. 적대적 공격 실험

**가능한가? -- 모달리티에 따라 다름.**

- **텍스트**: 기존 공격 프레임워크(Adversarial Paraphrasing, StealthRL) 재현 가능. 오픈소스 코드 있음
- **이미지**: 압축, 리사이징, 필터 적용 등 현실적 변형 테스트 가능
- **비디오**: 압축, 재인코딩 테스트 가능. 적대적 노이즈 추가는 연구 수준
- **오디오**: 코덱 변환, 노이즈 추가 테스트 가능
- **하이브리드**: **탐지기 자체가 없으므로 적대적 공격 실험도 탐색적(exploratory) 수준**

### 3-4. 이 논문은 CS/ML 논문인가, 학제간 논문인가?

**솔직한 답: CS/ML 논문이 맞다. 그러나 전략적으로 학제간 포지셔닝이 가능하다.**

- **핵심 기여는 CS**: 크로스-모달리티 벤치마크, 탐지 성능 비교, 하이브리드 탐지 파이프라인
- **학제간 확장 가능한 부분**: 플랫폼 모더레이션 정책 함의, Trust & Safety 실무 권고, 인간-AI 탐지 비교의 인지과학적 해석
- **현실적 선택지**:
  - (A) 순수 CS 논문 (NeurIPS/AAAI 타겟) -- 벤치마크와 기술적 기여 중심
  - (B) CS + 정책 하이브리드 (WWW/CHI 타겟) -- 벤치마크 + 플랫폼 모더레이션 분석
  - **(C) 추천: B 경로** -- WWW나 CHI는 기술적 기여와 사회적 함의 모두를 평가하므로 비대칭성의 정책적 함의까지 포함 가능

---

## 4. 방법론 (Methodology)

### 4-1. 통합 평가 프레임워크 (Unified Evaluation Framework)

**기존 연구와의 차별점: LOKI 벤치마크(ICLR 2025 Spotlight)를 확장**

LOKI는 비디오, 이미지, 3D, 텍스트, 오디오에 걸친 합성 데이터 탐지 벤치마크이다. GPT-4o가 오디오 제외 전체 정확도 **63.9%**를 달성. 그러나 LOKI에는 두 가지 핵심 한계가 있다:

1. **이미지+텍스트 하이브리드 모달리티 미포함**: 카드뉴스, 인포그래픽 등 실제 슬롭의 주요 형태가 빠져 있음
2. **"슬롭" 맥락 미반영**: LOKI는 합성 데이터 자체의 탐지에 집중하며, 대량 생산 / 저품질 / 클릭베이트라는 슬롭 고유의 특성을 반영하지 않음

**우리의 확장:**
- LOKI의 모달리티 커버리지에 **이미지+텍스트 하이브리드 추가**
- 단순 진위 판별(binary: real/fake)을 넘어 **슬롭 여부 판별**(binary: slop/non-slop) 추가
- **전문 탐지 도구(domain-specific detector)와 범용 LMM(general-purpose LMM) 모두 평가**

### 4-2. 벤치마크 데이터셋 구축

**Phase 1: 모달리티별 AI 생성 콘텐츠 수집/생성**

| 모달리티 | 생성 모델 | 슬롭 시나리오 | 비슬롭 대조군 |
|----------|----------|-------------|-------------|
| 텍스트 | GPT-4o, Claude 3.5, Gemini 1.5, DeepSeek | SEO 스팸, 가짜 뉴스, 제품 리뷰 | 인간 작성 기사/리뷰 |
| 이미지 | DALL-E 3, Midjourney v6, SD3, Flux | 클릭베이트 썸네일, 가짜 사진 | 실제 사진/일러스트 |
| 비디오 | Sora 2, Runway Gen-4, Kling 1.6 | AI 숏폼, 가짜 뉴스 영상 | 실제 숏폼/뉴스 영상 |
| 오디오 | ElevenLabs, XTTS, Bark | TTS 나레이션, 보이스 클론 | 실제 녹음/팟캐스트 |
| **하이브리드** | **Canva AI + LLM, Piktochart + DALL-E** | **카드뉴스, 인포그래픽, 교육 슬라이드** | **인간 제작 카드뉴스** |

**Phase 2: 주석(Annotation)**
- 이진 라벨: AI생성/인간생성
- 슬롭 라벨: 슬롭/비슬롭 (3인 주석자 합의)
- 모달리티별 탐지 단서 주석 (어떤 부분에서 AI임을 알 수 있는가)
- 하이브리드의 경우: 부분 AI 사용 라벨 (텍스트만 AI / 이미지만 AI / 전체 AI)

**Phase 3: 난이도 계층화**
- Easy: 명백한 아티팩트 있음
- Medium: 주의 깊게 보면 탐지 가능
- Hard: 고품질 생성, 인간과 구별 어려움

### 4-3. 평가 지표 (Standardized Metrics)

**모든 모달리티에 동일하게 적용:**
- **AUROC**: 전체 판별 성능
- **TPR@1%FPR**: 실무적으로 가장 중요한 지표 (낮은 오탐 상황에서의 탐지율)
- **F1 Score**: 정밀도-재현율 균형
- **FPR@95%TPR**: 높은 탐지율 유지 시 오탐률
- **적대적 강건성 지표**: 공격 전후 AUROC/TPR 변화량 (Delta-AUROC)

### 4-4. 인간 평가 구성요소 (Human Evaluation Component)

**설계:**
- 참가자 N=200+ (연령, 디지털 리터러시 수준 다양)
- 각 참가자에게 **모달리티별로 동일 수의 AI/인간 콘텐츠 제시**
- "이 콘텐츠가 AI로 생성되었다고 생각합니까?" + 확신도(confidence) 수집
- 모달리티 간 순서 효과 통제를 위한 라틴 방진 설계

**핵심 비교:**
- 인간 정확도 vs. 자동 탐지 정확도 (모달리티별)
- 인간이 AI보다 나은 모달리티가 있는가? (선행 연구에 따르면 비디오에서 가능)
- 인간+AI 앙상블이 단독보다 나은가?

### 4-5. 플랫폼 모더레이션 시뮬레이션

**탐지 비대칭성 → 모더레이션 비대칭성 전환 분석:**

1. 각 모달리티의 탐지 정확도를 이용하여 "탐지 실패율" 산출
2. 플랫폼에서 모달리티별 AI 슬롭 콘텐츠의 예상 분포와 결합
3. **"모더레이션 누수율(moderation leakage rate)"** 추정: 탐지를 피해 사용자에게 도달하는 슬롭의 비율
4. 모달리티별 모더레이션 누수율의 차이가 곧 **구조적 사각지대**

---

## 5. 약점 및 리스크 -- 솔직한 평가

### 5-1. "이것은 서베이 논문의 변장인가?"

**리스크: 중간-높음.**

- 모달리티별 탐지 성능을 나열하는 것만으로는 **서베이/벤치마크 논문**에 불과
- LOKI가 이미 ICLR 2025 Spotlight로 유사한 크로스-모달리티 벤치마크를 발표함
- **차별화 전략 (필수):**
  - (1) 이미지+텍스트 하이브리드 모달리티를 **최초로** 벤치마크에 포함 -- 이것이 핵심 novelty
  - (2) "탐지 가능성"이 아닌 **"탐지 비대칭성이 모더레이션에 미치는 영향"**이라는 분석적 프레임
  - (3) 적대적 공격 환경에서의 크로스-모달리티 비교 -- LOKI가 다루지 않은 영역
  - (4) 동일 슬롭 캠페인의 멀티-모달리티 버전이라는 통제된 실험 설계

### 5-2. 벤치마크의 빠른 노후화

**리스크: 높음.**

- AI 생성 모델은 3-6개월 주기로 세대 교체
- 2026년에 수집한 벤치마크는 2027년에 이미 구식일 수 있음
- **완화 전략:**
  - 벤치마크 자체보다 **"비대칭성의 구조적 패턴"**에 초점 (숫자가 아니라 패턴이 기여)
  - 데이터셋과 평가 프레임워크를 오픈소스로 공개하여 **커뮤니티 지속 업데이트 유도**
  - "이 비대칭성은 생성 모델이 발전해도 구조적으로 유지될 것인가?"라는 예측적 분석 포함

### 5-3. 전체 모달리티 커버리지의 현실적 부담

**리스크: 중간.**

- 5개 모달리티 x 다수 생성 모델 x 다수 탐지 도구 = 실험 행렬이 매우 큼
- **완화 전략:**
  - 모달리티당 대표 생성 모델 2-3개로 제한
  - 탐지 도구는 "최고 성능 상용 도구 1개 + 최고 성능 학술 모델 1개"로 한정
  - 모든 모달리티를 균등하게 다루기보다 **하이브리드 모달리티에 집중하되** 다른 모달리티를 비교 기준으로 활용

### 5-4. 하이브리드 탐지의 기초 연구 부재

**리스크: 중간.**

- 비교할 선행 연구가 없으므로 우리의 결과가 "최초"이기는 하나 검증할 기준선(baseline)도 없음
- **완화 전략:**
  - 나이브 파이프라인(이미지 탐지 + OCR + 텍스트 탐지)을 기준선으로 설정
  - 이 기준선이 얼마나 부족한지를 보여주는 것 자체가 기여

### 5-5. 더 넓은 AI 슬롭 연구 어젠다와의 정합성

**리스크: 낮음-중간.**

- 이 연구는 기술적이지만, 기존 research_framework의 RQ1(AI 슬롭의 규모/분포)과 직접 연결됨
- 모더레이션의 모달리티별 사각지대를 정량화하는 것은 RQ3(알고리즘/플랫폼 대응)의 기초 인프라
- **다만**: 한국 맥락의 특수성을 강조하기는 어려움 -- 기술적 비교는 본질적으로 범용적

---

## 6. 학술적 임팩트 예측

### 6-1. 타겟 학회

| 학회 | 적합도 | 근거 | 전략 |
|------|--------|------|------|
| **WWW (The Web Conference)** | ★★★★★ | 웹 콘텐츠 신뢰성, 플랫폼 모더레이션, Trust & Safety 트랙 존재 | **1순위 타겟**. 기술 + 사회적 함의 모두 수용 |
| **AAAI** | ★★★★ | AI for Social Good, AI Safety 트랙 | 기술적 기여 + 정책 함의 균형 |
| **NeurIPS** | ★★★ | Datasets & Benchmarks 트랙 존재 | 벤치마크 기여로 포지셔닝 가능하나, novelty 요구 높음 |
| **ACL** | ★★★ | 텍스트 탐지 중심이라면 적합 | 멀티모달 범위가 ACL의 NLP 중심 스코프와 다소 불일치 |
| **CHI** | ★★★★ | 인간-AI 탐지 비교, 모더레이션 UX | 인간 평가 구성요소 강화 시 적합 |
| **USENIX Security** | ★★★★ | 적대적 공격/방어 측면 | 보안 관점 포지셔닝 시 |
| **FAccT** | ★★★★ | 공정성, 책임, 투명성 | 모더레이션 비대칭이 특정 콘텐츠 유형/커뮤니티에 미치는 차별적 영향 |

**추천: WWW 2027 또는 AAAI 2027 메인, 불가 시 CHI 2027 LBW**

### 6-2. 실무적 가치

**Trust & Safety 팀에 대한 직접적 가치:**
- "어떤 모달리티에 모더레이션 자원을 집중해야 하는가?"에 대한 정량적 근거 제공
- 하이브리드 콘텐츠 탐지의 필요성을 데이터로 입증
- 모달리티별 탐지 도구의 성능 한계를 실제 슬롭 시나리오에서 측정
- 적대적 공격 환경에서의 탐지 강건성 비교 -- 방어 우선순위 설정에 필수

**플랫폼별 함의:**
- **인스타그램/페이스북**: 캐러셀(카드뉴스) 형태의 슬롭이 탐지 사각지대일 수 있음
- **유튜브**: 비디오 탐지는 상대적으로 양호하나 커뮤니티 탭의 이미지+텍스트는 미검증
- **네이버**: 블로그(텍스트), 포스트(카드뉴스형), 카페(하이브리드) 등 다양한 포맷이 공존하는 생태계에서 모달리티별 모더레이션 격차 분석 가능

### 6-3. 정책적 함의

- EU AI Act의 합성 콘텐츠 표시(labeling) 의무가 모달리티별로 다른 실효성을 가질 수 있음
- 한국의 AI 생성 콘텐츠 라벨링 의무제도 마찬가지
- C2PA 등 프로비넌스 기반 접근이 모달리티별로 다른 채택률/효과를 보이는 현실
- **정책적 권고**: 모달리티별로 차등화된(differentiated) 규제/가이드라인의 필요성

### 6-4. 인용 잠재력 예측

**솔직한 평가:**
- "크로스-모달리티 AI 탐지 비교"라는 프레이밍은 **기존 서베이가 이미 부분적으로 커버** (AIGC surveys in ACM Computing Surveys)
- 그러나 **실증적 크로스-모달리티 벤치마크 + 하이브리드 모달리티 최초 포함**이라는 조합은 참신
- LOKI(ICLR 2025)의 확장으로 포지셔닝하면 기존 연구와의 연결성 확보
- **현실적 인용 예측: 2년 내 50-150회** (벤치마크 논문은 꾸준히 인용되는 경향)

---

## 7. 최종 평가 및 실행 권고

### 이 연구 방향의 강점
1. **명확한 연구 공백**: 이미지+텍스트 하이브리드 탐지는 사실상 미개척 영역
2. **실증적 기여가 분명**: 벤치마크 데이터셋 + 크로스-모달리티 비교 결과
3. **실무적 가치**: Trust & Safety 팀에 직접 활용 가능한 결과물
4. **실현 가능성**: 예산 $10K-20K, GPU 1대, 6-9개월로 완료 가능

### 이 연구 방향의 약점
1. **순수 기술적 성격**: 한국 콘텐츠 생태계의 고유성을 강조하기 어려움
2. **노후화 위험**: 3-6개월 주기의 생성 모델 업데이트
3. **LOKI와의 차별화 부담**: "LOKI의 확장"이상의 novelty 필요
4. **하이브리드 탐지 기준선 부재**: 비교 대상이 없어 결과 해석이 주관적일 수 있음

### 실행 우선순위 권고

**기존 연구 프레임워크(research_framework_ai_slop.md)의 RQ1-RQ6과의 관계에서:**

이 연구 방향(C)은 **독립 논문으로 쓸 수도 있고**, 기존 프레임워크의 RQ1(AI 슬롭 규모/분포 파악)의 **기술적 하위 모듈**로 통합할 수도 있다.

- **독립 논문으로 쓸 경우**: WWW/AAAI 타겟, 순수 기술적 기여 중심, 6-9개월 소요
- **기존 프레임워크에 통합할 경우**: RQ1의 "계산적 콘텐츠 분석" 방법론에 모달리티별 탐지 가능성 분석을 포함. 다만 이 경우 기술적 깊이가 희석될 위험

**추천: 독립 논문으로 진행하되, 기존 프레임워크의 findings를 교차 참조.**

---

## 8. 구체적 다음 단계 (Next Steps)

1. **LOKI 논문 정독** (1주): ICLR 2025 Spotlight 논문 + 코드/데이터셋 확인. 확장 가능한 지점 매핑
2. **하이브리드 모달리티 파일럿** (2주): Canva AI + LLM으로 카드뉴스 100개 생성, 기존 이미지/텍스트 탐지기로 파일럿 테스트. 탐지 실패율 초기 추정
3. **데이터셋 설계 확정** (1주): 모달리티 x 생성모델 x 시나리오 행렬 확정
4. **본 데이터셋 구축 + 실험** (2-3개월)
5. **인간 평가** (1개월)
6. **논문 작성** (1-2개월)
7. **타겟: WWW 2027 (제출 마감 예상: 2026년 10월)**

---

## Sources

### 비디오 탐지
- [Beyond the Benchmark: Generalization Limits of Deepfake Detectors](https://www.ischool.berkeley.edu/sites/default/files/bb_paper.pdf)
- [Comprehensive Evaluation of Deepfake Detection Models (MDPI)](https://www.mdpi.com/2076-3417/15/3/1225)
- [Deepfake Detection that Generalizes Across Benchmarks](https://arxiv.org/html/2508.06248v1)
- [Human Performance in Deepfake Detection: A Systematic Review](https://onlinelibrary.wiley.com/doi/10.1155/hbe2/1833228)
- [Sora, Veo 3, and Kling: How to Detect AI-Generated Video in 2026](https://fauxlens.com/blog/detect-ai-generated-video-2026)
- [GenVideo: One-Stop Solution for AI-Generated Video Detection](https://arxiv.org/pdf/2601.11035)

### 텍스트 탐지
- [Are AI Detectors Accurate in 2026?](https://walterwrites.ai/are-ai-detectors-accurate/)
- [GPTZero Accuracy Test Results 2026 (MPGone)](https://mpgone.com/is-gptzero-accurate-our-2025-test-results-here/)
- [GPTZero Benchmarking Methodology](https://gptzero.me/news/ai-accuracy-benchmarking/)
- [Can We Trust Academic AI Detective? (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12331776/)
- [KatFishNet: Detecting LLM-Generated Korean Text (ACL 2025)](https://arxiv.org/abs/2503.00032)
- [Adversarial Paraphrasing: Universal Attack (NeurIPS 2025)](https://arxiv.org/abs/2506.07001)
- [StealthRL: RL Paraphrase Attacks for Multi-Detector Evasion](https://arxiv.org/abs/2602.08934)
- [Benchmarking AI Text Detection: Assessing Detectors (ACL GenAIDetect)](https://aclanthology.org/2025.genaidetect-1.4.pdf)

### 이미지 탐지
- [How Accurate Are Modern AI Image Detectors in 2026?](https://www.openpr.com/news/4295987/how-accurate-are-modern-ai-image-detectors-in-2026)
- [AI Image Detector V2: 95%+ Accuracy](https://aiphotocheck.com/blog/ai-image-detector-v2-accuracy-2026)
- [Best AI Image Detectors in 2026 (Word Spinner)](https://word-spinner.com/blog/best-ai-image-detectors/)

### 오디오 탐지
- [ASVspoof 5: Design, Collection and Validation (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0885230825000506)
- [Audio Deepfake Detection: What Has Been Achieved (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/)
- [Hybrid Deep Learning Framework for Deepfake Voice Detection](https://link.springer.com/article/10.1007/s00034-025-03464-4)
- [AI Music Deepfake Detection (Deezer/GitHub)](https://github.com/deezer/deepfake-detector)

### C2PA / 워터마킹
- [C2PA and the AI Supply Chain](https://aicompetence.org/c2pa-ai-supply-chain-verifying-authenticity/)
- [Missing the Mark: Adoption of Watermarking for Gen AI](https://arxiv.org/html/2503.18156v3)
- [Google and C2PA Transparency for Gen AI](https://blog.google/innovation-and-ai/products/google-gen-ai-content-transparency-c2pa/)
- [NSA/CISA Guidance on Content Credentials](https://media.defense.gov/2025/Jan/29/2003634788/-1/-1/0/CSI-CONTENT-CREDENTIALS.PDF)

### 크로스-모달리티 벤치마크
- [LOKI: Comprehensive Synthetic Data Detection Benchmark (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/afd6374c7f2839cba22f537f15f4f760-Paper-Conference.pdf)
- [LOKI GitHub Repository](https://github.com/opendatalab/LOKI)
- [AIGC Survey (ACM Computing Surveys)](https://dl.acm.org/doi/full/10.1145/3728633)

### AI 슬롭 / 플랫폼 모더레이션
- [AI Slop (Wikipedia)](https://en.wikipedia.org/wiki/AI_slop)
- [TechRadar: AI Slop Won in 2025](https://www.techradar.com/ai-platforms-assistants/ai-slop-won-in-2025-fingerprinting-real-content-might-be-the-answer-in-2026)
- [Kagi SlopStop: Community-driven AI Slop Detection](https://blog.kagi.com/slopstop)
- [Redefining Content Moderation in the Era of Synthetic Content (TrustLab)](https://www.trustlab.com/post/redefining-content-moderation-in-the-era-of-synthetic-content)
- [Human-AI Ensembles Improve Deepfake Detection](https://arxiv.org/html/2603.14658)
- [Human vs. AI: Benchmark for Detection of Generated Images](https://arxiv.org/html/2412.09715v1)

### 인간 vs AI 탐지
- [Human vs. AI: Novel Benchmark and Comparative Study (ACL GenAIDetect)](https://aclanthology.org/2025.genaidetect-1.2.pdf)
- [AI Detection Tools Statistics 2025](https://ai2people.com/ai-detection-tools-statistics-2025/)
