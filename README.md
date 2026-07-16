# LangChain AI Project

## Overview

This repository contains a LangChain-based AI chatbot project with modular folders for UI, embeddings, model logic, and bot orchestration.

## Repository structure

- `ChatModel/`
  - Streamlit interface and main chat application
  - `UIChatbot.py` is the front-end app file

- `EmbeddingModel/`
  - Embedding generation and vector search utilities
  - Contains code for building embeddings used by the assistant

- `LLM/`
  - Language model integration logic
  - Wrappers and helpers for calling Mistral, OpenAI, or other LLM providers

- `MTBot/`
  - Multi-turn bot behavior and agent orchestration
  - Implements chat flow, session state, and response handling

- `requirements.txt`
  - Python dependency list for reproducing the environment
  - Install with `pip install -r requirements.txt`

- `.gitignore`
  - Ignore local environment files and caches
  - Includes `venv/`, `.env`, `__pycache__/`, and related files

- `.env`
  - Local environment variables file
  - Contains API keys and secrets
  - Do not commit this file

- `venv/`
  - Local Python virtual environment
  - Should remain local and is excluded from Git

## What this project does

- Builds a chat assistant UI with Streamlit
- Uses LangChain for model orchestration
- Supports embeddings and memory for chat context
- Connects to external LLMs via API keys stored in `.env`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/priteshbeladiya07/langchain.git
   cd langchain
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```text
   MISTRAL_API_KEY=your_api_key_here
   ```

5. Run the app:
   ```bash
   streamlit run ChatModel/UIChatbot.py
   ```

## Notes

- `venv/` is local only and should not be pushed.
- `.env` is for secrets and should not be tracked.
- Review `requirements.txt` before installing.
