# Chatbot Project
FastAPI · NLP · React (Vite)

---

## 🚀 Tech Stack

### Backend
- Python 3.10+
- FastAPI
- scikit-learn

### Frontend
- React
- Vite
- Fetch API

---

## 📁 Project Structure

chatbot/
├── app/                  # Backend (FastAPI)
│   ├── api/              # API routes
│   ├── nlp/              # NLP model & inference
│   ├── services/         # Business logic (responses)
│   ├── schemas/          # Pydantic schemas
│   └── main.py           # FastAPI entry point
│
├── data/                 # Training datasets
│
├── frontend/             # React frontend (Vite)
│
├── requirements.txt
└── README.md

---

## Installation

### Download repozitory

First, download the project from GitHub:

git clone https://github.com/DanielLiqui/Chatbot-Project.git


## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create virtual environment

From project root:

python -m venv venv

Activate it:

Linux / macOS  
source venv/bin/activate

Windows  
venv\Scripts\activate

---

### 2️⃣ Install dependencies

pip install -r requirements.txt

---

### 3️⃣ Run backend server

uvicorn app.main:app --reload

Backend will be available at:
- API → http://127.0.0.1:8000
- Swagger → http://127.0.0.1:8000/docs

---

## 💬 Frontend Setup (React + Vite)

### 1️⃣ Go to frontend directory

cd frontend

---

### 2️⃣ Install frontend dependencies

npm install

---

### 3️⃣ Run frontend dev server

npm run dev

Frontend will be available at:
- http://localhost:5173

⚠️ Backend must be running for the chat to work

---

## 🔁 Local Development Flow

Terminal 1:
uvicorn app.main:app --reload

Terminal 2:
cd frontend  
npm run dev

Open browser:
http://localhost:5173

---

## 🧠 NLP Inference Flow

1. User sends message from frontend
2. /chat endpoint receives request
3. NLP model predicts intent and confidence
4. Response is selected from dictionary based on intent
5. Backend returns structured response to frontend

---

## 📡 API Example

POST /chat

Request:
{
  "message": "Where is my order?"
}

Response:
{
  "intent": "track_order",
  "confidence": 0.52,
  "response": "You can track your order using the tracking link."
}

---

## 🧪 Notes for Developers

- NLP model is loaded once at startup
- Responses are rule-based (dictionary-driven)
- Model training is decoupled from inference
- Frontend uses native fetch API

---

## 🚧 Roadmap

- Confidence-based fallback
- Clarification questions
- Multi-language support
- Generative response model
- Docker & docker-compose setup

---

## 🧩 Known Limitations

- No authentication
- No persistent chat history
- Open CORS (development only)
