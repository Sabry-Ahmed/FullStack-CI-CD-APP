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

def test_insert_data(client):
    response = client.post('/api/insert', json={'name': 'TestUser'})
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert 'message' in data
    assert data['message'] == 'User inserted successfully!'

def test_delete_data(client):
    # Assuming there's a user named 'TestUser' in the database
    response = client.post('/api/delete', json={'name': 'TestUser'})
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert 'message' in data
    assert data['message'] == 'User deleted successfully!'

def test_delete_nonexistent_user(client):
    response = client.post('/api/delete', json={'name': 'NonExistentUser'})
    assert response.status_code == 500
    data = json.loads(response.get_data(as_text=True))
    assert 'message' in data
    assert data['message'] == 'Failed to delete user.'


