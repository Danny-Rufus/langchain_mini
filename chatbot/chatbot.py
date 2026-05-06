from typing import List, Dict
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ChatBot:
    def __init__(self, model: str = "gpt-5.2"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.use_openai = bool(self.api_key)
        self.client = OpenAI(api_key=self.api_key) if self.use_openai else None

        # maintain simple chat history for context
        self.history: List[Dict[str, str]] = []

    def send_message(self, message: str) -> str:
        self.history.append({"role": "user", "content": message})

        if not self.use_openai:
            # simple fallback if no API key provided
            reply = f"(local fallback) I received: {message}"
            self.history.append({"role": "assistant", "content": reply})
            return reply

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                max_completion_tokens=512,
                temperature=0.2,
            )
            assistant_msg = (resp.choices[0].message.content or "").strip()
        except Exception as e:
            assistant_msg = f"(error) OpenAI request failed: {e}"

        self.history.append({"role": "assistant", "content": assistant_msg})
        return assistant_msg

    def reset(self) -> None:
        self.history = []
