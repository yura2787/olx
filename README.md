# AI Code Assistant Bot

Telegram бот для аналізу коду на базі Claude AI.

## Структура

```
code-assistant-bot/
├── bot/
│   ├── handlers/
│   │   ├── start.py          # /start команда
│   │   ├── code_review.py    # пошук багів
│   │   ├── explain.py        # пояснення коду
│   │   └── optimize.py       # оптимізація коду
│   ├── services/
│   │   └── claude_client.py  # Claude API клієнт
│   ├── keyboards/
│   │   └── inline.py         # inline кнопки
│   ├── middlewares/
│   │   └── rate_limiter.py   # захист від спаму
│   ├── utils/
│   │   └── code_parser.py    # визначення мови коду
│   └── main.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── .env
```

## Запуск

```bash
cp .env.example .env
# заповни BOT_TOKEN і ANTHROPIC_API_KEY в .env

pip install -r requirements.txt
python -m bot.main
```

## Docker

```bash
docker compose up -d
```
