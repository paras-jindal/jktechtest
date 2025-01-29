import openai
from db import establish_db_connection
import asyncio


async def answer_question(question):
    embeddings = await asyncio.to_thread(fetch_embeddings_from_db, question)
    answer = await asyncio.to_thread(generate_answer, question, embeddings)
    return answer


async def fetch_embeddings_from_db(question):
    conn = establish_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT embeddings FROM documents WHERE content ILIKE %s",
        ("%" + question + "%",),
    )
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return [result[0] for result in results]


def generate_answer(question, embeddings):
    local_url = "http://localhost:1234/v1/chat/completions"
    response = openai.ChatCompletion.create(
        url=local_url,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
            {"role": "system", "content": str(embeddings)},
        ],
    )
    return response["choices"][0]["message"]["content"]
