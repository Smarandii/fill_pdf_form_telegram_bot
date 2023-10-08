from aiogram.dispatcher import FSMContext

from telegram_bot import bot, dp, types, filters, AvailableFormsKeyboard
from phrases import START_PHRASE
from telegram_bot.form_ar_11.form_ar_11_state_group import Form_AR_11
from telegram_bot.form_i_131.form_i_131_state_group import FormI131
from telegram_bot.form_i_485.form_i_485_state_group import FormI485
from telegram_bot.form_i_589.form_i_589_state_group import Form_I_589
from telegram_bot.form_i_765.form_i_765_state_group import FormI765


@dp.message_handler(filters.Command("start"), state="*")
async def start_cmd_handler(message: types.Message):
    keyboard = AvailableFormsKeyboard()
    keyboard = keyboard.keyboard_markup
    await message.answer(START_PHRASE, reply_markup=keyboard)


@dp.message_handler(filters.Command("jump"), state="*")
async def jump_cmd_handler(message: types.Message, state: FSMContext):
    command, form, form_state = message.text.split()
    async with state.proxy() as data:
        data['form_identifier'] = form.upper()
    if form.upper() == "I-485":
        form_state = FormI485.__getattribute__(FormI485, form_state)
    if form.upper() == "I-131":
        form_state = FormI131.__getattribute__(FormI131, form_state)
    if form.upper() == "I-589":
        form_state = Form_I_589.__getattribute__(Form_I_589, form_state)
    if form.upper() == "I-765":
        form_state = FormI765.__getattribute__(FormI765, form_state)
    if form.upper() == "AR-11":
        form_state = Form_AR_11.__getattribute__(Form_AR_11, form_state)

    await form_state.set()
    await message.answer("Я прыгнул, напиши что-нибудь:")

from form_ar_11 import form_ar_11_handlers
from form_i_589 import form_i_589_handlers
from form_i_765 import form_i_765_handlers
from form_i_485 import form_i_485_handlers
from form_i_131 import form_i_131_handlers

async def on_startup(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been stopped')

if __name__ == '__main__':
    from aiogram import executor
    while True:
        try:
            executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
        except Exception as e:
            bot.send_message(chat_id=231584958, text=f'{e.args[0]} | {e.args}')


