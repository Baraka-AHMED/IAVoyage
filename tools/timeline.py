from utils.db import load_db, save_db

def add_to_timeline(day, activity):
    db = load_db()

    if "timeline" not in db:
        db["timeline"] = {}

    if day not in db["timeline"]:
        db["timeline"][day] = []

    db["timeline"][day].append(activity)
    save_db(db)

    return f"📅 Ajouté {activity} au jour {day}"


def get_timeline():
    db = load_db()
    return db.get("timeline", {})


def clear_timeline():
    db = load_db()
    db["timeline"] = {}
    save_db(db)
    return "🧹 Timeline reset"
