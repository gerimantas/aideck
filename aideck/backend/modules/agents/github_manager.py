"""
GitHubManager agent for AIDECK
"""
from .base import BaseAgent

class GitHubManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="GitHubManagerAgent")

    def run(self, input_data):
        return {"github": "GitHub actions managed."}
