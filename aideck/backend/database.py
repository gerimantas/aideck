"""
Async SQLAlchemy database setup for AIDECK
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from databases import Database
from config import settings

DATABASE_URL = settings.DATABASE_URL

database = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()
metadata = Base.metadata
