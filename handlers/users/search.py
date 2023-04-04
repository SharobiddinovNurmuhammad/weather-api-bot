from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from utils import weathers
from loader import dp

@dp.message_handler(Command('search')) # /qidiruv
async def search_bot(message: types.Message, state: FSMContext):
    await message.answer("🔍Qidirayotgan shaharingiz nomini kiriting: ")
    await state.set_state('searchstate')

@dp.message_handler(state='searchstate')
async def get_search(message: types.Message, state: FSMContext):
    try:
        msg = await weathers.weatherbot(message.text)
        await message.reply(msg)
    except:
        await message.answer('Natija topilmadi! :)')
    await state.finish()