import pytest

from .conftest import client


def test_up_to_date_reservation(create_table):
    table_id = create_table.json()['id']
    new_reservation = {"table_id": table_id, "customer_name": "Jane Doe",
                       "reservation_time": "2023-10-01T19:00:00",
                       'duration_minutes': 30}

    response = client.post("/reservations/", json=new_reservation)
    assert response.status_code == 400
    assert response.json()['detail'] == "Reservation time is in the past"



def test_upper_crossing_reservation(create_reservation):
    table_id = create_reservation.json()['table_id']
    new_reservation = {"table_id": table_id, "customer_name": "Jane Doe",
                       "reservation_time": "2026-10-01T17:50:00",
                       'duration_minutes': 30}

    response = client.post("/reservations/", json=new_reservation)
    assert response.status_code == 400
    assert response.json()['detail'] == "Table is booked at this time"



def test_lower_crossing_reservation(create_reservation):
    table_id = create_reservation.json()['table_id']
    new_reservation = {"table_id": table_id, "customer_name": "Jane Doe",
                       "reservation_time": "2026-10-01T18:20:00",
                       'duration_minutes': 30}

    response = client.post("/reservations/", json=new_reservation)
    assert response.status_code == 400
    assert response.json()['detail'] == "Table is booked at this time"