"""
Test Orchestrator with multiple agents and background task triggering
"""
import pytest
from modules.agents.orchestrator import Orchestrator

@pytest.mark.asyncio
async def test_orchestrator_multi_agent():
    agent_configs = ["planner", "progress_tracker"]
    orchestrator = Orchestrator(agent_configs)
    input_data = {"prompt": "Track project progress and generate a plan.", "context": "Project includes AI agents and frontend."}
    results = await orchestrator.run_workflow(input_data)
    assert "PlannerAgent" in results
    assert "ProgressTrackerAgent" in results
    assert isinstance(results["PlannerAgent"], dict)
    assert isinstance(results["ProgressTrackerAgent"], dict)

@pytest.mark.asyncio
async def test_orchestrator_background_task(monkeypatch):
    agent_configs = ["planner"]
    orchestrator = Orchestrator(agent_configs)
    called = {}
    def fake_delay(task_name, payload):
        called["task_name"] = task_name
        called["payload"] = payload
    monkeypatch.setattr("workers.tasks_worker.run_agent_task.delay", fake_delay)
    orchestrator.trigger_background_task("test_task", {"foo": "bar"})
    assert called["task_name"] == "test_task"
    assert called["payload"] == {"foo": "bar"}
