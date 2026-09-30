from fastapi import APIRouter

from app.gmail import send_contact_email
from app.models import ContactRequest


router = APIRouter()


@router.post("/api/contact")
def send_contact(request: ContactRequest):
    return send_contact_email(
        name=request.name,
        email=request.email,
        phone=request.phone,
        message=request.message,
    )