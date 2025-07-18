"""
Planner agent for AIDECK
"""
from .base import BaseAgent

from .base import BaseAgent, AgentInput, AgentOutput
import asyncio

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent")

    async def run(self, input_data):
        result = await super().run(input_data)
        return {"plan": result.result, "raw_response": result.raw_response}
