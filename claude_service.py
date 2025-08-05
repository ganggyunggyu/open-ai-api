from config import anthropic_client
from prompts import KO_PROMPT, ref

def send_prompt_to_claude(keyword):
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
"""                        }
                    ]
                }
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"An error occurred: {e}"
