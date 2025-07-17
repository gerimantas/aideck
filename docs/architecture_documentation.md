# Architecture Documentation

## Overview
AIDECK is a modular AI-powered project management platform. It consists of:
- **Backend**: FastAPI, Celery, PostgreSQL, Redis
- **Frontend**: React, Vite
- **Vector Store**: ChromaDB
- **Monitoring**: Prometheus, Grafana

## Main Components
- **Agents**: Modular AI agents for automation
- **Orchestrator**: Coordinates agent tasks
- **Routers**: API endpoints for projects, tasks, agents, auth
- **Workers**: Celery background tasks
- **Security**: OAuth2, rate limiting, secrets management

## Data Flow
1. Frontend sends requests to backend API
2. Backend processes requests, interacts with DB, agents, vector store
3. Celery handles async/background tasks
4. Monitoring via Prometheus/Grafana

## Diagrams
- See `/docs/architecture/diagrams/`
