def respond(query):
    query = query.lower()
    if "working hours" in query:
        return "Our working hours are from 9 AM to 6 PM, Monday to Friday."
    elif "location" in query:
        return "We are located at 123 AI Street, Technoville."
    elif "contact" in query:
        return "You can contact us at support@example.com."
    else:
        return "I'm not sure, but I can help with general information like working hours, location, or contact details."
