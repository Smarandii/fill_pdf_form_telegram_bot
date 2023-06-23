import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from form_ar_11 import Form_AR_11
from aiogram.dispatcher import FSMContext, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from fill_pdf_from_json_adapter import FillPdfFromJsonAdapter

from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(filters.Command("start"))
async def start_cmd_handler(message: types.Message):
    keyboard_markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("AR-11 form", callback_data="AR-11")
    keyboard_markup.add(button)
    await message.answer("Hello! Here are the forms available for filling:", reply_markup=keyboard_markup)


@dp.callback_query_handler(text="AR-11")
async def callback_query_handler(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "ar-11"
    await bot.send_message(callback_query.from_user.id, "You've chosen the AR-11 form. Let's start filling it.")
    await bot.send_message(callback_query.from_user.id, "Enter your FamilyName:")
    await Form_AR_11.S1_FamilyName.set()


@dp.message_handler(state=Form_AR_11.S1_FamilyName)
async def process_s1_family_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_FamilyName'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your Given Name:")


@dp.message_handler(state=Form_AR_11.S1_GivenName)
async def process_s1_given_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_GivenName'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your Middle Name:")


@dp.message_handler(state=Form_AR_11.S1_MiddleName)
async def process_s1_middle_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_MiddleName'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your Date Of Birth:")


@dp.message_handler(state=Form_AR_11.S1_DateOfBirth)
async def process_s1_date_of_birth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_DateOfBirth'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your Alien Number:")


@dp.message_handler(state=Form_AR_11.AlienNumber)
async def process_alien_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['AlienNumber'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your Street Name and Number:")


@dp.message_handler(state=Form_AR_11.S2B_StreetNumberName)
async def process_s2b_street_number_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_StreetNumberName'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your City or Town:")


@dp.message_handler(state=Form_AR_11.S2B_CityOrTown)
async def process_s2b_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_CityOrTown'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Apt. checkbox:")


@dp.message_handler(state=Form_AR_11.S2B_Unit)
async def process_s2b_unit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Apt. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
            data['S2B_Unit'] = ""
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Ste. checkbox")


@dp.message_handler(state=Form_AR_11.S2B_Unit_1)
async def process_s2b_unit_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit_1'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Ste. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
            data['S2B_Unit_1'] = ""
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Flr. checkbox")


@dp.message_handler(state=Form_AR_11.S2B_Unit_2)
async def process_s2b_unit_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit_2'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Flr. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
            data['S2B_Unit_2'] = ""
            await Form_AR_11.S2B_State.set()
            await bot.send_message(message.from_user.id, "Enter your state (e.g. CA, NY, AZ and so on):")


@dp.message_handler(state=Form_AR_11.S2B_AptSteFlrNumber)
async def process_s2b_apt_ste_flr_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_AptSteFlrNumber'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your state (e.g. CA, NY, AZ and so on):")


@dp.message_handler(state=Form_AR_11.S2B_State)
async def process_s2b_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_State'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your zipcode (e.g. 123456) "
                                                 "US ZIP code lookup: https://tools.usps.com/go/ZipLookupAction_input")


@dp.message_handler(state=Form_AR_11.S2B_ZipCode)
async def process_s2b_zip_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_ZipCode'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Ok! Let's fill previous physical address now:")
    await bot.send_message(message.from_user.id, "Enter your Street Name and Number:")


@dp.message_handler(state=Form_AR_11.S2A_StreetNumberName)
async def process_s2a_street_number_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2A_StreetNumberName'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your City or Town:")


@dp.message_handler(state=Form_AR_11.S2A_CityOrTown)
async def process_s2a_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2A_CityOrTown'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Apt. checkbox:")


@dp.message_handler(state=Form_AR_11.S2A_Unit)
async def process_s2a_unit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2A_Unit'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Apt. number:")
            await Form_AR_11.S2A_AptSteFlrNumber.set()
        else:
            data['S2A_Unit'] = ""
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Ste. checkbox")


@dp.message_handler(state=Form_AR_11.S2A_Unit_1)
async def process_s2a_unit_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2A_Unit_1'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Ste. number:")
            await Form_AR_11.S2A_AptSteFlrNumber.set()
        else:
            data['S2A_Unit_1'] = ""
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Flr. checkbox")


@dp.message_handler(state=Form_AR_11.S2A_Unit_2)
async def process_s2a_unit_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2A_Unit_2'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Flr. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
            data['S2A_Unit_2'] = ""
            await Form_AR_11.S2A_State.set()
            await bot.send_message(message.from_user.id, "Enter your state (e.g. CA, NY, AZ and so on):")


@dp.message_handler(state=Form_AR_11.S2A_AptSteFlrNumber)
async def process_s2a_apt_ste_flr_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2A_AptSteFlrNumber'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your state (e.g. CA, NY, AZ and so on):")


@dp.message_handler(state=Form_AR_11.S2A_State)
async def process_s2a_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2A_State'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your zipcode (e.g. 123456) "
                                                 "US ZIP code lookup: https://tools.usps.com/go/ZipLookupAction_input")


# Mailing address
@dp.message_handler(state=Form_AR_11.S2C_StreetNumberName)
async def process_s2c_street_number_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_StreetNumberName'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your City or Town:")


@dp.message_handler(state=Form_AR_11.S2C_CityOrTown)
async def process_s2c_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_CityOrTown'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Apt. checkbox:")


@dp.message_handler(state=Form_AR_11.S2C_Unit)
async def process_s2c_unit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2C_Unit'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Apt. number:")
            await Form_AR_11.S2C_AptSteFlrNumber.set()
        else:
            data['S2C_Unit'] = ""
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Ste. checkbox")


@dp.message_handler(state=Form_AR_11.S2C_Unit_1)
async def process_s2c_unit_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2C_Unit_1'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Ste. number:")
            await Form_AR_11.S2C_AptSteFlrNumber.set()
        else:
            data['S2C_Unit_1'] = ""
            await Form_AR_11.next()


@dp.message_handler(state=Form_AR_11.S2C_Unit_2)
async def process_s2c_unit_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_Unit_2'] = message.text
        await bot.send_message(message.from_user.id, "Enter your Flr. number:")
        await Form_AR_11.S2C_AptSteFlrNumber.set()


@dp.message_handler(state=Form_AR_11.S2C_AptSteFlrNumber)
async def process_s2c_apt_ste_flr_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_AptSteFlrNumber'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your state (e.g. CA, NY, AZ and so on):")


@dp.message_handler(state=Form_AR_11.S2C_State)
async def process_s2c_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_State'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Enter your zipcode (e.g. 123456) "
                                                 "US ZIP code lookup: https://tools.usps.com/go/ZipLookupAction_input")


@dp.message_handler(state=Form_AR_11.S2C_ZipCode)
async def process_s2b_zip_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_ZipCode'] = message.text
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Ok! All that's left is your signature:")


@dp.message_handler(state=Form_AR_11.S2A_ZipCode)
async def process_s2a_zip_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2A_ZipCode'] = message.text
    keyboard_markup = InlineKeyboardMarkup(row_width=3)
    button_yes = InlineKeyboardButton("MailingSameAsPhysical_Yes", callback_data="MailingSameAsPhysical_Yes")
    keyboard_markup.add(button_yes)
    button_no = InlineKeyboardButton("MailingSameAsPhysical_No", callback_data="MailingSameAsPhysical_No")
    keyboard_markup.add(button_no)
    button_empty = InlineKeyboardButton("MailingEmpty", callback_data="MailingEmpty")
    keyboard_markup.add(button_empty)
    await message.answer("Ok! Let's fill your Mailing Address now. "
                         "Before that a quick question, does your present physical address "
                         "is the same as your Mailing Address?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text="MailingSameAsPhysical_Yes", state="*")
async def callback_query_handler_mailing_same_as_physical_yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "You've pushed 'Yes' button, I will copy information "
                                                        "from Present Physical Address to Mailing Address")
    async with state.proxy() as data:
        data['S2C_StreetNumberName'] = data['S2B_StreetNumberName']
        data['S2C_StreetNumberName'] = data['S2B_CityOrTown']
        data['S2C_Unit'] = data['S2B_Unit']
        data['S2C_Unit_1'] = data['S2B_Unit_1']
        data['S2C_Unit_2'] = data['S2B_Unit_2']
        data['S2C_AptSteFlrNumber'] = data['S2B_AptSteFlrNumber']
        data['S2C_State'] = data['S2B_State']
        data['S2C_ZipCode'] = data['S2B_ZipCode']

    await Form_AR_11.S3_SignatureApplicant.set()
    await bot.send_message(callback_query.from_user.id, "Enter your Signature:")


@dp.callback_query_handler(text="MailingSameAsPhysical_No", state="*")
async def callback_query_handler_mailing_same_as_physical_no(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "You've pushed 'No' button, let's continue to fill form"
                                                        "with your Mailing Address")
    await Form_AR_11.S2C_StreetNumberName.set()
    await bot.send_message(callback_query.from_user.id, "Enter your Street name and number:")


@dp.callback_query_handler(text="MailingEmpty", state="*")
async def callback_query_handler_mailing_empty(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "You will not fill Mailing Address, "
                                                        "all that's left is your signature!")
    await Form_AR_11.S3_SignatureApplicant.set()
    await bot.send_message(callback_query.from_user.id, "Enter your Signature:")


@dp.message_handler(state=Form_AR_11.S3_SignatureApplicant)
async def process_s3_signature_applicant(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S3_SignatureApplicant'] = message.text
        data['S3_DateofSignature'] = datetime.now().strftime("%d/%m/%Y")

        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.now().strftime('%Y%m%d%H%M%S'))
        adapter.save_json(data)
        await bot.send_message(message.chat.id, "Your data for AR-11 form was successfully saved! Wait for pdf file.")
        await bot.send_chat_action(message.chat.id, "typing")
        pdf_file_path = adapter.fill_pdf()
        with open(pdf_file_path, 'rb') as file:
            await bot.send_document(message.chat.id, file)
    await state.finish()


async def on_startup(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been stopped')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
