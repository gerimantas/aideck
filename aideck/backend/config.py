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
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://aideck:aideck@db:5432/aideck"  # Docker Compose: host 'db'

    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]

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
