

import streamlit.components.v1 as components
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

if __name__ == "__main__":
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post("/chat")
    async def chat_api(payload: dict):
        user_input = payload.get("message", "")
        chat_history = payload.get("history", [SYSTEM_PROMPT])

        chat_history.append(f"You: {user_input}")
        context = "\n".join(chat_history)
        full_prompt = context + "\nDivya:"

        kobold_payload = {
            "prompt": full_prompt,
            "use_story": False,
            "use_memory": False,
            "max_context_length": 2048,
            "max_length": 80,
            "temperature": 1.5,
            "top_p": 0.95,
            "stop_sequence": ["You:", "\nYou:"]
        }

        try:
            response = requests.post(KOBOLD_API_URL, json=kobold_payload, timeout=60)
            data = response.json()
            result = data["choices"][0]["text"].strip()
            chat_history.append(f"Divya: {result}")
            return {"reply": result, "history": chat_history}
        except Exception as e:
            return {"reply": f"⚠️ Failed to get response: {e}", "history": chat_history}

    uvicorn.run(app, host="0.0.0.0", port=8000)
