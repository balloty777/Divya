# 🧠 MythoMax Chatbot

A chatbot powered by **MythoMax-L2-13B** running on **KoboldCPP**.  
Deployed with **FastAPI backend** + optional frontend.

---

## 🚀 Features
- Large Language Model inference with `MythoMax-L2-13B.Q5_K_S.gguf`
- FastAPI backend for chat requests
- Configurable generation parameters (temperature, top_p, etc.)
- Ready for GPU acceleration (tested on NVIDIA L4)
- Frontend integration (basic HTML/JS)

---

## 📂 Project Structure
├── ChatModels/ # Saved chat sessions
├── EmbeddedModels/ # Vector embeddings (if used)
├── front/ # Frontend files
├── LLMs/ # GGUF model storage
├── venv/ # Python virtual environment
├── chatbot.py # Main FastAPI server
├── messages.py # Message handling logic
├── requirements.txt # Python dependencies
├── .env # Environment variables
└── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Setup & Installation

1. **Clone this repo**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download KoboldCPP

bash
Copy
Edit
wget https://github.com/LostRuins/koboldcpp/releases/download/v1.61/koboldcpp-linux -O koboldcpp
chmod +x koboldcpp
Run KoboldCPP

bash
Copy
Edit
./koboldcpp --model ./LLMs/mythomax-l2-13b.Q5_K_S.gguf --threads 8 --smartcontext --port 5001
Run FastAPI backend

bash
Copy
Edit
uvicorn chatbot:app --host 0.0.0.0 --port 8000
📌 API Usage
POST request to /generate:

json
Copy
Edit
{
  "prompt": "Hello, how are you?",
  "max_length": 200,
  "temperature": 1.0
}
Response:

json
Copy
Edit
{
  "response": "I'm doing well, thank you!"
}
💻 Frontend
Open front/index.html in a browser to interact with the chatbot UI.

🛠️ Requirements
Python 3.9+

KoboldCPP

MythoMax-L2-13B GGUF model

FastAPI, Uvicorn
