from telegram_bot import bot, dp
from aiogram import types
from aiogram.dispatcher import filters
from telegram_bot import AvailableFormsKeyboard


@dp.message_handler(filters.Command("start"))
async def start_cmd_handler(message: types.Message):
    keyboard = AvailableFormsKeyboard()
    keyboard = keyboard.keyboard_markup
    await message.answer("Hello! Here are the forms available for filling:", reply_markup=keyboard)


async def on_startup(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been stopped')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
