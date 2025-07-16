# OpenAPI Auto-Generation (FastAPI)

- FastAPI automatically generates OpenAPI docs at `/docs` and `/openapi.json`
- No extra setup required
- For custom docs, use FastAPI's `openapi_url` and `docs_url` parameters
- Example:
```python
app = FastAPI(openapi_url="/openapi.json", docs_url="/docs")
```
