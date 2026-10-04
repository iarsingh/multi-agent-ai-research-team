from fastapi.testclient import TestClient
from maresearch2.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'plan a literature note', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert len(payload["roles"]) == 3
    refused = client.post("/agent/run", json={"goal": 'email the VP'}).json()
    assert refused["refused"] is True
