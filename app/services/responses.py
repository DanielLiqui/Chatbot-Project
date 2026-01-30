from typing import Dict

RESPONSES: Dict[str, str] = {
    "track_order": "Please provide your order ID so I can track your order.",
    "change_order": "Sure. What would you like to change in your order?",
    "cancel_order": "I can help with that. Please confirm your order number.",
    "recover_password": "You can reset your password using the 'Forgot password' option.",
    "newsletter_subscription": "You have been successfully subscribed to our newsletter.",
    "payment_issue": "I'm sorry to hear that. Could you describe the payment issue?",
    "contact_customer_service": "I will connect you with customer support.",
    "unknown": "I'm not sure I understood you. Could you please rephrase?"
}


def get_response(intent: str) -> str:
    """
    Return text answer by intent
    """
    return RESPONSES.get(intent, RESPONSES["unknown"])
