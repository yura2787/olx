from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from bot.services.claude_client import groq_client
from bot.keyboards.inline import back_button
from bot.utils.code_parser import extract_code, detect_language
from config import MAX_CODE_LENGTH

router = Router()


class ReviewStates(StatesGroup):
    waiting_for_code = State()


@router.callback_query(F.data == "review")
async def ask_for_code(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text(
        "🐛 Надішли код — знайду баги та проблеми.",
        reply_markup=back_button(),
    )
    await state.set_state(ReviewStates.waiting_for_code)
    await callback.answer()


@router.message(ReviewStates.waiting_for_code)
async def handle_code(message: Message, state: FSMContext) -> None:
    code, hint = extract_code(message.text or "")

    if not code:
        await message.answer("❌ Код не знайдено. Надішли текст або блок коду.", reply_markup=back_button())
        return

    if len(code) > MAX_CODE_LENGTH:
        await message.answer(f"❌ Код занадто довгий (максимум {MAX_CODE_LENGTH} символів).", reply_markup=back_button())
        return

    await state.clear()
    lang = detect_language(code, hint)
    status = await message.answer("🔍 Аналізую код...")

    try:
        result = await groq_client.review_code(code, lang)
        await status.edit_text(result, reply_markup=back_button())
    except Exception:
        await status.edit_text("❌ Помилка при зверненні до AI. Спробуй ще раз.", reply_markup=back_button())
