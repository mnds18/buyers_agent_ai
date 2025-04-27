# agents/feedback_agent.py

def collect_feedback(deals):
    feedback = {deal["property"]: "Positive" for deal in deals}
    return feedback
