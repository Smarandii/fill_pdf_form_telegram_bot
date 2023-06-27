from aiogram import types
from aiogram.dispatcher import FSMContext, filters
from form_i_589 import Form_I_589
from telegram_bot import bot, dp, FillPdfFromJsonAdapter, datetime


@dp.callback_query_handler(text="I-589")
async def i_589_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-589"
    await bot.send_message(callback_query.from_user.id, "You've chosen the I-589 form. Let's start filling it.")
    # await bot.send_message(callback_query.from_user.id, "Enter your Family Name:")
    # await Form_AR_11.S1_FamilyName.set()