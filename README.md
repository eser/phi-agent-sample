# Web Content Fetcher

This project was created during Emre Savci's Go Turkiye broadcast, which can be viewed at [YouTube](https://www.youtube.com/watch?v=qa_GRqWK9pY).

## About

A simple Python application that demonstrates fetching web content using the phi library and OpenAI's GPT-4 model. The application retrieves content from a specified URL and saves it to a local file.

## Features

- Fetches web content using HTTP GET requests
- Writes content to local files
- Uses OpenAI's GPT-4 for processing
- Includes error handling for network requests

## Requirements

- Python 3.9+
- phi library
- OpenAI API key
- Poetry for dependency management

## Usage

Run the main script:

```bash
python main.py
```

This will fetch the content from the specified URL and save it to a file named `output.txt`.
