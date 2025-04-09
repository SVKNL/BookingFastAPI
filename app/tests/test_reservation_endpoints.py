import pytest

from .conftest import client



def test_get_reservations():
    response = client.get("/reservations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_reservation(create_reservation):
    response = create_reservation
    assert response.status_code == 200
    assert response.json()['customer_name'] == 'John Doe'


def test_delete_reservation(create_reservation):
    reservation_id = create_reservation.json()['id']

    delete_response = client.delete(f"/reservations/{reservation_id}")
    assert delete_response.status_code == 200

    get_response = client.delete(f"/reservations/{reservation_id}")
    assert get_response.status_code == 404