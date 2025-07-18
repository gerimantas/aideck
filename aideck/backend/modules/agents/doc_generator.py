"""
DocGenerator agent for AIDECK
"""
from .base import BaseAgent

class DocGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="DocGeneratorAgent")

    async def run(self, input_data):
        result = await super().run(input_data)
        return {"docs": result.result, "raw_response": result.raw_response}
