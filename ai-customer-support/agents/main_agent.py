from transformers import pipeline

# Load the NLP model once
nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def handle_query(user_input):
    intents = [
        "refund request",
        "payment issue",
        "technical issue",
        "greeting",
        "incomplete transaction"
    ]
    
    result = nlp(user_input, candidate_labels=intents)
    best_intent = result["labels"][0]

    if best_intent == "refund request":
        return "To request a refund, please submit a support ticket with your payment ID."
    elif best_intent in ["payment issue", "incomplete transaction"]:
        return "It seems like your payment was incomplete. Please verify the transaction or contact support."
    elif best_intent == "technical issue":
        return "I'm here to assist you with technical issues. Could you please describe the problem?"
    elif best_intent == "greeting":
        return "Hello! How can I assist you today?"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
