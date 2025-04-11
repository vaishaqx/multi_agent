# agents/main_agent.py
from agents.main_agent import handle_query


def handle_query(user_input):
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

# Optional testing (for standalone run)
if __name__ == "__main__":
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']:
            break
        print("Bot:", handle_query(query))
