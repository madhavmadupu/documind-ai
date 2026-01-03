from langchain_openai import ChatOpenAI
from config.settings import settings

def get_llm():
    return ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        temperature=0
    )