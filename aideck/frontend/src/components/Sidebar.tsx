import { Link, useLocation } from 'react-router-dom';
import React from 'react';

const menuItems = [
  { path: '/', label: 'Dashboard' },
  { path: '/agents', label: 'Agents' },
  { path: '/plan', label: 'Plan' },
  { path: '/logs', label: 'Logs' },
];

export default function Sidebar() {
  const location = useLocation();
  return (
    <aside style={{ width: 200, background: '#f5f5f5', height: '100vh', padding: 16 }}>
      <nav>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {menuItems.map(item => (
            <li key={item.path} style={{ margin: '16px 0' }}>
              <Link
                to={item.path}
                style={{
                  color: location.pathname === item.path ? '#1976d2' : '#333',
                  fontWeight: location.pathname === item.path ? 'bold' : 'normal',
                  textDecoration: 'none',
                }}
              >
                {item.label}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
}
