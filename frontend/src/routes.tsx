import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AgentDashboard from './pages/AgentDashboard';
import PlanView from './pages/PlanView';
import LogsPage from './pages/LogsPage';

const AppRoutes: React.FC = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<AgentDashboard />} />
      <Route path="/plan" element={<PlanView />} />
      <Route path="/logs" element={<LogsPage />} />
    </Routes>
  </BrowserRouter>
);

export default AppRoutes;
