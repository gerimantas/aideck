"""
Tasks API router for AIDECK
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_tasks():
    return ["Task 1", "Task 2"]
