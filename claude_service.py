from config import anthropic_client
from prompts import getKoPrompt, ref

def send_prompt_to_claude(keyword):
    KO_PROMPT =  getKoPrompt(keyword)
    try:
        response = anthropic_client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=4096,
            temperature=0.7,
            system=KO_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"""
                 키워드: {keyword} 
                 ---
                 참고 문서: {ref}
                 **반드시 참고 문서의 어투 및 흐름을 참고하여 작업할 것**
                
"""                        }
                    ]
                }
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"An error occurred: {e}"
