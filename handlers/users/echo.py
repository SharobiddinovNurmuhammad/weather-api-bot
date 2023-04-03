from aiogram import types

from loader import dp

from utils import weathers

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer('Menyudan shaharni tanlang!')
    # try:
    #     msg = await weathers.weatherbot(message.text)
    #     await message.reply(msg)
    # except:
    #     await message.answer('Natija topilmadi! :)')