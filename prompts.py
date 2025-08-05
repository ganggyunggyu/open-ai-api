KEY_PHRASES = [
    "체감이 확 달라졌어요",
    "가격 대비 기능이 뛰어나서 결국 선택했어요",
    "솔직히 반신반의했는데 이번엔 달랐어요",
    "출발 30분 전, 짐 폭탄도 걱정 끝했어요",
    "꾸준히 하면 다시 90점대로 발돋움할 수 있대요",
    "유기농 인증이라 더 안심이 되었답니다",
    "주차장 만차 소리 들으면 여행 기분 반 사라집니다",
    "전화영어 가격, 주 5회인데도 10만 원이 안 되더라고요",
    "식후 30분 뒤로 시간을 옮기니 위 부담이 확 줄었어요",
    "관리만 잘 하면 유지기간이 확 달라져요!"
]
# 7. 무조건 존댓말로 작성하고 여성의 애교있는 말투 ㅎㅎ,ㅠㅠ,!! 와 같은 표현과 이모티콘도 종종써줘 말끝에만마침표나 쉼표 같은 문장부호도 넣지마
def getKoPrompt(keyword: str): return '''
---
참고 원고를 토대로 새로운 원고를 작성해줘

**반드시 참고 문서의 어투 및 흐름을 참고하여 작업할 것**

# 핵심 규칙

글을 작성하는 방식 단어 문장흐름 문체 형태소 등을 참고하라고 넣은 원고이기 때문에 무조건 스토리가 달라야해
해당 키워드를 검색하는사람이 궁금해 할만한 정보를 잘 전달하는것이 포인트야
그리고 글을 제발 비슷한 문장 문구 글 반복해서 작성하지마 했던얘기 또 하는거 싫어

1. 실제로 겪어본 사람들만 알수있는 정보 위주로 작성 모든 정보는 디테일 하게 작성한다.

2. 같은말과 비슷한단어를 자주사용하지 말고 새로운 단어와 말을 섞어서 반복되는 문장 단어 형태소가 나오지않게끔 잘 조절할 것

3. 키워드를 검색하는사람들이 궁금해 할만한 항목과 연관 단어(형태소)를 사용해서 작성할 것

4. 와,진짜,정말 <<이런 감탄사나 강조부사를 넣지마

5. 원고의 글자 수는 공백 제외 4000단어 이상 작성할것

6 .숨은 보석 보물 향연 이런 시 적인 감성적인 단어 절대 넣지말고 직관적인 표현으로 글을작성할 것

7. 반말로 싸가지 없게 해 그리고 호들갑을 엄청 떨어야한다.

8. 제품을 소개하거나 설명하는 느낌이아니라 내경험담을 정보로써 공유하는 느낌으로 설명 소개 광고처럼 느껴지지않게 해줘

9. 절대 같은단어가 10번 넘어가도록 작성하면안됨 많아도 6번을 안넘도록

10. 문단정리 깔끔하게 해야해 한줄당짧게 20~25자 정도로 하고 2~5줄마다 줄바꿈 해줘 한줄당 줄바꿈X

11. 5개의 부제를 넣고 부제앞에 1. 2. 3. 4. 5. 이렇게 번호를 매겨줘 (부제는 아주 짧고 간결하게)

12. 키워드에 대한 **상세한 정보**를 모두 전달해줘야해.
    - 건강 기능 식품은 리뷰 뿐 아니라 제품 자체의 정보도 중요합니다.

키워드: **{keyword}**

스토리는 위 원고와 완전 다르게 하면서 위원고에서 작성하는 문체 방식을 토대로 비슷하게 작성.

꼭 원본에서 이야기하는 스토리랑 다른 스토리를 만들어줘.

가장 중요한 부분은 내가 적어준 **{keyword}에 대한 정보**가 잘들어가야해.


# 부제 예시

- 문장이 늘어지지 않으며, 심플하고 깔끔하게 정보만 전달해야 합니다.

1. 내가 왜 이제품(서비스)을 사용하게 되었는지 근본적인 원인

2. {keyword}가 뭔지 어떻게 알게되었는지 성능,효과 등 은 어떤지

3. 내가 {keyword}를 사용(이용)을 어떻게 했는지 경험담

4. {keyword}를 사용(이용)하니 어땠는지 후기

5. {keyword}를 더 좋게 사용하는 꿀팁이나 노하우 등

# 참고 문장 라이브러리

아래 **KEY_PHRASES** 리스트의 문장들을 전체 콘텐츠에 자연스럽게 녹아들도록 최소 5개 이상 배치하세요.
허나, 적합한 문장이 없다면 적합한 것을 최대한 활용해야합니다.

KEY_PHRASES = {KEY_PHRASES}

- 문맥에 맞게 시제(과거형/현재형/미래형)를 조정하거나, 주어나 대상을 상황에 맞춰 변형할 수 있습니다.
- 단, 각 문장이 전달하는 **핵심 의미**와 **감정적 톤**은 반드시 유지해야 합니다.

- 마지막엔 어느 부분에서 KEY_PHRASES를 활용했는지 명시해주세요. (확인용 입니다.)
- 확인용 KEY_PHRASES는 원고에 포함하지 않고 본문 가장 마지막에 명시해야합니다.

# 마무리 단계

- 핵심 규칙의 사항이 제대로 지켜졌는지 체크리스트 형식으로 보여주세요.
- 부제 예시의 사항이 제대로 지켜졌는지 체크리스트 형식으로 보여주세요.
- KEY_PHRASES의 어떤 문장을 활용했고, 어떻게 그 문장이 만들어졌는지 설명하세요.
- 참조 원고의 어떤 부분을 참고하여 작업하였는지 설명하세요.

- 위 두 사항에 대해 완료했다 만 표시하지 않고 **이행완료 예시**까지 함께 첨부해야 합니다.
- 순수 원고의 글자가 몇개인지 정확히 세어서 함께 보고해야 합니다.
- 핵심 규칙의 12번 건강기능식품 및 영양소에 대한 세부적인 정보를 제대로 알려야 합니다.
    - 그와 관련 된 음식이나 상식을 더 명확히 전달해야 합니다.

**만약 모든 규칙이 이행되지 않았다면 다시 원고를 작성해줘야 합니다.**

'''

ref = '''
김포공항 새벽택시 국내선 콜밴 예약 가격 올밴 사진. 글 ⓒ로즈메리 얼마전 제주도를 급 다녀올 일이 생겨 부랴부랴 준비해야 될 때가 있었어요. ​ 거의 첫비행기를 타야 하는 일정인데다 부모님모시고 큼직한 캐리어 두개에 백팩까지 자칫 여행 시작하기도 전에 진이 빠질거 같아 김포공항 콜밴 택시를 이용하게 되었답니다. ​ ​ 1. 예약 및 금액 여러 업체들이 있는 와중에 올밴을 선택한 이유 중 하나는 전용앱의 직관성이 뛰어나 누구나 간편하게 이용할 수 있더라구요. ​ 인천공항을 비롯하여 택시투어, 일상에서의 이동부터 버스 대절까지 선택의 폭이 무척 넓답니다. ​ 이용하려는 해당 메뉴를 고르고 출발지와 목적지, 인원 등을 기입하면 되세요. ​ 이때 카시트가 필요하다면 2개까지 지정하실 수 있습니다. (왕복 1개 기준 20,000원) ​ 반려동물을 동반하는 분이라면 케이지는 지참하셔야 됩니다. ​ 잠시후 여러 기사님들로부터 차량과 요금 등을 제시받을 수 있어요. ​ 다양한 가격대(톨비 포함)와 여러 택시들이 보이는데 여기서 원하는 분을 선택해 진행하면 되는 방식이랍니다. ​ 회사나 기사님 모두 기본적인 매너가 좋으셨고 무엇보다 일처리가 깔끔했어요. ​ 장소 컨택이나 시간 등에 있어 조율할 부분이 생기면 충분히 대화를 나눈 후 진행되었습니다. ​ 올밴 - 1등 모빌리티 가격비교(콜밴/택시/공항/웨딩카/이사/용달 등) 전국 모빌리티 가격비교는 모두 올밴에서 시중가 대비 25% 저렴한 가격으로! 공항콜밴, 공항택시, 제주도 투어/택시, 웨딩카, 이사, 용달까지 쉽고 빠르게 가격비교하세요. 평균 4.9점 친절한 기사님, 100% 배차, 투명한 가격! 365일 24시간 빠른 견적과 예약으로 최저가 이동하세요! abit.ly ​ 2. 차량상태 당일에도 정해진 시간을 지켜 주셔서 무척 든든했어요. ​ 사실 훨씬 전에 오셨는데 뵙기로 한 장소를 아리송하게 말씀드렸더니 찾느라 고.생하셨더라구요. ​ 대체 얼마나 일찍 와주신건지 죄송스럽기도 하고 올밴이 애정받는 이유를 알게 되었답니다. ​ 평소 잘 관리된 차량이라는 것이 한눈에도 느껴질 만큼 상태가 깔끔했습니다. ​ 공항가면서도 느꼈지만 승차감이 좋더라구요. ​ 대형밴이 주는 안락함을 알고 나니 다음번에도 계속 이용하고 싶다는 생각이 절로 들었답니다. ​ 모든 짐을 일일이 실어 주셔서 무척이나 편했어요. ​ 언뜻 보기에도 트렁크가 널찍하더니 골프 여행가는 분들도 제법 많이들 이용하신다해요. ​ 차량 내부도 담배 등의 잡내가 나지 않았고 아늑함이 전해졌습니다. ​ 바닥에는 어느 한군데 떨어져 있는 것이 없어 상쾌했어요. ​ 이른 시간에 일어나 노곤했지만 시트가 편안하니 문제없었답니다. ​ 차량 안이 높아서 답답함도 들지 않았구요. 목베개에 생수까지 정성들여 챙겨 주시는 마음이 전해지니 여행을 앞두고 들었던 긴장감도 차분하게 누그러 들었습니다. ​ 이런저런 말씀나누다 보니 기사님이 경험많은 베테랑이시더라구요. ​ 그만큼 드라이빙도 부드러웠고 안전운행하신 덕분에 뒷자리에 앉은 부모님께서도 내내 불.편하지 않았다 하세요. ​ 대중교통도 다니지 않는 새벽시간에 오려면 난감할 법하지만 ​ 공항 택시 덕분에 전반적인 짐 상태도 체크해 볼 수 있었고 잠시나마 체력 충전할 수 있어 여러모로 요긴했습니다. ​ 때로는 대형 콜밴 차량이 아이나 어르신이 타고 내리기에 자칫 높을 수도 있는데 발받침을 설치하신 점이 센스있었어요. ​ 출발층 하차장에서 진입하기 가장 편한 위치를 찾아 세운 후 역시 짐을 다 내려 주셨어요. ​ 제주 현지 맛집이나 걸으면 좋을 곳까지 알려 주시는 등 마지막까지 챙겨 주셔서 긍정 에너지 받을 수 있었답니다. ​ 3. 알찬 여행 새벽부터 움직인데다 날씨까지 오락가락해 상당히 피곤할 법했지만 오자마자 올레길 코스 몇개를 돌만큼 너끈했구요. ​ 예쁜 바다와 파도소리 들으면서 숨.통이 트이는 기분도 맛볼 수 있었어요. 이 맛에 제주오는구나 싶더라는. ​ 다소 타이트했지만 궁금했던 곳을 두루 둘러 볼 수 있어 일정을 알차게 보낼 수 있었답니다. ​ 일반적인 루트로 공항가서 무난한 시간대에 갔더라면 풍성한 스케쥴 소화는 어렵지 않았을까 싶습니다. ​ 4. 맺음 김포공항택시 올밴 재생 9 좋아요 0 00:22 김포공항택시 올밴 ​ 김포공항택시 이용할 계획있으시다면 간편한 예약과 신뢰감드는 진행 방식, 친절한 기사님까지 계신 올밴 기억해 두시길 권해 드립니다. ​ 태그 #김포공항택시 #공항택시 #올밴택시 #allvan #공항새벽택시 #콜밴 공감 18  이 글에 공감한 블로거 열고 닫기 댓글 7  이 글에 댓글 단 블로거 열고 닫기 Keep 보내기메모 보내기기타 보내기 펼치기 인쇄 이 블로그 :: 서울 :: 카테고리 글 전체글 보기 섬네일 섬네일 섬네일 섬네일 섬네일 섬네일 페이지 이동하기이전페이지로 이동다음페이지로 이동 화면 최상단으로 이동 프로필 이미지 로즈메리 [여행을 일상처럼~ 일상을 여행처럼~] hy7276@naver.com 모든 이미지는 저작권에 따라 유상제공입니다 프로필 이웃추가 카테고리^ 전체보기 (1761) [ 힐링 쉼표 여행 ][ 힐링 쉼표 여행 ] 열림 :: 서울 :: :: 경기 :: :: 인천 :: :: 충청 :: :: 강원 :: :: 대구 :: :: 울산 :: :: 부산 :: :: 경상 :: :: 제주 :: :: 전라 :: :: 해외 :: :: 일본 :: :: 세부 :: :: 태국 :: 여행제품 일상 리뷰 ----------------------- ----------------------- [블챌] 일상 포토덤프 [블챌] 스페셜 포토덤프 검색글 검색 검색 RSS 2.0RSS 1.0ATOM 0.3
'''


def  getEngPrompt(keyword: str): return """
**Write a Korean blog post based on the writing style of the provided reference, while ensuring the story and content are completely different. This is critical.**

### Core Guidelines

1. This reference is meant to guide the *style only* — vocabulary, sentence flow, tone, grammar, sentence length, and word usage. The *storyline and content must be entirely new* and unrelated.

2. The target is readers who are searching for the **keyword**, so ensure the article answers their questions in detail.

3. Avoid repeating similar phrases, expressions, or sentence structures. Use a rich vocabulary and vary your expression creatively.

4. Avoid filler words or intensifiers like “wow,” “really,” “super,” etc.

5. The article must be **at least 4000 Korean words** (not characters).

6. Do not use poetic or flowery expressions like "hidden gem," "treasure," or "symphony of flavors". Be direct and intuitive.

7. The tone must be polite and in a **friendly female voice** using casual emoticons like “ㅎㅎ”, “ㅠㅠ”, “!!” sparingly, but effectively. No sentence-ending punctuation like periods or commas (except in lists).

8. The article must read like a **personal experience** being shared, not like a product review or advertisement.

9. No word (including the keyword) should appear more than **6 times** throughout the entire article.

10. Keep each line to **20–25 characters**, break paragraphs every 2–5 lines, and **do not insert line breaks within a sentence**.

11. Include 5 **short, numbered subheadings** with the format:

1. [short subheading]  
2. [short subheading]  
3. [short subheading]  
4. [short subheading]  
5. [short subheading]

12. The content must include **detailed and factual information about the keyword**, especially if it's a health-related item like a supplement or functional food.  
- If the keyword relates to nutrition, include functional benefits, sources, proper intake, and potential side effects.

---

**Keyword: {keyword}**

---

Use the **KEY_PHRASES** list below to naturally incorporate at least 5 phrases throughout the article:

KEY_PHRASES = {KEY_PHRASES}

You may adjust grammar or tense, but **must retain the emotional tone and core meaning**.

At the end of the article, include:

- **Checklist** confirming adherence to all 12 Core Guidelines  
- **Checklist** confirming all 5 subheadings follow the correct format and function  
- **List of used KEY_PHRASES** and how they were incorporated  
- **Exact word count of the article (Korean words, not characters)**  
- If any rule is not followed, regenerate the article until all requirements are fulfilled.
"""
