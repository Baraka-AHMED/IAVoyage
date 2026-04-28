from fastapi import FastAPI
from pydantic import BaseModel
from core.dispatcher import dispatch
from agent import call_gemini, parse_action
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

Tu es un agent IA de voyage.

Si tu dois agir, réponds uniquement sous ce format :
ACTION: TYPE | arg1 | arg2 | arg3
"""
    response = call_gemini(msg.text, context)

    action = parse_action(response)

    if action:
        result = dispatch(action)
        return {"response": result}

    return {"response": response}
