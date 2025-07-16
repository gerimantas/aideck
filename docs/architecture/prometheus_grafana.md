# Monitoring Stack: Prometheus + Grafana

## Prometheus
- Scrapes FastAPI metrics endpoint (`/metrics`)
- Configured in `docker-compose.yml`

## Grafana
- Visualizes Prometheus metrics
- Dashboard templates included

## Setup
1. Start with `docker-compose up`
2. Access Grafana at `localhost:3000` (default admin/admin)
3. Add Prometheus data source: `http://prometheus:9090`
4. Import dashboard templates from `docs/architecture/`
