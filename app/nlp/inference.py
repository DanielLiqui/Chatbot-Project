import os
import joblib
from typing import Dict

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'intent_model.joblib')
pipeline = joblib.load(MODEL_PATH)

CONFIDENCE_THRESHOLD = 0.5


def predict_intent(text: str) -> Dict[str, float | str]:
    '''
    Get text and return predict intent
    '''
    probabilities = pipeline.predict_proba([text])[0]
    max_proba = max(probabilities)
    intent_index = probabilities.argmax()
    intent = pipeline.classes_[intent_index]

    if not text:
        return "empty_input"
    if max_proba < CONFIDENCE_THRESHOLD:
        return {
            "intent": "unknown",
            "confidence": float(max_proba)
        }   

    return {
        "intent": intent,
        "confidence": float(max_proba)
    }
