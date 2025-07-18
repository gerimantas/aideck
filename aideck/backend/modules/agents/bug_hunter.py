"""
BugHunter agent for AIDECK
"""
from .base import BaseAgent

class BugHunterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="BugHunterAgent")

    async def run(self, input_data):
        # Optionally, keep RAG/embedding logic, but add OpenAI completion
        result = await super().run(input_data)
        return {"bugs": result.result, "raw_response": result.raw_response}
