from tools import budget, lists, context, travel
from core.validator import validate_action
from tools import memory

def dispatch(actions):
    if not actions:
        return None

    results = []

    for action in actions:

        if not isinstance(action, dict):
            continue

        is_valid, error = validate_action(action)

        if not is_valid:
            results.append(f"ERR {error}")
            continue

        action_type = action.get("type")
        args = action.get("args", [])

        # BUDGET
        if action_type == "SET_BUDGET":
            results.append(budget.set_budget(float(args[0])))

        elif action_type == "ADD_EXPENSE":
            results.append(
                budget.add_expense(
                    float(args[0]),
                    args[1] if len(args) > 1 else "general"
                )
            )

        elif action_type == "GET_TOTAL_EXPENSES":
            results.append(budget.get_total_expenses())

        elif action_type == "GET_REMAINING_BUDGET":
            results.append(budget.get_remaining_budget())

        elif action_type == "DELETE_EXPENSE":
            results.append(budget.delete_expense(int(args[0])))

        # LISTES
        elif action_type == "ADD_LIST_ITEM":
            results.append(lists.add_list_item(args[0], args[1]))

        elif action_type == "REMOVE_LIST_ITEM":
            results.append(lists.remove_list_item(args[0], args[1]))

        elif action_type == "CHECK_LIST_ITEM":
            results.append(lists.check_list_item(args[0], args[1]))

        elif action_type == "UNCHECK_LIST_ITEM":
            results.append(lists.uncheck_list_item(args[0], args[1]))

        elif action_type == "GET_LIST":
            results.append(lists.get_list(args[0]))

        # CONTEXT
        elif action_type == "SET_TRIP_CONTEXT":
            results.append(context.set_trip_context(args[0]))

        elif action_type == "GET_TRIP_SUMMARY":
            results.append(context.get_trip_summary())

        elif action_type == "RESET_TRIP":
            results.append(context.reset_trip())

        # TRAVEL

        elif action_type == "FIND_RESTAURANTS":
            results.append(travel.find_restaurants_near(args[0]))

        elif action_type == "FIND_ATTRACTIONS":
            results.append(travel.find_tourist_attractions_near(args[0]))

        elif action_type == "SUGGEST_PLACES":
            results.append(travel.suggest_places_to_visit(args[0]))

        elif action_type == "SUGGEST_ACTIVITIES":
            results.append(travel.suggest_activities(args[0]))

        elif action_type == "ADD_TO_TIMELINE":
            results.append(travel.add_to_timeline(args[0], args[1]))

        elif action_type == "GET_TIMELINE":
            results.append(travel.get_timeline())

        elif action_type == "CLEAR_TIMELINE":
            results.append(travel.clear_timeline())

        elif action_type == "UPDATE_USER_PROFILE":
            results.append(memory.update_user_profile(args[0]))

        elif action_type == "GET_USER_PROFILE":
            results.append(memory.get_user_profile())

        else:
            results.append(f"Action inconnue: {action_type}")

        print("ACTION EXEC:", action_type, args)


    return {
        "actions_result": results
    }

