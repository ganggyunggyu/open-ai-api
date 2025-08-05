from typing import Union
import os

def validate_api_key(service: str) -> Union[str, None]:
    env_key = {
        "gpt": "OPENAI_API_KEY",
        "claude": "ANTHROPIC_API_KEY"
    }.get(service)
    
    api_key = os.getenv(env_key)
    
    if not api_key or "YOUR_" in api_key:
        print(f"{service.upper()} API 키가 설정되어 있지 않습니다. .env 파일을 확인해주세요.")
        return None
    return api_key