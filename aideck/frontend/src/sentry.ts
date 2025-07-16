import * as Sentry from "@sentry/react";

Sentry.init({
  dsn: "<YOUR_SENTRY_DSN>",
  tracesSampleRate: 1.0,
  environment: process.env.NODE_ENV,
});
