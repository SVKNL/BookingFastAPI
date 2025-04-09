# from fastapi import HTTPException
# import pytest
#
# from .conftest import client
#
#
#
# def test_table_unique_name(create_table):
#     response = create_table
#     new_table = {"name": "Test Table", "seats": 4, 'location': 'San Francisco'}
#     with pytest.raises(HTTPException):
#         client.post("/tables/", json=new_table)
