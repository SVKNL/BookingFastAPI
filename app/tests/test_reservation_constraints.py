import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.fixture
def create_reservation():
    new_reservation = {"table_id": 2, "customer_name": "John Doe", "reservation_time": "2023-10-01T18:00:00", 'duration_minutes': 30}
    response = requests.post(f"{BASE_URL}/reservations/", json=new_reservation)
    return response.json()