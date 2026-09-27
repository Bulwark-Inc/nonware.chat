from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.gemini import generate_response
from app.models import ChatRequest


app = FastAPI(
    title="Nonware Chatbot API",
    version="1.0.0",
)

MAX_MESSAGES = 10


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    if len(request.messages) > MAX_MESSAGES:
        return {
            "error": "Demo conversation limit reached"
        }

    response = generate_response(
        messages=request.messages,
        context=request.context,
    )

    return {
        "response": response
    }