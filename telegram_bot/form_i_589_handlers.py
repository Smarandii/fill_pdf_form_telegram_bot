from aiogram import types
from aiogram.dispatcher import FSMContext
from form_i_589 import Form_I_589
from telegram_bot import bot, dp, \
    FillPdfFromJsonAdapter, datetime, \
    Form_I_589_Gender_Choice, \
    Form_I_589_Marital_Status_Choice, \
    Form_I_589_Immigration_Court_Choice, \
    Form_I_94_Number_Choice, \
    Form_I_589_English_Fluency_Choice, \
    Form_I_589_Marriage_Choice, \
    Form_I_589_Location_Choice, Form_I_589_Spouse_Immigration_Court_Choice, Form_I_589_Include_Spouse_Choice, \
    Form_I_589_Have_Children_Choice, Form_I_589_Fill_Next_Child_Choice


@dp.callback_query_handler(text="I-589")
async def i_589_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-589"
    await bot.send_message(callback_query.from_user.id, "You've chosen the I-589 form. Let's start filling it.")
    await bot.send_message(callback_query.from_user.id, "Enter your Alien Registration Number(s) (A-Number) (if any):")
    await Form_I_589.A_I_PtAILine1_ANumber_0.set()


@dp.message_handler(state=Form_I_589.A_I_PtAILine1_ANumber_0)
async def process_A_I_PtAILine1_ANumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your U.S. Social Security Number (if any):")


@dp.message_handler(state=Form_I_589.A_I_TextField1_0)
async def process_A_I_TextField1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "USCIS Online Account Number (if any)")


@dp.message_handler(state=Form_I_589.A_I_TextField1_8)
async def process_A_I_TextField1_8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[8]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Complete Last Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine4_LastName_0)
async def process_A_I_PtAILine4_LastName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine4_LastName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "First Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine5_FirstName_0)
async def process_A_I_PtAILine5_FirstName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine5_FirstName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Middle Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine6_MiddleName_0)
async def process_A_I_PtAILine6_MiddleName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine6_MiddleName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What other names have you used (include maiden name and aliases)?")


@dp.message_handler(state=Form_I_589.A_I_TextField1_1)
async def process_A_I_TextField1_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Street Number and Name:")


# 8. Residence in the U.S. (where you physically reside)
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_StreetNumandName_0)
async def process_A_I_PtAILine8_StreetNumandName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Apt. Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AptNumber_0)
async def process_A_I_PtAILine8_AptNumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your City:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_City_0)
async def process_A_I_PtAILine9_City_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your State:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_State_0)
async def process_A_I_PtAILine8_State_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Zip Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_Zipcode_0)
async def process_A_I_PtAILine8_Zipcode_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_Zipcode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Area Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AreaCode_0)
async def process_A_I_PtAILine8_AreaCode_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Number:")


# 9. Mailing Address in the U.S. (if different than the address in Item Number 8)
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_TelephoneNumber_0)
async def process_A_I_PtAILine8_TelephoneNumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_TelephoneNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter In Care Of (if applicable):")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_InCareOf_0)
async def process_A_I_PtAILine9_InCareOf_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_InCareOf[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Area Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_AreaCode_0)
async def process_A_I_PtAILine9_AreaCode_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_TelephoneNumber_0)
async def process_A_I_PtAILine8_TelephoneNumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Street Number and Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_StreetNumandName_0)
async def process_A_I_PtAILine9_StreetNumandName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Apt. Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_AptNumber_0)
async def process_A_I_PtAILine9_AptNumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter City:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_City_0)
async def process_A_I_PtAILine9_City_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_City[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter State:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_State_0)
async def process_A_I_PtAILine9_State_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Zip Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process_A_I_PtAILine9_ZipCode_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_ZipCode[0]'] = message.text
    keyboard = Form_I_589_Gender_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Choose Gender", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male", state=Form_I_589.A_I_ChooseGender)
async def process_A_I_PartALine9Gender_0(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = "Male"
        data['[0].PartALine9Gender[1]'] = ""
    keyboard = Form_I_589_Marital_Status_Choice()
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are a male.")
    await bot.send_message(callback_query.from_user.id, "Choose Marital Status", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female", state=Form_I_589.A_I_ChooseGender)
async def process_A_I_PartALine9Gender_1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = ""
        data['[0].PartALine9Gender[1]'] = "Female"
    keyboard = Form_I_589_Marital_Status_Choice()
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are a female.")
    await bot.send_message(callback_query.from_user.id, "Choose Marital Status", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_single", state=Form_I_589.A_I_ChooseMaritalStatus)
async def process_A_I_ChooseMaritalStatus(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = callback_query.data
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are single.")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_married", state=Form_I_589.A_I_ChooseMaritalStatus)
async def process_A_I_ChooseMaritalStatus(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = callback_query.data
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are married.")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_divorced", state=Form_I_589.A_I_ChooseMaritalStatus)
async def process_A_I_ChooseMaritalStatus(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = callback_query.data
        data['[0].Marital[3]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are divorced.")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_widowed", state=Form_I_589.A_I_ChooseMaritalStatus)
async def process_A_I_ChooseMaritalStatus(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are widowed.")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField1_0)
async def process_A_I_DateTimeField1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter City and Country of Birth:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_4)
async def process_A_I_TextField1_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Present Nationality (Citizenship):")


@dp.message_handler(state=Form_I_589.A_I_TextField1_3)
async def process_A_I_TextField1_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Nationality at Birth:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_5)
async def process_A_I_TextField1_5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Race, Ethnic, or Tribal Group:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_6)
async def process_A_I_TextField1_6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[6]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Religion:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_7)
async def process_A_I_TextField1_7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[7]'] = message.text
    keyboard = Form_I_589_Immigration_Court_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Check the button, that applies", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="never_been_imc", state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process_A_I_ChooseImmigrationCourtProceedingsStatus(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = callback_query.data
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are never been in Immigration Court proceedings.")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="now_in_imc", state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process_A_I_ChooseImmigrationCourtProceedingsStatus(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = callback_query.data
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are now in Immigration Court proceedings.")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="not_now_but_been_in_imc", state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process_A_I_ChooseImmigrationCourtProceedingsStatus(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are not now in Immigration Court proceedings, but I have been in the past.")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField6_0)
async def process_A_I_DateTimeField6_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_94_Number_Choice()
    await bot.send_message(message.from_user.id, "Enter What is your current I-94 Number, if any?", reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_I_TextField3_0)
async def process_A_I_TextField3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List first entry into the U.S. beginning with your most recent entry. List date, place, your status, date status expires (mm/dd/yyyy, place, status, date status expires).")


def retrieve_entry_into_us_description(text, n=2):
    if text.count(",") == n:
        return text.split(",")
    elif text.count(" ") == n:
        return text.split(" ")
    else:
        return ['', '', '', '']


@dp.message_handler(state=Form_I_589.A_I_FirstUsEntry)
async def process_A_I_FirstUsEntry(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        date, place, status, date_status_expires = retrieve_entry_into_us_description(message.text, 3)
        data['[0].DateTimeField2[0]'] = date
        data['[0].TextField4[0]'] = place
        data['[0].TextField4[1]'] = status
        data['[0].DateTimeField2[1]'] = date_status_expires
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List second entry into the U.S.. List date, place, your status.")


@dp.message_handler(state=Form_I_589.A_I_SecondUsEntry)
async def process_A_I_SecondUsEntry(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        date, place, status, date_status_expires = retrieve_entry_into_us_description(message.text, 2)
        data['[0].DateTimeField3[0]'] = date
        data['[0].TextField4[2]'] = place
        data['[0].TextField4[3]'] = status
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List third entry into the U.S.. List date, place, and your status.")


@dp.message_handler(state=Form_I_589.A_I_ThirdUsEntry)
async def process_A_I_ThirdUsEntry(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        date, place, status, date_status_expires = retrieve_entry_into_us_description(message.text, 2)
        data['[0].DateTimeField4[0]'] = date
        data['[0].TextField4[4]'] = place
        data['[0].TextField4[5]'] = status
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What country issued your last passport or travel document?")


@dp.message_handler(state=Form_I_589.A_I_TextField5_0)
async def process_A_I_TextField5_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport Number")


@dp.message_handler(state=Form_I_589.A_I_TextField5_1)
async def process_A_I_TextField5_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Travel Document Number")


@dp.message_handler(state=Form_I_589.A_I_TextField5_2)
async def process_A_I_TextField5_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Expiration Date (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_2)
async def process_A_I_DateTimeField2_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What is your native language (include dialect, if applicable)?")


@dp.message_handler(state=Form_I_589.A_I_TextField7_0)
async def process_A_I_TextField7_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField7[0]'] = message.text
    keyboard = Form_I_589_English_Fluency_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Are you fluent in English?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_eng_fluent", state=Form_I_589.A_I_EngFluencyChoice)
async def process_A_I_CheckBox4_1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox4[1]'] = callback_query.data
        data['[0].CheckBox4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are fluent in English.")
    await bot.send_message(callback_query.from_user.id, "Enter What other languages do you speak fluently?")


@dp.callback_query_handler(text="no_eng_fluent", state=Form_I_589.A_I_EngFluencyChoice)
async def process_A_I_CheckBox4_0(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox4[0]'] = callback_query.data
        data['[0].CheckBox4[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are not fluent in English.")
    await bot.send_message(callback_query.from_user.id, "Enter What other languages do you speak fluently?")


@dp.message_handler(state=Form_I_589.A_I_TextField7_1)
async def process_A_I_TextField7_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField7[1]'] = message.text
    keyboard = Form_I_589_Marriage_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Are you married?", reply_markup=keyboard)


@dp.callback_query_handler(text="yes_married", state=Form_I_589.A_II_CheckBox5_0)
async def process_A_I_CheckBox5_0(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox5[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are married.")
    await bot.send_message(callback_query.from_user.id, "Enter your spouse's Alien Registration Number (A-Number)\n(if any)?")


@dp.callback_query_handler(text="no_married", state=Form_I_589.A_II_CheckBox5_0)
async def process_A_I_CheckBox5_0(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox5[0]'] = ""
    await Form_I_589.A_II_HaveChildrenChoice.set()
    keyboard = Form_I_589_Have_Children_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are not married.")
    await bot.send_message(callback_query.from_user.id, "Do you have children? (regardless of age, location, or marital status)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine1_ANumber_0)
async def process_A_II_NotMarried_0_PtAIILine1_ANumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number (if any)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_1)
async def process_A_II_NotMarried_0_TextField10_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_DateTimeField7_0)
async def process_A_II_NotMarried_0_DateTimeField7_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].DateTimeField7[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number (if any)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_2)
async def process_A_II_NotMarried_0_TextField10_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Complete Last Name")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine5_LastName_0)
async def process_A_II_NotMarried_0_PtAIILine5_LastName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine5_LastName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "First Name")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine6_FirstName_0)
async def process_A_II_NotMarried_0_PtAIILine6_FirstName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine6_FirstName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Middle Name")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine7_MiddleName_0)
async def process_A_II_NotMarried_0_PtAIILine7_MiddleName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine7_MiddleName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Other names used (include\nmaiden name and aliases)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_3)
async def process_A_II_NotMarried_0_TextField10_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Marriage (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_DateTimeField8_0)
async def process_A_II_NotMarried_0_DateTimeField8_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].DateTimeField8[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Place of Marriage")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_4)
async def process_A_II_NotMarried_0_TextField10_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_5)
async def process_A_II_NotMarried_0_TextField10_5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_0)
async def process_A_II_NotMarried_0_TextField10_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_0)
async def process_A_II_NotMarried_0_TextField10_6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[6]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose Gender of your spouse", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female", state=Form_I_589.A_II_ChooseGenderSpouse)
async def process_A_II_ChooseSpouseGender(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = ""
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is female.")
    await bot.send_message(callback_query.from_user.id, "Is this person in the U.S.?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male", state=Form_I_589.A_II_ChooseGenderSpouse)
async def process_A_II_ChooseSpouseGender(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = callback_query.data
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is male.")
    await bot.send_message(callback_query.from_user.id, "Is this person in the U.S.?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location", state=Form_I_589.A_II_IsInUSChoiceSpouse)
async def process_A_II_IsSpouseInUSChoice(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[0]'] = ""
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[1]'] = callback_query.data
    await Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is in US.")
    await bot.send_message(callback_query.from_user.id, "Provide place of last entry into the U.S.")


@dp.callback_query_handler(text="no_location", state=Form_I_589.A_II_IsInUSChoiceSpouse)
async def process_A_II_IsSpouseInUSChoice(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[0]'] = callback_query.data
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[1]'] = ""
    await Form_I_589.A_II_NotMarried_0_PtAIILine15_Specify_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is not in US.")
    await bot.send_message(callback_query.from_user.id, "Specify location of your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine15_Specify_0)
async def process_A_II_NotMarried_0_PtAIILine15_Specify_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_Specify[0]'] = message.text
    keyboard = Form_I_589_Have_Children_Choice()
    await Form_I_589.A_II_HaveChildrenChoice.set()
    await bot.send_message(message.from_user.id, "Do you have children? (regardless of age, location, or marital status)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0)
async def process_A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine16_PlaceofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of last entry into the U.S. (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine17_DateofLastEntry_0)
async def process_A_II_NotMarried_0_PtAIILine17_DateofLastEntry_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine17_DateofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "I-94 Number (send 0 if you don't have I-94 number)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine18_I94Number_0)
async def process_A_II_NotMarried_0_PtAIILine18_I94Number_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Status when last admitted (Visa type, if any) (send 0 if you didn't have had Status when last admitted)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0)
async def process_A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What is your spouse's current status?")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine20_SpouseCurrentStatus_0)
async def process_A_II_NotMarried_0_PtAIILine20_SpouseCurrentStatus_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine20_SpouseCurrentStatus[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What is the expiration date of his/her authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0)
async def process_A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Spouse_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id, "Is your spouse in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_spouse_imc", state=Form_I_589.A_II_IsImmigrationCourtProceedingsSpouse)
async def process_A_II_IsImmigrationCourtProceedingsSpouse(callback_query: types.CallbackQuery,
                                                           state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine22_No[0]'] = ""
        data['[1].NotMarried[0].PtAIILine22_Yes[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "If previously in the U.S., date of previous arrival (mm/dd/yyyy) else send 0")


@dp.callback_query_handler(text="no_spouse_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsSpouse)
async def process_A_II_IsImmigrationCourtProceedingsSpouse(callback_query: types.CallbackQuery,
                                                           state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine22_No[0]'] = callback_query.data
        data['[1].NotMarried[0].PtAIILine22_Yes[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that your spouse is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "If previously in the U.S., date of previous arrival (mm/dd/yyyy) else send 0")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0)
async def process_A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine23_PreviousArrivalDate[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine23_PreviousArrivalDate[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Spouse_Choice()
    await bot.send_message(message.from_user.id, "If in the U.S., is your spouse to be included in this application?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_spouse", state=Form_I_589.A_II_IsSpouseIncludedInApplication)
async def process_A_II_IsSpouseIncludedInApplication(callback_query: types.CallbackQuery,
                                                     state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine24_No[0]'] = ""
        data['[1].NotMarried[0].PtAIILine24_Yes[0]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Have_Children_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated your spouse to be included in this application")
    await bot.send_message(callback_query.from_user.id, "Do you have children? (regardless of age, location, or marital status)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_include_spouse",
                           state=Form_I_589.A_II_IsSpouseIncludedInApplication)
async def process_A_II_IsSpouseIncludedInApplication(callback_query: types.CallbackQuery,
                                                     state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine24_No[0]'] = callback_query.data
        data['[1].NotMarried[0].PtAIILine24_Yes[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Have_Children_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that your spouse not to be included in this application")
    await bot.send_message(callback_query.from_user.id, "Do you have children? (regardless of age, location, or marital status)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="dont_have_children", state=Form_I_589.A_II_HaveChildrenChoice)
async def process_A_II_HaveChildrenChoice(callback_query: types.CallbackQuery,
                                          state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildrenCheckbox[0]'] = ""
        data['[1].ChildrenCheckbox[1]'] = callback_query.data
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you don't have children")
    await bot.send_message(callback_query.from_user.id, "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")


@dp.callback_query_handler(text="have_children",
                           state=Form_I_589.A_II_HaveChildrenChoice)
async def process_A_II_HaveChildrenChoice(callback_query: types.CallbackQuery,
                                          state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildrenCheckbox[0]'] = callback_query.data
        data['[1].ChildrenCheckbox[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that you have children")
    await bot.send_message(callback_query.from_user.id, "Total number of children:")


@dp.message_handler(state=Form_I_589.A_II_TotalChild_0)
async def process_A_II_TotalChild_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].TotalChild[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Alien Registration Number of your first child (A-Number) (if any)")


# Child 1
@dp.message_handler(state=Form_I_589.A_II_ChildAlien1_0)
async def process_A_II_ChildAlien1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your first child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport1_0)
async def process_A_II_ChildPassport1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital1_0)
async def process_A_II_ChildMarital1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN1_0)
async def process_A_II_ChildSSN1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name")


@dp.message_handler(state=Form_I_589.A_II_ChildLast1_0)
async def process_A_II_ChildLast1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst1_0)
async def process_A_II_ChildFirst1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle1_0)
async def process_A_II_ChildMiddle1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB1_0)
async def process_A_II_ChildDOB1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth")


@dp.message_handler(state=Form_I_589.A_II_ChildCity1_0)
async def process_A_II_ChildCity1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat1_0)
async def process_A_II_ChildNat1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group")


@dp.message_handler(state=Form_I_589.A_II_ChildRace1_0)
async def process_A_II_ChildRace1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of first child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female", state=Form_I_589.A_II_ChooseGenderChild1)
async def process_A_II_ChooseGenderChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox16[1]'] = callback_query.data
        data['[1].CheckBox16[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male", state=Form_I_589.A_II_ChooseGenderChild1)
async def process_A_II_ChooseGenderChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox16[0]'] = callback_query.data
        data['[1].CheckBox16[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location", state=Form_I_589.A_II_ChooseLocationChild1)
async def process_A_II_ChooseLocationChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox17[0]'] = callback_query.data
        data['[1].CheckBox17[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S.")


@dp.callback_query_handler(text="no_location", state=Form_I_589.A_II_ChooseLocationChild1)
async def process_A_II_ChooseLocationChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox17[1]'] = callback_query.data
        data['[1].CheckBox17[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is not in U.S")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify_0)
async def process_A_II_PtAIILine13_Specify_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify[0]'] = message.text
        total_number_of_children = data["[1].TotalChild[0]"]

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(message.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0)
async def process_A_II_PtAIILine14_PlaceofLastEntry_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your first child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_ExpirationDate_0)
async def process_A_II_PtAIILine15_ExpirationDate_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine15_ExpirationDate[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number (If any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number_0)
async def process_A_II_PtAIILine16_I94Number_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status when last admitted (Visa type, if any")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission_0)
async def process_A_II_PtAIILine17_StatusofLastAdmission_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_CurrentStatusofChild_0)
async def process_A_II_PtAIILine18_CurrentStatusofChild_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine18_CurrentStatusofChild[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of his/her authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay_0)
async def process_A_II_PtAIILine19_ExpDateofAuthorizedStay_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc", state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = callback_query.data
        data['[1].PtAIILine20_No[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc", state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = ""
        data['[1].PtAIILine20_No[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child", state=Form_I_589.A_II_IsIncludedInApplicationChild1)
async def process_A_II_IsIncludedInApplicationChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes[0]'] = callback_query.data
        data['[1].PtAIILine21_No[0]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is to be included in this application")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child", state=Form_I_589.A_II_IsIncludedInApplicationChild1)
async def process_A_II_IsIncludedInApplicationChild1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes[0]'] = ""
        data['[1].PtAIILine21_No[0]'] = callback_query.data
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is to be included in this application")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child", state=Form_I_589.A_II_IsFillChild2)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) for second child")


@dp.callback_query_handler(text="no_fill_next_child", state=Form_I_589.A_II_IsFillChild2)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")


# Child 2
@dp.message_handler(state=Form_I_589.A_II_ChildAlien2_0)
async def process_A_II_ChildAlien2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your second child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport2_0)
async def process_A_II_ChildPassport2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital2_0)
async def process_A_II_ChildMarital2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN2_0)
async def process_A_II_ChildSSN2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name")


@dp.message_handler(state=Form_I_589.A_II_ChildLast2_0)
async def process_A_II_ChildLast2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst2_0)
async def process_A_II_ChildFirst2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle2_0)
async def process_A_II_ChildMiddle2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB2_0)
async def process_A_II_ChildDOB2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth")


@dp.message_handler(state=Form_I_589.A_II_ChildCity2_0)
async def process_A_II_ChildCity2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat2_0)
async def process_A_II_ChildNat2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group")


@dp.message_handler(state=Form_I_589.A_II_ChildRace2_0)
async def process_A_II_ChildRace2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of second child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female", state=Form_I_589.A_II_ChooseGenderChild2)
async def process_A_II_ChooseGenderChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox26_Gender[0]'] = callback_query.data
        data['[3].CheckBox26_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male", state=Form_I_589.A_II_ChooseGenderChild2)
async def process_A_II_ChooseGenderChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox26_Gender[1]'] = callback_query.data
        data['[3].CheckBox26_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location", state=Form_I_589.A_II_ChooseLocationChild2)
async def process_A_II_ChooseLocationChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox27[0]'] = callback_query.data
        data['[1].CheckBox27[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S.")


@dp.callback_query_handler(text="no_location", state=Form_I_589.A_II_ChooseLocationChild2)
async def process_A_II_ChooseLocationChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox27[1]'] = callback_query.data
        data['[1].CheckBox27[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is not in U.S")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify2_0)
async def process_A_II_PtAIILine13_Specify2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify2[0]'] = message.text
        total_number_of_children = data["[1].TotalChild[0]"]

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(message.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry2_0)
async def process_A_II_PtAIILine14_PlaceofLastEntry2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your first child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry2_0)
async def process_A_II_PtAIILine15_DateofLastEntry2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number (If any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number2_0)
async def process_A_II_PtAIILine16_I94Number2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status when last admitted (Visa type, if any")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission2_0)
async def process_A_II_PtAIILine17_StatusofLastAdmission2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus2_0)
async def process_A_II_PtAIILine18_CurrentStatusofChild_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of his/her authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process_A_II_PtAIILine19_ExpDateofAuthorizedStay2_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc", state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process_A_II_IsImmigrationCourtProceedingsChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes2[0]'] = callback_query.data
        data['[1].PtAIILine20_No2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc", state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process_A_II_IsImmigrationCourtProceedingsChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes2[0]'] = ""
        data['[1].PtAIILine20_No2[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child", state=Form_I_589.A_II_IsIncludedInApplicationChild2)
async def process_A_II_IsIncludedInApplicationChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes2[0]'] = callback_query.data
        data['[1].PtAIILine21_No2[0]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is to be included in this application")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child", state=Form_I_589.A_II_IsIncludedInApplicationChild2)
async def process_A_II_IsIncludedInApplicationChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes2[0]'] = ""
        data['[1].PtAIILine21_No2[0]'] = callback_query.data
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is to be included in this application")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child", state=Form_I_589.A_II_IsFillChild3)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) for second child")


@dp.callback_query_handler(text="no_fill_next_child", state=Form_I_589.A_II_IsFillChild3)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")


# Child 3
@dp.message_handler(state=Form_I_589.A_II_ChildAlien3_0)
async def process_A_II_ChildAlien3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your third child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport3_0)
async def process_A_II_ChildPassport3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital3_0)
async def process_A_II_ChildMarital3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN3_0)
async def process_A_II_ChildSSN3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name")


@dp.message_handler(state=Form_I_589.A_II_ChildLast3_0)
async def process_A_II_ChildLast3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst3_0)
async def process_A_II_ChildFirst3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle3_0)
async def process_A_II_ChildMiddle3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB3_0)
async def process_A_II_ChildDOB3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth")


@dp.message_handler(state=Form_I_589.A_II_ChildCity3_0)
async def process_A_II_ChildCity3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat3_0)
async def process_A_II_ChildNat3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group")


@dp.message_handler(state=Form_I_589.A_II_ChildRace3_0)
async def process_A_II_ChildRace3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of third child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female", state=Form_I_589.A_II_ChooseGenderChild3)
async def process_A_II_ChooseGenderChild3(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox36_Gender[0]'] = callback_query.data
        data['[3].CheckBox36_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male", state=Form_I_589.A_II_ChooseGenderChild3)
async def process_A_II_ChooseGenderChild3(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox36_Gender[1]'] = callback_query.data
        data['[3].CheckBox36_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location", state=Form_I_589.A_II_ChooseLocationChild3)
async def process_A_II_ChooseLocationChild2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox37[0]'] = callback_query.data
        data['[1].CheckBox37[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S.")


@dp.callback_query_handler(text="no_location", state=Form_I_589.A_II_ChooseLocationChild3)
async def process_A_II_ChooseLocationChild3(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox37[1]'] = callback_query.data
        data['[1].CheckBox37[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is not in U.S")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify3_0)
async def process_A_II_PtAIILine13_Specify3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify3[0]'] = message.text
        total_number_of_children = data["[1].TotalChild[0]"]

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(message.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry3_0)
async def process_A_II_PtAIILine14_PlaceofLastEntry3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your third child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry3_0)
async def process_A_II_PtAIILine15_DateofLastEntry3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number (If any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number3_0)
async def process_A_II_PtAIILine16_I94Number3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status when last admitted (Visa type, if any")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission3_0)
async def process_A_II_PtAIILine17_StatusofLastAdmission3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus3_0)
async def process_A_II_PtAIILine18_CurrentStatusofChild3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of his/her authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay3_0)
async def process_A_II_PtAIILine19_ExpDateofAuthorizedStay3_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc", state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process_A_II_IsImmigrationCourtProceedingsChild3(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes3[0]'] = callback_query.data
        data['[1].PtAIILine20_No3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc", state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process_A_II_IsImmigrationCourtProceedingsChild3(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes3[0]'] = ""
        data['[1].PtAIILine20_No3[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child", state=Form_I_589.A_II_IsIncludedInApplicationChild3)
async def process_A_II_IsIncludedInApplicationChild3(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes3[0]'] = callback_query.data
        data['[1].PtAIILine21_No3[0]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is to be included in this application")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child", state=Form_I_589.A_II_IsIncludedInApplicationChild3)
async def process_A_II_IsIncludedInApplicationChild3(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes3[0]'] = ""
        data['[1].PtAIILine21_No3[0]'] = callback_query.data
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is to be included in this application")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child", state=Form_I_589.A_II_IsFillChild4)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) for fourth child")


@dp.callback_query_handler(text="no_fill_next_child", state=Form_I_589.A_II_IsFillChild4)
async def process_A_II_IsImmigrationCourtProceedingsChild1(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States. If this is not the country where you fear persecution, also list the last address in the country where you fear persecution. (List Address, City/Town, Department, Province, or State and Country.)")

# copy from Child 3 to 1661 row and then change to be a Child 4
# Child 4



































































