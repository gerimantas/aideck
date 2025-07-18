import React from "react";
import { AgentResultWS } from "./components/AgentResultWS";

export default function App() {
  return (
    <div>
      <h1>AIDECK Frontend</h1>
      <p>React app is running!</p>
      <AgentResultWS agentId="test-agent" />
    </div>
  );
}
