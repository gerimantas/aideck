import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../aideck/backend')))
from config import settings

def test_database_url():
    assert "db:5432" in settings.DATABASE_URL, "DATABASE_URL turi naudoti hostą 'db' ir portą 5432"

def test_secret_key():
    assert settings.SECRET_KEY != "your-secret-key-here", "SECRET_KEY turi būti pakeistas į saugų"

def test_cors_origins_env():
    env_origins = os.getenv("CORS_ORIGINS", "")
    config_origins = settings.CORS_ORIGINS
    assert config_origins or env_origins, "CORS_ORIGINS turi būti nustatytas .env arba environment kintamajame"

def test_cors_origins_parsing():
    origins = settings.cors_origins
    assert isinstance(origins, list), "cors_origins turi būti sąrašas"
    for origin in origins:
        assert origin.startswith("http"), f"CORS origin '{origin}' turi prasidėti nuo 'http'"

def test_env_file_usage():
    assert hasattr(settings.Config, "env_file"), ".env failas turi būti naudojamas konfigūracijoje"
