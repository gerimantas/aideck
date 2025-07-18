import React, { useEffect, useState } from "react";

interface AgentResultData {
  agent_id: string;
  status: string;
  result: string;
}

export function AgentResultWS({ agentId }: { agentId: string }) {
  const [data, setData] = useState<AgentResultData | null>(null);
  const [status, setStatus] = useState<string>("connecting");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const wsUrl = process.env.REACT_APP_BACKEND_WS_URL || `ws://localhost:8000/ws/agents/results/${agentId}`;
    const ws = new WebSocket(`${wsUrl.replace(/\/$/, '')}/${agentId}`);
    ws.onopen = () => setStatus("connected");
    ws.onmessage = (event) => {
      try {
        setData(JSON.parse(event.data));
      } catch (e) {
        setError("Invalid data format");
      }
    };
    ws.onerror = () => setError("WebSocket error");
    ws.onclose = () => setStatus("disconnected");
    return () => ws.close();
  }, [agentId]);

  if (status === "connecting") return <div>Connecting to agent result...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!data) return <div>Waiting for agent result...</div>;

  return (
    <div className="agent-result">
      <h3>Agent Result (WebSocket)</h3>
      <div><strong>Agent ID:</strong> {data.agent_id}</div>
      <div><strong>Status:</strong> {data.status}</div>
      <div><strong>Result:</strong> {data.result}</div>
    </div>
  );
}
