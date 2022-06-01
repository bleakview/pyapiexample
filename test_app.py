# This file is for test
from fastapi.testclient import TestClient
from app import app
import pytest

jsonheaders = {'Content-Type': 'application/json'}


@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as client:
        yield client


def test_read_books(test_app):
    response = test_app.get(
        "/books",
        headers=jsonheaders,
    )
    assert response.status_code == 200
    assert response.json() == [{
        "name": "name",
        "id": "5d596c01-e20b-4049-91e9-a0be77715260",

        "author": "author",
        "isbn": "isbn",
        "release_year": 1980
    }]


def test_read_book(test_app):
    response = test_app.get(
        "/books/5d596c01-e20b-4049-91e9-a0be77715260",
        headers=jsonheaders,
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "5d596c01-e20b-4049-91e9-a0be77715260",
        "name": "name",
        "author": "author",
        "isbn": "isbn",
        "release_year": 1980
    }


def test_put_book(test_app):
    body = {
        "name": "name test",
        "author": "author test",
        "release_year": 1981,
        "isbn": "isbn test"
    }
    response = test_app.put(
        "/books/5d596c01-e20b-4049-91e9-a0be77715260",
        headers=jsonheaders,
        json=body,
    )
    assert response.status_code == 200
    response = test_app.get(
        "/books/5d596c01-e20b-4049-91e9-a0be77715260",
        headers=jsonheaders,
    )
    assert response.json() == {
        "id": "5d596c01-e20b-4049-91e9-a0be77715260",
        "name": "name test",
        "author": "author test",
        "release_year": 1981,
        "isbn": "isbn test"
    }


def test_post_book(test_app):
    body = {
        "name": "name test post",
        "author": "author test post",
        "release_year": 1982,
        "isbn": "isbn test post"
    }
    response = test_app.post(
        "/books",
        headers=jsonheaders,
        json=body,
    )
    assert response.status_code == 200
    response_id = response.json()["id"]
    response = test_app.get(
        "/books/"+response_id,
        headers=jsonheaders,
    )
    body["id"] = response_id
    assert response.json() == body
