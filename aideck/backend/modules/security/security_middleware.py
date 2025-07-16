"""
Security middleware for rate limiting and auditing in AIDECK
"""
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import aioredis

def setup_rate_limiter(app):
    import asyncio
    async def init():
        redis = await aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
        await FastAPILimiter.init(redis)
    asyncio.get_event_loop().run_until_complete(init())
    return app

# Example usage in FastAPI:
# from modules.security.security_middleware import setup_rate_limiter
# app = FastAPI()
# app = setup_rate_limiter(app)
