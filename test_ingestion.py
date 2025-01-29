import pytest
from ingestion import process_and_store_document


@pytest.mark.asyncio
async def test_process_and_store_document():
    document = {"id": 1, "content": "Sample document content"}
    document_id = await process_and_store_document(document)
    assert document_id == document["id"]
