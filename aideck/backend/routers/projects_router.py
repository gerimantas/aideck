"""
Projects API router for AIDECK
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_projects():
    return ["Project 1", "Project 2"]
