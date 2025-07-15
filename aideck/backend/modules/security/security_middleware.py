"""
Security middleware for rate limiting and auditing in AIDECK
"""
class SecurityMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, scope, receive, send):
        # Placeholder for rate limiting/auditing
        return self.app(scope, receive, send)
