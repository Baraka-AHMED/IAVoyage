from fastapi import FastAPI
from pydantic import BaseModel
from agent import call_gemini
import os


app = FastAPI()

# context
trip_context = {
    "destination": os.getenv("DESTINATION"),
    "hotel": os.getenv("HOTEL"),
    "dates": os.getenv("DATES"),
    "budget": int(os.getenv("BUDGET")),
    "preferences": os.getenv("PREFERENCES")
}


class Message(BaseModel):
    text: str


@app.post("/chat")
def chat(msg: Message):

    context = f"""
Destination: {trip_context['destination']}
Hotel: {trip_context['hotel']}
Dates: {trip_context['dates']}
Budget: {trip_context['budget']}
Préférences: {trip_context['preferences']}
"""

    response = call_gemini(msg.text, context)

    return {"response": response}
