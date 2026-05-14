import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test GET /activities
def test_get_activities():
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Chess Club" in response.json()

# Test POST /activities/{activity_name}/signup
def test_signup_for_activity():
    # Arrange
    url = "/activities/Chess%20Club/signup?email=test@example.com"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@example.com for Chess Club"

# Test DELETE /activities/{activity_name}/unregister
def test_unregister_from_activity():
    # Arrange
    url = "/activities/Chess%20Club/unregister?email=test@example.com"

    # Act
    response = client.delete(url)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered test@example.com from Chess Club"