import { create } from 'zustand';

interface AgentState {
  agents: any[];
  logs: string[];
  setAgents: (agents: any[]) => void;
  addLog: (log: string) => void;
}

export const useAgentStore = create<AgentState>((set) => ({
  agents: [],
  logs: [],
  setAgents: (agents) => set({ agents }),
  addLog: (log) => set((state) => ({ logs: [...state.logs, log] })),
}));
