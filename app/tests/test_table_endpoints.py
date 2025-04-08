import requests
import pytest

BASE_URL = "http://localhost:8000"


@pytest.fixture
def create_table():
    new_table = {"name": "Test Table", "seats": 4, 'location': 'San Francisco'}
    response = requests.post(f"{BASE_URL}/tables/", json=new_table)
    return response.json()

def test_get_tables():
    response = requests.get(f"{BASE_URL}/tables/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_table():
    new_table = {"name": "Table 1", "seats": 4, 'location': 'San Francisco'}
    response = requests.post(f"{BASE_URL}/tables/", json=new_table)
    assert response.status_code == 200
    assert "id" in response.json()


def test_delete_table(create_table):
    table_id = create_table["id"]

    delete_response = requests.delete(f"{BASE_URL}/tables/{table_id}")
    assert delete_response.status_code == 200

    get_response = requests.delete(f"{BASE_URL}/tables/{table_id}")
    assert get_response.status_code == 404