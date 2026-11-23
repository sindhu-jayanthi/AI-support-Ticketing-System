import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")
client = genai.Client(api_key=GEMINI_API_KEY)

async def classify_ticket(description: str):

    prompt = f"""
    You are a support ticket classification assistant.

    Classify the following ticket into exactly one of these categories:
    - Payment Issue
    - Technical Issue
    - Account Access
    - General Inquiry

    Ticket Description: {description}

    Return only the category name. Do not provide explanations.
    """

    response = await client.aio.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    if not response.text:
        raise ValueError("Gemini returned an empty response")

    return response.text.strip()

async def analyze_sentiment(description: str):

    prompt = f"""
    Analyze the sentiment of the following customer support ticket.

    Classify it into exactly one of these categories:
    - Positive
    - Negative
    - Neutral

    Ticket Description: {description}

    Return only the sentiment category.
    """

    response = await client.aio.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response")

    return response.text.strip()
