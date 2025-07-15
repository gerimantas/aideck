"""
Planner agent for AIDECK
"""
from .base import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent")

    def run(self, input_data):
        return {"plan": "Generated project plan."}
