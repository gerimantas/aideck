import { useQuery } from 'react-query';

export const useAgents = () => {
  return useQuery('agents', async () => {
    const res = await fetch('/api/agents');
    return res.json();
  });
};
