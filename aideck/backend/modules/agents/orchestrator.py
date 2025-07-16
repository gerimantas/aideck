"""
Orchestrator coordinates agent collaboration for AIDECK
"""
from .base import BaseAgent
from .factory import AgentFactory
from aideck.backend.modules.utils.agent_logs import log_agent_action
from typing import Any

class Orchestrator:
    def __init__(self, agent_configs):
        self.agents = [AgentFactory.create_agent(cfg) for cfg in agent_configs]
        self.state = {}

    def run_workflow(self, input_data):
        results = {}
        for agent in self.agents:
            agent_result = agent.run(input_data)
            agent_id = getattr(agent, "name", agent.__class__.__name__)
            log_agent_action(agent_id, agent_result)
            results[agent_id] = agent_result
            self._update_state(agent, agent_result)
        return results

    def _update_state(self, agent: BaseAgent, result: Any):
        agent_id = getattr(agent, "name", agent.__class__.__name__)
        self.state[agent_id] = result

    def get_state(self):
        return self.state

    def trigger_background_task(self, task_name, payload):
        # This will enqueue a Celery task
        from aideck.backend.workers.tasks_worker import run_agent_task
        run_agent_task.delay(task_name, payload)
        log_agent_action("Orchestrator", f"Triggered background task: {task_name}")
