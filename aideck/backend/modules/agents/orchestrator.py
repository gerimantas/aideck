"""
Orchestrator coordinates agent collaboration for AIDECK
"""
class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def run_workflow(self, input_data):
        results = {}
        for agent in self.agents:
            results[agent.name] = agent.run(input_data)
        return results
