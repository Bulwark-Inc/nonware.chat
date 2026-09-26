import os

from google import genai
from google.genai.types import HttpOptions


client = genai.Client(
    vertexai=True,
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ["GOOGLE_CLOUD_LOCATION"],
    http_options=HttpOptions(api_version="v1"),
)


def generate_response(message: str) -> str:
    response = client.models.generate_content(
        model=os.environ["GEMINI_MODEL"],
        contents=message,
    )

    return response.text