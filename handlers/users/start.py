from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menukeyboards import menubtn, backbtn
from utils import weathers
from loader import dp


@dp.message_handler(CommandStart())
@dp.message_handler(commands='menu')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"\
                         f"Ob-Xavo ma'lumotlarini bilish uchun joyni tanlang:", reply_markup=menubtn)

@dp.callback_query_handler()
async def weatherstart(call: types.CallbackQuery):
    if call.data == 'back':
        await call.message.answer(text="Shaharni tanlang:", reply_markup=menubtn)
        await call.message.delete()
    else:
        text = call.data
        msg = await weathers.weatherbot(text)
        await call.message.answer(msg, reply_markup=backbtn)
        await call.message.delete()
        