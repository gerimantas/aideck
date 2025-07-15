"""
AI Agents trigger points router for AIDECK
"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/run")
def run_agent():
    return {"msg": "Agent run triggered"}
