import { useQuery } from 'react-query';

export const useAgents = () => {
  const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://aideck-backend:8000";
  return useQuery('agents', async () => {
    const res = await fetch(`${backendUrl}/api/agents`);
    return res.json();
  });
};
