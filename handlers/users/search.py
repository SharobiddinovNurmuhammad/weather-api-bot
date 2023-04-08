import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from utils import weathers
from loader import dp, bot

@dp.message_handler(Command('search')) # /qidiruv
async def search_bot(message: types.Message, state: FSMContext):
    await message.answer("🔍Qidirayotgan joyingiz nomini kiriting: ")
    await state.set_state('searchstate')

@dp.message_handler(state='searchstate')
async def get_search(message: types.Message, state: FSMContext):
    search_icon = await bot.send_message(chat_id=message.from_user.id, text='🔍')
    try:
        await asyncio.sleep(3)
        await search_icon.delete()
        msg = await weathers.weatherbot(message.text)
        await message.reply(msg)
    except:
        await asyncio.sleep(3)
        await search_icon.delete()
        await message.answer('Natija topilmadi! :)')
    await state.finish()