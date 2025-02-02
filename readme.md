# Project Title

This project is all about using local LLMs for answering questions and processing documents.

## Features

- Upload documents and store them in a database.
- Ask questions and get answers based on the documents you uploaded.
- Uses local LLMs so you don't need to worry about API keys and stuff.

## Getting Started

1. Clone the repo
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your local LLM server.
4. Run the app:
   ```bash
   python app.py
   ```

## Usage

You can use the `/upload-document` endpoint to upload your documents. Then, you can ask questions using the `/ask-question` endpoint.

## API Endpoints

- **POST /upload-document**
  - Description: Uploads a document to the server.
  - Request Body: 
    - `file`: The document file to upload.
  - Response: 
    - `200 OK`: Document uploaded successfully.
    - `400 Bad Request`: Invalid file format.

- **POST /ask-question**
  - Description: Asks a question based on the uploaded documents.
  - Request Body: 
    - `question`: The question to ask.
  - Response: 
    - `200 OK`: Answer to the question.
    - `404 Not Found`: No documents found.

## Testing Instructions with pytest

To run the tests using pytest, first ensure that pytest is installed. You can install it using pip:
```bash
pip install pytest
```

To run the tests, use the following command:
```bash
pytest
```


To run the tests, use the following command:
```bash
python -m unittest discover -s tests
```

## Docker Instructions

To build and run the Docker container, use the following commands:
```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
```
