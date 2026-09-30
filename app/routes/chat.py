from fastapi import APIRouter

from app.gemini import generate_response
from app.models import ChatRequest


router = APIRouter()

MAX_MESSAGES = 10


@router.post("/chat")
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