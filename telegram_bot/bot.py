import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5627655732:AAF5Bf4MK3av3HQLP_A6yH32c8Py8_FfFtE'

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Form(StatesGroup):
    # Information About You
    S1_FamilyName = State()
    S1_GivenName = State()
    S1_MiddleName = State()
    S1_DateOfBirth = State()
    AlienNumber = State()

    # Present Physical Address
    S2B_StreetNumberName = State()
    S2B_CityOrTown = State()
    S2B_Unit = State()  # Apt.
    S2B_Unit_1 = State()  # Ste.
    S2B_Unit_2 = State()  # Flr.
    S2B_AptSteFlrNumber = State()
    S2B_State = State()
    S2B_ZipCode = State()

    # Previous Physical Address
    S2A_StreetNumberName = State()
    S2A_CityOrTown = State()
    S2A_Unit = State()  # Apt.
    S2A_Unit_1 = State()  # Ste.
    S2A_Unit_2 = State()  # Flr.
    S2A_AptSteFlrNumber = State()
    S2A_State = State()
    S2A_ZipCode = State()

    # Mailing Address (optional)
    S2C_StreetNumberName = State()
    S2C_CityOrTown = State()
    S2C_Unit = State()  # Apt.
    S2C_Unit_1 = State()  # Ste.
    S2C_Unit_2 = State()  # Flr.
    S2C_AptSteFlrNumber = State()
    S2C_State = State()
    S2C_ZipCode = State()

    S3_SignatureApplicant = State()
    # Date of signature filled automatically


@dp.message_handler(filters.Command("start"))
async def start_cmd_handler(message: types.Message):
    keyboard_markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("AR-11 form", callback_data="AR-11")
    keyboard_markup.add(button)
    await message.answer("Hello! Here are the forms available for filling:", reply_markup=keyboard_markup)


@dp.callback_query_handler(text="AR-11")
async def callback_query_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "You've chosen the AR-11 form. Let's start filling it.")
    await bot.send_message(callback_query.from_user.id, "Enter your FamilyName:")
    await Form.S1_FamilyName.set()


@dp.message_handler(state=Form.S1_FamilyName)
async def process_s1_family_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_FamilyName'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Enter your Given Name:")


@dp.message_handler(state=Form.S1_GivenName)
async def process_s1_given_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_GivenName'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Enter your Middle Name:")


@dp.message_handler(state=Form.S1_MiddleName)
async def process_s1_middle_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_MiddleName'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Enter your Date Of Birth:")


@dp.message_handler(state=Form.S1_DateOfBirth)
async def process_s1_date_of_birth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S1_DateOfBirth'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Enter your Alien Number:")


@dp.message_handler(state=Form.AlienNumber)
async def process_alien_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['AlienNumber'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Enter your Street Name and Number:")


@dp.message_handler(state=Form.S2B_StreetNumberName)
async def process_s2b_street_number_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_StreetNumberName'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Enter your City or Town:")


@dp.message_handler(state=Form.S2B_CityOrTown)
async def process_s2b_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_CityOrTown'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Apt. checkbox:")


@dp.message_handler(state=Form.S2B_Unit)
async def process_s2b_unit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Apt. number:")
            await Form.S2B_AptSteFlrNumber.set()
        else:
            data['S2B_Unit'] = ""
            await Form.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Ste. checkbox")


@dp.message_handler(state=Form.S2B_Unit_1)
async def process_s2b_unit_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit_1'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Ste. number:")
            await Form.S2B_AptSteFlrNumber.set()
        else:
            data['S2B_Unit_1'] = ""
            await Form.next()


@dp.message_handler(state=Form.S2B_Unit_2)
async def process_s2b_unit_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_Unit_2'] = message.text
        await bot.send_message(message.from_user.id, "Enter your Flr. number:")
        await Form.S2B_AptSteFlrNumber.set()


@dp.message_handler(state=Form.S2B_CityOrTown)
async def process_s2b_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_CityOrTown'] = message.text
    await Form.next()
    await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Apt. checkbox:")














# After the form is filled
@dp.message_handler(state=Form.S3_SignatureApplicant)
async def process_s3_signatureapplicant(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S3_SignatureApplicant'] = message.text
        data['S3_DateofSignature'] = datetime.now().strftime("%d-%m-%Y")
        # Here the form is completed, and you can do whatever you want with the data
        await bot.send_message(message.chat.id, str(data))  # send filled form as a string, just for testing
    await state.finish()  # finish the form


async def on_startup(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=231584958, text='Bot has been stopped')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
