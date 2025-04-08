import requests
import pytest

BASE_URL = "http://localhost:8000"


@pytest.fixture
def create_reservation():
    new_reservation = {"table_id": 2, "customer_name": "John Doe", "reservation_time": "2023-10-01T18:00:00", 'duration_minutes': 30}
    response = requests.post(f"{BASE_URL}/reservations/", json=new_reservation)
    return response.json()


def test_get_reservations():
    response = requests.get(f"{BASE_URL}/reservations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_reservation():
    new_reservation = {"table_id": 2, "customer_name": "Jane Doe", "reservation_time": "2023-10-01T19:00:00", 'duration_minutes': 30}
    response = requests.post(f"{BASE_URL}/reservations/", json=new_reservation)
    assert response.status_code == 200
    assert "id" in response.json()
    requests.delete(f"{BASE_URL}/reservations/{response.json()['id']}")


def test_delete_reservation(create_reservation):
    reservation_id = create_reservation["id"]

    delete_response = requests.delete(f"{BASE_URL}/reservations/{reservation_id}")
    assert delete_response.status_code == 200

    get_response = requests.delete(f"{BASE_URL}/reservations/{reservation_id}")
    assert get_response.status_code == 404