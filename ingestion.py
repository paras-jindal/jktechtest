import openai
import psycopg2
from db import establish_db_connection
import asyncio


async def process_and_store_document(document):
    embeddings = await asyncio.to_thread(generate_embeddings, document)

    await asyncio.to_thread(store_embeddings, document, embeddings)

    return document["id"]


async def generate_embeddings(document):
    local_url = "http://localhost:1234/v1/generate-embeddings"
    response = openai.Embedding.create(
        url=local_url, input=document["content"], model="text-embedding-ada-002"
    )
    return response["data"][0]["embedding"]


async def store_embeddings(document, embeddings):
    conn = establish_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO documents (id, content, embeddings) VALUES (%s, %s, %s)",
        (document["id"], document["content"], embeddings),
    )
    conn.commit()
    cursor.close()
    conn.close()
