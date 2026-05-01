def is_number(value):
    try:
        float(value)
        return True
    except:
        return False


def validate_action(action):
    if not isinstance(action, dict):
        return False, "Format invalide"

    action_type = action.get("type")
    args = action.get("args", [])

    if not action_type:
        return False, "Action sans type"

    # CONFIG CENTRALISÉE
    rules = {
        # BUDGET
        "SET_BUDGET": lambda a: len(a) == 1 and is_number(a[0]),
        "ADD_EXPENSE": lambda a: len(a) >= 1 and is_number(a[0]),
        "DELETE_EXPENSE": lambda a: len(a) == 1 and isinstance(a[0], int),
        "GET_TOTAL_EXPENSES": lambda a: True,
        "GET_REMAINING_BUDGET": lambda a: True,

        # LISTES
        "ADD_LIST_ITEM": lambda a: len(a) == 2,
        "REMOVE_LIST_ITEM": lambda a: len(a) == 2,
        "CHECK_LIST_ITEM": lambda a: len(a) == 2,
        "UNCHECK_LIST_ITEM": lambda a: len(a) == 2,
        "GET_LIST": lambda a: len(a) == 1,

        # CONTEXT
        "SET_TRIP_CONTEXT": lambda a: len(a) == 1 and isinstance(a[0], dict),
        "GET_TRIP_SUMMARY": lambda a: True,
        "RESET_TRIP": lambda a: True,

        # TIMELINE
        "ADD_TO_TIMELINE": lambda a: len(a) == 2,
        "GET_TIMELINE": lambda a: True,
        "CLEAR_TIMELINE": lambda a: True,

        # TRAVEL
        "FIND_RESTAURANTS": lambda a: len(a) == 1,
        "FIND_ATTRACTIONS": lambda a: len(a) == 1,
        "SUGGEST_PLACES": lambda a: len(a) == 1,
        "SUGGEST_ACTIVITIES": lambda a: len(a) == 1,

        # MEMORY
        "UPDATE_USER_PROFILE": lambda a: len(a) == 1 and isinstance(a[0], dict),
        "GET_USER_PROFILE": lambda a: True,
    }

    if action_type not in rules:
        return False, f"Action inconnue: {action_type}"

    if not rules[action_type](args):
        return False, f"Arguments invalides pour {action_type}"

    return True, None
