import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")


def call_gemini(user_message, context=""):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"{context}\n\n{user_message}"}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    data = response.json()

    if "candidates" not in data:
        return f"Erreur Gemini: {data}"

    return data["candidates"][0]["content"]["parts"][0]["text"]
