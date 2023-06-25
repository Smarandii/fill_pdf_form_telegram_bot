import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from datetime import datetime
from fill_pdf_from_json_adapter import FillPdfFromJsonAdapter
from forms_keyboards import AvailableFormsKeyboardFactory, Form_AR_11_Mailing_Address_Choice_Keyboard

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())