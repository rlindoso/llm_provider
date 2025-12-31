from src.shared.container.providers.LLMProvider.models.ILLMProvider import ILLMProvider

class FakeLLMProvider(ILLMProvider):

    def ask(self, question: str) -> str:
        return f"This is a fake response to the question: {question}"