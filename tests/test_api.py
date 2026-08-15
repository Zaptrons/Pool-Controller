from fastapi.testclient import TestClient

from src.api.api_server import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "project": "Pool Controller",
        "status": "Running"
    }


def test_motor_initial_status():
    response = client.get("/motor/status")

    assert response.status_code == 200
    assert response.json() == {
        "running": False
    }


def test_motor_on():
    response = client.post("/motor/on")

    assert response.status_code == 200
    assert response.json() == {
        "motor": "ON"
    }

    status_response = client.get("/motor/status")

    assert status_response.json() == {
        "running": True
    }


def test_motor_off():
    response = client.post("/motor/off")

    assert response.status_code == 200
    assert response.json() == {
        "motor": "OFF"
    }

    status_response = client.get("/motor/status")

    assert status_response.json() == {
        "running": False
    }


def test_dashboard():
    response = client.get("/dashboard")

    assert response.status_code == 200
    assert "Pool Controller" in response.text
    assert "TURN ON" in response.text
    assert "TURN OFF" in response.text