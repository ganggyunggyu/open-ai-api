import os
from openai import OpenAI
import anthropic
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
upstage_api_key = os.getenv("UPSTAGE_API_KEY")

if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY가 설정되어 있지 않습니다.")

if not anthropic_api_key:
    raise RuntimeError("ANTHROPIC_API_KEY가 설정되어 있지 않습니다.")

if not upstage_api_key:
    raise RuntimeError("UPSTAGE_API_KEY가 설정되어 있지 않습니다.")

openai_client = OpenAI(api_key=openai_api_key)
anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)
solar_client = OpenAI(
    api_key=upstage_api_key,
    base_url="https://api.upstage.ai/v1/solar",
    default_headers={
        "Authorization": f"Bearer {upstage_api_key}"
    }
)