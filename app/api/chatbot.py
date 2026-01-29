from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse

from app.nlp.inference import predict_intent


router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_message = request.message
    intent = predict_intent(user_message)
    return ChatResponse(intent=intent)
