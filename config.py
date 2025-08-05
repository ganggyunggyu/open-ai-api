import os
from openai import OpenAI
import anthropic
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY가 설정되어 있지 않습니다.")

if not anthropic_api_key:
    raise RuntimeError("ANTHROPIC_API_KEY가 설정되어 있지 않습니다.")

openai_client = OpenAI(api_key=openai_api_key)
anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)
