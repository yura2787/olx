from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🐛 Знайти баги", callback_data="review"),
            InlineKeyboardButton(text="✨ Покращити код", callback_data="improve"),
        ],
        [
            InlineKeyboardButton(text="📖 Пояснити код", callback_data="explain"),
            InlineKeyboardButton(text="⚡ Оптимізувати", callback_data="optimize"),
        ],
    ])
