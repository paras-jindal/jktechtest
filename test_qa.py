import pytest
from qa import answer_question, fetch_embeddings_from_db


@pytest.mark.asyncio
async def test_answer_question():
    question = "What is AI?"
    answer = await answer_question(question)
    assert answer is not None


@pytest.mark.asyncio
async def test_fetch_embeddings_from_db():
    question = "What is AI?"
    embeddings = await fetch_embeddings_from_db(question)
    assert len(embeddings) > 0
