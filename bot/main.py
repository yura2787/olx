import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from bot.handlers import start, code_review, explain, optimize
from bot.middlewares.rate_limiter import RateLimitMiddleware

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.middleware(RateLimitMiddleware())

    dp.include_router(start.router)
    dp.include_router(code_review.router)
    dp.include_router(explain.router)
    dp.include_router(optimize.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
