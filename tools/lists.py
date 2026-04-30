from utils.db import load_db, save_db

def add_list_item(list_name, item):
    db = load_db()

    if "lists" not in db:
        db["lists"] = {}

    if list_name not in db["lists"]:
        db["lists"][list_name] = []

    # ANTI-DOUBLON
    existing_items = [i["name"] for i in db["lists"][list_name]]

    if item in existing_items:
        return f"⚠️ Déjà présent: {item} dans {list_name}"

    db["lists"][list_name].append({
        "name": item,
        "checked": False
    })

    save_db(db)
    return f"Ajouté {item} dans {list_name}"


def remove_list_item(list_name, item):
    db = load_db()
    items = db.get("lists", {}).get(list_name, [])

    db["lists"][list_name] = [
        i for i in items if i["name"] != item
    ]

    save_db(db)
    return f"Supprimé {item}"


def check_list_item(list_name, item):
    db = load_db()

    for i in db.get("lists", {}).get(list_name, []):
        if i["name"] == item:
            i["checked"] = True

    save_db(db)
    return f"Check: {item}"


def uncheck_list_item(list_name, item):
    db = load_db()

    for i in db.get("lists", {}).get(list_name, []):
        if i["name"] == item:
            i["checked"] = False

    save_db(db)
    return f"Uncheck: {item}"


def get_list(list_name):
    db = load_db()
    return db.get("lists", {}).get(list_name, [])
