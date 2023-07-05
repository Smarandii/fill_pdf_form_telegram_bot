import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from datetime import datetime
from fill_pdf_from_json_adapter import FillPdfFromJsonAdapter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from common_keyboards import AvailableFormsKeyboard
from f_ar_11_keyboards import Form_AR_11_Mailing_Address_Choice_Keyboard
from f_i_589_keyboards import Form_I_589_Gender_Choice, \
    Form_I_589_Marital_Status_Choice, \
    Form_I_589_Immigration_Court_Choice, \
    Form_I_94_Number_Choice, \
    Form_I_589_English_Fluency_Choice, \
    Form_I_589_Marriage_Choice, \
    Form_I_589_Location_Choice, \
    Form_I_589_Spouse_Immigration_Court_Choice, \
    Form_I_589_Include_Spouse_Choice,\
    Form_I_589_Have_Children_Choice, \
    Form_I_589_Child_Immigration_Court_Choice, \
    Form_I_589_Fill_Next_Child_Choice


load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())