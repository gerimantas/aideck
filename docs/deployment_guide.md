# Deployment Guide

## Prerequisites
- Docker & Docker Compose
- Node.js & npm
- Python 3.12+

## Steps
1. Clone repository
2. Configure `.env` file
3. Build and start services:
   ```sh
   docker-compose up --build
   ```
4. Access frontend: http://localhost:3000
5. Access backend API: http://localhost:8000

## CI/CD
- GitHub Actions automates tests and deployment
- See `.github/workflows/ci.yml` and `.github/workflows/deploy.yml`

## Troubleshooting
- Check logs with `docker-compose logs`
- Verify environment variables
