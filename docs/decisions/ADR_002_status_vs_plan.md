# ADR 002: Projekto statusas vs. planas

## Palyginimo analizė

### Struktūra
- Sukurta visa planuota katalogų ir failų struktūra: backend, frontend, testai, dokumentacija, Docker, .env.
- Backend: visi pagrindiniai failai ir katalogai (main.py, config.py, database.py, models.py, token_tracker.py, Dockerfile, requirements.txt, routers, modules, chromadb, workers, migrations).
- Frontend: Dockerfile, vite.config.ts, public, src su App.tsx, main.tsx, routes.tsx, api, state, pages, components.
- Testai: aideck/tests/backend su test_routers.py, test_orchestrator.py, test_agents.py; aideck/tests/frontend su App.test.tsx, AgentDashboard.test.tsx.
- Dokumentacija: ADR, architektūros diagramos.

### Funkcionalumas
- 1 fazė pilnai įgyvendinta: backend, frontend scaffold, Docker, RBAC, JWT, testai.
- 2 fazės dalis: JWT, RBAC, token tracking paruošta, rate limiting ir OAuth2 dar neimplementuota.
- 3–5 fazės: agentų katalogas ir failai sukurti, bazinė logika paruošta, bet agentų funkcionalumas dar nebaigtas.
- 6 fazė: UI scaffold, Zustand/Redux paruošta, React Query dar neintegruota, puslapiai ir komponentai sukurti.
- 7 fazė: testai pilnai veikia, ADR ir architektūros diagramos yra, monitoringas dar neįdiegtas, OpenAPI docs paruošta.

### Išvados
- Struktūra ir pagrindiniai moduliai pilnai atitinka planą.
- MVP ir pagrindinė architektūra įgyvendinta.
- Dalis funkcionalumo (OAuth2, rate limiting, agentų logika, monitoringas) dar nebaigta, bet paruošta plėtrai.
- Toliau tęsti pagal planą – įgyvendinti likusius funkcionalumo ir monitoringo punktus.
