
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import AgentDashboard from './pages/AgentDashboard';
import PlanView from './pages/PlanView';
import LogsPage from './pages/LogsPage';
import Sidebar from './components/Sidebar';

export function App() {
  return (
    <div style={{ display: 'flex' }}>
      <Sidebar />
      <div style={{ flex: 1, padding: 24 }}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/agents" element={<AgentDashboard />} />
          <Route path="/plan" element={<PlanView />} />
          <Route path="/logs" element={<LogsPage />} />
        </Routes>
      </div>
    </div>
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
