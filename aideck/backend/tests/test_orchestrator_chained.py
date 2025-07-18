"""
Test Orchestrator chained workflow with error handling
"""
import pytest
from aideck.backend.modules.agents.orchestrator import Orchestrator

@pytest.mark.asyncio
async def test_orchestrator_chained_workflow():
    agent_configs = ["planner", "progress_tracker"]
    orchestrator = Orchestrator(agent_configs)
    input_data = {"prompt": "Generate a project plan and track progress.", "context": "Project includes AI agents and frontend."}
    results = await orchestrator.run_chained_workflow(input_data)
    assert "PlannerAgent" in results
    assert results["PlannerAgent"]["status"] == "success"
    assert "ProgressTrackerAgent" in results
    assert results["ProgressTrackerAgent"]["status"] in ["success", "error"]
    # If error, error message should be present
    if results["ProgressTrackerAgent"]["status"] == "error":
        assert "error" in results["ProgressTrackerAgent"]
