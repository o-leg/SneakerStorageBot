from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
            types.BotCommand("help", "Retrieve list of bot commands"),
            types.BotCommand("model_by_article", "Search for available models by article🖼🆑"),
            types.BotCommand("model_by_name", "Search for available models by name"),
        ]
    )