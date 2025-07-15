"""
ProgressTracker agent for AIDECK
"""
from .base import BaseAgent

class ProgressTrackerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ProgressTrackerAgent")

    def run(self, input_data):
        return {"progress": "All tasks on track."}
