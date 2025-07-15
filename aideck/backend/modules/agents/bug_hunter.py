"""
BugHunter agent for AIDECK
"""
from .base import BaseAgent

class BugHunterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="BugHunterAgent")

    def run(self, input_data):
        return {"bugs": ["No bugs found."]}
