"""
BaseAgent class with standardized I/O for AIDECK agents
"""
class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def run(self, input_data):
        raise NotImplementedError("Each agent must implement the run method.")
