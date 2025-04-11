def handle_query(user_input):
    user_input = user_input.lower()

    # Greetings and small talk
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you! 😊"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Let me know if you need anything else."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day 😊"

    # Existing query logic
    if "refund" in user_input:
        return "To process a refund, please provide your order ID and reason for the refund."
    elif "status" in user_input or "track" in user_input:
        return "You can track your order using the tracking link sent to your email."
    elif "cancel" in user_input:
        return "Your order can be cancelled within 24 hours of placement. Please confirm your order ID."
    elif "help" in user_input or "assist" in user_input:
        return "Sure! I'm here to help. Please tell me what you need assistance with."
    else:
        return "I'm sorry, I couldn't understand your request. Could you please rephrase it?"
