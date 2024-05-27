from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мои пари"), KeyboardButton(text="Добавить пари")]
    ],
    resize_keyboard=False
)

