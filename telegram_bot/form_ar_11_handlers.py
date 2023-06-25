from aiogram import types
from aiogram.dispatcher import FSMContext, filters
from form_ar_11 import Form_AR_11
from telegram_bot import bot, dp, FillPdfFromJsonAdapter, datetime, Form_AR_11_Mailing_Address_Choice_Keyboard


@dp.callback_query_handler(text="AR-11")
async def ar_11_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "AR-11"
    await bot.send_message(callback_query.from_user.id, "You've chosen the AR-11 form. Let's start filling it.")
    await bot.send_message(callback_query.from_user.id, "Enter your Family Name:")
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
        data['S2B_Unit'] = ""
        data['S2B_AptSteFlrNumber'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Apt. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Ste. checkbox")


@dp.message_handler(state=Form_AR_11.S2B_Unit_1)
async def process_s2b_unit_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_Unit_1'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit_1'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Ste. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Flr. checkbox")


@dp.message_handler(state=Form_AR_11.S2B_Unit_2)
async def process_s2b_unit_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2B_Unit_2'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2B_Unit_2'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Flr. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
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
        data['S2A_Unit'] = ""
        data['S2A_AptSteFlrNumber'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2A_Unit'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Apt. number:")
            await Form_AR_11.S2A_AptSteFlrNumber.set()
        else:
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Ste. checkbox")


@dp.message_handler(state=Form_AR_11.S2A_Unit_1)
async def process_s2a_unit_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2A_Unit_1'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2A_Unit_1'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Ste. number:")
            await Form_AR_11.S2A_AptSteFlrNumber.set()
        else:
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Flr. checkbox")


@dp.message_handler(state=Form_AR_11.S2A_Unit_2)
async def process_s2a_unit_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2A_Unit_2'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2A_Unit_2'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Flr. number:")
            await Form_AR_11.S2B_AptSteFlrNumber.set()
        else:
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
        data['S2C_Unit'] = ""
        data['S2C_AptSteFlrNumber'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2C_Unit'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Apt. number:")
            await Form_AR_11.S2C_AptSteFlrNumber.set()
        else:
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Ste. checkbox")


@dp.message_handler(state=Form_AR_11.S2C_Unit_1)
async def process_s2c_unit_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_Unit_1'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2C_Unit_1'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Ste. number:")
            await Form_AR_11.S2C_AptSteFlrNumber.set()
        else:
            await Form_AR_11.next()
            await bot.send_message(message.from_user.id, "Send 'x' if you want to check the Flr. checkbox")


@dp.message_handler(state=Form_AR_11.S2C_Unit_2)
async def process_s2c_unit_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['S2C_Unit_2'] = ""
        if message.text.lower() == "x" or message.text.lower() == "х":
            data['S2C_Unit_2'] = message.text
            await bot.send_message(message.from_user.id, "Enter your Flr. number:")
            await Form_AR_11.S2C_AptSteFlrNumber.set()
        else:
            await bot.send_message(message.from_user.id, "Enter your state (e.g. CA, NY, AZ and so on):")
            await Form_AR_11.S2C_State.set()


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
    keyboard = Form_AR_11_Mailing_Address_Choice_Keyboard()
    await message.answer("Ok! Let's fill your Mailing Address now. "
                         "Before that a quick question, does your present physical address "
                         "is the same as your Mailing Address?", reply_markup=keyboard.keyboard_markup)


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
        data['S2C_CityOrTown'] = data['S2B_CityOrTown']
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