from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from bot.services.claude_client import ClaudeClient
from bot.utils.code_parser import extract_code, detect_language
from config import MAX_CODE_LENGTH

router = Router()
claude = ClaudeClient()


class OptimizeStates(StatesGroup):
    waiting_for_code = State()


@router.callback_query(F.data == "optimize")
async def ask_for_code(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text("⚡ Надішли код — оптимізую продуктивність та читабельність.")
    await state.set_state(OptimizeStates.waiting_for_code)
    await callback.answer()


@router.message(OptimizeStates.waiting_for_code)
async def handle_code(message: Message, state: FSMContext) -> None:
    code = extract_code(message.text or "")

    if not code:
        await message.answer("❌ Код не знайдено. Надішли текст або блок коду.")
        return

    if len(code) > MAX_CODE_LENGTH:
        await message.answer(f"❌ Код занадто довгий (максимум {MAX_CODE_LENGTH} символів).")
        return

    await state.clear()
    lang = detect_language(code)
    status = await message.answer("⚡ Оптимізую...")

    result = await claude.optimize_code(code, lang)
    await status.edit_text(result)
