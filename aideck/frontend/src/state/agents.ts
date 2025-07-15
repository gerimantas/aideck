// Zustand state for agents
import { create } from 'zustand';


interface Agent {
  // Apibrėžkite agento laukus pagal poreikį, pvz.:
  id?: string;
  name?: string;
}

interface AgentState {
  agents: Agent[];
  setAgents: (agents: Agent[]) => void;
}

export const useAgentStore = create<AgentState>((set) => ({
  agents: [],
  setAgents: (agents) => set({ agents }),
}));
