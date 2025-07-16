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

# Example usage:
# def log_token_usage(user_id: int, tokens: int, model: str, db):
#     usage = TokenUsage(user_id=user_id, tokens_used=tokens, model=model)
#     db.add(usage)
#     db.commit()
