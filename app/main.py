from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.routes.chat import router as chat_router
from app.routes.contact import router as contact_router


app = FastAPI(
    title="Nonware Chatbot API",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(chat_router)
app.include_router(contact_router)