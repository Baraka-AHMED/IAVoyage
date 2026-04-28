from tools import budget, lists, travel, context


def dispatch(action):

    if not action:
        return None

    action_type = action["type"]
    args = action.get("args", [])

    # BUDGET
    if action_type == "ADD_EXPENSE":
        return add_expense(float(args[0]), args[1], args[2] if len(args) > 2 else "general")

    if action_type == "GET_TOTAL_EXPENSES":
        return get_total_expenses()

    if action_type == "GET_EXPENSES_BY_CATEGORY":
        return get_expenses_by_category(args[0])

    if action_type == "GET_REMAINING_BUDGET":
        return get_remaining_budget()

    if action_type == "SET_BUDGET":
        return set_budget(float(args[0]))

    if action_type == "DELETE_EXPENSE":
        return delete_expense(int(args[0]))

    # LISTES
    if action_type == "ADD_LIST_ITEM":
        return add_list_item(args[0], args[1])

    if action_type == "REMOVE_LIST_ITEM":
        return remove_list_item(args[0], args[1])

    if action_type == "CHECK_LIST_ITEM":
        return check_list_item(args[0], args[1])

    if action_type == "UNCHECK_LIST_ITEM":
        return uncheck_list_item(args[0], args[1])

    if action_type == "GET_LIST":
        return get_list(args[0])

    # TRAVEL
    if action_type == "FIND_RESTAURANTS_NEAR":
        return find_restaurants_near(args[0])

    if action_type == "FIND_TOURIST_ATTRACTIONS_NEAR":
        return find_tourist_attractions_near(args[0])

    if action_type == "SUGGEST_PLACES_TO_VISIT":
        return suggest_places_to_visit(args[0])

    if action_type == "SUGGEST_ACTIVITIES":
        return suggest_activities(args[0])

    # TRANSPORT
    if action_type == "GET_TRAVEL_TIME":
        return get_travel_time(args[0], args[1])

    if action_type == "GET_ROUTE":
        return get_route(args[0], args[1])

    if action_type == "OPTIMIZE_ROUTE":
        return optimize_route(args)

    # CONTEXT
    if action_type == "SET_TRIP_CONTEXT":
        return set_trip_context(args[0])

    if action_type == "GET_TRIP_SUMMARY":
        return get_trip_summary()

    if action_type == "RESET_TRIP":
        return reset_trip()

    return f"Action inconnue: {action_type}"

    # TIMELINE
    if action_type == "START_EVENT":
    return start_event(args[0], args[1] if len(args) > 1 else None)

    if action_type == "END_EVENT":
        return end_event()

    if action_type == "GET_TIMELINE":
        return get_timeline()


