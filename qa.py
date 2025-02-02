from ollama import chat
from ollama import ChatResponse
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


def generate_answer(question, embeddings=None):
    # Define the chat input
    messages = [
        {
            "role": "user",
            "content": question,
        },
    ]

    # If embeddings are provided, add them to the chat input
    if embeddings is not None:
        messages.append(
            {
                "role": "assistant",
                "content": embeddings,
            }
        )

    # Generate the response
    response: ChatResponse = chat(model="llama3.2", messages=messages)

    # Return the generated answer
    return response.message.content
