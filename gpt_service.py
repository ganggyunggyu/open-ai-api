from config import openai_client
from prompts import getKoPrompt, ref

def send_prompt_to_gpt(keyword):
    KO_PROMPT = getKoPrompt(keyword)
    
    try:
        response = openai_client.chat.completions.create(
            model='gpt-4.1-2025-04-14',
            messages=[
                {"role": "system", "content": KO_PROMPT},
                {"role": "user", "content": f"""
                 
                 3000단어 이상 필수
                 ---
                 키워드: {keyword} 
                 ---
                 참고 문서: {ref}
"""}
            ],
            temperature=0.0,
            top_p=1.0,
            presence_penalty=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"
