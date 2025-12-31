from src.config.llm import llm_config

if llm_config["provider"] == "gemini":
    from src.shared.container.providers.LLMProvider.implementations.GeminiLLMProvider import GeminiLLMProvider
    LLMProvider = GeminiLLMProvider
elif llm_config["provider"] == "openai":
    from src.shared.container.providers.LLMProvider.implementations.OpenAILLMProvider import OpenAILLMProvider
    LLMProvider = OpenAILLMProvider
else:
    from src.shared.container.providers.LLMProvider.fakes.FakeLLMProvider import FakeLLMProvider
    LLMProvider = FakeLLMProvider

