import pytest
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for the API"""
    return os.getenv("API_BASE_URL", "https://api.practiceautomatedtesting.com")

@pytest.fixture(scope="session")
def api_client(base_url):
    """Return a requests session with base URL configured"""
    session = requests.Session()
    session.base_url = base_url
    return session

@pytest.fixture(scope="function")
def auth_token(api_client):
    """Get authentication token"""
    response = api_client.post(
        f"{api_client.base_url}/practice/auth",
        json={"username": "admin", "password": "password123"}
    )
    if response.ok:
        return response.json().get("token")
    return None 