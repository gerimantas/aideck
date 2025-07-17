"""
Celery worker for background tasks in AIDECK
"""

from celery import Celery
from aideck.backend.modules.agents.factory import AgentFactory
from aideck.backend.modules.agents.base import BaseAgent
from aideck.backend.modules.utils.agent_logs import log_agent_action
from aideck.backend.config import settings

celery_app = Celery(
    'aideck_tasks',
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

@celery_app.task
def run_agent_task(agent_type: str, payload: dict):
    agent = AgentFactory.create_agent({'type': agent_type})
    result = agent.run(payload)
    log_agent_action(agent_type, result)
    return result
