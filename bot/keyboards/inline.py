from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🐛 Find Bugs", callback_data="review"),
            InlineKeyboardButton(text="✨ Improve Code", callback_data="improve"),
        ],
        [
            InlineKeyboardButton(text="📖 Explain Code", callback_data="explain"),
            InlineKeyboardButton(text="⚡ Optimize", callback_data="optimize"),
        ],
    ])


def back_button() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Back", callback_data="back")],
    ])
