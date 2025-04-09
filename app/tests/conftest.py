from fastapi.testclient import TestClient
import pytest

from app.main import app


client = TestClient(app)

@pytest.fixture
def create_table():
    new_table = {"name": "Test Table", "seats": 4, 'location': 'San Francisco'}
    response = client.post("/tables/", json=new_table)
    yield response
    table_id = response.json().get("id")
    if table_id:
        client.delete(f"/tables/{table_id}")


@pytest.fixture
def create_reservation(create_table):
    table_id = create_table.json()["id"]
    new_reservation = {"table_id": table_id, "customer_name": "John Doe",
                       "reservation_time": "2026-10-01T18:00:00",
                       'duration_minutes': 30}
    response = client.post("/reservations/", json=new_reservation)
    yield response
    table_id = response.json().get("table_id")
    reservation_id = response.json().get("id")
    if table_id and reservation_id:
        client.delete(f"/reservations/{reservation_id}")
        client.delete(f"/tables/{table_id}")
