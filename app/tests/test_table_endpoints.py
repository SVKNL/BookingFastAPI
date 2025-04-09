import pytest

from .conftest import client



def test_get_tables():
    response = client.get("/tables/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_table(create_table):
    response = create_table
    assert response.status_code == 200
    assert response.json()['name'] == 'Test Table'


def test_delete_table(create_table):
    table_id = create_table.json()['id']
    delete_response = client.delete(f"/tables/{table_id}")
    assert delete_response.status_code == 200
    get_response = client.delete(f"/tables/{table_id}")
    assert get_response.status_code == 404