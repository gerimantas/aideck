import React from 'react';
import { useAgentStore } from '../state/agents';

export const LogsPage: React.FC = () => {
  const logs = useAgentStore((state) => state.logs);
  return (
    <div>
      <h2>Agent Logs</h2>
      <ul>
        {logs.map((log, idx) => (
          <li key={idx}>{log}</li>
        ))}
      </ul>
    </div>
  );
};
export default LogsPage;
