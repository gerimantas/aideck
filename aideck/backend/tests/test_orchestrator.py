"""
Test Orchestrator with PlannerAgent using real AI functionality
"""
import pytest
from aideck.backend.modules.agents.orchestrator import Orchestrator
from aideck.backend.modules.agents.planner import PlannerAgent

@pytest.mark.asyncio
async def test_orchestrator_with_planner():
    agent_configs = ["planner"]
    orchestrator = Orchestrator(agent_configs)
    input_data = {"prompt": "Generate a project plan for an AI platform.", "context": "The platform should support agents, vector store, and frontend integration."}
    results = await orchestrator.run_workflow(input_data)
    assert "PlannerAgent" in results
    assert "plan" in results["PlannerAgent"]
    assert isinstance(results["PlannerAgent"]["plan"], str)
