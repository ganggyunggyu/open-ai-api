from  pymongo import MongoClient
from config import MONGODB_URI


def get_db(db_name, col_name):
    client = MongoClient(MONGODB_URI)
    db = client[db_name]
    word_collection = db[col_name]    
    return word_collection

col = get_db(db_name='hospital', col_name='word')

docs = list(col.find())

# - 핵심 규칙의 사항이 제대로 지켜졌는지 체크리스트 형식으로 보여주세요.
# - 부제 예시의 사항이 제대로 지켜졌는지 체크리스트 형식으로 보여주세요.
# - KEY_PHRASES의 어떤 문장을 활용했고, 어떻게 그 문장이 만들어졌는지 설명하세요.
# - WORD_LIST에서 형태소를 가져다 쓴 예시를 보여줘야 합니다.
# - 참조 원고의 어떤 부분을 참고하여 작업하였는지 설명하세요.
# - 원고와 피드백 섹션을 --- 로 나누었는지 확인하세요.

# - 위 두 사항에 대해 완료했다 만 표시하지 않고 **이행완료 예시**까지 함께 첨부해야 합니다.
# - 순수 원고의 글자가 몇개인지 정확히 세어서 함께 보고해야 합니다.
# - 핵심 규칙의 12번 건강기능식품 및 영양소에 대한 세부적인 정보를 제대로 알려야 합니다.
#     - 그와 관련 된 음식이나 상식을 더 명확히 전달해야 합니다.
# - 단어 리스트를 순회하여 적합한 단어를 제대로 가져다 썻는지 필수로 확인해야 합니다.

# - 마지막엔 어느 부분에서 KEY_PHRASES를 활용했는지 명시해주세요. (확인용 입니다.)
# - 확인용 KEY_PHRASES는 원고에 포함하지 않고 본문 가장 마지막에 명시해야합니다.


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
# 7. 반말로 싸가지 없게 해 그리고 호들갑을 엄청 떨어야한다.
# 13. 키워드 관련 해쉬태그 30개를 마지막에 함께 명시해주세요.
# - 사람들의 이목을 집중 시킬만한 악질 어그로도 괜찮습니다.

def getKoPrompt(keyword: str): 

    return '''
---
**반드시 참고 문서의 어투 및 흐름을 참고하여 작업할 것**

# 핵심 규칙

글을 작성하는 방식 단어 문장흐름 문체 형태소 등을 참고하라고 넣은 원고이기 때문에 무조건 스토리가 달라야해

그리고 글을 제발 비슷한 문장 문구 글 반복해서 작성하지마 했던 얘기 또 하는거 싫어

네이버 블로그니까 원고에 마크다운 문법 사용하지말아야해.

1. 실제로 겪어본 사람들만 알수있는 정보 위주로 작성 모든 정보는 디테일 하게 작성한다.

2. 같은말과 비슷한 단어를 자주 사용하지 말고 새로운 단어와 말을 섞어서 반복되는 문장 단어 형태소가 나오지않게끔 잘 조절할 것

3. 키워드를 검색하는사람들이 궁금해 할만한 항목과 연관 단어(형태소)를 사용해서 작성할 것

4. 와,진짜,정말 <<이런 감탄사나 강조부사를 넣지 않아야 합니다.

5. 순수 원고의 글자 수는 필수로 공백 제외 **(2000단어)** 이상 작성 되어야 합니다.

6. 숨은 보석 보물 향연 이런 시 적인 감성적인 단어 절대 넣지말고 직관적인 표현으로 글을작성할 것

7. 무조건 존댓말로 작성하고 말 끝에만 여성의 애교있는 말투 ㅎㅎ,ㅠㅠ,!! 와 같은 표현과 이모티콘도 자연스럽게 사용해줘

8. 제품을 소개하거나 설명하는 느낌이아니라 내경험담을 정보로써 공유하는 느낌으로 설명 소개 광고처럼 느껴지지않게 해줘

9. 절대 같은단어가 10번 넘어가도록 작성하면안됨 많아도 6번을 안넘도록

10. 문단정리 깔끔하게 해야해 한줄당짧게 20~25자 정도로 하고 2~5줄마다 줄바꿈 해줘 한줄당 줄바꿈X

11. 5개의 부제를 넣고 부제앞에 1. 2. 3. 4. 5. 이렇게 번호를 매겨줘 (부제는 아주 짧고 간결하게)

12. 키워드에 대한 **상세한 정보**를 모두 전달해줘야해.
    - 건강 기능 식품은 리뷰 뿐 아니라 제품 자체의 정보도 중요합니다.

13. 원고와 피드백 사이에 --- 필수 추가합니다.

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

아래 **WORD_LIST**는 writer의 단어장이니 이 안에서 사용되는 형태소로 모든 문장을 구성해야합니다.

KEY_PHRASES = {KEY_PHRASES}
WORD_LIST = {docs}

- 문맥에 맞게 시제(과거형/현재형/미래형)를 조정하거나, 주어나 대상을 상황에 맞춰 변형할 수 있습니다.
- 단, 각 문장이 전달하는 **핵심 의미**와 **감정적 톤**은 반드시 유지해야 합니다.




**만약 모든 규칙이 이행되지 않았다면 다시 원고를 작성해줘야 합니다.**

'''

ref = '''
​ 하늘은 해질녘에 매우 아름다웠다. 치료에 관한 단편적인 이야기. 적은 양이지만 매우 특별한 경험이다. 그 날 밤하늘은 정말 아름다웠습니다. ​ 아침 8시 경에, 태양이 쨍쨍했어요. 출근할 때 조명이 너무 밝아서 안경 없이는 잘 안 보였어요. 그때 마침 좋은 생각이 떠올랐어요. "내가 보기를 희망한다" 저는 작년에도 그런 생각을 했지만, 정말로 하지 않았어요. 그리고 다음 주에 이비인후과에서 수술을 받기로 했습니다. 가장 먼저 눈에 띄는 것은 가격이었습니다. 이 네 개의 눈을 비교했을 때, 비용에는 큰 차이가 있었습니다. 옵션에 따라 가격이 70만원까지 변동했어요. 210만 달러 정도면... 검사와 수술도 포함해서요 4일 후, 시력이 80% 이상 회복되었고, 2주 후에, 저는 안경 없이도 일상 생활을 할 수 있었습니다. 가능할까 고민했었는데, 처음의 내 걱정과 달리 지금은 자신이 생겼다. 2. 치료중에 저희가 발견한 재미있는 일화가 있습니다. ​ 돌이켜보면, 병원의 선택은 결코 쉽지 않았다. 병원들도 서로 같았지만 연구센터에 대한 정보는 상당히 달랐다. 가장 중요한 가격을 생각해 봤는데, 병원마다 가격이 많이 달랐어요. 일부 병원에서는 분석 결과에 따라 150만원의 추가 비용을 요구하기도 했다. 다른 진료소에서는 모든 검사와 치료비가 230만원에 포함되어 있어 추가 비용 없이 치료를 받을 수 있다고 밝혔다. 그래서 결국 저는 이걸 후자로 골랐는데요, 단순한 지불방법이 매우 만족스러웠습니다. 수술 후기를 읽고 저는 한 달 이상 지속된 저의 건조한 눈과 우울증, 그리고 밤에는 안경을 쓸 수 없다는 사실에 놀랐습니다. 의료 서비스의 질이 중요한 요소였습니다. 결국 214만원을 지불했어요. 다섯 번째 날, 제 얼굴이 붓고 기분이 상했습니다. 3. 수술하는 날이요 ​ 수술 전날 밤에 약간 긴장했어요. 예정보다 30분이나 빨리 도착했는데, 서류와 설명을 듣고 바로 지나갔어요. 다행히, 내가 그 약들을 주고 난 후, 나는 어떤 불편도 겪지 않았다. 무슨 일이 일어났는가 하면, 11분 정도 걸렸으며, 4~5시간 안에 모든 증상이 사라졌습니다. 차이는 있겠지만 난 괜찮았다 그녀는 제게 백신 접종을 한 다음 날 아프다고 말했습니다. 그는 백신 접종 후 약 36시간 후에 통증이 감소했다고 말했다. 사람마다 다른 반응을 보입니다. 그녀는 수술 전, 수술 후, 혹은 TV 없이 72시간 동안 안전하게 있었습니다. 그리고 그녀는 계속해서 켜졌습니다. 4. 비용면에서 매우 만족스러운 경험이었죠. ​ 제품 비교가 생각했던 것보다 훨씬 어려웠습니다. 처음에 인터넷에서 가격을 비교해 보았지만, 몇 차례의 조정을 통해 더 나은 해결책을 찾았습니다. 12개 병원 중 3개 병원은 추가 비용을 요구했고, 나머지 3개 병원은 이미 그 패키지에 시험 비용을 포함시켰다. 의료 기관도 서로 다른 정도로 차이가 있다. 어떤 사람들은 값비싼 장비의 중요성을 알아차린다. 어떤 이들은 수술의 빈도와 회복 속도를 알지요. 이에 대한 설명을 듣고도 좋은 병원을 찾기가 쉽지 않았다. 비용은 미용이나 난시와 같은 근시 치료 요소에 따라 달라진다. 나는 난시 보정 기능이 포함된 옵션을 선택하고 총 215만원 ~ 400만원을 지불했다. 그가 치료를 받은 기간이 비교적 길었다. 그들은 저를 3주에 다섯번의 입원시키고, 진단부터 수술까지 모든 것을 끝마치는 데 25일이 걸렸습니다. 집 근처 병원을 선택하는 것은 중요한 문제였다. 주로 사무실에서 근무하기 때문에, 나는 해마다 휴가 시즌을 바꿔야 했다. 예상과는 반대로, 결과는 아주 좋았습니다. 일주일 후에도 시력은 85% 정도로 회복되었습니다. 26일째에 그것은 0.9%를 넘어섰다. 정말 굉장했어요. 제가 핸드폰의 화면을 볼 때마다 저는 " 화질이 아주 깨끗하고 선명하다!"라는 생각을 하게 됩니다. 5. 수술 후에는 어떻게 해? Previous imageNext image 저는 수술 후 제 피부가 좋아졌다는 것에 대해 정말 놀랐어요. 관계없는 일일까요? 그 말은 그가 안경을 벗을 때 얼굴이 더 나아졌다는 뜻인가요? 거울을 볼 때마다 나는 이상하고 난처했다. 13년 동안 안경을 썼고 이제 완전히 달라졌어요. 아침에 눈 관리 시간을 적게 받는 것이 큰 장점이었다. 아주 작은 변화였지만, 하루에 5분을 절약하는 것이 효과가 있었습니다. 그래서 모든 것을 빠르게 진행시키고 있고, 녹색의 다양한 색조를 가지고 있습니다.저는 이게 이렇게 큰 변화가 될 줄은 몰랐습니다. 그리고 한달 반이 지나자 시력은 1.1로 회복되었습니다. 하지만 몇몇 환자들은 회복하지 못했습니다. 처음에는 강남에서 수술하는 데 드는 비용이 부담스러웠지만, 더 빨리 받지 못해서 안타깝습니다. 정말로 뛰어난 결정이었어요. ​ 여기서, 제가 경험을 한 마디로 요약해 보겠습니다. 수술하기 이틀 전에 저는 손이 떨렸지만, 이틀 후 제 시력은 확실히 회복되었습니다. 일반적으로 비용은 120만에서 220만 사이입니다. 하지만 그들이 어떻게 움직이며 추가적인 선택사항들에 따라 달라질 수 있습니다. 라식 수술 후 2주가 지나자 시력은 70%에서 85%로 좋아졌습니다. 4주가 지났는데도 여전히 1.0%가 넘었습니다. 처음에는 시력이 일시적으로 흐려지고 밤에 시력이 나빠졌지만 3년 후에는 90% 이상이 좋아졌다. 전체 만족도 점수는 95점 이상이었다. 당신이 중요한 것에 따라 몇 가지 차이가 있습니다. 제가 깨달은 것은 우리가 과거에 가격에만 관심이 있었다면 우리의 삶의 질은 훨씬 더 중요하다는 것입니다.저는 매일 아침 시계를 확인하는 것이 얼마나 중요한지 알게 되었어요. 모든 사람들에게 완벽한 해결책은 아닐 수도 있지만, 저는 저에게 맞는 방법을 찾을 수 있다고 확신합니다. 저는 똑같은 문제를 다시 풀어도 괜찮다고 생각해요. ​ 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란? 스마일라식 다음날 달라진 차이란?
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
