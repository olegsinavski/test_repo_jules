from fastapi.testclient import TestClient
# Ensure 'main' is resolvable, adjust if your FastAPI app instance is named differently or located elsewhere
# If main.py is in the same directory (backend) and app is named 'app':
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}


def test_get_greetings():
    response = client.get("/api/greetings")
    assert response.status_code == 200
    # The exact greetings can be checked if they are stable,
    # or just the structure and type.
    data = response.json()
    assert "greetings" in data
    assert isinstance(data["greetings"], list)
    assert len(data["greetings"]) > 0 # Ensure it's not an empty list
    # Example of checking specific content if desired:
    # assert data["greetings"] == ["Hello from FastAPI!", "Hola desde FastAPI!", "Bonjour de FastAPI!"]
