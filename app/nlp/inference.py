import os
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'intent_model.joblib')
pipeline = joblib.load(MODEL_PATH)

def predict_intent(text: str) -> str:
    '''
    Get text and return predict intent
    '''

    if not text:
        return "empty_input"
    pred = pipeline.predict([text])[0]
    return pred