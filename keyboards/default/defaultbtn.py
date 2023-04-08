from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

locationbtn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📌Lokatsiya", request_location=True)
        ]
    ]
)
