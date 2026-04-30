from utils.db import load_db, save_db

def add_expense(amount, category="general"):
    db = load_db()

    if "expenses" not in db:
        db["expenses"] = []

    db["expenses"].append({
        "amount": amount,
        "category": category
    })

    save_db(db)
    return f"Ajouté: {amount}€ ({category})"


def get_total_expenses():
    db = load_db()
    total = sum(e["amount"] for e in db.get("expenses", []))
    return f"Total dépenses: {total}€"


def get_remaining_budget():
    db = load_db()
    budget = db.get("budget", 0)
    total = sum(e["amount"] for e in db.get("expenses", []))
    return f"Reste: {budget - total}€"


def set_budget(amount):
    db = load_db()
    db["budget"] = amount
    save_db(db)
    return f"Budget fixé à {amount}€"


def delete_expense(index):
    db = load_db()
    if 0 <= index < len(db.get("expenses", [])):
        removed = db["expenses"].pop(index)
        save_db(db)
        return f"Supprimé: {removed}"
    return "Index invalide"
