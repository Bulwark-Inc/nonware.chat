from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatbotContext(BaseModel):
    site_name: str
    site_description: str
    assistant_purpose: str
    capabilities: list[str] = []


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    context: ChatbotContext