"""
Authentication utilities for AIDECK
"""

def authenticate_user(username: str, password: str):
    # Dummy user for demonstration; replace with DB lookup
    users = [
        {"username": "admin", "password": "adminpass", "role": "admin"},
        {"username": "user", "password": "userpass", "role": "user"}
    ]
    for user in users:
        if username == user["username"] and password == user["password"]:
            return {"username": user["username"], "role": user["role"]}
    return None

def create_or_get_oauth_user(username: str):
    # Placeholder for DB logic to create/find OAuth2 user
    # Always returns user with 'user' role for demo
    return {"username": username, "role": "user"}
