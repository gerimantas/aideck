"""
Authentication utilities for AIDECK
"""
def authenticate_user(username: str, password: str):
    # Dummy user for demonstration; replace with DB lookup
    dummy_user = {"username": "admin", "password": "adminpass", "role": "admin"}
    if username == dummy_user["username"] and password == dummy_user["password"]:
        return {"username": dummy_user["username"], "role": dummy_user["role"]}
    return None
