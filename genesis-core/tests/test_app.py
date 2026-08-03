from fastapi.testclient import TestClient

from genesis_core.main import app

API_ENDPOINT = "/api/v1"

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    # Since no routes are explicitly defined yet, a 404 or a basic response is expected.
    # Let's ensure the app can be initialized and tested via TestClient.
    assert response.status_code in (200, 404)
    assert response.text == "Welcome to Genesis!"


def test_health_check():
    response = client.get(f"{API_ENDPOINT}/status")
    assert response.text == "OK"
    assert response.status_code == 200
