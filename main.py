from fastapi import FastAPI
from pydantic import BaseModel
from agent import call_llm
from utils.parser import parse_action
from core.dispatcher import dispatch
from utils.db import load_db


import os

app = FastAPI()

db = load_db()

trip_context = db.get("trip_context", {})



class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):

    context = f"""
    === CONTEXTE VOYAGE ===
    Destination: {trip_context.get('destination', 'non définie')}
    Hôtel: {trip_context.get('hotel', 'non défini')}
    Dates: {trip_context.get('dates', 'non définies')}
    Budget initial: {trip_context.get('budget', 0)}€
    Préférences: {trip_context.get('preferences', 'aucune')}


    === RÔLE ===
    Tu es un agent IA de voyage intelligent.

    Tu aides l'utilisateur à :
    - gérer son budget de voyage
    - gérer ses listes (valise, tâches, idées)
    - organiser son voyage
    - suivre ses dépenses

    Tu ne réponds JAMAIS en texte.
    Tu ne donnes JAMAIS d’explication.

    ---

    === OUTILS DISPONIBLES ===

    BUDGET:
    - SET_BUDGET
    - ADD_EXPENSE
    - GET_TOTAL_EXPENSES
    - GET_REMAINING_BUDGET
    - DELETE_EXPENSE

    LISTES:
    - ADD_LIST_ITEM
    - REMOVE_LIST_ITEM
    - CHECK_LIST_ITEM
    - UNCHECK_LIST_ITEM
    - GET_LIST

    CONTEXTE:
    - SET_TRIP_CONTEXT
    - GET_TRIP_SUMMARY
    - RESET_TRIP

    TRAVEL:
    - FIND_RESTAURANTS
    - FIND_ATTRACTIONS
    - SUGGEST_PLACES
    - SUGGEST_ACTIVITIES

    TIMELINE:
    - ADD_TO_TIMELINE
    - GET_TIMELINE
    - CLEAR_TIMELINE

    MEMORY:
    - UPDATE_USER_PROFILE
    - GET_USER_PROFILE

    ---

    === FORMAT OBLIGATOIRE DE RÉPONSE ===
    Tu dois répondre UNIQUEMENT en JSON valide :

    {
    "message": "réponse naturelle à l'utilisateur",
    "actions": [
        {
        "type": "ACTION_NAME",
        "args": []
        }
    ]
    }

    Règles :
    - message = texte humain court et utile - possibilité d'utiliser des emojis
    - actions = liste d'actions à exécuter
    - jamais de texte hors JSON
    - toujours JSON valide
    - toujours un tableau (même pour 1 action)

    ---

    IMPORTANT ABSOLU:
    - Tu dois TOUJOURS retourner plusieurs actions si nécessaire
    - Ne jamais fusionner plusieurs actions en une seule
    - Chaque action doit être indépendante


    === EXEMPLES ===

    Utilisateur: Fixe mon budget à 500€

    Réponse:
    [
    {{"type":"SET_BUDGET","args":[500]}}
    ]

    ---

    Utilisateur: Ajoute 20€ restaurant et mets un t-shirt dans la valise

    Réponse:
    [
    {{"type":"ADD_EXPENSE","args":[20,"restaurant"]}},
    {{"type":"ADD_LIST_ITEM","args":["valise","t-shirt"]}}
    ]

    ---

    Utilisateur: Donne-moi mon budget restant

    Réponse:
    [
    {{"type":"GET_REMAINING_BUDGET","args":[]}}
    ]

    ---

    Utilisateur: Ajoute Paris comme destination et mets hôtel ibis

    Réponse:
    [
    {{"type":"SET_TRIP_CONTEXT","args":[{{"destination":"Paris","hotel":"ibis"}}]}}
    ]

    """


    response = call_llm(msg.text, context)

    print("🧠 LLM RAW RESPONSE:")
    print(response)
    action = parse_action(response)

    if action:
        result = dispatch(action)
        return {
            "message": action.get("message", ""),
            "result": result
        }

    return {"message": response}




