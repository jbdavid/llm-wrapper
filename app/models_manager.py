from langchain_openai import ChatOpenAI
import os

def get_model():
    provider = os.getenv("PROVIDER", "openai").lower()
    if provider == "openai":
        return ChatOpenAI(model="gpt-4o")
    elif provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    else:
        raise ValueError(f"Provider {provider} not supported. Use 'openai' or 'gemini'.")
