# Project Title

This project is all about using local LLMs for answering questions and processing documents.

## Features

- Upload documents and store them in a database.
- Ask questions and get answers based on the documents you uploaded.
- Uses local LLMs so you dont need to worry about API keys and stuff.

## Getting Started

1. Clone the repo
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Set up your local LLM server.
4. Run the app:
   ```
   python app.py
   ```

## Usage

You can use the `/upload-document` endpoint to upload your documents. Then, you can ask questions using the `/ask-question` endpoint. 

## Note

Make sure to have your local LLM running before you try to use the app.In my case i am running LLama 3.2 in LM studio If you have any issues, just check the code and see if you can figure it out. 
