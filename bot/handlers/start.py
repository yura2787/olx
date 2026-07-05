from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline import main_menu

router = Router()

MAIN_TEXT = "👋 Hi! I'm a code review bot powered by Groq AI.\n\nWhat do you want to do with your code?"


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(MAIN_TEXT, reply_markup=main_menu())


@router.callback_query(F.data == "back")
async def go_back(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.edit_text(MAIN_TEXT, reply_markup=main_menu())
    await callback.answer()
