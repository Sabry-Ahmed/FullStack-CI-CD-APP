import pytest
import requests
from unittest.mock import patch
from streamlit_app import fetch_data, insert_user, delete_user

sample_data = [{"nom": "User1"}, {"nom": "User2"}]

# Mock responses for API calls
class MockResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json_data = json_data

    def json(self):
        return self._json_data

# Mocking API calls
def mock_get(*args, **kwargs):
    return MockResponse(200, {"data": sample_data})

def mock_post(*args, **kwargs):
    return MockResponse(200)

def mock_failed_post(*args, **kwargs):
    return MockResponse(500)

# Fixture to patch requests.get and requests.post
@pytest.fixture
def patch_requests():
    with patch("requests.get", side_effect=mock_get), \
         patch("requests.post", side_effect=mock_post):
        yield

# Tests
def test_fetch_data(patch_requests, capsys):
    fetch_data()
    captured = capsys.readouterr()
    assert "Data from the database:" in captured.out
    assert "User1" in captured.out
    assert "User2" in captured.out

def test_insert_user(patch_requests, capsys):
    insert_user("NewUser")
    captured = capsys.readouterr()
    assert "User NewUser inserted successfully!" in captured.out

def test_delete_user(patch_requests, capsys):
    delete_user("UserToDelete")
    captured = capsys.readouterr()
    assert "User UserToDelete deleted successfully!" in captured.out
    assert "Failed to delete user." not in captured.out  


def test_failed_delete_user(patch_requests, capsys):
    # Mock a failed delete request
    with patch("requests.post", side_effect=mock_failed_post):
        delete_user("NonExistentUser")
    captured = capsys.readouterr()
    assert "Failed to delete user." in captured.out
