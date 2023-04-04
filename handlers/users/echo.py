from aiogram import types

from loader import dp

from utils import weathers

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer('Menyudan shaharni tanlang!')

