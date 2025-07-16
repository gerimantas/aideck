# Sentry Error Tracking Setup

## Backend (FastAPI)
- Install: `pip install sentry-sdk`
- Usage:
```python
import sentry_sdk
sentry_sdk.init(dsn="<YOUR_SENTRY_DSN>")
```
- Add to `main.py` before app startup

## Frontend (React)
- Install: `npm install @sentry/react @sentry/tracing`
- Usage:
```js
import * as Sentry from "@sentry/react";
Sentry.init({ dsn: "<YOUR_SENTRY_DSN>" });
```
- Add to `src/main.tsx`
