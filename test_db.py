import pytest
from db import establish_db_connection, create_tables


def test_establish_db_connection():
    conn = establish_db_connection()
    assert conn is not None


def test_create_tables():
    create_tables()
