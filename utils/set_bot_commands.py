from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("search", "Qidiruv"),
            types.BotCommand("menu", "Bosh menu"),
            types.BotCommand("location search", "Joylashuv orqali qidiruv")
        ]
    )
