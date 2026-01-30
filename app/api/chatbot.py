from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse

from app.nlp.inference import predict_intent
from app.services.responses import get_response



router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = predict_intent(request.message)
    response_text = get_response(result["intent"])
    return {
        **result,
        "response": response_text
    }