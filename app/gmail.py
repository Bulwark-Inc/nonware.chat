import os
import base64
import requests

from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


GMAIL_SCOPE = "https://www.googleapis.com/auth/gmail.send"

REFRESH_TOKEN = os.environ["GMAIL_REFRESH_TOKEN"]
CLIENT_ID = os.environ["GMAIL_CLIENT_ID"]
CLIENT_SECRET = os.environ["GMAIL_CLIENT_SECRET"]
RECIPIENT_EMAIL = os.environ["RECIPIENT_EMAIL"]


def send_contact_email(
    name: str,
    email: str,
    phone: str | None,
    message: str,
):
    credentials = Credentials(
        token=None,
        refresh_token=REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=[GMAIL_SCOPE],
    )

    credentials.refresh(Request())

    email_message = EmailMessage()

    email_message["To"] = RECIPIENT_EMAIL
    email_message["Subject"] = f"New website enquiry from {name}"
    email_message["Reply-To"] = email

    email_message.set_content(
        f"""New contact form submission

Name: {name}
Email: {email}
Phone: {phone or "Not provided"}

Message:
{message}
"""
    )

    encoded_message = (
        base64.urlsafe_b64encode(email_message.as_bytes())
        .decode()
    )

    response = requests.post(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
        headers={
            "Authorization": f"Bearer {credentials.token}",
            "Content-Type": "application/json",
        },
        json={"raw": encoded_message},
        timeout=30,
    )

    response.raise_for_status()

    return {
        "success": True,
        "message": "Email sent successfully",
    }