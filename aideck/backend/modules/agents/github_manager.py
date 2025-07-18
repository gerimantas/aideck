"""
GitHubManager agent for AIDECK
"""
from .base import BaseAgent

class GitHubManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="GitHubManagerAgent")

    async def run(self, input_data):
        result = await super().run(input_data)
        return {"github": result.result, "raw_response": result.raw_response}
