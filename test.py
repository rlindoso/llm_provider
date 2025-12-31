from dotenv import load_dotenv
# Loads the variables from the .env file.
load_dotenv()

from src.shared.container.providers.LLMProvider import LLMProvider


llm = LLMProvider()
prompt = "Briefly explain what cloud computing is to a beginner."
print(f"Question: {prompt}")
print("-" * 30)

response = llm.ask(prompt)
print(f"LLM's response:\n{response}")