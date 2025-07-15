"""
Tracks OpenAI token usage for AIDECK
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TokenUsage(Base):
    __tablename__ = "token_usage"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tokens_used = Column(Integer, default=0)
    model = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")
