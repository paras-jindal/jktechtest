import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_upload_document(client):
    response = client.post(
        "/upload-document",
        json={"document": {"id": 1, "content": "Sample document content"}},
    )
    assert response.status_code == 201
    assert "document_id" in response.get_json()


def test_ask_question(client):
    response = client.post("/ask-question", json={"question": "What is AI?"})
    assert response.status_code == 200
    assert "answer" in response.get_json()
