"""
GitHub interactions router for AIDECK
"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/webhook")
def github_webhook():
    return {"msg": "GitHub webhook received"}
