"""
Celery worker for background tasks in AIDECK
"""
from celery import Celery

celery_app = Celery('aideck', broker='redis://localhost:6379/0')

@celery_app.task
def run_agent_task(agent_type, input_data):
    # Placeholder for running agent in background
    return f"Ran {agent_type} with {input_data}"
