from fastapi import FastAPI
import uvicorn
from app.api.chatbot import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chatbot API",
    description="API for dyplom work",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


@app.get("/")
def root():

    return{
        "message": "bot is running"
    }



if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)