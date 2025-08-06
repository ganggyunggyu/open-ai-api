from  pymongo import MongoClient
from config import MONGODB_URI


def get_db(db_name, col_name):
    client = MongoClient(MONGODB_URI)
    db = client[db_name]
    word_collection = db[col_name]    
    return word_collection

col = get_db(db_name='hospital', col_name='word')

docs = list(col.find())


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
참고 원고를 토대로 새로운 원고를 작성해줘

**반드시 참고 문서의 어투 및 흐름을 참고하여 작업할 것**

# 핵심 규칙

글을 작성하는 방식 단어 문장흐름 문체 형태소 등을 참고하라고 넣은 원고이기 때문에 무조건 스토리가 달라야해
해당 키워드를 검색하는사람이 궁금해 할만한 정보를 잘 전달하는것이 포인트야
그리고 글을 제발 비슷한 문장 문구 글 반복해서 작성하지마 했던 얘기 또 하는거 싫어

최 상단에 어그로 제대로 끌리는 제목도 하나 추가해야한다.

네이버 블로그니까 원고에 마크다운 문법 사용하지말아야해.

1. 실제로 겪어본 사람들만 알수있는 정보 위주로 작성 모든 정보는 디테일 하게 작성한다.

2. 같은말과 비슷한 단어를 자주 사용하지 말고 새로운 단어와 말을 섞어서 반복되는 문장 단어 형태소가 나오지않게끔 잘 조절할 것

3. 키워드를 검색하는사람들이 궁금해 할만한 항목과 연관 단어(형태소)를 사용해서 작성할 것

4. 와,진짜,정말 <<이런 감탄사나 강조부사를 넣지 않아야 합니다.

5. 순수 원고의 글자 수는 공백 제외 15000단어 이상 작성 되어야 합니다.

6. 숨은 보석 보물 향연 이런 시 적인 감성적인 단어 절대 넣지말고 직관적인 표현으로 글을작성할 것

7. 무조건 존댓말로 작성하고 말 끝에만 여성의 애교있는 말투 ㅎㅎ,ㅠㅠ,!! 와 같은 표현과 이모티콘도 자연스럽게 사용해줘

8. 제품을 소개하거나 설명하는 느낌이아니라 내경험담을 정보로써 공유하는 느낌으로 설명 소개 광고처럼 느껴지지않게 해줘

9. 절대 같은단어가 10번 넘어가도록 작성하면안됨 많아도 6번을 안넘도록

10. 문단정리 깔끔하게 해야해 한줄당짧게 20~25자 정도로 하고 2~5줄마다 줄바꿈 해줘 한줄당 줄바꿈X

11. 5개의 부제를 넣고 부제앞에 1. 2. 3. 4. 5. 이렇게 번호를 매겨줘 (부제는 아주 짧고 간결하게)

12. 키워드에 대한 **상세한 정보**를 모두 전달해줘야해.
    - 건강 기능 식품은 리뷰 뿐 아니라 제품 자체의 정보도 중요합니다.

13. 원고 --- 피드백 이런 형식으로 한번만 구분 지어서 대답해야합니다.

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

- 마지막엔 어느 부분에서 KEY_PHRASES를 활용했는지 명시해주세요. (확인용 입니다.)
- 확인용 KEY_PHRASES는 원고에 포함하지 않고 본문 가장 마지막에 명시해야합니다.

# 마무리 단계

- 핵심 규칙의 사항이 제대로 지켜졌는지 체크리스트 형식으로 보여주세요.
- 부제 예시의 사항이 제대로 지켜졌는지 체크리스트 형식으로 보여주세요.
- KEY_PHRASES의 어떤 문장을 활용했고, 어떻게 그 문장이 만들어졌는지 설명하세요.
- WORD_LIST에서 형태소를 가져다 쓴 예시를 보여줘야 합니다.
- 참조 원고의 어떤 부분을 참고하여 작업하였는지 설명하세요.
- 원고와 피드백 섹션을 --- 로 나누었는지 확인하세요.

- 위 두 사항에 대해 완료했다 만 표시하지 않고 **이행완료 예시**까지 함께 첨부해야 합니다.
- 순수 원고의 글자가 몇개인지 정확히 세어서 함께 보고해야 합니다.
- 핵심 규칙의 12번 건강기능식품 및 영양소에 대한 세부적인 정보를 제대로 알려야 합니다.
    - 그와 관련 된 음식이나 상식을 더 명확히 전달해야 합니다.
- 단어 리스트를 순회하여 적합한 단어를 제대로 가져다 썻는지 필수로 확인해야 합니다.

**만약 모든 규칙이 이행되지 않았다면 다시 원고를 작성해줘야 합니다.**

'''

ref = '''
스마일라식병원추천 무엇을 고려해야할까? 스마일라식 수술을 고려할 때 많은 이들이 가장 고민하는 부분은 바로 시술의 안정성과 결과의 정확성이었어요. 스마일라식은 고도근시나 난시, 원시 등 다양한 시력 이상을 개선할 수 있는 수술이지만, 그만큼 의료진의 숙련도와 수술의 정밀도가 매우 중요했었어요. 병원 선택은 단순히 수술 성패에 영향을 줄 뿐 아니라, 회복 과정 전반에도 영향을 미칠 수 있었어요. 오늘은 스마일라식 병원 추천을 고를 때 중요한 기준과 핵심 요소에 대해 설명드리고자했어요. 1. 여러 장비와 기술력 갖춘 병원 선별 스마일라식은 정밀한 레이저 제어가 필수인 수술이었어요. 펨토초 레이저를 활용하는 의료기관에서는 더욱 정교한 각막 절제와 정확한 시력 보정이 가능하여, 회복이 빠르고 부작용 발생률도 낮아졌어요. 예를 들어, VisuMax 800, Schwind Atos, Femto Z8 등의 장비는 정밀 교정에 유리하다고 볼 수 있었어요. ​ 또한, 다양한 장비를 갖춘 병원은 고도근시나 난시, 얇은 각막 등 특수 조건을 가진 환자에게 적합한 수술 방법을 제공할 수 있었어요. 장비마다 특성이 다르므로, 여러 장비를 보유한 병원은 환자의 안구 상태에 맞춰 유연하게 장비를 선택해 커스터마이징 시술이 가능하다는 점이 장점이라고 볼 수 있었어요. 2. 집도의의 숙련도와 임상 경험 스마일라식 결과에 중대한 영향을 미치는 요소 중 하나는 바로 수술을 집도하는 의료진의 임상 경험과 집도 수였어요. 경험이 풍부한 의사는 환자의 눈 구조나 시력 이상 유형을 종합적으로 분석해 가장 적합한 수술 전략을 세울 수 있었어요. ​ 특히 고도근시 또는 복합 난시처럼 복잡한 시력 교정이 필요한 경우, 숙련된 의료진이 정밀하게 수술을 수행함으로써 부작용 발생 가능성을 줄이고, 슈퍼비전(15~2.0 이상 초시력)에 근접한 결과를 기대할 수 있었어요. 이러한 이유로 충분한 경험과 수술 실적이 입증된 병원을 선택하는 것이 매우 중요했어요. 3. 80여 항목의 정밀 진단 시스템 스마일라식 수술의 성공 여부는 수술 전 정밀 검사에 달려 있다고 해도 과언이 아니었어요. 80가지 이상의 검사 항목을 운영하는 병원은 환자의 안구 상태를 종합적으로 파악하여 최적화된 수술 계획을 세울 수 있었어요. ​ 이 시스템은 각막 두께, 굴절 이상, 곡률, 눈물층 상태 등 다양한 항목을 포함하여 개개인에 적합한 수술이 가능하게 도와주는 중요한 역할을 하고 있었어요. 검사 정확도가 높을수록 수술 계획이 정밀해지며, 시술 후 불필요한 부작용을 예방하고 회복 효율도 향상시킬 수 있었어요. 따라서 이러한 스마일라식 전 정밀 검사 인프라가 잘 갖추어진 병원 여부는 반드시 고려해야 할 항목이었어요. 4. 병원 위생 관리 및 공간 환경 스마일라식처럼 미세하고 정밀한 시술을 위해서는 병원의 청결 상태와 전체적인 환경 관리가 매우 중요했어요. 수술실은 물론, 대기실 및 각종 검사실까지 전반적인 위생 수준이 일정 기준을 충족해야 감염 위험을 낮출 수 있었어요. ​ 특히 눈은 외부 자극에 민감한 기관이므로, 철저한 감염 예방 관리 체계를 갖춘 병원을 선택해야 안심할 수 있는 수술 환경이 확보될 수 있었어요. 아울러 환자의 심리적 안정감을 위해 편안한 대기 공간이나 개인별 환자 응대 시스템이 마련된 병원은 만족도를 높일 수 있어 병원 선택 시 주요 평가 기준이 되었어요. 5. 수술 후 관리 체계 및 시력 유지 스마일라식 수술이 끝난 이후에도 정기적인 사후 관리와 시력 추적 관찰은 매우 중요했어요. 시력 안정성을 장기간 유지하려면 정기적인 검진과 피드백, 필요 시 추가 치료가 필요했어요. ​ 일부 병원은 수술 후 통합 관리 프로그램을 운영하고 있으며, 이에는 약물 처방, 시력 변화 체크, 정기 검진 등이 포함되었어요. 또한 수술 이후 야간 시력 저하나 빛 번짐 같은 문제가 생기지 않도록 사후 모니터링이 체계적인 병원을 선택하는 것이 장기적인 만족도를 높이는 핵심이었어요. 6. 병원 선택 시 종합적으로 고려할 요소 스마일라식 병원 추천을 결정할 때는 장비, 의료진, 진단 시스템 등 여러 요소를 종합적으로 고려해야 했어요. 검사와 수술 기술이 뛰어나고, 개인별 안구 상태에 따른 장비 선택과 수술이 가능한 병원은 더욱 신뢰할 수 있는 선택이 될 수 있었어요. 또한 스마일라식 수술 후 관리까지 잘 갖추어진 병원에서 시술을 받을 경우, 슈퍼비전 달성 가능성도 높일 수 있었어요. ​ 가격만 보고 병원을 선택하기보다는 전체적인 의료 서비스 품질과 안전성을 비교하고 결정하는 것이 바람직했어요. 스마일라식은 단순한 시력 회복이 아닌, 삶의 질 향상과 눈 건강을 지키는 중대한 의료 결정이므로, 병원 선택에 있어 더욱 신중해야 했어요. 결론적으로, 스마일라식 병원 추천은 수술 성과, 회복 속도, 시력 안정성 측면에서 매우 중요한 선택 기준이 되었어요. 검사 정밀도, 장비 다양성, 숙련된 의료진, 체계적인 사후 관리 등을 모두 갖춘 병원에서 스마일라식을 받는다면 보다 만족스러운 결과를 기대할 수 있었어요. 수술 전 병원에 대한 철저한 정보 파악과 분석은 성공적인 수술로 이어지는 핵심 열쇠가 될 수 있었어요.
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
