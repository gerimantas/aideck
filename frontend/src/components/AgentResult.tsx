import React from "react";
import { useQuery } from "react-query";
import axios from "axios";

export function AgentResult({ agentId }) {
  const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://aideck-backend:8000";
  const { data, isLoading, error } = useQuery([
    "agentResult",
    agentId,
  ], async () => {
    const res = await axios.get(`${backendUrl}/api/agents/results/${agentId}`);
    return res.data;
  });

  if (isLoading) return <div>Loading agent result...</div>;
  if (error) return <div>Error loading agent result</div>;

  return (
    <div className="agent-result">
      <h3>Agent Result</h3>
      <div><strong>Agent ID:</strong> {data.agent_id}</div>
      <div><strong>Status:</strong> {data.status}</div>
      <div><strong>Result:</strong> {data.result}</div>
    </div>
  );
}
