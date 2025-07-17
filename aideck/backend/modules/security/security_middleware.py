"""
Security middleware for rate limiting and auditing in AIDECK
"""
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as aioredis


# Middleware setup (if needed)
def setup_rate_limiter(app):
    # Add any custom middleware here if needed
    return app

# Async rate limiter initialization for FastAPI startup event
async def init_rate_limiter():
    import os
    redis_host = os.environ.get("REDIS_HOST", "redis")
    redis_port = os.environ.get("REDIS_PORT", "6379")
    redis_url = f"redis://{redis_host}:{redis_port}"
    redis = await aioredis.from_url(redis_url, encoding="utf8", decode_responses=True)
    await FastAPILimiter.init(redis)

# Example usage in FastAPI:
# from modules.security.security_middleware import setup_rate_limiter
# app = FastAPI()
# app = setup_rate_limiter(app)
