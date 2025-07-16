# ADR 001: Pradinė architektūra

## Sprendimas
Pasirinkta modulinių katalogų struktūra, atskiriant backend, frontend, testus, dokumentaciją ir DevOps failus. Backend naudoja FastAPI, async SQLAlchemy, JWT, RBAC, Docker, agentų sistemą, Celery, ChromaDB. Frontend – React, Vite, Zustand/Redux, Jest. Testavimas – Pytest, Jest/Cypress. Monitoringas – Prometheus, Grafana, Sentry.

## Priežastys
- Aiškus atskyrimas tarp backend ir frontend
- Lengva plėsti agentų sistemą
- Paprasta CI/CD integracija
- Patogus testavimas ir monitoringas

## Alternatyvos
- Monolitinė architektūra
- Kiti framework'ai (Django, Flask, Vue)

## Pasekmės
- Greitas MVP vystymas
- Lengva modulių plėtra
- Aiškus testų ir dokumentacijos palaikymas
