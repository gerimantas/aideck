"""
Pytest tests for orchestrator
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
import pytest
from aideck.backend.modules.agents.orchestrator import Orchestrator
from aideck.backend.modules.agents.state_transitions import AgentState, StateTransition

class DummyAgent:
    def __init__(self, name):
        self.name = name
    def run(self, input_data):
        return {"status": "success", "output": f"{self.name} processed"}

class DummyFactory:
    @staticmethod
    def create_agent(cfg):
        return DummyAgent(cfg['type'])

@pytest.fixture(autouse=True)
def patch_factory(monkeypatch):
    import aideck.backend.modules.agents.factory
    monkeypatch.setattr(aideck.backend.modules.agents.factory.AgentFactory, "create_agent", DummyFactory.create_agent)


def test_orchestrator_workflow():
    agent_configs = [{"type": "Planner"}, {"type": "BugHunter"}]
    orchestrator = Orchestrator(agent_configs)
    input_data = {"project_id": 123}
    results = orchestrator.run_workflow(input_data)
    assert "Planner" in results
    assert "BugHunter" in results
    assert results["Planner"]["status"] == "success"
    assert results["BugHunter"]["status"] == "success"
    assert orchestrator.get_state()["Planner"]["output"] == "Planner processed"


def test_state_transitions():
    assert StateTransition.next_state(AgentState.INIT, "success") == AgentState.SUCCESS
    assert StateTransition.next_state(AgentState.RUNNING, "failure") == AgentState.FAILURE
    assert StateTransition.next_state(AgentState.RUNNING, "retry") == AgentState.RETRY
    assert StateTransition.next_state(AgentState.RUNNING, "other") == AgentState.WAITING
    
def test_orchestrator():
    assert True  # Placeholder
    assert True  # Placeholder
