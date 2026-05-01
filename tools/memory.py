from utils.db import load_db, save_db

def update_user_profile(data: dict):
    db = load_db()

    if "user_profile" not in db:
        db["user_profile"] = {}

    for key, value in data.items():
        if isinstance(value, list):
            existing = db["user_profile"].get(key, [])
            db["user_profile"][key] = list(set(existing + value))
        else:
            db["user_profile"][key] = value

    save_db(db)

    return "Profil utilisateur mis à jour"


def get_user_profile():
    db = load_db()
    return db.get("user_profile", {})
