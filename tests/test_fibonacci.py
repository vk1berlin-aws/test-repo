import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


class TestFibonacciValid:
    """Tests for valid inputs to the /fibonacci/{n} endpoint."""

    def test_fibonacci_n1(self, client):
        response = client.get("/fibonacci/1")
        assert response.status_code == 200
        assert response.json() == [0]

    def test_fibonacci_n10(self, client):
        response = client.get("/fibonacci/10")
        assert response.status_code == 200
        assert response.json() == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_n2(self, client):
        response = client.get("/fibonacci/2")
        assert response.status_code == 200
        assert response.json() == [0, 1]

    def test_fibonacci_n5(self, client):
        response = client.get("/fibonacci/5")
        assert response.status_code == 200
        assert response.json() == [0, 1, 1, 2, 3]


class TestFibonacciBoundary:
    """Tests for boundary cases of the /fibonacci/{n} endpoint."""

    def test_fibonacci_n100(self, client):
        response = client.get("/fibonacci/100")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 100
        # Verify first few elements
        assert data[:7] == [0, 1, 1, 2, 3, 5, 8]
        # Verify the sequence property: each element is sum of previous two
        for i in range(2, len(data)):
            assert data[i] == data[i - 1] + data[i - 2]


class TestFibonacciInvalid:
    """Tests for invalid inputs to the /fibonacci/{n} endpoint."""

    def test_fibonacci_n0_returns_422(self, client):
        response = client.get("/fibonacci/0")
        assert response.status_code == 422
        assert "Must be a positive integer between 1 and 100" in response.json()["detail"]

    def test_fibonacci_negative_returns_422(self, client):
        response = client.get("/fibonacci/-1")
        assert response.status_code == 422
        assert "Must be a positive integer between 1 and 100" in response.json()["detail"]

    def test_fibonacci_n101_returns_422(self, client):
        response = client.get("/fibonacci/101")
        assert response.status_code == 422
        assert "Must be a positive integer between 1 and 100" in response.json()["detail"]

    def test_fibonacci_non_integer_string_returns_422(self, client):
        response = client.get("/fibonacci/abc")
        assert response.status_code == 422
        assert "Must be a positive integer between 1 and 100" in response.json()["detail"]

    def test_fibonacci_float_returns_422(self, client):
        response = client.get("/fibonacci/3.5")
        assert response.status_code == 422
        assert "Must be a positive integer between 1 and 100" in response.json()["detail"]

    def test_fibonacci_large_number_returns_422(self, client):
        response = client.get("/fibonacci/1000")
        assert response.status_code == 422
        assert "Must be a positive integer between 1 and 100" in response.json()["detail"]
