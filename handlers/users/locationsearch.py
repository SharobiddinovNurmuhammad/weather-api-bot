from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.defaultbtn import locationbtn
from utils import weathers
from loader import dp

@dp.message_handler(commands='mylocation')
async def get_location(message: types.Message):
    await message.answer("Joylashuvingizni yuboring:", reply_markup=locationbtn)

@dp.message_handler(content_types='location')
async def locationstart(message: types.Message):
    lat = message['location']['latitude']
    lon = message['location']['longitude']
    msg = await weathers.weather_location(lat, lon)
    await message.answer(msg, reply_markup=ReplyKeyboardRemove(True))
