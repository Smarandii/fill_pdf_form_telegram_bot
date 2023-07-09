from aiogram import types
from aiogram.dispatcher import FSMContext

from telegram_bot.form_i_589.f_i_589_keyboards import \
    Form_I_589_You_Fear_Harm_Or_Mistreatment_Choice, \
    Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice, \
    Form_I_589_Gender_Choice, \
    Form_I_589_Marital_Status_Choice, \
    Form_I_589_Immigration_Court_Choice, \
    Form_I_94_Number_Choice, \
    Form_I_589_English_Fluency_Choice, \
    Form_I_589_Location_Choice, \
    Form_I_589_Spouse_Immigration_Court_Choice, \
    Form_I_589_Include_Spouse_Choice, \
    Form_I_589_Have_Children_Choice, \
    Form_I_589_Fill_Next_Child_Choice, \
    Form_I_589_Mother_Deceased_Choice, \
    Form_I_589_Father_Deceased_Choice, \
    Form_I_589_1Sibling_Deceased_Choice, \
    Form_I_589_2Sibling_Deceased_Choice, \
    Form_I_589_3Sibling_Deceased_Choice, \
    Form_I_589_Asylum_Reason_Choice, \
    Form_I_589_Family_Experienced_Harm_Choice

from telegram_bot.form_i_589.form_i_589_state_group import Form_I_589

from telegram_bot import \
    bot,\
    dp, \
    FillPdfFromJsonAdapter, \
    datetime


@dp.callback_query_handler(text="I-589")
async def i_589_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-589"
    await bot.send_message(callback_query.from_user.id, "You've chosen the I-589 form. Let's start filling it")
    await bot.send_message(callback_query.from_user.id, "Enter your Alien Registration Number(s) (A-Number) (if any):")
    await Form_I_589.A_I_PtAILine1_ANumber_0.set()


@dp.message_handler(state=Form_I_589.A_I_PtAILine1_ANumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your U.S. Social Security Number (if any):")


@dp.message_handler(state=Form_I_589.A_I_TextField1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "USCIS Online Account Number (if any)")


@dp.message_handler(state=Form_I_589.A_I_TextField1_8)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[8]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Complete Last Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine4_LastName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine4_LastName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "First Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine5_FirstName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine5_FirstName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Middle Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine6_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine6_MiddleName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What other names have you used (include maiden name and aliases)?")


@dp.message_handler(state=Form_I_589.A_I_TextField1_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Street Number and Name:")


# 8. Residence in the U.S. (where you physically reside)
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_StreetNumandName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Apt. Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your City:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_City_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your State:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Zip Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_Zipcode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_Zipcode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Area Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AreaCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Number:")


# 9. Mailing Address in the U.S. (if different than the address in Item Number 8)
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_TelephoneNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_TelephoneNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter In Care Of (if applicable):")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_InCareOf_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_InCareOf[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Area Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_AreaCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_TelephoneNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Street Number and Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_StreetNumandName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Apt. Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_AptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter City:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter State:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Zip Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_ZipCode[0]'] = message.text
    keyboard = Form_I_589_Gender_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Choose Gender", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_I_ChooseGender)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = "Male"
        data['[0].PartALine9Gender[1]'] = ""
    keyboard = Form_I_589_Marital_Status_Choice()
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are a male")
    await bot.send_message(callback_query.from_user.id, "Choose Marital Status", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_I_ChooseGender)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = ""
        data['[0].PartALine9Gender[1]'] = "Female"
    keyboard = Form_I_589_Marital_Status_Choice()
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are a female")
    await bot.send_message(callback_query.from_user.id, "Choose Marital Status", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_single",
                           state=Form_I_589.A_I_ChooseMaritalStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = callback_query.data
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = ""
        data['[1].CheckBox5[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are single")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_married",
                           state=Form_I_589.A_I_ChooseMaritalStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = callback_query.data
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = ""
        data['[1].CheckBox5[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are married")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_divorced",
                           state=Form_I_589.A_I_ChooseMaritalStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = callback_query.data
        data['[0].Marital[3]'] = ""
        data['[1].CheckBox5[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are divorced")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.callback_query_handler(text="ms_widowed",
                           state=Form_I_589.A_I_ChooseMaritalStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = ""
        data['[0].Marital[1]'] = ""
        data['[0].Marital[2]'] = ""
        data['[0].Marital[3]'] = callback_query.data
        data['[1].CheckBox5[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are widowed")
    await bot.send_message(callback_query.from_user.id, "Enter Date of Birth (mm/dd/yyyy):")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter City and Country of Birth:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Present Nationality (Citizenship):")


@dp.message_handler(state=Form_I_589.A_I_TextField1_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Nationality at Birth:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Race, Ethnic, or Tribal Group:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[6]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Religion:")


@dp.message_handler(state=Form_I_589.A_I_TextField1_7)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[7]'] = message.text
    keyboard = Form_I_589_Immigration_Court_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Check the button, that applies", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="never_been_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = callback_query.data
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are never been in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="now_in_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = callback_query.data
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are now in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="not_now_but_been_in_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are not now in Immigration Court proceedings, but I have been in the past")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_94_Number_Choice()
    await bot.send_message(message.from_user.id, "Enter What is your current I-94 Number, if any?", reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_I_TextField3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List most recent entry entry into the U.S. Enter date of your most recent entry:")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List most recent entry entry into the U.S. Enter place of your most recent entry:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List most recent entry entry into the U.S. Enter status of your most recent entry:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List most recent entry entry into the U.S. Enter date status of your most recent entry expires :")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List second most recent entry entry into the U.S. Enter date:")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List second most recent entry entry into the U.S. Enter place:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List second most recent entry entry into the U.S. Enter status:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List third most recent entry entry into the U.S. Enter date:")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List third most recent entry entry into the U.S. Enter place:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "List third most recent entry entry into the U.S. Enter status:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What country issued your last passport or travel document?")


@dp.message_handler(state=Form_I_589.A_I_TextField5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport Number")


@dp.message_handler(state=Form_I_589.A_I_TextField5_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Travel Document Number")


@dp.message_handler(state=Form_I_589.A_I_TextField5_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Expiration Date (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What is your native language (include dialect, if applicable)?")


@dp.message_handler(state=Form_I_589.A_I_TextField7_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField7[0]'] = message.text
    keyboard = Form_I_589_English_Fluency_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Are you fluent in English?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_eng_fluent",
                           state=Form_I_589.A_I_EngFluencyChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox4[1]'] = callback_query.data
        data['[0].CheckBox4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are fluent in English")
    await bot.send_message(callback_query.from_user.id, "Enter What other languages do you speak fluently?")


@dp.callback_query_handler(text="no_eng_fluent",
                           state=Form_I_589.A_I_EngFluencyChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox4[0]'] = callback_query.data
        data['[0].CheckBox4[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you are not fluent in English")
    await bot.send_message(callback_query.from_user.id, "Enter What other languages do you speak fluently?")


@dp.message_handler(state=Form_I_589.A_I_TextField7_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField7[1]'] = message.text
        is_married = data['[1].CheckBox5[0]']
        is_divorced = data['[1].CheckBox5[0]']
    if is_married:
        await Form_I_589.next()
        await bot.send_message(message.from_user.id, "You have indicated that you are married")
        await bot.send_message(message.from_user.id,
                               "Enter your spouse's Alien Registration Number of your spouse (A-Number)\n(if any)?")
    if is_divorced:
        await Form_I_589.A_II_HaveChildrenChoice.set()
        await bot.send_message(message.from_user.id, "You have indicated that you are not married")
        keyboard = Form_I_589_Have_Children_Choice()
        await bot.send_message(message.from_user.id,
                               "Do you have children? (regardless of age, location, or marital status)",
                               reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine1_ANumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your spouse (if any)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your spouse (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_DateTimeField7_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].DateTimeField7[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number of your spouse (if any)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Complete Last Name of your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine5_LastName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine5_LastName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "First Name of your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine6_FirstName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine6_FirstName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Middle Name of your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine7_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine7_MiddleName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Other names of your spouse used (include maiden name and aliases)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Marriage with your spouse (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_DateTimeField8_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].DateTimeField8[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Place of Marriage with your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Your spouse City and Country of Birth")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your spouse (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[6]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose Gender of your spouse", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = ""
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is female")
    await bot.send_message(callback_query.from_user.id, "Is this person in the U.S.?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = callback_query.data
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is male")
    await bot.send_message(callback_query.from_user.id, "Is this person in the U.S.?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_IsInUSChoiceSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[0]'] = ""
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[1]'] = callback_query.data
    await Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is in US")
    await bot.send_message(callback_query.from_user.id, "Provide place of last entry of your spouse into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_IsInUSChoiceSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[0]'] = callback_query.data
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[1]'] = ""
    await Form_I_589.A_II_NotMarried_0_PtAIILine15_Specify_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is not in US")
    await bot.send_message(callback_query.from_user.id, "Specify location of your spouse")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine15_Specify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_Specify[0]'] = message.text
    keyboard = Form_I_589_Have_Children_Choice()
    await Form_I_589.A_II_HaveChildrenChoice.set()
    await bot.send_message(message.from_user.id, "Do you have children? (regardless of age, location, or marital status)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine16_PlaceofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of last entry into the U.S. of your spouse (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine17_DateofLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine17_DateofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "I-94 Number of your spouse (send 0 if you don't have I-94 number)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine18_I94Number_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Status of your spouse when last admitted (Visa type, if any) (send 0 if you didn't have had Status when last admitted)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What is your spouse's current status?")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine20_SpouseCurrentStatus_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine20_SpouseCurrentStatus[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What is the expiration date of your spouse authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Spouse_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id, "Is your spouse in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_spouse_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine22_No[0]'] = ""
        data['[1].NotMarried[0].PtAIILine22_Yes[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You have indicated that your spouse is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "If previously in the U.S., date of previous arrival (mm/dd/yyyy) else send 0")


@dp.callback_query_handler(text="no_spouse_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine22_No[0]'] = callback_query.data
        data['[1].NotMarried[0].PtAIILine22_Yes[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that your spouse is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "If previously in the U.S., date of previous arrival of your spouse (mm/dd/yyyy) else send 0")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0":
            data['[1].NotMarried[0].PtAIILine23_PreviousArrivalDate[0]'] = message.text
        else:
            data['[1].NotMarried[0].PtAIILine23_PreviousArrivalDate[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Spouse_Choice()
    await bot.send_message(message.from_user.id, "If in the U.S., is your spouse to be included in this application?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_spouse",
                           state=Form_I_589.A_II_IsSpouseIncludedInApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
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
async def process(callback_query: types.CallbackQuery,
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


@dp.callback_query_handler(text="dont_have_children",
                           state=Form_I_589.A_II_HaveChildrenChoice)
async def process(callback_query: types.CallbackQuery,
                                          state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildrenCheckbox[0]'] = ""
        data['[1].ChildrenCheckbox[1]'] = callback_query.data
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you don't have children")
    await bot.send_message(callback_query.from_user.id, "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


@dp.callback_query_handler(text="have_children",
                           state=Form_I_589.A_II_HaveChildrenChoice)
async def process(callback_query: types.CallbackQuery,
                                          state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildrenCheckbox[0]'] = callback_query.data
        data['[1].ChildrenCheckbox[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that you have children")
    await bot.send_message(callback_query.from_user.id, "Total number of children:")


@dp.message_handler(state=Form_I_589.A_II_TotalChild_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].TotalChild[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Alien Registration Number of your first child (A-Number) (if any)")


# Child 1
@dp.message_handler(state=Form_I_589.A_II_ChildAlien1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your first child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status of your first child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number of your first child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your first child")


@dp.message_handler(state=Form_I_589.A_II_ChildLast1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your first child")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your first child")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your first child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your first child")


@dp.message_handler(state=Form_I_589.A_II_ChildCity1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your first child (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your first child")


@dp.message_handler(state=Form_I_589.A_II_ChildRace1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of your first child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox16[1]'] = callback_query.data
        data['[1].CheckBox16[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild1
                           )
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox16[0]'] = callback_query.data
        data['[1].CheckBox16[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox17[0]'] = callback_query.data
        data['[1].CheckBox17[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox17[1]'] = callback_query.data
        data['[1].CheckBox17[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is not in U.S")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify[0]'] = message.text
        total_number_of_children = data["[1].TotalChild[0]"]

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(message.from_user.id,
                               "Do you wish fill same data for your second child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your first child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_ExpirationDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine15_ExpirationDate[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number (If any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status when last admitted of your first child (Visa type, if any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is current status of your first child?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_CurrentStatusofChild_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine18_CurrentStatusofChild[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your first child authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your first child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = callback_query.data
        data['[1].PtAIILine20_No[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = ""
        data['[1].PtAIILine20_No[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
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
                               "Do you wish fill same data for your second child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
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
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) of your second child")


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 2
@dp.message_handler(state=Form_I_589.A_II_ChildAlien2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your second child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status of your second child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number of your second child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildLast2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your second child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildCity2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your second child (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildRace2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of your second child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox26_Gender[0]'] = callback_query.data
        data['[3].CheckBox26_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox26_Gender[1]'] = callback_query.data
        data['[3].CheckBox26_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox27[0]'] = callback_query.data
        data['[1].CheckBox27[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox27[1]'] = callback_query.data
        data['[1].CheckBox27[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is not in U.S")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify2[0]'] = message.text
        total_number_of_children = data["[1].TotalChild[0]"]

    if total_number_of_children > 2:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(message.from_user.id,
                               "Do you wish fill same data for your third child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your second child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your second child (If any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your second child when last admitted (Visa type, if any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your second child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your second child authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your second child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes2[0]'] = callback_query.data
        data['[1].PtAIILine20_No2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes2[0]'] = ""
        data['[1].PtAIILine20_No2[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes2[0]'] = callback_query.data
        data['[1].PtAIILine21_No2[0]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is to be included in this application")

    if total_number_of_children > 2:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes2[0]'] = ""
        data['[1].PtAIILine21_No2[0]'] = callback_query.data
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is to be included in this application")

    if total_number_of_children > 2:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your third child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) of your third child")


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 3
@dp.message_handler(state=Form_I_589.A_II_ChildAlien3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your third child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status of your third child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number of your third child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildLast3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your third child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildCity3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your third child (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildRace3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of your third child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox36_Gender[0]'] = callback_query.data
        data['[3].CheckBox36_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox36_Gender[1]'] = callback_query.data
        data['[3].CheckBox36_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox37[0]'] = callback_query.data
        data['[1].CheckBox37[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S of your third child")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox37[1]'] = callback_query.data
        data['[1].CheckBox37[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is not in U.S")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify3[0]'] = message.text
        total_number_of_children = data["[1].TotalChild[0]"]

    if total_number_of_children > 3:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(message.from_user.id,
                               "Do you wish fill same data for your fourth child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. of your third child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your third child (If any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your third child when last admitted  (Visa type, if any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your third child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your third child authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your third child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes3[0]'] = callback_query.data
        data['[1].PtAIILine20_No3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes3[0]'] = ""
        data['[1].PtAIILine20_No3[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes3[0]'] = callback_query.data
        data['[1].PtAIILine21_No3[0]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is to be included in this application")

    if total_number_of_children > 3:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your fourth child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes3[0]'] = ""
        data['[1].PtAIILine21_No3[0]'] = callback_query.data
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is to be included in this application")

    if total_number_of_children > 3:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your next child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number of your fourth child (A-Number) (if any)")


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 4
@dp.message_handler(state=Form_I_589.A_II_ChildAlien4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your fourth child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status of your fourth child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number of your fourth child (if any)")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildLast4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your fourth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildCity4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your fourth child (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildRace4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of your fourth child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox46_Gender[0]'] = callback_query.data
        data['[3].CheckBox46_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox46_Gender[1]'] = callback_query.data
        data['[3].CheckBox46_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox47[0]'] = callback_query.data
        data['[1].CheckBox47[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox47[1]'] = callback_query.data
        data['[1].CheckBox47[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is not in U.S")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify4[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
    await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your fourth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your fourth child (If any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your fourth child when last admitted (Visa type, if any)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your fourth child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your fourth child authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your fourth child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes4[0]'] = callback_query.data
        data['[1].PtAIILine20_No4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes4[0]'] = ""
        data['[1].PtAIILine20_No4[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes4[0]'] = callback_query.data
        data['[1].PtAIILine21_No4[0]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is to be included in this application")

    if total_number_of_children > 4:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild5.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your fifth child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes4[0]'] = ""
        data['[1].PtAIILine21_No4[0]'] = callback_query.data
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is to be included in this application")

    if total_number_of_children > 4:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild5.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your fifth child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number of your fifth child (A-Number) (if any)")


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 5
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[6]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your fifth child (if any)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_7)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[7]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status of your fifth child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_8)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[8]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number of your fifth child (if any)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_9)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[9]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your fifth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your fifth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your fifth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your fifth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.Supplement_A_DateTimeField14_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].DateTimeField14[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your fifth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your fifth child (Citizenship)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your fifth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[5]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of your fifth child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.Supplement_A_ChooseGenderChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox12_Gender[1]'] = callback_query.data
        data['[12].CheckBox12_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fifth child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.Supplement_A_ChooseGenderChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox12_Gender[1]'] = ""
        data['[12].CheckBox12_Gender[0]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fifth child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox57[0]'] = callback_query.data
        data['[12].CheckBox57[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fifth child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox57[0]'] = ""
        data['[12].CheckBox57[1]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fifth child is not in U.S")


@dp.message_handler(state=Form_I_589.Supplement_A_SuppLALine13_Specify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppLALine13_Specify[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
    await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.Supplement_A_ChildEntry5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildEntry5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your fifth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildExp5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExp5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your fifth child (If any)")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildINum5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your fifth child when last admitted (Visa type, if any)")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildStatus5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your fifth child's current status?")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildCurrent5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildCurrent5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your fifth child authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildExpAuth5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth5[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your fifth child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[0]'] = callback_query.data
        data['[12].SuppA_CheckBox20[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fifth child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[1]'] = callback_query.data
        data['[12].SuppA_CheckBox20[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fifth child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.Supplement_A_IsIncludedInApplicationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[0]'] = callback_query.data
        data['[12].SuppA_CheckBox20[1]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fifth child is to be included in this application")

    if total_number_of_children > 5:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild6.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your sixth child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.Supplement_A_IsIncludedInApplicationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[1]'] = callback_query.data
        data['[12].SuppA_CheckBox20[0]'] = ""
        total_number_of_children = data["[1].TotalChild[0]"]
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fifth child is to be included in this application")

    if total_number_of_children > 5:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild6.set()
        await bot.send_message(callback_query.from_user.id,
                               "Do you wish fill same data for your sixth child?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number of your sixth child (A-Number) (if any)")


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 6
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_16)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[16]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Passport/ID Card Number of your sixth child (if any)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_17)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[17]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Marital Status of your sixth child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_18)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[18]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "U.S. Social Security Number of your sixth child (if any)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_19)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[19]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your sixth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_10)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[10]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your sixth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_12)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[12]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your sixth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_13)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[13]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your sixth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.Supplement_A_DateTimeField14_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].DateTimeField14[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your sixth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_11)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[11]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your sixth child (Citizenship)")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_14)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[14]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your sixth child")


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_15)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[15]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose gender of your sixth child", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.Supplement_A_ChooseGenderChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL12_CheckBox[1]'] = callback_query.data
        data['[12].SuppAL12_CheckBox[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your sixth child is female")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.Supplement_A_ChooseGenderChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL12_CheckBox[0]'] = callback_query.data
        data['[12].SuppAL12_CheckBox[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "You indicated that your sixth child is male")
    await bot.send_message(callback_query.from_user.id, "Is this child in U.S?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL13_CheckBox[0]'] = callback_query.data
        data['[12].SuppAL13_CheckBox[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your sixth child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL13_CheckBox[1]'] = callback_query.data
        data['[12].SuppAL13_CheckBox[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your sixth child is not in U.S")


@dp.message_handler(state=Form_I_589.Supplement_A_SuppLALine13_Specify2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppLALine13_Specify2[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
    await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.Supplement_A_ChildEntry6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildEntry6[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. of your sixth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildExp6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExp6[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your sixth child (If any)")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildINum6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum6[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your sixth child when last admitted (Visa type, if any")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildStatus6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus6[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your sixth child's current status?")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildCurrent6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildCurrent6[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your sixth child authorized stay, if any? (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.Supplement_A_ChildExpAuth6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your sixth child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppALine20_CheckBox2[0]'] = callback_query.data
        data['[12].SuppALine20_CheckBox2[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your sixth child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppALine20_CheckBox2[1]'] = callback_query.data
        data['[12].SuppALine20_CheckBox2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your sixth child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?")


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.Supplement_A_IsIncludedInApplicationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppALine21_CheckBox[0]'] = callback_query.data
        data['[12].SuppALine21_CheckBox[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your sixth child is to be included in this application")

    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.Supplement_A_IsIncludedInApplicationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[1]'] = callback_query.data
        data['[12].SuppA_CheckBox20[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your sixth child is to be included in this application")
    await bot.send_message(callback_query.from_user.id,
                               "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Last address with no fear of persecution
@dp.message_handler(state=Form_I_589.A_III_TextField13_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter City/Town of your last address where you lived before coming to the United States where you DON'T FEAR persecution")


@dp.message_handler(state=Form_I_589.A_III_TextField13_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Department, Province, or State of your last address where you lived before coming to the United States where you don't fear persecution")


@dp.message_handler(state=Form_I_589.A_III_TextField13_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Country of your last address where you lived before coming to the United States where you don't fear persecution")


@dp.message_handler(state=Form_I_589.A_III_TextField13_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[6]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date From (Mo/Yr) you were living on your last address where you lived before coming to the United States where you don't fear persecution")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField21_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField21[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Last Date (Mo/Yr) when you were living on your last address where you lived before coming to the United States where you don't fear persecution")


# Address Where Fear Persecution
@dp.message_handler(state=Form_I_589.A_III_DateTimeField20_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField20[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List your last address where you lived before coming to the United States where you FEAR persecution. First enter Number and Street")


# Last address with fear of persecution
@dp.message_handler(state=Form_I_589.A_III_TextField13_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter City/Town of your last address where you lived before coming to the United States where you FEAR persecution")


@dp.message_handler(state=Form_I_589.A_III_TextField13_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Department, Province, or State of your last address where you lived before coming to the United States where you fear persecution")


@dp.message_handler(state=Form_I_589.A_III_TextField13_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Country of your last address where you lived before coming to the United States where you fear persecution")


@dp.message_handler(state=Form_I_589.A_III_TextField13_7)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[7]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date From (Mo/Yr) you were living on your last address where you lived before coming to the United States where you fear persecution")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField22_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField22[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Last Date (Mo/Yr) when you were living on your last address where you lived before coming to the United States where you don't fear persecution")


# Present Address
@dp.message_handler(state=Form_I_589.A_III_DateTimeField23_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField23[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List your present address. First Enter Number and Street")


@dp.message_handler(state=Form_I_589.A_III_TextField13_8)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[8]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List your present address. Enter City/Town")


@dp.message_handler(state=Form_I_589.A_III_TextField13_10)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[10]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List your present address. Enter Department, Province, or State")


@dp.message_handler(state=Form_I_589.A_III_TextField13_12)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[12]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List your present address. Enter Country")


@dp.message_handler(state=Form_I_589.A_III_TextField13_14)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[14]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List your present address. Enter Date when you moved in")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField24_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField24[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List your present address. Enter Date when you planning to move out")


# First Residence
@dp.message_handler(state=Form_I_589.A_III_DateTimeField26_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField26[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your residences during the past 5 years. Enter Number and Street of first residence")


@dp.message_handler(state=Form_I_589.A_III_TextField13_9)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[9]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter City/Town")


@dp.message_handler(state=Form_I_589.A_III_TextField13_11)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[11]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Department, Province, or State")


@dp.message_handler(state=Form_I_589.A_III_TextField13_13)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[13]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Country")


@dp.message_handler(state=Form_I_589.A_III_TextField13_15)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[15]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved in")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField25_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField25[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved out")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField27_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField27[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your residences during the past 5 years. Enter Number and Street of second residence")


# Second Residence
@dp.message_handler(state=Form_I_589.A_III_TextField13_16)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[16]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your residences during the past 5 years. Enter City/Town of second residence")


@dp.message_handler(state=Form_I_589.A_III_TextField13_17)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[17]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Department, Province, or State")


@dp.message_handler(state=Form_I_589.A_III_TextField13_18)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[18]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Country")


@dp.message_handler(state=Form_I_589.A_III_TextField13_19)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[19]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved in")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField28_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField28[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved out")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField29_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField29[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your residences during the past 5 years. Enter Number and Street of third residence")


# Third Residence
@dp.message_handler(state=Form_I_589.A_III_TextField13_20)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[20]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter City/Town")


@dp.message_handler(state=Form_I_589.A_III_TextField13_21)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[21]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Department, Province, or State")


@dp.message_handler(state=Form_I_589.A_III_TextField13_22)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[23]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Country")


@dp.message_handler(state=Form_I_589.A_III_TextField13_23)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[22]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved in")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField30_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField30[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved out")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField31_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField31[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your residences during the past 5 years. Enter Number and Street of fourth residence")


# Fourth Residence
@dp.message_handler(state=Form_I_589.A_III_TextField13_24)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[24]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter City/Town")


@dp.message_handler(state=Form_I_589.A_III_TextField13_25)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[25]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Department, Province, or State")


@dp.message_handler(state=Form_I_589.A_III_TextField13_26)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[26]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Country")


@dp.message_handler(state=Form_I_589.A_III_TextField13_23)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[27]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved in")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField32_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField32[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date when you moved out")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField31_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField33[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your education, beginning with the most recent school that you attended. Enter Name of School")


# First School
@dp.message_handler(state=Form_I_589.A_III_TextField13_28)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[28]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Type of School")


@dp.message_handler(state=Form_I_589.A_III_TextField13_30)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[30]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Location (Address)")


@dp.message_handler(state=Form_I_589.A_III_TextField13_32)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[32]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended From (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField41_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField41[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended To (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField40_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField40[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Second Name of School")


# Second School
@dp.message_handler(state=Form_I_589.A_III_TextField13_29)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[29]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Type of School")


@dp.message_handler(state=Form_I_589.A_III_TextField13_31)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[31]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Location (Address)")


@dp.message_handler(state=Form_I_589.A_III_TextField13_33)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[33]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended From (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField38_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField38[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended To (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField39_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField39[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your education, beginning with the third school that you attended. Enter Name of School")


# Third School
@dp.message_handler(state=Form_I_589.A_III_TextField13_34)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[34]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Type of School")


@dp.message_handler(state=Form_I_589.A_III_TextField13_35)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[35]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Location (Address)")


@dp.message_handler(state=Form_I_589.A_III_TextField13_36)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[36]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended From (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField37_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField37[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended To (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField39_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField36[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your education, beginning with the fourth school that you attended. Enter Name of School")


# Fourth School
@dp.message_handler(state=Form_I_589.A_III_TextField13_37)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[37]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Type of School")


@dp.message_handler(state=Form_I_589.A_III_TextField13_38)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[38]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Location (Address)")


@dp.message_handler(state=Form_I_589.A_III_TextField13_39)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[39]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended From (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField34_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField34[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Attended To (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField35_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField35[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Name and Address of Employer")


# First Employer
@dp.message_handler(state=Form_I_589.A_III_TextField13_40)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[40]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Your Occupation")


@dp.message_handler(state=Form_I_589.A_III_TextField13_42)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[42]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Dates From (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField42_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField42[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Dates To (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField44_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField44[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. Enter Name and Address of Employer")


# Second Employer
@dp.message_handler(state=Form_I_589.A_III_TextField13_41)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[41]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Your Occupation")


@dp.message_handler(state=Form_I_589.A_III_TextField13_43)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[43]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Dates From (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField43_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField43[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Dates To (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField45_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField45[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. Enter Name and Address of Employer")


# Third Employer
@dp.message_handler(state=Form_I_589.A_III_TextField13_44)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[44]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Your Occupation")


@dp.message_handler(state=Form_I_589.A_III_TextField13_45)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[45]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Dates From (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField46_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField46[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your employment during the past 5 years. List your present employment first. Enter Dates To (Mo/Yr)")


@dp.message_handler(state=Form_I_589.A_III_DateTimeField47_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField47[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of Mother")


# Mother
@dp.message_handler(state=Form_I_589.A_III_TextField13_46)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[46]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter City/Town and Country of Birth of Mother")


@dp.message_handler(state=Form_I_589.A_III_TextField13_49)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[49]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Mother_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Is your mother Deceased?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_mother_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_m_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.m[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your Mother is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of Father")
    await Form_I_589.A_III_TextField13_47.set()


@dp.callback_query_handler(text="no_mother_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_m_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.m[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your Mother is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of Mother")
    await Form_I_589.A_III_TextField35_0.set()


@dp.message_handler(state=Form_I_589.A_III_TextField35_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of Father")


# Father
@dp.message_handler(state=Form_I_589.A_III_TextField13_47)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[47]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter City/Town and Country of Birth of Father")


@dp.message_handler(state=Form_I_589.A_III_TextField13_50)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[50]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Father_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Is your father Deceased?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_father_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_f_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.f[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your Father is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 1 Sibling")
    await Form_I_589.A_III_TextField13_48.set()


@dp.callback_query_handler(text="no_father_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_f_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.f[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your Father is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of Father")
    await Form_I_589.A_III_TextField35_1.set()


@dp.message_handler(state=Form_I_589.A_III_TextField35_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 1 Sibling")


# Sibling 1
@dp.message_handler(state=Form_I_589.A_III_TextField13_48)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[48]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter City/Town and Country of Birth of 1 Sibling")


@dp.message_handler(state=Form_I_589.A_III_TextField13_51)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[51]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_1Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Is your 1 sibling deceased?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_1sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s1[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 1 sibling is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 2 sibling")
    await Form_I_589.A_III_TextField13_52.set()


@dp.callback_query_handler(text="no_1sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s1[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 1 sibling is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of 1 sibling")
    await Form_I_589.A_III_TextField35_1.set()


@dp.message_handler(state=Form_I_589.A_III_TextField35_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 2 Sibling")


# Sibling 2
@dp.message_handler(state=Form_I_589.A_III_TextField13_52)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[52]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter City/Town and Country of Birth of 2 Sibling")


@dp.message_handler(state=Form_I_589.A_III_TextField13_53)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[53]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_2Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Is your 2 sibling deceased?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_2sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s2[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 2 sibling is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 3 sibling")
    await Form_I_589.A_III_TextField13_54.set()


@dp.callback_query_handler(text="no_2sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 2 sibling is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of 2 sibling")
    await Form_I_589.A_III_TextField35_1.set()


@dp.message_handler(state=Form_I_589.A_III_TextField35_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 3 Sibling")


# Sibling 3
@dp.message_handler(state=Form_I_589.A_III_TextField13_54)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[54]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter City/Town and Country of Birth of 3 Sibling")


@dp.message_handler(state=Form_I_589.A_III_TextField13_55)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[55]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_3Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Is your 3 sibling deceased?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_3sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s3[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 3 sibling is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 4 sibling")
    await Form_I_589.A_III_TextField13_56.set()


@dp.callback_query_handler(text="no_3sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 3 sibling is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of 3 sibling")
    await Form_I_589.A_III_TextField35_4.set()


@dp.message_handler(state=Form_I_589.A_III_TextField35_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 4 Sibling")


# Sibling 4
@dp.message_handler(state=Form_I_589.A_III_TextField13_56)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[56]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter City/Town and Country of Birth of 4 Sibling")


@dp.message_handler(state=Form_I_589.A_III_TextField13_57)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[57]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_3Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Is your 4 sibling deceased?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_4sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s4[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 4 sibling is deceased")
    keyboard = Form_I_589_Asylum_Reason_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "I am seeking asylum or withholding of removal based on:",
                           reply_markup=keyboard.markup)
    await Form_I_589.B_Asylum_Reason_Choice.set()


@dp.callback_query_handler(text="no_4sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\.s4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 4 sibling is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of 4 sibling")
    await Form_I_589.A_III_TextField35_5.set()


@dp.message_handler(state=Form_I_589.A_III_TextField35_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[5]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Asylum_Reason_Choice()
    await bot.send_message(message.from_user.id,
                           "I am seeking asylum or withholding of removal based on:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="race_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxrace[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you seeking asylum or withholding of removal based on Race")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you, your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="religion_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxreligion[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you seeking asylum or withholding of removal based on Religion")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you, your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="nationality_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxnationality[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you seeking asylum or withholding of removal based on Nationality")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you, your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="political_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxpolitics[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you seeking asylum or withholding of removal based on Political opinion")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you, your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="membership_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxsocial[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you seeking asylum or withholding of removal based on Membership in a particular social group")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you, your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="torture_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxtorture[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you seeking asylum or withholding of removal based on Torture Convention")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you, your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_family_harm",
                           state=Form_I_589.B_Family_Experienced_Harm_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1a[0]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1a[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that  your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone")
    await bot.send_message(callback_query.from_user.id,
                           "Explain in detail:\n"
                           "1. What happened;\n"
                           "2. When the harm or mistreatment or threats occurred;\n"
                           "3. Who caused the harm or mistreatment or threats;\n"
                           "Why you believe the harm or mistreatment or threats occurred")


@dp.callback_query_handler(text="no_family_harm",
                           state=Form_I_589.B_Family_Experienced_Harm_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1a[1]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1a[0]'] = ""
    await Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that  your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone")
    keyboard = Form_I_589_You_Fear_Harm_Or_Mistreatment_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Do you fear harm or mistreatment if you return to your home country?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_you_fear_harm",
                           state=Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1b[0]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1b[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you fear harm or mistreatment if you return to your home country")
    keyboard = Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you or your family members ever been accused, charged, arrested, detained, interrogated, convicted and sentenced, or imprisoned in any country other than the United States (including for an immigration law violation)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_you_fear_harm",
                           state=Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1b[1]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1b[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that you don't fear harm or mistreatment if you return to your home country")
    keyboard = Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you or your family members ever been accused, charged, arrested, detained, interrogated, convicted and sentenced, or imprisoned in any country other than the United States (including for an immigration law violation)?",
                           reply_markup=keyboard.markup)





