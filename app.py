from flask import Flask, request, jsonify
from ingestion import process_and_store_document
from qa import answer_question
from db import create_tables
import asyncio

app = Flask(__name__)

create_tables()


@app.route("/upload-document", methods=["POST"])
async def ingest():
    data = request.json
    try:
        document_id = await asyncio.to_thread(
            process_and_store_document, data["document"]
        )
        return jsonify({"document_id": document_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/ask-question", methods=["POST"])
async def qa():
    data = request.json
    try:
        answer = await asyncio.to_thread(answer_question, data["question"])
        return jsonify({"answer": answer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
