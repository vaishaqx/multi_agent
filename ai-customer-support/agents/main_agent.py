# agents/main_agent.py

def get_agent_response(user_input):
    # Simple rule-based logic for demo
    user_input = user_input.lower()

    if "refund" in user_input:
        return "To process a refund, please provide your order ID and reason for the refund."
    elif "order status" in user_input or "track order" in user_input:
        return "You can track your order using the tracking link sent to your email."
    elif "cancel order" in user_input:
        return "Your order can be cancelled within 24 hours of placement. Please confirm your order ID."
    elif "help" in user_input:
        return "Sure! I'm here to help. Please tell me what you need assistance with."
    else:
        return "I'm sorry, I couldn't understand your request. Could you please rephrase it?"

# Example usage (for testing only)
if name == "main":
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']:
            break
        print("Bot:", get_agent_response(query))