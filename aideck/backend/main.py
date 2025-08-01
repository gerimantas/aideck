"""
AIDECK FastAPI entrypoint
Main application setup with routers and middleware
"""
print("[AIDECK] main.py started!")
## Sentry error tracking laikinai išjungtas
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from fastapi import WebSocket, WebSocketDisconnect
import uvicorn

from prometheus_fastapi_instrumentator import Instrumentator

from config import settings
from database import database, engine
from models import metadata
from routers import auth_router, projects_router, tasks_router, agents_router, github_router
from modules.security.security_middleware import setup_rate_limiter, init_rate_limiter

# Create FastAPI app
app = FastAPI(
    title="AIDECK - AI Development Platform",
    description="AI-powered development project management system",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)


# Security
security = HTTPBearer()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus metrics endpoint
Instrumentator().instrument(app).expose(app)




# Database and rate limiter setup
@app.on_event("startup")
async def startup():
    """Initialize database connection and rate limiter"""
    await database.connect()
    # Rate limiter async init
    await init_rate_limiter()
    # Create tables (async)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    """Close database connection"""
    await database.disconnect()

# Include routers
app.include_router(auth_router.router, prefix="/api/auth", tags=["authentication"])
app.include_router(projects_router.router, prefix="/api/projects", tags=["projects"])
app.include_router(tasks_router.router, prefix="/api/tasks", tags=["tasks"])
app.include_router(agents_router.router, prefix="/api/agents", tags=["agents"])
app.include_router(github_router.router, prefix="/api/github", tags=["github"])

# WebSocket endpoint for agent results
@app.websocket("/ws/agents/results/{agent_id}")
async def websocket_agent_results(websocket: WebSocket, agent_id: str):
    await websocket.accept()
    try:
        # Dummy loop: send a test message every 2 seconds
        import asyncio
        import json
        while True:
            data = {
                "agent_id": agent_id,
                "status": "completed",
                "result": "Test result from backend"
            }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        print(f"WebSocket disconnected for agent {agent_id}")

# Viešas konfigūracijos endpointas frontend'ui
@app.get("/api/config")
async def get_config():
    return {
        "version": app.version,
        "environment": settings.ENV,
        "cors_origins": settings.CORS_ORIGINS
    }
@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "AIDECK API is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True if settings.ENV == "development" else False
    )
