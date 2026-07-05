# AI Code Assistant Bot

A Telegram bot that reviews, explains, and improves code using Groq AI (Llama 3.3 70B).

## Features

- 🐛 **Bug Review** — finds bugs, security issues, and potential problems
- ✨ **Code Improvement** — suggests better structure and quality
- 📖 **Explain Code** — breaks down what the code does in plain English
- ⚡ **Optimize** — improves performance and readability
- 🛡️ **Rate Limiting** — protects against spam (5 requests / 60s per user)
- 🌐 **Auto Language Detection** — supports Python, JS, TS, Go, Rust, Java, SQL, HTML, CSS

## Tech Stack

- **Python 3.13**
- **aiogram 3** — Telegram bot framework
- **Groq API** — LLM inference (Llama 3.3 70B)
- **Docker** — containerized deployment
- **uv** — package management

## Project Structure

```
├── bot/
│   ├── handlers/
│   │   ├── start.py          # /start command and back navigation
│   │   ├── code_review.py    # bug finder
│   │   ├── explain.py        # code explainer
│   │   ├── optimize.py       # optimizer
│   │   └── improve.py        # code improver
│   ├── services/
│   │   └── claude_client.py  # Groq API client
│   ├── keyboards/
│   │   └── inline.py         # inline keyboards
│   ├── middlewares/
│   │   └── rate_limiter.py   # request rate limiting
│   ├── utils/
│   │   └── code_parser.py    # language detection and code extraction
│   └── main.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── .env.example
```

## Setup

```bash
git clone <repo-url>
cd code-assistant-bot

cp .env.example .env
# fill in BOT_TOKEN and GROQ_API_KEY in .env

uv sync
uv run python -m bot.main
```

## Docker

```bash
docker compose up -d --build
docker compose logs -f
```

## Environment Variables

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Telegram bot token from [@BotFather](https://t.me/BotFather) |
| `GROQ_API_KEY` | Groq API key from [console.groq.com](https://console.groq.com) |
| `RATE_LIMIT_REQUESTS` | Max requests per window (default: 5) |
| `RATE_LIMIT_WINDOW` | Time window in seconds (default: 60) |
