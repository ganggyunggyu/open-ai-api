from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import re

from gpt_service import send_prompt_to_gpt
from claude_service import send_prompt_to_claude
from sola_service import send_prompt_to_solar
from utils import validate_api_key
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

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
    Generates text using the specified service (gpt, claude, or solar).
    """
    service = request.service.lower()
    keyword = request.keyword.strip()

    if service not in ['gpt', 'claude', 'solar']:
        raise HTTPException(status_code=400, detail="Invalid service. Choose 'gpt', 'claude', or 'solar'.")

    if not validate_api_key(service):
        raise HTTPException(status_code=401, detail=f"{service.upper()} API key is not configured.")

    if service == "gpt":
        response_text = send_prompt_to_gpt(keyword)
    elif service == "claude":
        response_text = send_prompt_to_claude(keyword)
    elif service == "solar":
        response_text = send_prompt_to_solar(keyword)
    else:
        # This case should not be reached due to the check above, but as a fallback:
        raise HTTPException(status_code=500, detail="Internal server error: service not handled.")

    clean_text = re.sub(r'\s+', '', response_text)
    
    return {
        "service": service,
        "keyword": keyword,
        "response": response_text,
        "char_count_excluding_spaces": len(clean_text)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
