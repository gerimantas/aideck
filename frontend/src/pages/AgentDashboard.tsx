import React from 'react';
import { useAgentStore } from '../state/agents';

export const AgentDashboard: React.FC = () => {
  const agents = useAgentStore((state) => state.agents);
  return (
    <div>
      <h2>Agent Dashboard</h2>
      <ul>
        {agents.map((agent, idx) => (
          <li key={idx}>{agent.name || 'Unnamed Agent'}</li>
        ))}
      </ul>
    </div>
  );
};
export default AgentDashboard;
