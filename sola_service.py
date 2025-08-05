from config import solar_client
from prompts import getKoPrompt, ref

def send_prompt_to_solar(keyword: str) -> str:
    KO_PROMPT =  getKoPrompt(keyword)
    try:
        # prompt_ref = ref if len(ref) <= 3000 else ref[:3000] + "\n…(생략됨)"
        
        messages = [
            {"role": "user", "content": f"{KO_PROMPT}\n\n키워드: {keyword}\n---\n참고 문서: {ref}"}
        ]

        response = solar_client.chat.completions.create(
            model="solar-pro2",
            messages=messages,
            # max_tokens=4096,
            temperature=0.7,
            top_p=0.95
        )

        choices = getattr(response, "choices", [])
        if choices and hasattr(choices[0], "message"):
            return choices[0].message.content or ""
        return "응답이 없습니다."
    except Exception as e:
        return f"Error: {e}"