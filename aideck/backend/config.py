"""
Application configuration settings
Centralizuotas .env failas naudojamas visiems servisams (žr. .env šakniniame kataloge)
"""
import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings
    Naudojamos .env reikšmės iš šakninio katalogo
    """

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://aideck:aideck@localhost:5432/aideck"  # Localhost for local run

    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: str = ""

    @property
    def cors_origins(self) -> list[str]:
        import json
        raw = self.CORS_ORIGINS or os.getenv("CORS_ORIGINS", "")
        # Palaiko JSON sąrašą arba CSV
        try:
            origins = json.loads(raw)
            if isinstance(origins, list):
                return [o.strip() for o in origins if isinstance(o, str) and o.strip()]
        except Exception:
            pass
        return [origin.strip() for origin in raw.split(",") if origin.strip()]

    # Environment
    ENV: str = "development"

    # OpenAI
    OPENAI_API_KEY: str = ""

    # GitHub
    GITHUB_TOKEN: str = ""

    # Redis (for Celery)
    REDIS_URL: str = "redis://redis:6379"

    # Vector Store
    CHROMA_PERSIST_DIRECTORY: str = "./chromadb"

    # Rate limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 3600  # 1 hour

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
