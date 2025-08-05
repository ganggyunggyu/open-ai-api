from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    """
    A simple test endpoint.
    """
    return {"message": "Hello, this is a test endpoint."}

if __name__ == "__main__":
    # To run the server, execute `python main.py` in your terminal.
    # The server will be available at http://127.0.0.1:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
