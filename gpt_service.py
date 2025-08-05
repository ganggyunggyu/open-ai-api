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
                 키워드: {keyword} 
                 ---
                 참고 문서: {ref}
"""}
            ],
            temperature=0.7,
            top_p=0.95
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"
