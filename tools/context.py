from utils.db import load_db, save_db

def set_trip_context(context):
    db = load_db()
    db["trip_context"] = context
    save_db(db)
    return "Contexte voyage mis à jour"


def get_trip_summary():
    db = load_db()
    return db.get("trip_context", {})


def reset_trip():
    db = load_db()
    db["trip_context"] = {}
    db["expenses"] = []
    db["lists"] = {}
    save_db(db)
    return "Voyage reset"
