"""
ProgressTracker agent for AIDECK
"""
from .base import BaseAgent

class ProgressTrackerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ProgressTrackerAgent")

    async def run(self, input_data):
        # Use BaseAgent's async run method for AI completion
        result = await super().run(input_data)
        return {"progress": result.result, "raw_response": result.raw_response}
