from db_api.body_formulator import RequestBodyFormulator
from db_api.database_api import perform_request
from keyboards.utils.output_formulator import format_sizes, format_message
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class NameState(StatesGroup):
    name = State()


@dp.message_handler(commands="model_by_name")
async def get_name(message: types.Message):
    await message.reply("Type in the name of the model you want to find...")
    await NameState.name.set()


@dp.message_handler(state=NameState.name)
async def get_model_availability_by_name(message: types.Message, state: FSMContext):
    message_text = ' '.join(message.text.split())
    body_by_name_request = RequestBodyFormulator.form_by_name(message_text)
    response = perform_request(body_by_name_request)
    if not response:
        await message.answer("No models found😢...")
    else:
        for found_model in response:
            caption = format_message(found_model)

            await message.answer_photo(found_model["image"], caption=caption, parse_mode="Markdown")
    print("Response: ", response)
    await state.finish()
