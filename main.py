import os
import re
from gpt_service import send_prompt_to_gpt
from claude_service import send_prompt_to_claude

from dotenv import load_dotenv

load_dotenv()
if __name__ == "__main__":
    service_choice = input("사용할 서비스를 선택하세요 (gpt/claude): ").strip().lower()
    keyword = input("사용할 키워드를 입력하세요: ").strip()

    if service_choice == 'gpt':
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key or api_key == "YOUR_OPENAI_API_KEY":
            print("OpenAI API 키가 설정되어 있지 않습니다. .env 파일을 확인해주세요.")
        else:
            print("\nGPT에게 요청 중...\n")
            response = send_prompt_to_gpt(keyword)
            print("GPT 응답 결과:\n")
            print(f'{response}\n')
            clean_text = re.sub(r'\s+', '', response)
            print(f'공백제거 후 글자 수: {len(clean_text)}')

    elif service_choice == 'claude':
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key or api_key == "YOUR_ANTHROPIC_API_KEY":
            print("Anthropic API 키가 설정되어 있지 않습니다. .env 파일을 확인해주세요.")
        else:
            print("\nClaude에게 요청 중...\n")
            response = send_prompt_to_claude(keyword)
            print("📄 Claude 응답 결과:\n")
            print(f'{response}\n')
            clean_text = re.sub(r'\s+', '', response)
            print(f'공백제거 후 글자 수: {len(clean_text)}')
    else:
        print("잘못된 서비스 선택입니다. 'gpt' 또는 'claude'를 입력해주세요.")