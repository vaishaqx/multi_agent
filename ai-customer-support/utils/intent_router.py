print("intent_router loaded")
def route_query(user_input):
    user_input = user_input.lower()

    if "refund" in user_input or "payment" in user_input or "invoice" in user_input:
        return "billing"
    elif "login" in user_input or "error" in user_input or "crash" in user_input:
        return "tech"
    elif "hours" in user_input or "location" in user_input or "contact" in user_input:
        return "general"
    else:
        return "general"