from fastapi.testclient import TestClient

from app.main import app


def test_root_returns_name_and_version() -> None:
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"]
    assert body["version"]


def test_healthz_ok() -> None:
    client = TestClient(app)
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

