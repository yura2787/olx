from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.inline import main_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        "👋 Привіт! Я бот для аналізу коду на базі Claude AI.\n\n"
        "Що хочеш зробити з кодом?",
        reply_markup=main_menu(),
    )
