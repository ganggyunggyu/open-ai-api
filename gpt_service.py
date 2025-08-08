
from  pymongo import MongoClient
from config import MONGODB_URI
from config import openai_client
from prompts import getKoPrompt, ref
def get_db(db_name, col_name):
    client = MongoClient(MONGODB_URI)
    db = client[db_name]
    word_collection = db[col_name]    
    return word_collection

col = get_db(db_name='hospital', col_name='word')

docs = list(col.find())
def send_prompt_to_gpt(keyword):
    KO_PROMPT = getKoPrompt(keyword)
    
    try:
        response = openai_client.chat.completions.create(
            model='gpt-4.1-2025-04-14',
            messages=[
                {"role": "system", "content": ' You are a professional blog post writer. Your task is to generate a blog post based on provided analysis data and user instructions.'},
                {"role": "user", "content": f"""
                [사용자 요구사항]
                 
                {KO_PROMPT}
                
                [키워드] [참고 문서] [추가 요청사항]

                {keyword}

                {ref}                

                [참고 단어]
                {col}
"""}
            ],
            temperature=0.0,
            top_p=1.0,
            presence_penalty=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"
