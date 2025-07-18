import pytest
from fastapi.testclient import TestClient
from aideck.backend.main import app

def test_root_health():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
