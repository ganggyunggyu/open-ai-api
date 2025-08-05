from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import re

from gpt_service import send_prompt_to_gpt
from claude_service import send_prompt_to_claude
from utils import validate_api_key

app = FastAPI()

class GenerationRequest(BaseModel):
    service: str
    keyword: str

@app.get("/")
def read_root():
    """
    A simple test endpoint.
    """
    return {"message": "Hello, this is a test endpoint."}

@app.post("/generate")
def generate_text(request: GenerationRequest):
    """
    Generates text using the specified service (gpt or claude).
    """
    service = request.service.lower()
    keyword = request.keyword.strip()

    if service not in ['gpt', 'claude']:
        raise HTTPException(status_code=400, detail="Invalid service. Choose 'gpt' or 'claude'.")

    if not validate_api_key(service):
        raise HTTPException(status_code=401, detail=f"{service.upper()} API key is not configured.")

    if service == "gpt":
        response_text = send_prompt_to_gpt(keyword)
    if service == 'claude':
        response_text = send_prompt_to_claude(keyword)
    else:
        response_text = send_prompt_to_gpt(keyword)

    clean_text = re.sub(r'\s+', '', response_text)
    
    return {
        "service": service,
        "keyword": keyword,
        "response": clean_text,
        "char_count_excluding_spaces": len(clean_text)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)