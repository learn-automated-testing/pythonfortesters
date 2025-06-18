import pytest
import requests

BASE_PATH = "/practice/auth"

class TestAuthAPI:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        """Setup for each test"""
        self.client = api_client

    def test_auth_success(self):
        """Test successful authentication"""
        response = self.client.post(
            f"{self.client.base_url}{BASE_PATH}",
            json={"username": "admin", "password": "password123"}
        )
        assert response.ok
        data = response.json()
        assert "token" in data
        assert data["user"] == "admin"

    def test_auth_failure(self):
        """Test failed authentication"""
        response = self.client.post(
            f"{self.client.base_url}{BASE_PATH}",
            json={"username": "admin", "password": "wrongpassword"}
        )
        assert response.status_code in [401, 400]
        data = response.json()
        assert "error" in data
        assert "invalid" in data["error"].lower() 