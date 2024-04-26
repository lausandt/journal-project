from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Message': 'George is an async rhino, very lazy indeed!'}
