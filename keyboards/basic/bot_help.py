"""
The second command commonly invoked in a Telegram bot is the 'help' command.
Whenever you add a new command, ensure to include it here as well.

Maintain consistency: list commands here in the same sequence as in 'set_bot_commands.py',
begin every description with the same capitalization as previous commands,
and omit any punctuation if previous commands do not include it.

Remember, the 'help' command is crucial for every Telegram bot.
Make sure to update this documentation whenever you introduce a new command.
"""
from aiogram import types
from loader import dp


@dp.message_handler(commands="help")
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - start bot👟",
            "/help - retrieve list of commands🗒",
            "/model_by_article - get list of available sizes by article",
            "/model_by_name - get list of available models and sizes by name",
            )
    await message.answer("\n".join(text))