"""
Factory to create agents for AIDECK
"""
from .planner import PlannerAgent
from .bug_hunter import BugHunterAgent
from .progress_tracker import ProgressTrackerAgent
from .doc_generator import DocGeneratorAgent
from .github_manager import GitHubManagerAgent

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str):
        if agent_type == "planner":
            return PlannerAgent()
        elif agent_type == "bug_hunter":
            return BugHunterAgent()
        elif agent_type == "progress_tracker":
            return ProgressTrackerAgent()
        elif agent_type == "doc_generator":
            return DocGeneratorAgent()
        elif agent_type == "github_manager":
            return GitHubManagerAgent()
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
