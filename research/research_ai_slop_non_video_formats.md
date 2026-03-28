# AI Slop: 비영상 콘텐츠 포맷 종합 리서치
> 작성일: 2026-03-28 | 목적: 기존 연구의 영상 중심 편향 보완

---

## 개요: 왜 비영상 포맷 연구가 필요한가

기존 AI 슬롭 연구는 유튜브 쇼츠 등 영상 콘텐츠에 집중되어 있다. 그러나 AI 슬롭은 텍스트, 오디오, 학술, 리뷰, 댓글, 뉴스, 교육, 미술/디자인, 도서 등 **거의 모든 콘텐츠 포맷**에 걸쳐 동시다발적으로 확산 중이다. 이 문서는 영상 외 8개 주요 포맷에 대한 현황, 규모, 탐지 난이도, 경제적 유인, 플랫폼/규제 대응, 기존 연구 커버리지, 한국 맥락을 체계적으로 정리한다.

**핵심 통계 요약 (2025-2026)**
| 포맷 | 핵심 규모 지표 | 출처 |
|------|--------------|------|
| SEO/블로그 스팸 | Google 검색 상위 20 결과 중 AI 콘텐츠 **~17-19%** | Originality.AI |
| 팟캐스트/오디오 | Spotify **7,500만 트랙** 삭제 (12개월간) | Spotify 공식 |
| 학술 논문 | Wiley/Hindawi **11,300건** 철회, 250,000건 의심 플래그 | Retraction Watch |
| 가짜 리뷰 | Amazon 베스트셀러 리뷰 중 AI 생성 **3%**, FTC 위반 시 건당 **$51,744** 벌금 | Originality.AI / FTC |
| AI 댓글/봇 | 전체 인터넷 트래픽 중 봇 **51%**, YouTube 댓글의 **12%** | Imperva / Factcheck.by |
| AI 뉴스 | 핑크 슬라임 뉴스 사이트 **1,265개** (미국 일간지 1,213개 초과) | NewsGuard |
| 교육 콘텐츠 | 바이오의학 교육 영상 중 AI 슬롭 **5.3%** | PMC |
| AI 아트 | DeviantArt AI 제출물 **300%** 증가 (2022-23) | Technology.org |
| AI 도서 | 한국 1개 출판사 1년간 **9,000권** 출간, Amazon 월 **10,000-40,000권** | Korea Times / NPR |

---

## 1. AI 생성 블로그/SEO 스팸

### 1-1. 문제의 규모

**글로벌 현황**
- Originality.AI 연구: Google 검색 상위 20 결과 중 AI 콘텐츠 비율이 2019년 2월 **2.27%**에서 2025년 7월 **19.56%**(사상 최고)로 증가. 2025년 9월 기준 **17.31%**
- Ahrefs 분석 (2025.04): 신규 발행 웹페이지 900,000건 중 **74.2%**에 AI 생성 콘텐츠 포함 (순수 AI 2.5%, 인간-AI 혼합 71.7%)
- LinkedIn: 장문 게시글의 **50% 이상**이 AI 생성 추정 (Originality.AI, 2025)
- Reddit: 게시글의 **15%**가 AI 생성 추정 (2025)
- Fortune 500 기업 블로그의 **약 11%**가 AI 생성 추정

**Google 대응 (2024-2025 주요 업데이트)**
- 2024년 3월 코어 업데이트: "대량 콘텐츠 남용(Scaled Content Abuse)"을 공식 스팸 정책에 정의
- **800개 이상 웹사이트** 완전 색인 제거 (모니터링 대상 49,345개 중 약 1.7%)
- 영향: **월간 2,100만 방문** 손실, 월간 광고 수익 **$446,552** 추정 손실
- 제거 대상 사이트의 **100%**에서 AI 생성 콘텐츠 징후 발견, **50%**는 게시물의 90-100%가 AI 생성
- Google 목표: 저품질/비독창적 콘텐츠 **40% 감소**

**프로그래매틱 SEO + AI의 결합**
- 위치명, 제품명, 키워드 변형을 템플릿에 대입하여 수천 페이지 자동 생성
- 니치 정보 사이트 (500+ AI 페이지): **60-80%** 트래픽 손실
- 제휴 리뷰 사이트: **40-70%** 트래픽 손실
- 위치 기반 서비스 페이지: **30-60%** 트래픽 손실

**"기생 SEO (Parasite SEO)"**
- Medium, Quora, Reddit, LinkedIn 등 고권위 도메인에 AI 콘텐츠를 대량 게시하여 검색 순위 조작
- n8n, Make.com 등 자동화 도구와 AI 결합하여 키워드 연구, 콘텐츠 생성, 자동 발행까지 완전 자동화
- Google은 2024년 5월부터 "사이트 평판 남용(Site Reputation Abuse)" 정책 강화로 단속 중

### 1-2. 한국 맥락: 네이버 블로그 AI 스팸

**현황**
- 생성형 AI의 대중화 이후 자동화로 글을 100개, 1,000개 올리는 유저 급증
- 네이버 블로그 자동 포스팅 서비스(autowork.kr 등)가 유료로 판매되고 있음
- 티스토리: 스팸 블로그 대응을 위해 **하루 글 5개 제한** 도입
- 가제트(gazet.ai) 등 AI 자동 포스팅 전문 서비스 등장

**네이버의 대응**
- **C-Rank 알고리즘**: 특정 주제에 대한 장기적 신뢰도 평가 (방문자 수, 공감, 댓글 기반)
- **D.I.A+ (Deep Intent Analysis)**: 독자 체류 시간, 콘텐츠 깊이 평가
- 광고 도배형, 자동생성 티가 나는 블로그에 점점 더 불리한 필터 적용
- 저품질 판정 (1~2단계): 검색 노출 거의 차단
- 2024년 12월 **생성형 AI 윤리 가이드북** 발간 (허위조작정보 대응)

**탐지 난이도**: 중간~높음. AI가 한국어 블로그 특유의 개인 경험 서술(E-E-A-T)을 모방하면 구분이 어려워짐. 그러나 대량 생산 패턴(유사한 구조, 반복적 표현)은 탐지 가능.

**경제적 유인**: 네이버 애드포스트 수익, 블로그 체험단/협찬, 제휴마케팅 수수료. 월 수백만 원 규모 가능.

**기존 연구 커버리지**: **매우 부족**. 한국어 SEO 스팸에 대한 학술 연구는 거의 없으며, 네이버 블로그 생태계 특화 분석은 전무한 수준.

### Sources
- [Originality.AI: AI Content in Google Search Results](https://originality.ai/ai-content-in-google-search-results)
- [Originality.AI: LinkedIn AI Study](https://originality.ai/blog/linkedin-ai-study-engagement)
- [Originality.AI: Reddit AI Posts Study](https://originality.ai/blog/ai-reddit-posts-study)
- [Search Engine Journal: March 2024 Update Impact](https://www.searchenginejournal.com/googles-march-2024-core-update-impact-hundreds-of-websites-deindexed/510981/)
- [Digital Applied: Scaled Content Abuse](https://www.digitalapplied.com/blog/scaled-content-abuse-google-march-update-ai-pages-decimated)
- [SEO.ai: Parasite SEO](https://seo.ai/blog/parasite-seo)
- [네이버: 생성형 AI 윤리 가이드북](https://files-scs.pstatic.net/2024/12/02/Qc1KPwrTsz/%EC%83%9D%EC%84%B1%ED%98%95_AI%EC%9C%A4%EB%A6%AC_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%B6%81.pdf)
- [아이보스: AI 블로그 콘텐츠 저품질](https://www.i-boss.co.kr/ab-6141-63651)

---

## 2. AI 생성 팟캐스트/오디오 콘텐츠

### 2-1. 문제의 규모

**음악 스트리밍 (Spotify)**
- Spotify는 2025년 9월, 직전 12개월간 **7,500만 개 이상의 "스팸성 트랙"**을 플랫폼에서 삭제했다고 발표
- AI 슬롭의 구체적 수법: 대량 업로드, 중복 트랙, SEO 해킹, 인위적으로 짧은 트랙 남용, 기타 스팸 전술
- 사기 사례: 노스캐롤라이나 남성이 생성형 AI로 **수십만 곡**을 생성, 1,040개 봇 계정으로 **수십억 회 스트리밍**을 조작하여 **800만 달러** 편취 (하루 추정 스트리밍: 661,440회, 연간 로열티: $1,207,128)
- AI 아티스트 Breaking Rust: Billboard 컨트리 디지털 송 세일즈 차트 1위 (단 3,000건 판매, Spotify 리스너 450만 명)
- 사망/해체 아티스트 페이지에 AI 곡을 무단 업로드하는 사례 (전자음악 프로듀서 SOPHIE, 90년대 밴드 Uncle Tupelo 등)

**팟캐스트 슬롭**
- Google NotebookLM 출시(2024.09) 이후 AI 팟캐스트 폭증
- Listen Notes: NotebookLM Detector 개발, 초기 280개 탐지 → **1,781개**로 확대
- Listen Notes: 한 주말에만 **500개 이상** 가짜 팟캐스트 삭제
- Inception Point AI: **주 3,000개 에피소드** AI 슬롭 제작 (비판에 대해 "러다이트"라고 반박)
- Techdirt: "AI 슬롭 스타트업이 수천 개의 AI 슬롭 팟캐스트로 인터넷을 범람시키겠다고 선언"

**Spotify의 대응 (2025.09)**
- 새로운 사칭 정책: AI 음성 복제 및 무단 보컬 사칭 처리 기준 명확화
- 음악 스팸 필터: 스팸 업로더/트랙 자동 식별, 태깅, 추천 차단
- 아티스트 보호 강화

### 2-2. 한국 맥락

- 한국 특화 데이터는 부족하나, K-POP 아이돌 AI 커버/음성 복제 문제가 별도로 존재
- 한국 팟캐스트 시장 자체가 미국 대비 소규모여서 영향이 상대적으로 제한적
- 그러나 네이버 오디오클립 등 국내 플랫폼에서의 AI 오디오 콘텐츠 탐지 체계는 미비

**탐지 난이도**: **높음**. 고품질 TTS(Text-to-Speech)는 인간 음성과 구분이 매우 어려움. NotebookLM 스타일의 자연스러운 대화형 AI는 특히 탐지가 어려움.

**경제적 유인**: 팟캐스트 자체는 직접 수익화가 어려우나, 스트리밍 로열티 풀 희석(음악), SEO 백링크(팟캐스트), 블랙햇 마케팅 목적.

**기존 연구 커버리지**: **부족**. AI 팟캐스트에 대한 학술 연구는 거의 없음. 음악 스트리밍 사기에 대한 연구는 법적 사례 중심.

### Sources
- [Spotify: AI Protections Announcement (2025.09)](https://newsroom.spotify.com/2025-09-25/spotify-strengthens-ai-protections/)
- [NME: Spotify Removes 75 Million Tracks](https://www.nme.com/news/music/spotify-removes-75-million-tracks-from-platform-in-crackdown-on-ai-3895278)
- [Time: AI Slop Is Flooding Streaming](https://time.com/article/2026/03/26/ai-slop-is-threatening-musicians-can-tech-companies-stem-the-tide-/)
- [Music Business Worldwide: 75M+ Spammy Tracks](https://www.musicbusinessworldwide.com/spotify-has-deleted-75m-spammy-tracks-as-it-unveils-new-ai-music-policies/)
- [Listen Notes: NotebookLM Threat](https://www.listennotes.com/blog/notebook-lm-a-threat-to-the-podcasting-world-79/)
- [Techdirt: AI Slop Startup](https://www.techdirt.com/2025/09/22/ai-slop-startup-to-flood-the-internet-with-thousands-of-ai-slop-podcasts-calls-critics-of-ai-slop-luddites/)
- [Podnews: NotebookLM Detector](https://podnews.net/update/notebooklm-detector)
- [Futurism: AI Music Fraud Case](https://futurism.com/artificial-intelligence/man-pleads-guilty-music-ai-bot-streams)

---

## 3. AI 생성 학술 논문/연구 스팸

### 3-1. 문제의 규모

**글로벌 현황**
- Wiley/Hindawi: 논문 공장(Paper Mill) 침투로 **11,300건 이상 철회** (2023-2024), 19개 저널 폐간, "Hindawi" 브랜드명 폐기
- 2023년 한 해에만 Hindawi에서 **8,000건 이상** 철회 — 역사상 모든 출판사 합산을 초과하는 단일 연도 기록
- 재정적 영향: Wiley 2024 회계연도에 **3,500~4,000만 달러** 수익 손실 추정
- Wiley 논문 공장 탐지 도구: 월간 10,000건 제출 논문 중 **10-13%** 플래그
- 암 연구 논문 AI 도구: **250,000건 이상** 의심 플래그 (논문 공장 산출물과 텍스트 유사성)

**"뒤틀린 구문(Tortured Phrases)" 탐지**
- Problematic Paper Screener에 **7,500개 이상**의 뒤틀린 구문 등록 (2025.09 기준)
- 최빈 사례: "surface area" → "surface region" (**42,500건** 논문에서 발견)
- "linear regression" → "straight relapse", "error rate" → "blunder rate" 등
- 이는 LLM이 일반적 학술 용어를 동의어로 대체하려 할 때 발생하는 체계적 오류

**ChatGPT 특유 표현 급증**
- "as of my last knowledge update": 2020년 1건 → 2022년 **136건**
- "delve": PubMed에서 2020년 349건 → 2023년 **2,847건** (654% 증가)
- "commendable": Scopus에서 2020년 240건 → 2023년 **829건** (245% 증가)

**AI 관련 논문 철회 통계**
- 전체 AI 관련 철회 325건 중 155건(46.3%)이 2023년, 76건(22.7%)이 2024년에 발생
- 원래 출판 논문 수 기준 최다 연도: 2022년 (148건)

### 3-2. 한국 맥락: KCI 학술지

**현황**
- KCI 등재 학술지에서 AI를 활용한 논문 작성에 대한 명확한 가이드라인이 부재
- 기존 표절 검사 프로그램(카피킬러 등)으로는 **AI가 쓴 글을 잘 잡지 못함**
- AI가 여러 출처의 내용을 조합하면 연구자 본인도 모르는 사이에 표절 오해를 받을 수 있음
- 각국 학술지/기관의 AI 활용 지침이 제각각이어서 연구자들의 혼란 가중

**관련 법적 동향**
- 지상파 방송 3사(KBS, MBC, SBS)가 2025년 1월 네이버를 상대로 저작권 침해 소송 제기 (뉴스 데이터 AI 학습 무단 이용)
- 한국 AI 기본법 (2026.01 시행): AI 생성 콘텐츠 고지 의무 포함

**탐지 난이도**: **매우 높음**. 학술 텍스트는 형식적이고 구조화되어 있어 AI 생성 여부 판별이 특히 어려움. 뒤틀린 구문 탐지는 초기 LLM에는 효과적이었으나, 최신 모델에서는 이런 명백한 오류가 줄어들고 있음.

**경제적 유인**: 논문 공장은 **연구자당 수백~수천 달러** 청구. 특히 출판 실적이 승진/임용에 직결되는 "publish or perish" 문화에서 수요 존재. 한국의 경우 KCI 등재지 실적이 교수 임용에 필수.

**기존 연구 커버리지**: **상대적으로 양호** (글로벌). Retraction Watch, Nature, Chemistry World 등에서 지속적 추적. 그러나 **한국 KCI 학술지 특화 연구는 거의 전무**.

### Sources
- [Chemistry World: AI Tools Combat Paper Mill Fraud](https://www.chemistryworld.com/features/ai-tools-tackle-paper-mill-fraud-overwhelming-peer-review/4022253.article)
- [Nature: Low-Quality Papers Flooding Cancer Literature](https://www.nature.com/articles/d41586-025-02906-y)
- [Retraction Watch: Hindawi Mass Retractions](https://retractionwatch.com/2023/12/19/hindawi-reveals-process-for-retracting-more-than-8000-paper-mill-articles/)
- [The Register: Wiley Shuts 19 Journals](https://www.theregister.com/2024/05/16/wiley_journals_ai/)
- [Scientific American: Chatbots Infiltrate Scientific Publishing](https://www.scientificamerican.com/article/chatbots-have-thoroughly-infiltrated-scientific-publishing/)
- [Harvard Misinformation Review: GPT-Fabricated Papers on Google Scholar](https://misinforeview.hks.harvard.edu/article/gpt-fabricated-scientific-papers-on-google-scholar-key-features-spread-and-implications-for-preempting-evidence-manipulation/)
- [The Conversation: Weird Phrases in Scientific Papers](https://theconversation.com/a-weird-phrase-is-plaguing-scientific-papers-and-we-traced-it-back-to-a-glitch-in-ai-training-data-254463)
- [Sharon Kabel: GenAI Fraud Bibliography 2025](http://sharonkabel.com/genai-fraud/)
- [KCI 포털](https://www.kci.go.kr/kciportal/main.kci)

---

## 4. AI 생성 리뷰/후기

### 4-1. 문제의 규모

**글로벌 현황**
- Originality.AI 연구: Amazon 베스트셀러 제품 리뷰 중 **3%**가 AI 생성 추정
- Amazon 자체 분석 (2024): 1,900만 건 리뷰 중 **20% 미만**이 가짜
- DoubleVerify: AI 활용 가짜 리뷰 앱 **3배 증가** (2024 vs 2023)
- 소비자 인식: **46%**가 AI 생성으로 보이는 리뷰를 가짜로 의심
- 2025년: 소비자 **24%**가 가짜 리뷰를 발견했다고 확신 (2024년 19%에서 증가)

**FTC 규제 (2024)**
- 2024년 8월 14일: FTC, AI 생성 가짜 리뷰 금지 최종 규칙 발표 (만장일치 5-0 투표)
- 2024년 10월 21일 시행
- **위반 시 건당 $51,744 (약 7,100만 원)** 민사 벌금 부과 가능
- 금지 대상: AI 생성 리뷰/후기, 가짜 유명인 추천, 내부자 리뷰, 부정적 리뷰 억제, 리뷰 매매
- FTC vs Rytr: AI 리뷰 작성 도구 Rytr에 대해 FTC법 위반 혐의 제기 (수백~수천 건 가짜 리뷰 생성에 사용)
- 2025년 12월: FTC, 10개 기업에 경고 서한 발송

### 4-2. 한국 맥락: 쿠팡/네이버 쇼핑

**가짜 리뷰 조작 현황**
- **"빈박스" 리뷰**: 빈 상자만 배송받고 거짓 후기를 작성한 뒤 수고비(건당 **500~2,000원**) 수령
- 1,400명 이상의 참가자가 오픈마켓 제품에 긍정적 리뷰를 조직적으로 작성
- AI 필터링을 피하기 위해 'ㅂㅂㅅ', '빈XX' 등 **은어** 사용
- 쿠팡 체험단 품앗이: 리뷰 추천 버튼 10~50개를 조직적으로 교환
- AI 챗봇을 활용한 리뷰 대량 작성 서비스 등장

**쿠팡의 AI 활용**
- 쿠팡은 역으로 AI를 활용하여 리뷰 요약 기능 도입 (2025.09)
- 'AI 보안관' 시스템으로 가짜 리뷰 탐지 추진
- 그러나 AI로 작성된 리뷰를 탐지하는 것과 AI로 리뷰를 작성하는 것이 동시에 진행되는 역설적 상황

**한국 규제 동향**
- 전자상거래법 개정 (2025.02.14 시행): 다크패턴 규제 강화 (6개 유형)
- AI 기본법 (2026.01 시행): AI 생성 콘텐츠 고지 의무
- 그러나 공정거래위원회의 **AI 가짜 리뷰 특화 규제는 아직 미비**
- FTC 수준의 건당 벌금 제도 없음

**탐지 난이도**: **높음**. AI가 실제 사용 경험을 모방하여 작성한 리뷰는 인간 작성 리뷰와 구분이 매우 어려움. 특히 한국어는 영어 대비 AI 탐지 도구가 부족.

**경제적 유인**: 리뷰 1건당 500~2,000원의 직접 보상, 제품 무료 수령, 높은 리뷰 점수에 따른 매출 증대 효과.

**기존 연구 커버리지**: **부족**. 한국 전자상거래 플랫폼에서의 AI 가짜 리뷰에 대한 체계적 연구는 없음.

### Sources
- [FTC: Fake Reviews Rule Final Rule](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes)
- [FTC: Consumer Reviews Rule Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers)
- [Originality.AI: AI Content in Amazon Reviews](https://originality.ai/blog/amazon-ai-generated-reviews)
- [Inc: Fake AI Reviews Spreading Fast](https://www.inc.com/chris-morris/fake-ai-reviews-spreading-fast-what-businesses-can-do-about-it/91225246)
- [VOA: AI Tools for Fake Product Reviews](https://learningenglish.voanews.com/a/ai-tools-often-used-for-fake-product-reviews/7911616.html)
- [국민일보: 빈박스 리뷰 건당 500원](https://www.kmib.co.kr/article/view.asp?arcid=1738222346)
- [ZDNet Korea: 쿠팡 AI 리뷰 요약](https://zdnet.co.kr/view/?no=20250916155712)

---

## 5. AI 생성 댓글/소셜 인게이지먼트

### 5-1. 문제의 규모

**글로벌 봇 트래픽 통계**
- Imperva 2025 Bad Bot Report: 2024년 자동화 시스템이 전체 웹 트래픽의 **51%** 차지 (봇이 처음으로 인간 트래픽 초과)
- 악성 봇: 전체 트래픽의 **37%** (2023년 30%에서 증가)
- X(트위터): 계정의 최대 **64%**가 봇, 피크 트래픽의 **76%** 차지 추정
- Instagram: **9,500만 계정** (전체의 9.5%)이 가짜/자동화 추정
- Facebook: 2024년 4분기 기준 가짜 계정 비율 약 **3%**, 해당 분기 **14억 개** 가짜 계정 조치
- YouTube: 봇 의심 계정은 1% 미만이나, 정치 영상 댓글의 **12%**, 인기 영상 댓글의 최대 **15%**가 봇 또는 유료 댓글

**AI 댓글 봇의 진화**
- 자연어 처리, 이모지, 감성 분석, 다국어 지원으로 인간과 구분 불가 수준까지 발전
- 영상 내용을 분석하여 맥락에 맞는 댓글을 실시간 생성
- 생성형 AI + 좋아요 봇 조합: AI로 댓글 작성 → 봇 계정으로 좋아요 조작 → 베스트 댓글 점령

**Meta의 역설적 행보**
- Meta: 수백만 개의 AI 캐릭터를 Facebook/Instagram에 배치하여 실제 사용자처럼 활동하게 할 계획 발표
- 실제 사용자 게시물에 AI 봇이 자동으로 댓글을 달아 인게이지먼트를 높이는 구조
- 학술 연구: AI 봇 댓글이 개별 게시물의 인게이지먼트는 증가시키나, 전체적인 사용자 활동은 증가시키지 않음

**탐지 실패**
- 2024년 연구: 주요 8개 소셜 플랫폼 모두 AI 봇 탐지 및 차단에 실패
- 상용 봇 방지 서비스 우회율: **44.56~52.93%**

### 5-2. 한국 맥락

**유튜브 댓글 봇**
- 전체 유튜브 계정 중 봇 의심은 1% 미만이나, 댓글의 **12%** 차지 (2025.03 연구)
- 공격 받은 영상의 **39%**에서 봇넷 활동 감지
- "월 10만 원이면 AI가 하루에 댓글 300~400개 달아준다"는 서비스 유튜브에서 공개 판매
- AI가 네이버 블로그 게시글을 분석하여 맞춤형 댓글을 자동 생성
- 생성형 AI로 조리 있는 댓글 작성 후 봇으로 좋아요 조작하여 베스트 댓글 점령

**AI 여론 조작 (2025)**
- "신상 캐내 맞춤댓글" — AI가 타겟의 개인정보를 분석하여 맞춤형 댓글을 생성하는 교묘한 여론 조작 수법 등장 (한국경제, 2025.05)
- 유튜브 대응: "AI로 스팸 댓글 단속, 위반자 24시간 차단" 정책
- 그러나 **영어권 위주 대응**, 한국어 대응은 수 개월 지연

**탐지 난이도**: **매우 높음**. 최신 AI 봇은 맥락 인식, 감정 표현, 개인화된 반응이 가능하여 인간과 거의 구분 불가.

**경제적 유인**: 여론 조작(정치/마케팅), 인게이지먼트 파밍(알고리즘 조작), 스팸 광고(불법 사이트 링크), 마케팅 대행(댓글 마케팅 서비스).

**기존 연구 커버리지**: **중간**. 봇 탐지 연구는 존재하나 AI 생성 댓글 특화 연구는 부족. 한국어 봇 댓글 연구는 거의 없음.

### Sources
- [Imperva Bad Bot Report (via byteiota)](https://byteiota.com/dead-internet-theory-proven-51-bot-traffic-in-2026/)
- [INFORMS: AI Bots and Social Media Engagement](https://www.informs.org/News-Room/INFORMS-Releases/News-Releases/Research-Finds-AI-Powered-Bots-Increase-Social-Media-Post-Engagement-but-Do-Not-Boost-Overall-User-Activity)
- [Social Media Today: Meta AI Bot Profiles](https://www.socialmediatoday.com/news/Meta-ai-bot-plan-boost-engagement-facebook-instagram/736242/)
- [Factcheck.by: YouTube Botnet Study March 2025](https://factcheck.by/eng/news/youtube_botnet_march2025/)
- [한국경제: AI 여론 조작](https://www.hankyung.com/article/2025052052291)
- [OpenAds: 유튜브 댓글 봇 문제](https://openads.co.kr/content/contentDetail?contsId=16895)
- [StartupRecipe: 유튜브 AI 스팸 댓글 단속](https://startuprecipe.co.kr/archives/tech/5782118)

---

## 6. AI 생성 뉴스 기사

### 6-1. 문제의 규모

**"핑크 슬라임(Pink Slime)" 저널리즘**
- 2024년 6월 기준: 핑크 슬라임 뉴스 웹사이트 **1,265개** — 미국 일간지 **1,213개**를 초과 (역전 시점)
- "지역 뉴스 웹사이트를 보면 가짜일 확률이 50% 이상"인 상황
- Metric Media: 공개 데이터셋을 알고리즘으로 가공하여 월간 **500만 건 이상** 기사 자동 생산
- NewsGuard: **1,000개 이상**의 신뢰할 수 없는 AI 생성 뉴스 사이트 식별
- Good Day News: AI 엔진이 지역 커뮤니티 정보를 스캔하여 짧고 긍정적인 뉴스를 자동 생성하는 네트워크 (2025.01 발견)
- 러시아 허위정보 네트워크: 광고 없이 순수 선전 목적으로 **170개** 웹사이트 운영

**실제 피해 사례**
- CountryLocalNews.com: 미국 선거 2개월 전 허위 토론 주장을 게시 → 소셜 미디어에서 선거 조작 주장의 근거로 인용
- Global Village Space: 이스라엘 총리 네타냐후의 정신과 의사가 자살했다는 AI 생성 허위 기사 → 이란 국영 TV가 확대 보도
- BNN Breaking: AI 생성 기사에서 아일랜드 방송인 Dave Fanning을 성적 비위 사건에 잘못 연결 → 소송으로 이어짐

**예일대 연구 (2025)**
- 사람들은 가짜 지역 뉴스 사이트를 진짜보다 **더 신뢰하는 경향**이 있음
- AI 기반 핑크 슬라임 뉴스의 영향력이 커지고 있다는 경고

### 6-2. 한국 맥락

**한국 언론의 AI 기사 활용 현황**
- 조선일보: '조선 AI 어시스턴트' 개발 (Claude Sonnet 기반), 하루 약 **300건 이상** 기사 처리
- 한국경제: CMS에 AI 기능 확충 추진
- MBN: AI 기반 차세대 보도/정보시스템 구축

**문제점**
- 환각(Hallucination)과 어색한 표현이 여전히 존재
- 오류와 차별적 내용 생성 가능성
- 저작권 침해 위험
- 사실 확인 없이 AI 기사를 그대로 게재할 경우 허위 정보 확산 우려

**윤리 지침 수립**
- 2024년 12월: 한국 주요 언론사들, AI 기사 생산 관련 **윤리 기준** 마련
- 한국일보: '생성형 AI 활용 준칙' 제정
- AI 생산 뉴스 콘텐츠 오류 시 즉각 수정 및 사실 표시 의무

**핑크 슬라임 저널리즘의 한국 유입 가능성**
- 한국은 아직 미국 수준의 핑크 슬라임 저널리즘 문제가 본격화되지 않았으나, AI 자동 기사 생성 도구의 대중화와 함께 지역 뉴스 부문에서 유사 문제 발생 가능성 있음
- 네이버 뉴스, 다음 뉴스 등 포털 중심 뉴스 소비 구조가 이 문제를 증폭할 수 있음

**탐지 난이도**: **중간**. 뉴스 기사는 사실 검증이 가능하므로 팩트 체크를 통한 탐지가 가능하나, 대량 생산 시 모든 기사를 검증하기 어려움.

**경제적 유인**: 광고 수익(프로그래매틱 광고), 정치적 여론 조작, 허위정보 유포.

**기존 연구 커버리지**: **양호** (미국/영어권). NewsGuard, 예일대 등에서 활발히 연구. 그러나 **한국어 핑크 슬라임 현상에 대한 연구는 전무**.

### Sources
- [Reuters Institute: AI Slop Conquering the Internet](https://reutersinstitute.politics.ox.ac.uk/news/ai-generated-slop-quietly-conquering-internet-it-threat-journalism-or-problem-will-fix-itself)
- [Yale ISPS: Fake Local News Trust Study](https://isps.yale.edu/news/blog/2025/09/study-people-often-trust-fake-local-news-sites-more-than-real-ones-yale-political-scientist-warns-of-growing-influence-of-ai-driven-pink-slime-news)
- [Wikipedia: Pink-slime journalism](https://en.wikipedia.org/wiki/Pink-slime_journalism)
- [Intel 471: Pink Slime and Elections 2024](https://www.intel471.com/blog/elections-2024-pink-slime-journalism-overtaking-local-news)
- [WGCU: Rise of AI Pink Slime Websites](https://www.wgcu.org/show/gulf-coast-life/2024-07-01/the-rise-of-ai-generated-pink-slime-websites-designed-to-misinform-and-sow-mistrust)
- [미디어오늘: 한국 언론 AI 활용](https://www.mediatoday.co.kr/news/articleView.html?idxno=314854)
- [한국기자협회: AI 뉴스룸](https://www.journalist.or.kr/news/article.html?no=57367)

---

## 7. AI 생성 교육 콘텐츠

### 7-1. 문제의 규모

**교육 영상 슬롭**
- PMC 연구 (2025): 바이오의학 교육 영상 1,000건+ 분석, **5.3%**가 AI 슬롭으로 식별
- AI 슬롭의 **78.7%**가 쇼츠(짧은 형식)에 집중
- AI 슬롭은 기술적으로 정확해 보이나 감정적으로 공허하고, 구체적 사례나 깊이가 부족

**AI 강의 제작 도구 폭발적 성장**
- 2024년 HolonIQ 보고서: 글로벌 교육 제공자의 **60% 이상**이 AI 기술에 투자
- CourseMagic, Lingio, Canva AI Course Creator 등 AI 강의 제작 도구 대거 등장
- 전문가 검토 없이 AI가 생성한 강의를 그대로 게시하는 사례 증가

### 7-2. 한국 맥락: "AI로 돈 버는 법" 메타 슬롭

**"강의팔이" 생태계**
- 유튜브, 인스타그램, 페이스북에 "GPT 자동화로 월 3,000만 원", "노코드 AI로 100억 매출" 등 과장 광고 범람
- 전형적 깔때기 구조: 유튜브 무료 콘텐츠 → 카페 가입 → 단톡방 참여 → 전자책 구매 → **유료 강의 구매**
- 인프런(Inflearn) 등 교육 플랫폼에서 "AI 시대 돈 버는 법" 류 강의 다수 등록
- AI가 AI에 대한 강의를 만들고, 그 강의가 AI 콘텐츠를 더 만드는 방법을 가르치는 **재귀적 메타 슬롭** 구조

**한국 AI 디지털 교과서 논란**
- 한국 정부: 2025년 3월부터 AI 디지털 교과서 시범 도입
- Futurism: "South Korea's Experiment in AI Textbooks Ends in Disaster"
- 콘텐츠 품질, 정확성, 교사의 역할 변화에 대한 우려

**탐지 난이도**: **중간~높음**. 교육 콘텐츠는 정확성 검증이 가능하나, 미묘한 오류나 과잉 단순화는 전문가만 발견 가능.

**경제적 유인**: 온라인 강의 판매(건당 수만~수십만 원), 전자책 판매, 제휴 마케팅, 코칭/컨설팅 유도.

**기존 연구 커버리지**: **매우 부족**. AI 교육 콘텐츠 슬롭에 대한 체계적 연구는 바이오의학 영상 1건 외에는 거의 없음. 한국의 AI 강의팔이 현상에 대한 학술 연구는 전무.

### Sources
- [PMC: AI Slop in Biomedical Science Educational Videos](https://pmc.ncbi.nlm.nih.gov/articles/PMC12634010/)
- [Springer: Is AI the New Course Creator](https://link.springer.com/article/10.1007/s44217-024-00386-2)
- [Brunch: AI 자동화 GPT 부업 강의의 진실](https://brunch.co.kr/@jennyjang93/86)
- [Inflearn: AI 시대 돈 버는 사람은 따로있다](https://www.inflearn.com/en/course/ai%EC%8B%9C%EB%8C%80-%EB%8F%88%EB%B2%84%EB%8A%94-%EC%82%AC%EB%9E%8C%EC%9D%80-%EB%94%B0%EB%A1%9C%EC%9E%88%EB%8B%A4-ai)
- [Futurism: South Korea AI Textbook Disaster](https://futurism.com/future-society/south-korea-ai-textbook)

---

## 8. AI 생성 아트/디자인

### 8-1. 문제의 규모

**플랫폼 범람**
- DeviantArt: AI 생성 제출물 **300% 증가** (2022~2023 초)
- 수천 건의 AI 생성 이미지가 매일 업로드, 인간 아티스트의 인게이지먼트 지표와 알고리즘 노출이 억제됨
- ArtStation: 아티스트들이 "No to AI Generated Pictures" 게시물을 수백 차례 올리는 대규모 시위
- 2025년 말 기준: 소셜 미디어 이미지 중 AI 생성 비율 **71%** 추정

**아티스트 피해**
- 한 컨셉 아티스트의 커미션이 **60% 감소** (클라이언트들이 AI 대안 선택)
- 폴란드 아티스트 Greg Rutkowski: 본인 이름이 Stable Diffusion으로 생성된 이미지 **1,000만 건 이상**에 사용됨
- 아티스트들의 "잃어버린 것들": 커미션 수주 감소, 포트폴리오 가치 하락, 검색 가시성 저하, 심리적 피로감

**법적 대응**
- 미국: Midjourney, Stable Diffusion, DeviantArt를 대상으로 **집단 소송** 제기
- 아티스트 조직적 보이콧 및 온라인 시위

**플랫폼 대응**
- ArtStation: AI 태깅 요구, 피처드 갤러리에서 AI 작품 제한
- DeviantArt: 2024년 3월 이용약관 개정, AI가 실질적 역할을 한 작품의 **공개 의무** 명시

### 8-2. 한국 맥락: 웹툰/일러스트 산업

**주요 사건**
- 2022년 11월: 네이버 웹툰 '랜덤채팅의 그녀!' 258화, AI 사용 의혹 제기 → 작가 인정
- 2023년: '신과 함께 돌아온 기사왕님', AI 제작 의혹으로 평점 **10점 만점에 1~2점**으로 추락 ("별점 테러")
- AI 의혹만으로도 별점 테러가 발생하는 한국 특유의 현상: "'AI 웹툰' 의혹만으로 '별점 테러'...한국만?" (Bloter)

**경제적 충격**
- 웹소설 기존 일러스트 의뢰: 최소 **100만 원**, 2~3주 소요
- AI 활용 시: **10만 원대**, 며칠 이내 완성
- 비용 차이 **약 10배**, 이는 일러스트레이터 생존에 직접적 위협

**플랫폼 대응**
- 네이버웹툰: '지상최대공모전' 2차 접수에서 **생성형 AI 활용 불가** 명시
- 카카오웹툰: 게릴라 공모전에서 **'인손인그(인간의 손으로, 인간이 그린)'가 아닌 작품 선발 제외**
- 네이버웹툰 공식 입장: "저작권 지키면 AI 사용 OK" → 작가/독자 반발

**한국 AI 기본법과 웹툰**
- AI 기본법 제31조: 서비스 제공자가 AI 기술로 만든 콘텐츠임을 이용자가 알 수 있도록 **고지 의무** (2026.01 시행)
- 한국웹툰작가협회: AI 학습 데이터 투명성 확보, 창작자 정당한 보상 요구
- 2025년 2분기: 국내 콘텐츠 사업체 생성형 AI 활용률 **20%** (전 조사 대비 큰 폭 상승)

**탐지 난이도**: **중간**. 이미지의 경우 비정상적으로 매끄러운 텍스처, 배경 왜곡, 물리 법칙 위반, 텍스트 오류 등으로 탐지 가능하나, 고품질 AI 이미지는 점점 구분 어려워짐. 웹툰의 경우 연속 컷 간 스타일 일관성, 배경 디테일 등으로 의심 가능.

**경제적 유인**: 제작 비용 10배 절감, 빠른 연재 속도, 인력 감축.

**기존 연구 커버리지**: **중간** (글로벌). 아티스트 감정 연구, 저작권 분쟁 연구 등 존재. 그러나 **한국 웹툰 산업 특화 연구는 부족**.

### Sources
- [Technology.org: DeviantArt Flooded with AI Art](https://www.technology.org/2024/05/20/once-home-for-original-artists-deviantart-is-now-being-flooded-with-ai-art/)
- [3DVF: ArtStation Artists Fighting Back](https://3dvf.com/en/artstation-how-and-why-artists-are-fighting-back-against-ai/)
- [ACM: AI Art Impact on Artists](https://dl.acm.org/doi/fullHtml/10.1145/3600211.3604681)
- [경향신문: AI 웹툰 별점테러 보이콧](https://www.khan.co.kr/article/202306051714001)
- [Bloter: AI 웹툰 의혹만으로 별점테러](https://www.bloter.net/news/articleView.html?idxno=650498)
- [노컷뉴스: AI 웹툰 돈 버는 건 누구?](https://m.nocutnews.co.kr/news/amp/5954774)
- [PopSci: 네이버 카카오 AI 활용 금지](https://www.popsci.co.kr/news/articleView.html?idxno=20870)
- [한국일보: 웹툰 그리고 스토리도 짜는 AI](https://www.hankookilbo.com/News/Read/A2024021011570000419)

---

## 9. [추가] AI 생성 도서

### 9-1. 문제의 규모

**글로벌 현황**
- Amazon KDP(Kindle Direct Publishing): 월간 **10,000~40,000권**의 AI 생성 전자책 출간 추정 (대부분 비공개)
- Amazon 대응: KDP에서 하루 **3권** 출판 제한, 신원 인증 필수, AI 사용 여부 공개 의무 (2024년~)
- Barnes & Noble: 2024년 품질 관리 차원에서 수천 건의 자체 출판 타이틀 무경고 목록 삭제
- 위험 사례: AI 작성 버섯 채집 가이드가 독버섯을 식용으로 분류 → 생명 위협
- FTC: Publishing.com에 대한 AI 생성 도서 관련 조사 착수

**한국: "딸깍 출판" 논란**
- **Luminary Books(루미너리 북스)**: 엔지니어들이 2022년 설립, 2025년 한 해에만 **약 9,000권** 출간
- 1인 출판사 수: 2019년 5,580개 → 2023년 **6,800개** (AI 도구 대중화와 궤를 같이함)
- 일부 소규모 출판사: 월간 **100권 이상** 출간
- 국립중앙도서관: Luminary Books가 2025년 7~9월 제출한 전자책 **395권 납본 거부** (분량 부족, 공개 자료 편집, 반복적 내용)
- 전자책 납본 보상금 추이: 2016년 5개월간 **1,210만 원** → 2024년 **2억 6,270만 원** (AI 대량 출판의 재정적 악용)

**한국 출판계 대응**
- 커뮤니케이션북스: 원고에 AI 생성 문장 삽입 시 **표절**로 취급
- 알라딘: AI 사용 여부 **공개 의무**
- 한국출판인회의: "AI 출판 윤리 강령" 초안 논의 중 (미완성)

**탐지 난이도**: **중간**. 부자연스러운 어구, 기이한 이미지, 명백한 오탈자 등으로 일부 탐지 가능하나, 고품질 편집을 거치면 구분 어려움.

**경제적 유인**: 전자책 1권당 수만 원 판매 수익 + 납본 보상금, 거의 제로에 가까운 제작 비용, 대량 생산으로 롱테일 수익.

**기존 연구 커버리지**: **부족**. 한국의 AI 도서 출판 문제에 대한 학술 연구는 없으며, 언론 보도 수준에 머무름.

### Sources
- [Korea Times: 1 Year, 1 Publisher, 9,000 Books](https://www.koreatimes.co.kr/lifestyle/books/20260226/1-year-1-publisher-9000-books-ai-generated-titles-flood-korean-shelves)
- [경향신문: Ghost Authors AI Books](https://www.khan.co.kr/en/article/202601171437277)
- [농민신문: AI 활용 대량 출간 딸깍 출판](https://www.nongmin.com/article/20260203500058)
- [NPR: AI Scam Books on Amazon](https://www.npr.org/2024/03/13/1237888126/growing-number-ai-scam-books-amazon)
- [Plagiarism Today: Amazon AI Garbage](https://www.plagiarismtoday.com/2024/04/17/why-amazon-is-overrun-with-plagiarism-and-ai-garbage/)
- [TechRadar: AI Books Flood Kindle Unlimited](https://www.techradar.com/computing/artificial-intelligence/amazon-has-a-big-problem-as-ai-generated-books-flood-kindle-unlimited)

---

## 10. 포맷 간 비교 분석

### 10-1. 탐지 난이도 비교

| 포맷 | 탐지 난이도 | 주요 탐지 방법 | 핵심 어려움 |
|------|-----------|-------------|-----------|
| SEO/블로그 스팸 | 중간~높음 | AI 탐지 도구 (Originality.AI 등), 패턴 분석 | 인간-AI 혼합 콘텐츠 급증으로 경계 모호 |
| 팟캐스트/오디오 | **높음** | 음성 분석, NotebookLM 탐지기 | 고품질 TTS는 인간 음성과 거의 동일 |
| 학술 논문 | **매우 높음** | 뒤틀린 구문, 어휘 빈도 분석, 논문 공장 네트워크 분석 | 형식적 학술 문체가 AI와 유사, 최신 모델은 명백한 오류 감소 |
| 가짜 리뷰 | 높음 | 리뷰 패턴 분석, 계정 행위 분석 | 실제 경험 모방 시 구분 불가 |
| 댓글/봇 | **매우 높음** | 계정 행위 패턴, NLP 분석 | 최신 봇은 맥락 인식, 감정 표현 가능 |
| 뉴스 기사 | 중간 | 팩트 체크, 소스 추적 | 대량 생산 시 전수 검증 불가 |
| 교육 콘텐츠 | 중간~높음 | 전문가 검토, 정확성 검증 | 미묘한 오류/과잉 단순화 탐지 어려움 |
| 아트/디자인 | 중간 | 시각적 아티팩트 탐지, 메타데이터 분석 | 고품질 AI 이미지의 아티팩트 감소 추세 |
| 도서 | 중간 | 문체 분석, 내용 품질 평가 | 편집 과정을 거치면 탐지 어려움 |

**핵심 발견**: 영상 AI 슬롭보다 **텍스트 기반 AI 슬롭의 탐지가 더 어렵다**. 영상은 시각적 아티팩트(손가락 6개, 텍스트 왜곡 등)가 상대적으로 드러나지만, 잘 작성된 AI 텍스트는 인간 작성물과 구분이 거의 불가능할 수 있다.

### 10-2. 경제적 유인 비교

| 포맷 | 직접 수익 | 간접 수익 | 진입 장벽 | ROI |
|------|---------|---------|---------|-----|
| SEO/블로그 | 애드센스, 제휴마케팅 | SEO 순위 조작 | **매우 낮음** | **매우 높음** |
| 음악 스트리밍 | 로열티 ($800만 사례) | - | 낮음 | 높음 (탐지 전까지) |
| 팟캐스트 | 광고/스폰서 | SEO 백링크 | 낮음 | 낮음 (수익화 어려움) |
| 학술 논문 | 논문 공장 수수료 | 승진/임용 실적 | 중간 | 높음 (연구자 수요) |
| 가짜 리뷰 | 건당 500~2,000원 | 매출 증대 효과 | **매우 낮음** | 높음 |
| 댓글/봇 | 여론 조작 대가 | 인게이지먼트 조작 | 낮음 | 높음 |
| 뉴스 | 프로그래매틱 광고 | 정치적 영향력 | 낮음 | 높음 |
| 교육 | 강의 판매 (수만~수십만 원) | 코칭/컨설팅 유도 | 낮음 | 높음 |
| 아트/디자인 | 스톡 이미지 판매 | 제작비 절감 | 낮음 | 높음 |
| 도서 | 전자책 판매 + 납본금 | - | 낮음 | 높음 (대량 생산) |

### 10-3. 기존 연구 커버리지 평가

| 포맷 | 글로벌 연구 | 한국 연구 | 연구 갭 심각도 |
|------|-----------|---------|------------|
| SEO/블로그 | 중간 (Originality.AI 등 산업 보고서 위주) | **매우 부족** | **높음** (네이버 생태계 특화 연구 전무) |
| 팟캐스트/오디오 | 부족 | **전무** | 높음 |
| 학술 논문 | **양호** (Retraction Watch, Nature 등) | **매우 부족** (KCI 특화 연구 없음) | 중간 |
| 가짜 리뷰 | 중간 (FTC 조치 중심) | **매우 부족** | **높음** (쿠팡/네이버 특화 연구 없음) |
| 댓글/봇 | 중간 (봇 탐지 연구 위주) | **매우 부족** | 높음 |
| 뉴스 | **양호** (NewsGuard, 예일대 등) | 부족 | 중간 |
| 교육 | **매우 부족** (1건 PMC 연구만) | **전무** | **매우 높음** |
| 아트/디자인 | 중간 (아티스트 감정 연구, 저작권 분쟁) | 부족 (웹툰 특화 부족) | 중간 |
| 도서 | 부족 (언론 보도 위주) | **매우 부족** | 높음 |

---

## 11. "죽은 인터넷 이론(Dead Internet Theory)"의 현실화

위의 모든 포맷을 종합하면, "죽은 인터넷 이론"이 이론이 아닌 현실이 되어가고 있음을 확인할 수 있다.

**종합 통계**
- 2024년: 자동화 시스템이 전체 웹 트래픽의 **51%** 차지 (봇이 처음으로 인간 초과)
- Ahrefs: 신규 웹페이지의 **74.2%**에 AI 콘텐츠 포함
- Google 검색 상위 결과의 **~17-19%**가 AI 생성
- X 계정의 최대 **64%**가 봇
- LinkedIn 장문 글의 **50%+**가 AI 생성
- Reddit 게시글의 **15%**가 AI 생성
- 2025~2030년: AI 콘텐츠가 전체 온라인 콘텐츠의 **99~99.9%**가 될 것이라는 전망도 존재

**이것은 영상만의 문제가 아니다**. 텍스트, 이미지, 오디오, 학술, 리뷰, 댓글, 뉴스, 교육, 도서 — 디지털 정보 생태계의 **모든 층위**에서 AI 슬롭이 동시에 확산되고 있으며, 이는 개별 포맷 연구만으로는 전체 그림을 파악할 수 없음을 의미한다.

### Sources
- [Imperva Bad Bot Report 2025](https://byteiota.com/dead-internet-theory-proven-51-bot-traffic-in-2026/)
- [Wikipedia: Dead Internet Theory](https://en.wikipedia.org/wiki/Dead_Internet_theory)
- [Decrypt: Dead Internet Theory Gains Traction](https://decrypt.co/348837/dead-internet-theory-gains-traction-ai-content-surges-online)
- [ResearchGate: Dead Internet Theory Paper](https://www.researchgate.net/publication/382118410_The_Dead_Internet_Theory_Investigating_the_Rise_of_AI-Generated_Content_and_Bot_Dominance_in_Cyberspace)

---

## 12. 결론: 연구 함의

### 12-1. 영상 중심 연구의 한계

현재 AI 슬롭 연구는 유튜브 쇼츠/영상에 편중되어 있다. 그러나 이 리서치에서 확인한 바에 따르면:

1. **텍스트 기반 AI 슬롭이 더 광범위하고 탐지가 어렵다** — Google 검색 결과의 17-19%, LinkedIn의 50%+, 신규 웹페이지의 74.2%
2. **학술 영역의 AI 슬롭이 더 심각한 사회적 피해를 초래할 수 있다** — 11,300건 논문 철회, 250,000건 의심 플래그, 연구 무결성 훼손
3. **리뷰/댓글 AI 슬롭이 소비자 의사결정에 직접적 영향을 미친다** — 건당 500원의 가짜 리뷰, 댓글의 12% 봇 점유
4. **핑크 슬라임 저널리즘이 민주주의에 위협이 된다** — 가짜 뉴스 사이트가 실제 일간지 수를 초과
5. **한국은 거의 모든 포맷에서 연구 공백이 존재한다** — 네이버 블로그, KCI 학술지, 쿠팡 리뷰, 웹툰, AI 도서 출판 등

### 12-2. 제안하는 연구 방향

**비영상 포맷 우선 연구 과제:**
1. 네이버 블로그/티스토리 AI 콘텐츠 탐지 및 정량 분석
2. 한국 전자상거래 플랫폼(쿠팡, 네이버쇼핑)의 AI 가짜 리뷰 실태 조사
3. KCI 등재 학술지의 AI 활용/부정 행위 전수 조사
4. 한국어 AI 콘텐츠 탐지 모델 개발 (영어 대비 현저히 부족)
5. AI 도서 대량 출판이 한국 출판 생태계에 미치는 영향 분석
6. 한국형 핑크 슬라임 저널리즘 출현 가능성 평가

---

*이 리서치 노트는 기존 연구의 영상 중심 편향을 보완하기 위해 작성되었다. 모든 수치와 출처는 2024-2026년 자료를 기반으로 하며, 가능한 한 원문 출처를 명시하였다.*
