from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json() == {'status': 'ok'}

def test_network():
    r = client.get('/network')
    assert r.status_code == 200
    data = r.json()
    assert 'bytes_sent' in data
    assert 'bytes_recv' in data
    assert 'packets_sent' in data
    assert 'packets_recv' in data
    assert isinstance(data['bytes_sent'], int)
    assert isinstance(data['bytes_recv'], int)
