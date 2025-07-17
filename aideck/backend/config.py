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
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://aideck:aideck@db:5432/aideck")  # Docker Compose: host 'db'
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    CORS_ORIGINS: List[str] = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    
    # Environment
    ENV: str = os.getenv("ENV", "development")
    
    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # GitHub
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    
    # Redis (for Celery)
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379")

    # Papildomai galima naudoti pydantic BaseSettings automatinį .env failo nuskaitymą:
    # class Settings(BaseSettings):
    #     class Config:
    #         env_file = "../../.env"
    
    # Vector Store
    CHROMA_PERSIST_DIRECTORY: str = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chromadb")
    
    # Rate limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 3600  # 1 hour
    
    class Config:
        env_file = ".env"

settings = Settings()
