# Simple Chatbot

This is a minimal CLI chatbot that uses OpenAI's Chat Completions API through the current OpenAI Python SDK. If no `OPENAI_API_KEY` is found in the environment, the chatbot uses a simple local fallback.

Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r chatbot/requirements.txt
```

2. Set your OpenAI API key (optional — without it the bot uses a fallback):

```bash
export OPENAI_API_KEY="sk-..."
```

3. Run the CLI:

```bash
python chatbot/run_chatbot.py
```

Notes:
- The bot preserves a running conversation in memory (no persistence).
- To clear history restart the program or call `reset()` in code.
