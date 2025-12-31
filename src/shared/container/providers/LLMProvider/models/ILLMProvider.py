from abc import ABC, abstractmethod

class ILLMProvider(ABC):

    @abstractmethod
    def ask(self, question: str) -> str:
        pass
