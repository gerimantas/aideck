"""
DocGenerator agent for AIDECK
"""
from .base import BaseAgent

class DocGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="DocGeneratorAgent")

    def run(self, input_data):
        return {"docs": "Documentation generated."}
