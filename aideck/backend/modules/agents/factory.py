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
    def create_agent(config_or_type):
        if isinstance(config_or_type, dict):
            agent_type = config_or_type.get("type", "planner").lower()
        else:
            agent_type = str(config_or_type).lower()
        if agent_type == "planner":
            return PlannerAgent()
        elif agent_type == "bughunter" or agent_type == "bug_hunter":
            return BugHunterAgent()
        elif agent_type == "progresstracker" or agent_type == "progress_tracker":
            return ProgressTrackerAgent()
        elif agent_type == "docgenerator" or agent_type == "doc_generator":
            return DocGeneratorAgent()
        elif agent_type == "githubmanager" or agent_type == "github_manager":
            return GitHubManagerAgent()
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
