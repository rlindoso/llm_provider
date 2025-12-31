# LLM Provider

A lightweight, extensible **LLM provider abstraction layer** for Python projects.
This project provides a clean interface to interact with different Large Language Model (LLM) providers (such as **OpenAI**, **Google Gemini**, or **fake/mock providers**) while keeping your application **decoupled from vendor-specific implementations**.

The design follows **SOLID principles**, making it easy to switch providers, add new ones, and test your application without depending on external APIs.

---

## 📌 Goals

* Provide a **single, unified interface** for LLM interaction
* Allow **provider swapping via environment variables**
* Enable **easy mocking/faking** of LLMs for tests
* Keep provider-specific logic isolated
* Encourage **clean architecture and dependency inversion**

---

## 🧱 Project Structure

```
llm_provider/
├── src/
│   ├── config/
│   │   └── llm.py
│   └── shared/
│       └── container/
│           └── providers/
│               └── LLMProvider/
│                   ├── models/
│                   │   └── ILLMProvider.py
│                   ├── implementations/
│                   │   ├── OpenAILLMProvider.py
│                   │   └── GeminiLLMProvider.py
│                   ├── fakes/
│                   │   └── FakeLLMProvider.py
│                   └── __init__.py
├── test.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🔌 Core Concepts

### 1. LLM Interface (Dependency Inversion)

All providers implement the same interface:

```python
class ILLMProvider(ABC):
    @abstractmethod
    def ask(self, question: str) -> str:
        pass
```

Your application **depends on this interface**, not on OpenAI, Gemini, or any concrete SDK.

---

### 2. Providers

#### ✅ OpenAI Provider

* Uses the OpenAI API
* Reads API key from environment variables
* Handles API errors gracefully

#### ✅ Gemini Provider

* Uses Google Gemini API
* Same interface as OpenAI
* Fully swappable via config

#### ✅ Fake Provider

* Returns deterministic responses
* Ideal for:

  * Unit tests
  * Local development
  * CI pipelines

---

### 3. Provider Resolution (Configuration)

The provider is selected **at runtime** via environment variables.

`src/config/llm.py`:

```python
config = {
    "provider": __provider,
    "model": __model
}
```

`LLM_PROVIDER` controls which implementation is injected:

* `openai`
* `gemini`
* `fake`

---

## ⚙️ Environment Configuration

Create a `.env` file based on `.env.example`:

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key

LLM_PROVIDER=fake
LLM_MODEL=gemini-2.5-flash-lite
```

---

## ▶️ Usage Example

```python
from dotenv import load_dotenv
load_dotenv()

from src.shared.container.providers.LLMProvider import LLMProvider

llm = LLMProvider()
response = llm.ask("What is SOLID?")
print(response)
```

Changing the provider **requires no code changes**, only environment variables.

---

## 🧪 Testing with Fake Provider

Set:

```env
LLM_PROVIDER=fake
```

The fake provider will respond with:

```text
This is a fake response to the question: <your question>
```

This ensures:

* Fast tests
* No API costs
* No external dependencies

---

## 🧠 Design Principles Applied

### ✔ Single Responsibility

Each provider handles **only** its own API logic.

### ✔ Open / Closed

New providers can be added without modifying existing ones.

### ✔ Liskov Substitution

All providers can be used interchangeably via `ILLMProvider`.

### ✔ Interface Segregation

The interface is minimal and focused (`ask()` only).

### ✔ Dependency Inversion

The application depends on an abstraction, not concrete providers.

---

## ➕ Adding a New Provider

1. Create a new class implementing `ILLMProvider`
2. Place it in:

   ```
   implementations/
   ```
3. Register it in `LLMProvider/__init__.py`
4. Select it via `LLM_PROVIDER`

No changes required in application code.

---

## 📦 Requirements

Python version:

```
3.12+
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Possible Improvements

* Add streaming support (`ask_stream`)
* Introduce retry and timeout policies
* Add structured responses (JSON mode)
* Implement token/cost tracking
* Add async support (`async def ask`)
* Integrate prompt templates
* Add observability hooks (logs, metrics)

---

## 📄 License

This project is provided as-is for educational and architectural reference purposes.
You are free to adapt it to your own projects.
