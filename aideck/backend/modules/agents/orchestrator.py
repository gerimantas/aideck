"""
Orchestrator coordinates agent collaboration for AIDECK
"""
from .base import BaseAgent
from .factory import AgentFactory
from modules.utils.agent_logs import log_agent_action
from typing import Any
import inspect

class Orchestrator:
    async def run_chained_workflow(self, input_data):
        """
        Runs agents in sequence, passing previous agent's output as input to the next.
        Returns dict with agent results, errors, and statuses.
        """
        results = {}
        state = {}
        last_output = input_data
        for agent in self.agents:
            run_method = getattr(agent, "run", None)
            agent_id = getattr(agent, "name", agent.__class__.__name__)
            try:
                if inspect.iscoroutinefunction(run_method):
                    agent_result = await run_method(last_output)
                else:
                    agent_result = run_method(last_output)
                results[agent_id] = {
                    "status": "success",
                    "result": agent_result
                }
                last_output = agent_result  # Pass output to next agent
            except Exception as e:
                results[agent_id] = {
                    "status": "error",
                    "error": str(e)
                }
                last_output = last_output  # Pass unchanged input if error
            self._update_state(agent, results[agent_id])
        return results
    def __init__(self, agent_configs):
        self.agents = [AgentFactory.create_agent(cfg) for cfg in agent_configs]
        self.state = {}

    import inspect
    async def run_workflow(self, input_data):
        results = {}
        for agent in self.agents:
            run_method = getattr(agent, "run", None)
            if inspect.iscoroutinefunction(run_method):
                agent_result = await run_method(input_data)
            else:
                agent_result = run_method(input_data)
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
        from workers.tasks_worker import run_agent_task
        run_agent_task.delay(task_name, payload)
        log_agent_action("Orchestrator", f"Triggered background task: {task_name}")
