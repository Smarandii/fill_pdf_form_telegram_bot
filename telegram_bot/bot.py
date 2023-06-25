from telegram_bot import bot, dp
from aiogram import types
from form_ar_11 import Form_AR_11
from aiogram.dispatcher import FSMContext, filters
from telegram_bot import AvailableFormsKeyboardFactory
import form_ar_11_handlers


@dp.message_handler(filters.Command("start"))
async def start_cmd_handler(message: types.Message):
    keyboard_factory = AvailableFormsKeyboardFactory()
    keyboard = keyboard_factory.keyboard_markup
    await message.answer("Hello! Here are the forms available for filling:", reply_markup=keyboard)


@dp.callback_query_handler(text="I-589")
async def i_589_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-589"
    await bot.send_message(callback_query.from_user.id, "You've chosen the I-589 form. Let's start filling it.")
    await bot.send_message(callback_query.from_user.id, "Enter your Family Name:")
    await Form_AR_11.S1_FamilyName.set()


async def on_startup(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been stopped')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
