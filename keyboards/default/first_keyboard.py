from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💬 Fikr bildirish 💬"),
        ],
    ],
    resize_keyboard=True,
)