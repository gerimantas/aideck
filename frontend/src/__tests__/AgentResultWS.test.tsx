import React from "react";
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { AgentResultWS } from "../components/AgentResultWS";

describe("AgentResultWS", () => {
  it("renders loading state initially", () => {
    render(<AgentResultWS agentId="test-agent" />);
    expect(screen.getByText(/Connecting to agent result/i)).toBeInTheDocument();
  });

  // WebSocket mocking and further tests can be added here
});
