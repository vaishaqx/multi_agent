def respond(query):
    query = query.lower()
    if "refund" in query:
        return "To request a refund, please submit a support ticket with your payment ID."
    elif "invoice" in query:
        return "You can download your invoice from your account billing section."
    elif "payment" in query:
        return "Please ensure your payment method is updated in your profile settings."
    else:
        return "Sure, I can help with billing-related issues like refunds, payments, or invoices."
