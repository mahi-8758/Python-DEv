# Gemini Chatbot

A terminal-based conversational AI chatbot powered by Google's Gemini 2.0 Flash model.

## Features

- **AI-Powered Conversations**: Chat with Google's advanced Gemini 2.0 Flash model
- **Multi-turn Dialogue**: Maintains conversation context across multiple messages
- **Terminal Interface**: Simple and interactive command-line chat experience
- **Error Handling**: Graceful error handling for API issues
- **Exit Command**: Easily exit the chat with the 'exit' command
- **Real-time Responses**: Get instant AI-generated responses

## Project Structure

- **`main.py`**: Entry point of the application that handles the chat interface
- **`api.py`**: Contains the Google Generative AI API key configuration

## How It Works

1. API key is loaded from `api.py`
2. Generative AI is configured with your API credentials
3. A chat session is initialized with the Gemini 2.0 Flash model
4. The application enters a loop waiting for user input
5. Each message is sent to Gemini, which processes and responds
6. The conversation context is maintained throughout the session
7. User can exit by typing 'exit'

## How to Run

```bash
python main.py
```

Then simply start typing your messages and press Enter to get responses from the AI.

## Example Output

```
=== TERMINAL BASED - GOOGLE GEMINI 2.0 ===
Type 'exit' to quit

You: What is Python?

AI: Python is a high-level, interpreted programming language known for its simplicity and readability...

You: Tell me about machine learning

AI: Machine learning is a subset of artificial intelligence that enables computers to learn from data...

You: exit
Goodbye!
```

## Requirements

- Python 3.x
- Google Generative AI library (`google-generativeai`)
- Valid Google Gemini API key (set in `api.py`)
- Internet connection for API calls

## Installation

```bash
pip install google-generativeai
```