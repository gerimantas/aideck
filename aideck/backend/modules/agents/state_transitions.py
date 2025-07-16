from enum import Enum, auto

class AgentState(Enum):
    INIT = auto()
    RUNNING = auto()
    WAITING = auto()
    SUCCESS = auto()
    FAILURE = auto()
    RETRY = auto()

class StateTransition:
    @staticmethod
    def next_state(current: AgentState, result: str) -> AgentState:
        if result == "success":
            return AgentState.SUCCESS
        elif result == "failure":
            return AgentState.FAILURE
        elif result == "retry":
            return AgentState.RETRY
        else:
            return AgentState.WAITING
