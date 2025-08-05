import re
from gpt_service import send_prompt_to_gpt
from claude_service import send_prompt_to_claude
from sola_service import send_prompt_to_solar
from utils import validate_api_key

def handle_response(service: str, keyword: str):
    print(f"\n{service.capitalize()}에게 요청 중...\n")
    
    if service == "gpt":
        response = send_prompt_to_gpt(keyword)
    elif service == "claude":
        response = send_prompt_to_claude(keyword)
    elif service == "solar":
        response = send_prompt_to_solar(keyword)
    
    print(f"📄 {service.capitalize()} 응답 결과:\n")
    print(response + "\n")
    
    clean_text = re.sub(r'\s+', '', response)
    print(f"공백 제거 후 글자 수: {len(clean_text)}")

def run_prompt_service():
    service_choice = input("사용할 서비스를 선택하세요 (gpt/claude/solar): ").strip().lower()
    keyword = input("사용할 키워드를 입력하세요: ").strip()

    if service_choice not in ['gpt', 'claude', 'solar']:
        print("잘못된 서비스 선택입니다. 'gpt', 'claude', 또는 'solar'를 입력해주세요.")
        return
    
    if validate_api_key(service_choice):
        handle_response(service_choice, keyword)

if __name__ == "__main__":
    run_prompt_service()