import os

__provider = os.getenv("LLM_PROVIDER", "fake")  # Options: "openai", "gemini", "fake"
__model = os.getenv("LLM_MODEL", "") # Model name based on the provider

print(__provider, __model)

llm_config = {
    "provider": __provider,
    "model": __model
}
