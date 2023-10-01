import logging
import os
import datetime

from aiogram import \
    Bot, \
    Dispatcher

from aiogram import types
from aiogram.dispatcher import filters

from aiogram.types import \
    InlineKeyboardMarkup, \
    InlineKeyboardButton, Message

from aiogram.contrib.fsm_storage.memory import \
    MemoryStorage

from dotenv import \
    load_dotenv

from telegram_bot.fill_pdf_from_json_adapter import \
    FillPdfFromJsonAdapter

from common_keyboards import \
    AvailableFormsKeyboard

from telegram_bot.form_ar_11.f_ar_11_keyboards import \
    Form_AR_11_Mailing_Address_Choice_Keyboard

from telegram_bot.form_i_589.f_i_589_keyboards import \
    FormI589GenderChoice, \
    FormI589MaritalStatusChoice, \
    FormI589ImmigrationCourtChoice, \
    FormI94NumberChoice, \
    FormI589EnglishFluencyChoice, \
    FormI589LocationChoice, \
    FormI589SpouseImmigrationCourtChoice, \
    FormI589IncludeSpouseChoice,\
    FormI589HaveChildrenChoice, \
    FormI589ChildImmigrationCourtChoice, \
    FormI589FillNextChildChoice, \
    FormI589MotherDeceasedChoice, \
    FormI589FatherDeceasedChoice, \
    FormI5891siblingDeceasedChoice, \
    FormI5892siblingDeceasedChoice, \
    FormI5893siblingDeceasedChoice, \
    FormI5894siblingDeceasedChoice, \
    FormI589AsylumReasonChoice, \
    FormI589FamilyExperiencedHarmChoice, \
    FormI589IfAnyChoice


load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())