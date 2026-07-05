import time
from collections import defaultdict
from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from config import RATE_LIMIT_REQUESTS, RATE_LIMIT_WINDOW


class RateLimitMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self._requests: dict[int, list[float]] = defaultdict(list)

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        if not event.from_user:
            return await handler(event, data)

        user_id = event.from_user.id
        now = time.monotonic()

        self._requests[user_id] = [
            t for t in self._requests[user_id] if now - t < RATE_LIMIT_WINDOW
        ]

        if len(self._requests[user_id]) >= RATE_LIMIT_REQUESTS:
            wait = int(RATE_LIMIT_WINDOW - (now - self._requests[user_id][0]))
            await event.answer(f"⏳ Забагато запитів. Зачекай {wait} сек.")
            return

        self._requests[user_id].append(now)
        return await handler(event, data)
