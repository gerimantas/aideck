"""
Celery worker for background tasks in AIDECK
"""
from celery import Celery
from aideck.backend.modules.agents.factory import AgentFactory
from aideck.backend.modules.agents.base import BaseAgent
from aideck.backend.modules.utils.agent_logs import log_agent_action

celery_app = Celery(
    'aideck_tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task
def run_agent_task(agent_type: str, payload: dict):
    agent = AgentFactory.create_agent({'type': agent_type})
    result = agent.run(payload)
    log_agent_action(agent_type, result)
    return result

celery_app = Celery('aideck_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery_app.task
def run_agent_task(agent_type: str, payload: dict):
    # Placeholder for running agent in background
    agent = AgentFactory.create_agent({'type': agent_type})
    result = agent.run(payload)
    log_agent_action(agent_type, result)
    return result
