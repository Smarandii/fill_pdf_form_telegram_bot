from aiogram.dispatcher import FSMContext

from telegram_bot import bot, dp, types, filters, AvailableFormsKeyboard
from phrases import START_PHRASE
from telegram_bot.form_i_485.form_i_485_state_group import FormI485


@dp.message_handler(filters.Command("start"), state="*")
async def start_cmd_handler(message: types.Message):
    keyboard = AvailableFormsKeyboard()
    keyboard = keyboard.keyboard_markup
    await message.answer(START_PHRASE, reply_markup=keyboard)


@dp.message_handler(filters.Command("jump"), state="*")
async def jump_cmd_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-485"
    command, state = message.text.split()

    state = FormI485.__getattribute__(FormI485, state)

    await state.set()
    await message.answer("Я прыгнул, напиши что-нибудь:")

from form_ar_11 import form_ar_11_handlers
from form_i_589 import form_i_589_handlers
from form_i_765 import form_i_765_handlers
from form_i_485 import form_i_485_handlers

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


