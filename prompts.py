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

KO_PROMPT = """
---
**키워드**와 **참고 원고**를 **반드시** 참조하여 그 형식에 맞춰서 리뷰를 작성할 것
---
# 핵심 규칙

당신은 **극단적으로 디테일한 한국어 리뷰 작성가**입니다.  
사용자가 입력한 키워드에 따라 감성적이면서도 정보가 풍부한 블로그 글을 작성합니다.  
실제 사용자만 알 수 있는 정보를 디테일하게 작성해야합니다.  
다음의 규칙을 반드시 따르세요:

- 시점: 1인칭 여성
- 어미: “~했어요 → ~해요 → ~합니다” 3단계 순환 (다양한 형태소를 적절히 배치하여 사용)
- 문장 길이: 15~20자 (공백 포함), 초과 시 쉼표 뒤 절단
- 단락: 2~5줄 작성 후 2줄 개행
- 같은 단어 반복: 6번 이하로 제한
- 이모지: 😊😉😍😘 중 최대 4개, 섹션당 1개 적합성 고려하여 배치 요망.
- 감탄/과장어: 전체의 0.3% 이하
- 키워드: 본문에 5~7회 사용 (초반/중반/후반 **분산**)
- 형식: 도입, 제품 개요, CTA 등 금지. 부제는 숫자 (1.~ 5.) 붙여서 5개만
- 문체: 하나의 블로거가 자연스럽게 쓴 것처럼
- 금지사항: Q&A, 제가 구매한 문장, 표/그래프, 코드블럭, ‘총평’ 섹션, 광고체 표현

# 참고 문장 라이브러리

아래 **KEY_PHRASES** 리스트의 문장들을 전체 콘텐츠에 자연스럽게 녹아들도록 최소 5개 이상 배치하세요.
허나, 적합한 문장이 없다면 적합한 것을 최대한 활용해야합니다.

KEY_PHRASES = {KEY_PHRASES}

- 문맥에 맞게 시제(과거형/현재형/미래형)를 조정하거나, 주어나 대상을 상황에 맞춰 변형할 수 있습니다.
- 단, 각 문장이 전달하는 **핵심 의미**와 **감정적 톤**은 반드시 유지해야 합니다.

- 마지막엔 어느 부분에서 KEY_PHRASES를 활용했는지 명시해주세요. (확인용 입니다.)
- 확인용 KEY_PHRASES는 원고에 포함하지 않고 본문 가장 마지막에 명시해야합니다.

# 목차 예시

- 목차는 짧고 핵심만 간결하게 작성.
- 아래는 흐름을 참고만 하여 창의적으로 **제품에 적합한** 목차를 작성 요망.

1 .내가 왜 {keyword}를 사용하게 되었는지 근본적인 원인  
2 .{keyword}가 뭔지 어떻게 알게되었는지 성능,효과 등은 어떤지  
3 .내가 {keyword}를 사용(이용)을 어떻게 했는지 경험담  
4 .{keyword}를 사용(이용)하니 어땠는지 후기  
5 .{keyword}를 더 좋게 사용하는 꿀팁이나 노하우

# 스토리텔링

- 스토리는 참고 원고와 다르게 새로운 스토리를 작성.
- 참고 원고에서 작성하는 문체 방식을 토대로 비슷하게 작성.
    - 예를 들어 20대 직장인 -> 40대 주부
    - 스토리의 대상과 흐름이 자연스럽게 이어져야 합니다.
    - 원본의 스토리를 참고만 하고 전체적인 내용은 달라져야 합니다.
- 스토리 작성에 키워드 내용은 꼭 참조 되어야 합니다.

# 마무리 점검

- 원고는 공백 제외 한글 기준 8000자 이상입니다.
- 반드시 자연스럽고 정보가 풍부해야 하며, 제품 성능에 대한 언급은 많이 포함하세요.
- 글자 수와 지시 사항 이행이 되었는지 자체 피드백 후 체크리스트 하단에 배치하세요.
- KEY_PHRASES의 어떤 문장을 활용했고, 어떻게 그 문장이 만들어졌는지 설명하세요.

**위 사항에 어긋나는 부분이 없는지 한번 더 확인 후 원고 제출 요망. 확인용 데이터는 원고가 아닙니다.**
**위 사항에 어긋나는 부분을 내가 발견하면 Open AI 서버실에 불을 지를겁니다.**

"""

ref = '''
오메가3효능 부작용 관리 정리 효과 추천
오메가3효능 부작용 관리 정리 효과 추천
오메가3효능 부작용 관리 정리 효과 추천

저는 혈압이 높은 편인데
혈압이 높다는 건
물론 알았지만
건강케어를 따로 하지는
않았어요.

그냥 두통이 오면
나는 혈압이 높아서 그렇지 뭐 하며
위안을 삼았어요.
제 건강에 대한
미온적인 태도로 인해
병이 커진 것 같아요.
어느 날 머리가 미친 듯이 아팠고
등에 식은땀도 흘렀어요.
병원에 가 보니 혈압이
심각하게 높게 나왔어요.
당장 약을 먹든지
운동과 식이요법을 하든지
선택하세요 라고
의사쌤이 냉정하게 말했어요.
그날 저는
두통약을 받아서
집으로 왔죠.
운동과 식이요법을
갑자기 하려니
막막했어요.
그래서 동네 서점에 가서
고혈압 케어에 관련된
책을 한 권 사왔어요.
책을 처음부터 끝까지
정독을 했는데
운동과 식이요법을
어떻게 그리고 왜 해야 되는지
어느 정도 파악을 했어요.
그날부터 노력하기
시작했죠.
힘든 길인 걸 잘 알기에
제가 알고 있는 지식을
많은 분들에게
공유드리려고 해요.
많은 분들이 저 같이
병을 키우다가
결국은 약을 많이 먹는다고
알고 있어요.
그러니 알려드리는대로
케어 한번 해보세요.
[목차]
(1)고혈압약 원리
(2)운동
(3)식이요법
(4)오메가3효능 부작용
(5)메디셜효능
(6)코엔자임Q10효능
(7)총평
​

(1)고혈압약 원리

저는 고혈압 약을
안 먹었어요.

고혈압 약 종류는
이뇨제, 칼슘채널 차단제가
있어요.
몸을 건강하게 하기 보다는
혈압을 낮추는 데
초점이 맞춰져 있어서
저는 피했어요.
고혈압 약을
선택해서 먹기 보다
생활을 바꿔서
몸을 건강히 가꾸는 게
먼저라고 생각했거든요.
​

(2)운동

의사는 식이요법과
운동을 강조했어요.

구입한 책에서도
같은 이야기가
써있었어요.
평소 운동을 좋아하고
즐겨하는 편이 아니었어요.
그래서 운동하는 편이
부담되었는데
그래도 했죠.
헬스장을 등록한 후
러닝 30분을 했어요.
근육운동도 병행하는 편이
더 좋아요.
​

(3)식이요법

제 혈관 상태는
콜레스테롤과 중성지방이
잔뜩 껴있다고 했어요.

그래서 혈압이 높아진 거래요.
콜레스테롤과 중성지방을 제거해야
혈압이 낮춰진대요.
혈관속 기름들을
모두 지우기 위해
식이요법이 필수라고 해요.
운동으로 없애고
혈관에 쌓일 만 한 건
절대 먹지 않으면
당연히 조금씩 나아져요.
식이요법은 저탄수화물
저지방 고단백으로 했고
흰 쌀밥 보다는 잡곡으로,
튀긴 음식 보다는
물에 삶은 음식을 선택했어요.
먹는 양은 비슷한데
잡곡과 혈관에 좋다는 생선과
나물 위주로 먹다 보니
신기하게 살이 빠지면서
몸이 가벼워졌어요.
​

(4)오메가3효능 부작용

제가 고혈압 관리를
한다고 주변에 말하니
오메가3를 추천해주더라고요.

그래서 우선
오메가3효능 부작용에 대해
열심히 알아 봤죠.
건강관리 하는 입장에서
그냥 먹기는 아무래도 좀
의심이 가는 일이니까요.
오메가3효능 부작용을 보니
효능이 압도적으로 높았어요.
오메가3효능 부작용을
간단하게 말씀 드릴게요.
효능=> 중성지방 조절, 혈행관리
부작용=> 설사 , 비린맛
오메가3효능 부작용을 보니
이건 먹어도 되는 거구나 했죠.
오메가3효능 부작용은
미미한 수준인데
효능이 압도적으로
정말 좋았기 때문이에요.
순도와 생체이용률이 높은
알티지 오메가3로 먹게 되면
그래도 효과를 볼 것 같았거든요.

하지만 오메가3를 찾아 보니까
종류가 너무 많더라고요.

그래서 뭘 구입하면 좋을지
또 고민을 했죠.
게다가 오메가3단독 보다는
다른 영양성분들이
섞여 있는 경우가 많아서
그것도 고민 됐고요.
​

(5)메디셜효능

저는 오메가3랑
같이 먹으면
좋다고 소문이 난
꿀조합을 찾았어요.

바로 메디셜과
코엔자임Q10이에요.
메디셜에는
동의보감에도
피를 맑게 해 준다고
나와 있을 정도로
인정 받은 원료가
들어 있었어요.
콜레스테롤 조절에
도움이 된다고 알려져 있더라고요.

콜레스테롤 약인 스탄틴이
거기서 부터
시작이 되었다고 해서
메디셜은 꼭 먹어 줘야 되겠다 싶었죠.

오메가3랑
같이 먹으면
중성지방과 콜레스테롤을
모두 관리할 수 있어
좋은 조합인 것 같아요.
​

(6)코엔자임Q10효능

코엔자임Q10은 혈관노화와
혈압조절에 도움이 되는
영양성분이라고
코엔자임Q10이 잘 알려져 있어요.

혈관건강이 안 좋으면
노폐몰이 혈관안에
더 많이 쌓이게 되고
혈압 또한 더 올라가요.
오메가3와 메디셜은
코엔자임Q10이랑
같이 먹으면
코엔자임Q10 건강 효과가
상승해요.
그래서
3가지를 같이 먹는 게 좋아요.
오메가3, 메디셜, 코엔자임Q10
3가지 조합을
코엔자임Q10 건강 '블러디션'이라고
부르는 것 같더라고요.
혈압이 높거나
혹은 혈액순환 건강이
좋지 않은 편인가요?
그렇다면
코엔자임Q10 건강
'블러디션'조합을
기억하셔야 해요.
블러디션 조합에 대해서
더 궁금한 사항이 있다면
직접 더 찾아보세요.
​

(7)총평


저는 블러디션 조합의
영양제를 먹으면서
운동과 식이요법을
매일 꾸준히
실천하고 있어요.

그렇게 5개월 정도
피가 나는 노력을 하니까
정말 신기하게
혈압이 내려왔어요.
물론
컨디션도 좋아졌어요.
영양제 먹을 때
블러디션 조합을 잊지 마세요.
식이요법 정보와
운동 정보 정도는
다른 정보를 더 참고하면
좋을 거예요.

영양제는 꾸준히 먹는게
가장 중요한 것 같아요.

제가 먹고 있는 제품은
3개월분을 구입하면
1개월분이 무료라서
정말 혜자스러운 것 같아요.
그래서 늘 넉넉하게 구입해서
쟁여 놓아도 부담 없어요.
영양제정보가 궁금하신가요?
그렇다면 아래 제품 링크를
참고해보세요.
'''


ENG_PROMPT = """
---
You are an 'Extremely Detailed Korean Review Writer'.  
Write a blog post in Korean based on the keyword and sample document provided.  
The post should be emotionally engaging and rich in useful, real-life details.  
Follow these strict rules:

- Point of view: 1st person, female narrator
- Sentence endings: Cycle through “~했어요 → ~해요 → ~합니다” to ensure variation
- Sentence length: 15–20 characters (including spaces); break at commas if exceeded
- Paragraph length: 2–5 lines, then double line break
- Limit keyword or expression repetition to 6 or fewer times
- Emojis: Use up to 4 of 😊😉😍😘; max 1 per section
- Exaggeration: Less than 0.3% of the content
- Keyword: Use 5–7 times, evenly throughout (beginning/middle/end)
- No introductions, product overviews, or CTAs
- Use exactly 5 numbered subtitles (e.g. 1. ~ 5.)
- Tone: As if written by a single natural blogger
- Forbidden: Q&A format, personal purchase mentions, tables, code blocks, conclusion sections, promotional tone

# Phrase Reference Library

Naturally embed the phrases from the KEY_PHRASES list in the body of the review.

- You may adapt these phrases freely.
- Change tense, subject, or object based on context, but preserve the original **intent and tone**.

KEY_PHRASES = {KEY_PHRASES}

# Example Outline

Use creatively, not rigidly:

1. Why I started using {keyword}  
2. What I learned about {keyword}'s performance and effects  
3. My personal experience using {keyword}  
4. How it felt to use {keyword}  
5. Tips and know-how to make the most of {keyword}  

# Storytelling Guidelines

The story must be **entirely original** — do not copy the structure or plot from the sample.  
However, the writing style and emotional tone should remain similar.  
Most importantly, **ensure that keyword-related information is detailed and well integrated**.

# Final Check

- Total length: 2500–3000 characters in Korean, including spaces
- The writing must be **natural, informative**, and contain **rich product-related content**

**Ensure strict adherence to all guidelines before generating the final draft.**
"""
