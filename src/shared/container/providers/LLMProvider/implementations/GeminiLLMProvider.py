from src.shared.container.providers.LLMProvider.models.ILLMProvider import ILLMProvider
from src.config.llm import llm_config

import os
from google import genai


class GeminiLLMProvider(ILLMProvider):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)

    def ask(self, question: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=llm_config["model"], 
                contents=question
            )
            return response.text
        except Exception as e:
            return f"Error connecting to the API: {e}"