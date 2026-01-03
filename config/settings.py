try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    OPENAI_API_KEY: str
    LLM_PROVIDER: str = "openai"
    EMBEDDING_MODEL: str
    VECTOR_STORE: str = "faiss"

    class Config:
        env_file = ".env"

settings = Settings()