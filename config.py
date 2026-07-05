from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN: str = os.environ["BOT_TOKEN"]
ANTHROPIC_API_KEY: str = os.environ["ANTHROPIC_API_KEY"]
RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "5"))
RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))
CLAUDE_MODEL: str = "claude-opus-4-8"
MAX_CODE_LENGTH: int = 10_000
