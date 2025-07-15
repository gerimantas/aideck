# AIDECK (APS) – Final Architecture and Development Plan with Integrated Improvements

---

## 📦 Project Directory Tree (with Descriptions)

```plaintext
aideck/
├── backend/
│   ├── main.py                   # FastAPI entrypoint
│   ├── config.py                 # App configuration
│   ├── database.py               # SQLAlchemy async DB setup
│   ├── models.py                 # ORM models incl. RBAC roles
│   ├── token_tracker.py          # Tracks OpenAI token usage
│   ├── Dockerfile                # Backend Docker config
│   ├── requirements.txt          # Python dependencies
│   ├── routers/                  # FastAPI route modules
│   │   ├── auth_router.py        # JWT/OAuth2 auth
│   │   ├── projects_router.py    # Projects API
│   │   ├── tasks_router.py       # Tasks API
│   │   ├── agents_router.py      # AI agents trigger points
│   │   └── github_router.py      # GitHub interactions
│   ├── modules/
│   │   ├── agents/
│   │   │   ├── base.py           # BaseAgent with standardized I/O
│   │   │   ├── factory.py        # Factory to create agents
│   │   │   ├── planner.py
│   │   │   ├── bug_hunter.py
│   │   │   ├── progress_tracker.py
│   │   │   ├── doc_generator.py
│   │   │   ├── github_manager.py
│   │   │   └── orchestrator.py   # Coordinates agent collaboration
│   │   ├── utils/
│   │   │   ├── vector_tools.py   # Embedding tools
│   │   │   ├── github_tools.py
│   │   │   ├── fs_tools.py
│   │   │   └── agent_logs.py     # Logs agent actions
│   │   ├── security/
│   │   │   ├── auth.py
│   │   │   ├── jwt_handler.py
│   │   │   ├── password_utils.py
│   │   │   └── security_middleware.py # Rate limiting, auditing
│   ├── chromadb/
│   │   └── init_vectorstore.py
│   ├── workers/
│   │   ├── tasks_worker.py       # Celery worker
│   │   └── logging.yaml          # JSON logging config
│   └── migrations/
│
├── frontend/
│   ├── Dockerfile
│   ├── vite.config.ts
│   ├── public/
│   └── src/
│       ├── App.tsx
│       ├── main.tsx
│       ├── routes.tsx
│       ├── api/
│       ├── state/                # Zustand or Redux Toolkit
│       │   └── agents.ts
│       ├── pages/
│       │   ├── Dashboard.tsx
│       │   ├── AgentDashboard.tsx
│       │   ├── PlanView.tsx
│       │   └── LogsPage.tsx
│       └── components/
│
├── tests/
│   ├── backend/
│   │   ├── test_agents.py
│   │   ├── test_orchestrator.py
│   │   └── test_routers.py
│   └── frontend/
│       ├── App.test.tsx
│       └── AgentDashboard.test.tsx
│
├── docs/
│   ├── decisions/
│   │   └── ADR_001_initial_architecture.md
│   └── architecture/
│       └── diagrams/
│
├── docker-compose.yml
└── .env
```

---

## 🛠️ Numbered Development Phases (with Improvements)

### Phase 1: Foundation & MVP Core

1.1 Set up FastAPI backend and async PostgreSQL  
1.2 Implement JWT-based authentication  
1.3 Define RBAC roles in `models.py`  
1.4 Create Docker + Docker Compose setup  
1.5 Scaffold React frontend app  

---

### Phase 2: Secure Auth & Token Tracking

2.1 Integrate OAuth2 provider  
2.2 Add rate-limiting via FastAPI-Limiter  
2.3 Implement token and role-based permissions  
2.4 Initialize token tracking (OpenAI usage)  

---

### Phase 3: Agent System

3.1 Create BaseAgent class with Pydantic I/O  
3.2 Add Planner, ProgressTracker, BugHunter agents  
3.3 Log all agent output in `agent_logs.py`  
3.4 Create AgentFactory  

---

### Phase 4: AI Orchestration + Vector Store Abstraction

4.1 Implement `orchestrator.py` for inter-agent workflows  
4.2 Add Celery + Redis for background task execution  
4.3 Abstract VectorStore into switchable backend (ChromaDB, Pinecone)  
4.4 Define standard agent state transitions  

---

### Phase 5: RAG & Embeddings

5.1 Configure embedding logic in `vector_tools.py`  
5.2 Store project vectors in ChromaDB  
5.3 Enable RAG-based BugHunter functionality  
5.4 Link embeddings to per-project IDs  

---

### Phase 6: Frontend UI & State Management

6.1 Build AgentDashboard, PlanView, LogsPage  
6.2 Use Zustand or Redux Toolkit to manage agent states  
6.3 Integrate React Query for API call caching  
6.4 Display AI results + logs visually  

---

### Phase 7: Testing, Monitoring, Docs

7.1 Write tests (Pytest for backend, Jest/Cypress for frontend)  
7.2 Load test orchestration with Locust  
7.3 Add Prometheus + Grafana dashboard  
7.4 Enable Sentry error tracking  
7.5 Auto-generate OpenAPI docs  
7.6 Maintain ADRs in `docs/decisions/`  

---

## ✅ Key Risk Mitigations

- Orchestration bottlenecks → Use Celery with retry support  
- Unpredictable agent flows → Standardize via Pydantic  
- Debugging issues → Enable structured JSON logging + Prometheus  
- Vector store lock-in → Abstract implementation behind provider interface  

---

## 📌 Prioritization (from risk table)

| Priority | Action                            | Phase |
|----------|-----------------------------------|--------|
| High     | RBAC + rate limiting              | 2      |
| High     | Testing framework (unit + load)   | 7      |
| High     | Celery queue for agents           | 4      |
| Medium   | Frontend state & React Query      | 6      |
| Medium   | Monitoring stack + logs           | 7      |
| Low      | Vector store abstraction layer    | 4      |