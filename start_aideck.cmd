@echo off
REM Universalus AIDECK paleidimo failas

REM 1. Paleiskite visus Docker Compose servisus (backend, db, monitoring, frontend jei yra)
echo Starting Docker Compose services...
docker-compose up -d


REM 2. Paleidžiamas frontend dev serveris atskirame lange
echo Starting frontend dev server in new window...
start cmd /k "cd aideck\frontend && npm install && npm run dev"

REM 3. Automatiškai atidaromas naršyklėje Frontend UI
timeout /t 5 >nul
start http://localhost:5173

echo.
echo --- Sistemos adresai ---
echo Backend API:       http://localhost:8000/api/docs
echo Frontend UI:       http://localhost:5173  (arba portą, kurį rodo terminalas)
echo Prometheus:        http://localhost:9090
echo Grafana:           http://localhost:3000
echo.
echo --- Testavimas ---
echo Backend testai:    python -m pytest aideck/tests/backend --maxfail=5 --disable-warnings -v
echo Frontend testai:   cd aideck/frontend && npm run test
echo Locust:            locust -f aideck/tests/load/locustfile.py --headless -u 10 -r 2 --run-time 30s --host=http://localhost:8000
echo.
echo --- Dokumentacija ---
echo ADR:               docs/decisions/
echo Sentry:            Patikrinkite savo Sentry paskyrą

echo AIDECK sistema paleista. Atidarykite naršyklėje nurodytus adresus.
pause
