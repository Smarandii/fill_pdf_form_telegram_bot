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
    Form_I_589_Location_Choice


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
    await bot.send_message(message.from_user.id, "Choose Gender", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male", state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process_A_I_PartALine9Gender_0(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = "Male"
        data['[0].PartALine9Gender[1]'] = ""
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are a male.")
    await bot.send_message(callback_query.from_user.id, "Choose Marital Status", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female", state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process_A_I_PartALine9Gender_1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = ""
        data['[0].PartALine9Gender[1]'] = "Female"
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are a female.")
    await bot.send_message(callback_query.from_user.id, "Choose Marital Status", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_single", state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process_A_I_Marital_0(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = callback_query.data
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = ""
    await Form_I_589.A_I_DateTimeField1_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are single.")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_married", state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process_A_I_Marital_1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = callback_query.data
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = ""
    await Form_I_589.A_I_DateTimeField1_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are married.")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_divorced", state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process_A_I_Marital_2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = callback_query.data
        data['[0].Marital[3]'] = ""
    await Form_I_589.A_I_DateTimeField1_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are divorced.")
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
    await bot.send_message(message.from_user.id, "Check the button, that applies", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="never_been_imc", state=Form_I_589.A_I_TextField1_7)
async def process_A_I_CheckBox3_0(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = callback_query.data
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.A_I_DateTimeField6_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are never been in Immigration Court proceedings.")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="now_in_imc", state=Form_I_589.A_I_TextField1_7)
async def process_A_I_CheckBox3_1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = callback_query.data
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.A_I_DateTimeField6_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are now in Immigration Court proceedings.")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="not_now_but_been_in_imc", state=Form_I_589.A_I_TextField1_7)
async def process_A_I_CheckBox3_2(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = callback_query.data
    await Form_I_589.A_I_DateTimeField6_0.set()
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
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are not married.")
    await bot.send_message(callback_query.from_user.id, "Enter What other languages do you speak fluently?")


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


@dp.callback_query_handler(text="female", state=Form_I_589.A_II_ChooseSpouseGender)
async def process_A_II_ChooseSpouseGender(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = ""
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is female.")
    await bot.send_message(callback_query.from_user.id, "Is this person in the U.S.?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male", state=Form_I_589.A_II_ChooseSpouseGender)
async def process_A_II_ChooseSpouseGender(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = callback_query.data
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is male.")
    await bot.send_message(callback_query.from_user.id, "Is this person in the U.S.?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location", state=Form_I_589.A_II_ChooseSpouseGender)
async def process_A_II_IsSpouseInUSChoice(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[0]'] = ""
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[1]'] = callback_query.data
    await Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is in US.")
    await bot.send_message(callback_query.from_user.id, "Provide place of last entry into the U.S.")


@dp.callback_query_handler(text="no_location", state=Form_I_589.A_II_ChooseSpouseGender)
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
    await Form_I_589.A_II_HaveChildrenChoice.set()
    await bot.send_message(message.from_user.id, "Choose Gender of your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0)
async def process_A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine16_PlaceofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of last entry into the U.S. (mm/dd/yyyy)")

































































































