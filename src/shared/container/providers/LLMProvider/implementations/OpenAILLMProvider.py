from src.shared.container.providers.LLMProvider.models.ILLMProvider import ILLMProvider
from src.config.llm import llm_config
from openai import OpenAI

import os



class OpenAILLMProvider(ILLMProvider):
    def __init__(self):
        self.client = OpenAI()  # uses the OPENAI_API_KEY environment variable

    def ask(self, question: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=llm_config["model"],
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                temperature=0.7
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error connecting to the API: {e}"