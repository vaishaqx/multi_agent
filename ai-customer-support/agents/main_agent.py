from agents import billing_agent, tech_agent, general_agent

def handle_query(query):
    query = query.lower()

    # Greet back if user says hi/hello
    if any(greet in query for greet in ["hi", "hello", "hey", "hii", "hiii"]):
        return "Hello! How can I help you today?"

    # Billing queries
    if any(word in query for word in ["refund", "payment", "invoice"]):
        return billing_agent.respond(query)
    
    # Tech support queries
    elif any(word in query for word in ["error", "issue", "bug", "not working"]):
        return tech_agent.respond(query)
    
    # General info queries
    elif any(word in query for word in ["working hours", "location", "contact"]):
        return general_agent.respond(query)
    
    # Fallback
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
