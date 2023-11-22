import os
import json
import logging
import aiofiles
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from phrases import START_PHRASE
from aiogram.dispatcher import FSMContext
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from telegram_bot import bot, dp, types, filters, AvailableFormsKeyboard, strapi_client
from telegram_bot.form_ar_11.form_ar_11_state_group import Form_AR_11
from telegram_bot.form_i_131.form_i_131_state_group import FormI131
from telegram_bot.form_i_485.form_i_485_state_group import FormI485
from telegram_bot.form_i_589.form_i_589_state_group import Form_I_589
from telegram_bot.form_i_765.form_i_765_state_group import FormI765
from flask import Flask, request

webhook_hosts = {"LOCAL": "https://a9f8-46-138-2-17.ngrok-free.app",
                 "PROD": "https://galleon-7f277686eddf.herokuapp.com"}
WEBHOOK_HOST = webhook_hosts[os.getenv('RUNNING_ENV', default="PROD")]

WEBHOOK_PATH = f'/webhook/{os.getenv("API_TOKEN")}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

hosts = {"LOCAL": "localhost", "PROD": "0.0.0.0"}

WEBAPP_HOST = hosts[os.getenv('RUNNING_ENV', default="PROD")]
WEBAPP_PORT = os.getenv('PORT', default=5000)

logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

app = Flask(__name__)


class Form(StatesGroup):
    main_menu = State()


def get_main_menu_keyboard():
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    btn_forms = InlineKeyboardButton('Формы', callback_data='forms')
    btn_info = InlineKeyboardButton('Информация', callback_data='info')
    keyboard_markup.add(btn_forms, btn_info)
    return keyboard_markup


def get_back_button():
    keyboard_markup = InlineKeyboardMarkup()
    btn_back = InlineKeyboardButton('Назад', callback_data='back')
    keyboard_markup.add(btn_back)
    return keyboard_markup


@dp.message_handler(commands=['start'], state="*")
async def start_cmd_handler(message: types.Message):
    await Form.main_menu.set()  # Set state to main menu
    keyboard = get_main_menu_keyboard()
    user = strapi_client.find_client(message.from_user.id)
    logger = logging.getLogger("START HANDLER")
    logger.info(f"Trying to find user, result: {user}")
    if user is None:
        strapi_client.save_client_to_strapi(message)
    await message.answer(
        "Привет! Добро пожаловать в главное меню.\n\n"
        "Для выбора формы к заполнению нажмите кнопку \"формы\". "
        "Для того, чтобы ознакомиться с информацией по подаче, нажмите кнопку \"информацию\".",
        reply_markup=keyboard
    )


@dp.callback_query_handler(Text(startswith='forms'), state=Form.main_menu)
async def handle_forms(callback_query: types.CallbackQuery):
    keyboard = AvailableFormsKeyboard()
    keyboard = keyboard.keyboard_markup
    await bot.send_message(callback_query.from_user.id, START_PHRASE, reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='info'), state=Form.main_menu)
async def handle_info(callback_query: types.CallbackQuery):
    keyboard = get_back_button()
    await bot.send_message(
        callback_query.from_user.id,
        "Информация:\n\n"
        "Кто мы?\n\n"
        "Мы - Galleon Legal Advice, сервис удобного заполнения и отправки иммиграционных форм.\n\n"
        "Какие услуги мы предоставляем?\n\n"
        "Мы предоставляем услуги по удобному, оперативному заполнению иммиграционных форм. "
        "Мы также предоставляем консультации по вопросам заполнения и отправки.\n\n"
        "Какая у нас модель оплаты?\n\n"
        "Мы берем предоплату в размере 50% от стоимости услуги на этапе отправки заполненной формы. "
        "После проверки формы и консультации по заполнению и отправке вы отправляете нам вторую часть суммы.\n\n"
        "Какие формы оплаты мы принимаем?\n\n"
        "Мы принимаем оплату в Zelle и посредством криптовалют (USDT, TRC-20).\n\n"
        "На каком языке заполнять анкету?\n\n"
        "На текущий момент заполнение анкеты работает только на английском языке.\n\n"
        "Что делать, если я не знаю, что отвечать?\n\n"
        "Напишите, что думаете, или оставьте поле пустым.",
        reply_markup=keyboard
    )


@dp.callback_query_handler(Text(startswith='back'), state=Form.main_menu)
async def handle_back(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = get_main_menu_keyboard()
    await bot.send_message(
        callback_query.from_user.id,
        "Вы вернулись в главное меню. Выберите действие:",
        reply_markup=keyboard
    )


@dp.message_handler(state="*", content_types=types.ContentType.DOCUMENT)
async def fill_cmd_handler(message: types.Message, state: FSMContext):
    document_id = message.document.file_id
    file_path = rf"../json_inputs/{document_id}.json"
    await bot.download_file_by_id(document_id, rf"../json_inputs/{document_id}.json")
    async with aiofiles.open(file_path, mode='r', encoding="utf-8") as f:
        json_data = await f.read()
    json_data = json.loads(json_data)
    async with state.proxy() as data:
        for key, value in json_data.items():
            data[key] = value
    await message.answer("Я заполнил данные, можно писать /end.")


@dp.message_handler(filters.Command("jump"), state="*")
async def jump_cmd_handler(message: types.Message, state: FSMContext):
    try:
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
    except Exception as e:
        await message.answer(f"Error: {e}")  

from form_ar_11 import form_ar_11_handlers
from form_i_589 import form_i_589_handlers
from form_i_765 import form_i_765_handlers
from form_i_485 import form_i_485_handlers
from form_i_131 import form_i_131_handlers


@app.route(WEBHOOK_PATH, methods=['POST'])
async def webhook(request):
    update = types.Update(**request.json)
    await dp.process_update(update)
    return '', 200


async def on_startup(dispatcher):
    await bot.send_message(chat_id=231584958, text='Bot has been started')
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dispatcher):
    await bot.send_message(chat_id=231584958, text='Bot has been stopped')
    await bot.delete_webhook()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
