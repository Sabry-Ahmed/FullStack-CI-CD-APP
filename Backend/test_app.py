import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert 'data' in data
    assert isinstance(data['data'], list)


