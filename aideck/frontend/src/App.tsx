
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import AgentDashboard from './pages/AgentDashboard';
import PlanView from './pages/PlanView';
import LogsPage from './pages/LogsPage';

export function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/agents" element={<AgentDashboard />} />
      <Route path="/plan" element={<PlanView />} />
      <Route path="/logs" element={<LogsPage />} />
    </Routes>
  );
}

export function AppWithRouter() {
  return (
    <Router>
      <App />
    </Router>
  );
}

export default AppWithRouter;
