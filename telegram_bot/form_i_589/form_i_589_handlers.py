from aiogram import types
from aiogram.dispatcher import FSMContext, filters

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
    Form_I_589_Family_Experienced_Harm_Choice, Form_I_589_You_Been_Associated_With_Any_Organizations_Choice, \
    Form_I_589_You_Continue_To_Participate_In_Organizations_Choice, \
    Form_I_589_You_Afraid_Of_Being_Subjected_To_Torture_Choice, Form_I_589_Family_Applied_For_USRefugee_Status_Choice, \
    Form_I_589_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice, \
    Form_I_589_Family_Recieved_Any_Lawful_Status_Choice, Form_I_589_You_Or_Family_Caused_Harm_Or_Suffering_Choice, \
    Form_I_589_Returned_To_Bad_Country_Choice, Form_I_589_Last_Arrival_To_US_More_Than_1_Year_Choice, \
    Form_I_589_You_Or_Family_Did_Crime_Choice, Form_I_589_Family_Helped_Complete_Application_Choice, \
    Form_I_589_Family_Helped_Complete_Fill_Next_Member_Choice, Form_I_589_Not_Family_Helped_Complete_Application_Choice, \
    Form_I_589_Provided_With_List_Of_Persons_Who_May_Assist_Choice, Form_I_589_If_Any_Choice, \
    Form_I_589_Mailing_Address_Choice_Keyboard, Form_I_589_If_Applicable, Form_I_589_Child_Immigration_Court_Choice, \
    Form_I_589_If_Previously_In_US, Form_I_589_Include_Child_Choice, Form_I_589_4Sibling_Deceased_Choice

from telegram_bot.form_i_589.form_i_589_state_group import Form_I_589

from telegram_bot import \
    bot, \
    dp, \
    FillPdfFromJsonAdapter, \
    datetime


@dp.message_handler(filters.Command("end"), state='*')
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        adapter.save_json(data)
        await bot.send_message(message.chat.id,
                               "Your data for Form-I-589 form was successfully saved! Wait for pdf file.")
        await bot.send_chat_action(message.chat.id, "typing")
        pdf_file_path = adapter.fill_pdf()
        with open(pdf_file_path, 'rb') as file:
            await bot.send_document(message.chat.id, file)
    await state.finish()


@dp.callback_query_handler(text="I-589")
async def i_589_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-589"
    await bot.send_message(callback_query.from_user.id, "You've chosen the I-589 form. Let's start filling it")
    await bot.send_message(callback_query.from_user.id, "Part A.I. Information About You")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id, "Enter your Alien Registration Number(s) (A-Number) (if any)",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_PtAILine1_ANumber_0.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_PtAILine1_ANumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine1_ANumber[0]'] = ""
    await bot.send_message(callback_query.from_user.id,
                           "You chose to leave Alien Registration Number(s) (A-Number) blank")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id, "Enter U.S. Social Security Number (if any)",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_TextField1_0.set()


@dp.message_handler(state=Form_I_589.A_I_PtAILine1_ANumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your U.S. Social Security Number (if any)")


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[0]'] = ""
    await bot.send_message(callback_query.from_user.id, "You chose to leave U.S. Social Security Number blank")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id, "Enter USCIS Online Account Number (if any)",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_TextField1_8.set()


@dp.message_handler(state=Form_I_589.A_I_TextField1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "USCIS Online Account Number (if any)")


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField1_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[8]'] = ""
    await bot.send_message(callback_query.from_user.id, "You chose to leave USCIS Online Account Number blank")
    await bot.send_message(callback_query.from_user.id, "Enter Complete Last Name")
    await Form_I_589.A_I_PtAILine4_LastName_0.set()


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
    await bot.send_message(message.from_user.id, "Residence in the U.S. (where you physically reside). "
                                                 "Enter your Street Number and Name:")


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
    keyboard = Form_I_589_Mailing_Address_Choice_Keyboard()
    await bot.send_message(message.from_user.id,
                           "Is your mailing address different than the address of residence in the US?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="MailingSameAsResidence_Yes",
                           state=Form_I_589.A_I_Mailing_Address_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(callback_query.from_user.id, "Choose your Gender",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_ChooseGender.set()


@dp.callback_query_handler(text="MailingSameAsResidence_No",
                           state=Form_I_589.A_I_Mailing_Address_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = Form_I_589_If_Applicable()
    await bot.send_message(callback_query.from_user.id, "Enter In Care Of (if applicable)",
                           reply_markup=keyboard.markup)
    await Form_I_589.next()


@dp.callback_query_handler(text="not_applicable",
                           state=Form_I_589.A_I_PtAILine9_InCareOf_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "Enter Telephone Area Code")
    await Form_I_589.A_I_PtAILine9_AreaCode_0.set()


# @dp.message_handler(state=Form_I_589.A_I_PtAILine8_TelephoneNumber_0)
# async def process(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['[0].PtAILine8_TelephoneNumber[0]'] = message.text
#     await Form_I_589.next()
#     await bot.send_message(message.from_user.id, "Enter In Care Of (if applicable):")


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
        data['[1].CheckBox5[0]'] = "x"
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
        data['[1].CheckBox5[0]'] = ""
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
        data['[1].CheckBox5[0]'] = "x"
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
        data['[1].CheckBox5[0]'] = "x"
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
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that you are never been in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="now_in_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = callback_query.data
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that you are now in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.callback_query_handler(text="not_now_but_been_in_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that you are not now in Immigration Court proceedings, but I have been in the past")
    await bot.send_message(callback_query.from_user.id, "Enter When did you last leave your country? (mm/dd/yyyy):")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter What is your current I-94 Number, if any?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField3[0]'] = ""
    await Form_I_589.A_I_DateTimeField2_0.set()
    await bot.send_message(callback_query.from_user.id, "You have indicated that you don't have I-94 number")
    await bot.send_message(callback_query.from_user.id,
                           "List most recent entry entry into the U.S. Enter date of your most recent entry:")


@dp.message_handler(state=Form_I_589.A_I_TextField3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List most recent entry entry into the U.S. Enter date of your most recent entry:")


@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List most recent entry entry into the U.S. Enter place of your most recent entry:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List most recent entry entry into the U.S. Enter status of your most recent entry:")


@dp.message_handler(state=Form_I_589.A_I_TextField4_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "List most recent entry entry into the U.S. Enter date status of your most recent entry expires :")


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
        is_married = data['[0].Marital[1]']
        is_not_married = not data['[0].Marital[1]']
    await bot.send_message(message.from_user.id, "You filled Part A.I. Information About You completely, next is:")
    await bot.send_message(message.from_user.id, "Part A.II. Information About Your Spouse and Children")
    if is_married:
        await Form_I_589.next()
        await bot.send_message(message.from_user.id, "You have indicated that you are married")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(message.from_user.id,
                               "Enter your spouse's Alien Registration Number of your spouse (A-Number)\n(if any)?",
                               reply_markup=keyboard.markup)
    if is_not_married:
        await Form_I_589.A_II_HaveChildrenChoice.set()
        await bot.send_message(message.from_user.id, "You have indicated that you are not married")
        keyboard = Form_I_589_Have_Children_Choice()
        await bot.send_message(message.from_user.id,
                               "Do you have children? (regardless of age, location, or marital status)",
                               reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine1_ANumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine1_ANumber[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Passport/ID Card Number of your spouse (if any)?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine1_ANumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Passport/ID Card Number of your spouse (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_TextField10_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Date of Birth of your spouse (mm/dd/yyyy)?")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "U.S. Social Security Number of your spouse (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_TextField10_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Complete Last Name of your spouse")


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


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[6]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Choose Gender of your spouse", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_TextField10_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Complete Last Name of your spouse")


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
    await bot.send_message(message.from_user.id,
                           "Do you have children? (regardless of age, location, or marital status)",
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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "I-94 Number of your spouse (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine18_I94Number_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Status of your spouse when last admitted (Visa type if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine18_I94Number_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Status of your spouse when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "What is your spouse s current status?")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What is your spouse's current status?")


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine20_SpouseCurrentStatus_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine20_SpouseCurrentStatus[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "What is the expiration date of your spouse authorized stay, if any? (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Spouse_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your spouse in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Spouse_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your spouse in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_spouse_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine22_No[0]'] = ""
        data['[1].NotMarried[0].PtAIILine22_Yes[0]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_If_Previously_In_US()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that your spouse is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If previously in the U.S., date of previous arrival (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_spouse_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine22_No[0]'] = callback_query.data
        data['[1].NotMarried[0].PtAIILine22_Yes[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Previously_In_US()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that your spouse is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If previously in the U.S., date of previous arrival of your spouse (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="not_previously_in_us",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Spouse_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated that your spouse was not in US previously")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is your spouse to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine23_PreviousArrivalDate[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Spouse_Choice()
    await bot.send_message(message.from_user.id, "If in the U.S., is your spouse to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_spouse",
                           state=Form_I_589.A_II_IsSpouseIncludedInApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine24_No[0]'] = ""
        data['[1].NotMarried[0].PtAIILine24_Yes[0]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Have_Children_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "You have indicated your spouse to be included in this application")
    await bot.send_message(callback_query.from_user.id,
                           "Do you have children? (regardless of age, location, or marital status)",
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
    await bot.send_message(callback_query.from_user.id,
                           "Do you have children? (regardless of age, location, or marital status)",
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
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Alien Registration Number of your first child (A-Number) (if any)",
                           reply_markup=keyboard.markup)


# Child 1

@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildAlien1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien1[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Passport/ID Card Number of your first child (if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_ChildAlien1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Passport/ID Card Number of your first child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport1[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Marital Status of your first child (Married Single Divorced Widowed)")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "U.S. Social Security Number of your first child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN1[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter complete Last Name of your first child")


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
    await bot.send_message(callback_query.from_user.id, "You indicated that your first child is not in U.S")
    total_number_of_children = int(data["[1].TotalChild[0]"])

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


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify[0]'] = message.text
        total_number_of_children = int(data["[1].TotalChild[0]"])

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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your first child (If any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Status when last admitted of your first child (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter Status when last admitted of your first child (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter What is current status of your first child?")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your first child authorized stay, if any? (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your first child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your first child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = callback_query.data
        data['[1].PtAIILine20_No[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your first child is in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = ""
        data['[1].PtAIILine20_No[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your first child is not in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes[0]'] = callback_query.data
        data['[1].PtAIILine21_No[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your first child is to be included in this application")

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
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your first child is to be included in this application")

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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) of your second child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 2
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildAlien2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Passport/ID Card Number of your second child (if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_ChildAlien2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Passport/ID Card Number of your second child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildPassport2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Marital Status of your second child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildPassport2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Marital Status of your second child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMarital2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "U.S. Social Security Number of your second child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter complete Last Name of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter complete Last Name of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildLast2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildLast2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildFirst2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMiddle2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your second child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildDOB2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildCity2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildCity2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your second child (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildNat2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your second child")


@dp.message_handler(state=Form_I_589.A_II_ChildRace2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildRace2[0]'] = message.text
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
        data['[3].CheckBox27[0]'] = callback_query.data
        data['[3].CheckBox27[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry2_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox27[1]'] = callback_query.data
        data['[3].CheckBox27[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])

    await bot.send_message(callback_query.from_user.id, "You indicated that your second child is not in U.S")

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


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine13_Specify2[0]'] = message.text
        total_number_of_children = int(data["[1].TotalChild[0]"])

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
        data['[3].PtAIILine14_PlaceofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your second child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your second child (If any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Status of your second child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your second child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter What is your second child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your second child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your second child authorized stay, if any? (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your second child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your second child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your second child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes2[0]'] = callback_query.data
        data['[3].PtAIILine20_No2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your first child is in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes2[0]'] = ""
        data['[3].PtAIILine20_No2[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your second child is not in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine21_Yes2[0]'] = callback_query.data
        data['[3].PtAIILine21_No2[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your second child is to be included in this application")

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
        data['[3].PtAIILine21_Yes2[0]'] = ""
        data['[3].PtAIILine21_No2[0]'] = callback_query.data
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your second child is to be included in this application")

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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) of your third child",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 3
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildAlien3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien3[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Passport/ID Card Number of your third child (if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_ChildAlien3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Passport/ID Card Number of your third child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Marital Status of your third child (Married Single Divorced Widowed)")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "U.S. Social Security Number of your third child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter complete Last Name of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildLast3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildLast3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildFirst3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMiddle3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your third child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildDOB3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildCity3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildCity3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your third child (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildNat3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your third child")


@dp.message_handler(state=Form_I_589.A_II_ChildRace3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildRace3[0]'] = message.text
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
        data['[3].CheckBox37[0]'] = callback_query.data
        data['[3].CheckBox37[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry3_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S of your third child")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox37[1]'] = callback_query.data
        data['[3].CheckBox37[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id, "You indicated that your third child is not in U.S")

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


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine13_Specify3[0]'] = message.text
        total_number_of_children = int(data["[1].TotalChild[0]"])

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
        data['[3].PtAIILine14_PlaceofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. of your third child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your third child (If any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number3[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Status of your third child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your third child when last admitted  (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter What is your ершкв child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your third child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your third child authorized stay, if any? (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay3[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your third child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your third child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes3[0]'] = callback_query.data
        data['[3].PtAIILine20_No3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your third child is in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes3[0]'] = ""
        data['[3].PtAIILine20_No3[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your third child is not in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine21_Yes3[0]'] = callback_query.data
        data['[3].PtAIILine21_No3[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your third child is to be included in this application")

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
        data['[3].PtAIILine21_Yes3[0]'] = ""
        data['[3].PtAIILine21_No3[0]'] = callback_query.data
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your third child is to be included in this application")

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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) of your fourth child",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 4
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildAlien4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien4[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Passport/ID Card Number of your fourth child (if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_ChildAlien4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Passport/ID Card Number of your fourth child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildPassport4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Marital Status of your fourth child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildPassport4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildPassport4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Marital Status of your fourth child (Married Single Divorced Widowed)")


@dp.message_handler(state=Form_I_589.A_II_ChildMarital4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMarital4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "U.S. Social Security Number of your fourth child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter complete Last Name of your foruth child")


@dp.message_handler(state=Form_I_589.A_II_ChildSSN4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter complete Last Name of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildLast4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildLast4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter First Name of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildFirst4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildFirst4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Middle Name of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildMiddle4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMiddle4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Date of Birth of your fourth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_ChildDOB4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildDOB4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "City and Country of Birth of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildCity4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildCity4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Nationality of your fourth child (Citizenship)")


@dp.message_handler(state=Form_I_589.A_II_ChildNat4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildNat4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Race, Ethnic, or Tribal Group of your fourth child")


@dp.message_handler(state=Form_I_589.A_II_ChildRace4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildRace4[0]'] = message.text
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
        data['[3].CheckBox47[0]'] = callback_query.data
        data['[3].CheckBox47[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry4_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox47[1]'] = callback_query.data
        data['[3].CheckBox47[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])

    await bot.send_message(callback_query.from_user.id, "You indicated that your fourth child is not in U.S")

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


@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine13_Specify4[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
    await Form_I_589.A_III_TextField13_0.set()


@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine14_PlaceofLastEntry4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Date of last entry into the U.S. for your fourth child (mm/dd/yyyy)")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your fourth child (If any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number4[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Status of your fourth child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your fourth child when last admitted  (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter What is your fourth child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter What is your fourth child's current status?")


@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your fourth child authorized stay, if any? (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay4[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your fourth child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your fourth child in Immigration Court proceedings?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes4[0]'] = callback_query.data
        data['[3].PtAIILine20_No4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fourth child is in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes4[0]'] = ""
        data['[3].PtAIILine20_No4[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fourth child is not in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine21_Yes4[0]'] = callback_query.data
        data['[3].PtAIILine21_No4[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fourth child is to be included in this application")

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
        data['[3].PtAIILine21_Yes4[0]'] = ""
        data['[3].PtAIILine21_No4[0]'] = callback_query.data
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fourth child is to be included in this application")

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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) of your fifth child",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 5
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[6]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Passport/ID Card Number of your fifth child (if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[6]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Passport/ID Card Number of your fifth child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_7)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[7]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Marital Status of your fifth child (Married Single Divorced Widowed)")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "U.S. Social Security Number of your fifth child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_9)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[9]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter complete Last Name of your fifth child")


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
    await Form_I_589.Supplement_A_ChildEntry5_0.set()
    await bot.send_message(callback_query.from_user.id, "You indicated that your fifth child is in U.S")
    await bot.send_message(callback_query.from_user.id, "Enter Place of last entry into the U.S")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox57[0]'] = ""
        data['[12].CheckBox57[1]'] = callback_query.data
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id, "You indicated that your fifth child is not in U.S")

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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your fifth child (If any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildINum5_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum5[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Status of your fifth child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.Supplement_A_ChildINum5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum5[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your fifth child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildStatus5_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus5[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter What is your fifth child's current status?")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your fifth child authorized stay, if any? (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildExpAuth5_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth5[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your fifth child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.Supplement_A_ChildExpAuth5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth5[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your fifth child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[0]'] = callback_query.data
        data['[12].SuppA_CheckBox20[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fifth child is in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[1]'] = callback_query.data
        data['[12].SuppA_CheckBox20[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your fifth child is not in Immigration Court proceedings")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.Supplement_A_IsIncludedInApplicationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox21[0]'] = callback_query.data
        data['[12].SuppA_CheckBox21[1]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
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
        data['[12].SuppA_CheckBox21[1]'] = callback_query.data
        data['[12].SuppA_CheckBox21[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Alien Registration Number (A-Number) (if any) of your sixth child",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")


# Child 6
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_16)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[16]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Passport/ID Card Number of your sixth child (if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_16)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[16]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Passport/ID Card Number of your sixth child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_17)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[17]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Marital Status of your sixth child (Married Single Divorced Widowed)")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "U.S. Social Security Number of your sixth child (if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_19)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[19]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter complete Last Name of your sixth child")


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
    await Form_I_589.Supplement_A_ChildEntry6_0.set()
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
    await bot.send_message(callback_query.from_user.id,
                           "List your last address where you lived before coming to the United States where don't you fear persecution. First enter Number and Street")
    await Form_I_589.A_III_TextField13_0.set()


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter I-94 Number of your sixth child (If any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildINum6_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum6[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Enter Status of your sixth child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.Supplement_A_ChildINum6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter Status of your sixth child when last admitted (Visa type, if any)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildStatus6_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus6[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Enter What is your sixth child's current status?")


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
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Enter What is the expiration date of your sixth child authorized stay, if any? (mm/dd/yyyy)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildExpAuth6_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth6[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Is your sixth child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.Supplement_A_ChildExpAuth6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Is your sixth child in Immigration Court proceedings?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppALine20_CheckBox2[0]'] = callback_query.data
        data['[12].SuppALine20_CheckBox2[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your sixth child is in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppALine20_CheckBox2[1]'] = callback_query.data
        data['[12].SuppALine20_CheckBox2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your sixth child is not in Immigration Court proceedings")
    await bot.send_message(callback_query.from_user.id,
                           "If in the U.S., is this child to be included in this application?",
                           reply_markup=keyboard.markup)


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
        data['[12].SuppALine21_CheckBox[1]'] = callback_query.data
        data['[12].SuppALine21_CheckBox[0]'] = ""
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


@dp.message_handler(state=Form_I_589.A_III_TextField13_27)
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


@dp.message_handler(state=Form_I_589.A_III_DateTimeField33_0)
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


@dp.message_handler(state=Form_I_589.A_III_DateTimeField36_0)
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
        data["""[4].CheckBoxAIII5\\.m[0]"""] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your Mother is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of Father")
    await Form_I_589.A_III_TextField13_47.set()


@dp.callback_query_handler(text="no_mother_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_m_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.m[0]'] = ""
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
        data['[4].CheckBoxAIII5\\\\.f[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your Father is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 1 Sibling")
    await Form_I_589.A_III_TextField13_48.set()


@dp.callback_query_handler(text="no_father_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_f_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.f[0]'] = ""
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
        data['[4].CheckBoxAIII5\\\\.s1[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 1 sibling is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 2 sibling")
    await Form_I_589.A_III_TextField13_52.set()


@dp.callback_query_handler(text="no_1sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s1[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 1 sibling is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of 1 sibling")
    await Form_I_589.A_III_TextField35_2.set()


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
        data['[4].CheckBoxAIII5\\\\.s2[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 2 sibling is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 3 sibling")
    await Form_I_589.A_III_TextField13_54.set()


@dp.callback_query_handler(text="no_2sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 2 sibling is not deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Current Location of 2 sibling")
    await Form_I_589.A_III_TextField35_3.set()


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
        data['[4].CheckBoxAIII5\\\\.s3[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "You indicated that your 3 sibling is deceased")

    await bot.send_message(callback_query.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Enter Full Name of 4 sibling")
    await Form_I_589.A_III_TextField13_56.set()


@dp.callback_query_handler(text="no_3sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s3[0]'] = ""
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
    keyboard = Form_I_589_4Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Provide the following information about your parents and siblings (brothers and sisters). Is your 4 sibling deceased?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_4sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s4[0]'] = callback_query.data
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
        data['[4].CheckBoxAIII5\\\\.s4[0]'] = ""
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
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you seeking asylum or withholding of removal based on Race")
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
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you seeking asylum or withholding of removal based on Religion")
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
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you seeking asylum or withholding of removal based on Nationality")
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
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you seeking asylum or withholding of removal based on Political opinion")
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
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you seeking asylum or withholding of removal based on Membership in a particular social group")
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
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you seeking asylum or withholding of removal based on Torture Convention")
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
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that  your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone")
    await bot.send_message(callback_query.from_user.id,
                           "Explain in detail:\n"
                           "1. What happened;\n"
                           "2. When the harm or mistreatment or threats occurred;\n"
                           "3. Who caused the harm or mistreatment or threats;\n"
                           "Why you believe the harm or mistreatment or threats occurred")


@dp.message_handler(state=Form_I_589.B_TextField14_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].TextField14[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Fear_Harm_Or_Mistreatment_Choice()
    await bot.send_message(message.from_user.id,
                           "Do you fear harm or mistreatment if you return to your home country?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_family_harm",
                           state=Form_I_589.B_Family_Experienced_Harm_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1a[1]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1a[0]'] = ""
    await Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that  your family, or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone")
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
    await Form_I_589.B_TextField15_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you fear harm or mistreatment if you return to your home country")
    await bot.send_message(callback_query.from_user.id,
                           "If Yes, explain in detail:\n"
                           "1. What harm or mistreatment you fear;\n"
                           "2. Who you believe would harm or mistreat you; and\n"
                           "3. Why you believe you would or could be harmed or mistreated.")


@dp.message_handler(state=Form_I_589.B_TextField15_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].TextField15[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice()
    await bot.send_message(message.from_user.id,
                           "Have you or your family members ever been accused, charged, arrested, detained, interrogated, convicted and sentenced, or imprisoned in any country other than the United States (including for an immigration law violation)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_you_fear_harm",
                           state=Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1b[1]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1b[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you don't fear harm or mistreatment if you return to your home country")
    keyboard = Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you or your family members ever been accused, charged, arrested, detained, interrogated, convicted and sentenced, or imprisoned in any country other than the United States (including for an immigration law violation)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_violated_law",
                           state=Form_I_589.B_You_Or_Family_Accused_Charged_Arrested_Detained_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn2[0]'] = callback_query.data
        data['[7].ckboxyn2[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your family members have been accused, charged, arrested, detained, interrogated, convicted and sentenced, or imprisoned in any country other than the United States")
    await bot.send_message(callback_query.from_user.id,
                           "If Yes, explain the circumstances and reasons for the action.")


@dp.message_handler(state=Form_I_589.B_PBL2_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PBL2_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Been_Associated_With_Any_Organizations_Choice()
    await bot.send_message(message.from_user.id,
                           "Have you or your family members ever belonged to or been associated with any organizations or groups in your home country such as but not limited to a political party student group labor union religious organization military or paramilitary group civil patrol guerrilla organization ethnic group human rights group or the press or media?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_violated_law",
                           state=Form_I_589.B_You_Or_Family_Accused_Charged_Arrested_Detained_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn2[1]'] = callback_query.data
        data['[7].ckboxyn2[0]'] = ""
    await Form_I_589.B_Been_Associated_With_Any_Organizations_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your family members have never been accused, charged, arrested, detained, interrogated, convicted and sentenced, or imprisoned in any country other than the United States")
    keyboard = Form_I_589_You_Been_Associated_With_Any_Organizations_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you or your family members ever belonged to or been associated with any organizations or groups in your home country such as but not limited to a political party student group labor union religious organization military or paramilitary group civil patrol guerrilla organization ethnic group human rights group or the press or media?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Been_Associated_With_Any_Organizations",
                           state=Form_I_589.B_Been_Associated_With_Any_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3a[0]'] = callback_query.data
        data['[7].ckboxyn3a[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your family members have ever belonged to or been associated with any organizations or groups in your home country such as but not limited to a political party student group labor union religious organization military or paramilitary group civil patrol guerrilla organization ethnic group human rights group or the press or media?")
    await bot.send_message(callback_query.from_user.id,
                           "Describe for each person the level of participation, any leadership or other positions held, and the length of time you or your family members were involved in each organization or activity.")


@dp.message_handler(state=Form_I_589.B_PBL3A_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PBL3A_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Continue_To_Participate_In_Organizations_Choice()
    await bot.send_message(message.from_user.id,
                           "Do you or your family members continue to participate in any way in these organizations or groups?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Been_Associated_With_Any_Organizations",
                           state=Form_I_589.B_Been_Associated_With_Any_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3a[1]'] = callback_query.data
        data['[7].ckboxyn3a[0]'] = ""
    await Form_I_589.B_Continue_To_Participate_In_Organizations_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your family members have never belonged to or been associated with any organizations or groups in your home country such as but not limited to a political party student group labor union religious organization military or paramilitary group civil patrol guerrilla organization ethnic group human rights group or the press or media?")
    keyboard = Form_I_589_You_Continue_To_Participate_In_Organizations_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Do you or your family members continue to participate in any way in these organizations or groups?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Continue_To_Participate_In_Organizations",
                           state=Form_I_589.B_Continue_To_Participate_In_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3b[0]'] = callback_query.data
        data['[7].ckboxyn3b[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your family members continue to participate in any way in these organizations or groups")
    await bot.send_message(callback_query.from_user.id,
                           "Describe for each person your or your family members' current level of participation, any leadership or other positions currently held, and the length of time you or your family members have been involved in each organization or group.")


@dp.message_handler(state=Form_I_589.B_PBL3B_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PBL3B_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Afraid_Of_Being_Subjected_To_Torture_Choice()
    await bot.send_message(message.from_user.id,
                           "Are you afraid of being subjected to torture in your home country or any other country to which you may be returned?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Continue_To_Participate_In_Organizations",
                           state=Form_I_589.B_Continue_To_Participate_In_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3b[1]'] = callback_query.data
        data['[7].ckboxyn3b[0]'] = ""
    await Form_I_589.B_Afraid_Of_Being_Subjected_To_Torture_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your family members don't continue to participate in any way in these organizations or groups")
    keyboard = Form_I_589_You_Afraid_Of_Being_Subjected_To_Torture_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Are you afraid of being subjected to torture in your home country or any other country to which you may be returned?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Afraid_Of_Being_Subjected_To_Torture",
                           state=Form_I_589.B_Afraid_Of_Being_Subjected_To_Torture_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn4[0]'] = callback_query.data
        data['[7].ckboxyn4[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you afraid of being subjected to torture in your home country or any other country to which you may be returned?")
    await bot.send_message(callback_query.from_user.id,
                           "Explain why you are afraid and describe the nature of torture you fear, by whom, and why it would be inflicted.")


@dp.message_handler(state=Form_I_589.B_PB4_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PB4_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Applied_For_USRefugee_Status_Choice()
    await bot.send_message(message.from_user.id,
                           "Have you your spouse your child(ren) your parents or your siblings ever applied to the U_S_ Government for refugee status asylum or withholding of removal?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Afraid_Of_Being_Subjected_To_Torture",
                           state=Form_I_589.B_Afraid_Of_Being_Subjected_To_Torture_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn4[1]'] = callback_query.data
        data['[7].ckboxyn4[0]'] = ""
    await Form_I_589.C_Family_Applied_For_USRefugee_Status_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you don't afraid of being subjected to torture in your home country or any other country to which you may be returned?")
    keyboard = Form_I_589_Family_Applied_For_USRefugee_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you your spouse your child(ren) your parents or your siblings ever applied to the U_S_ Government for refugee status asylum or withholding of removal?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Applied_For_USRefugee_Status",
                           state=Form_I_589.C_Family_Applied_For_USRefugee_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync1[0]'] = callback_query.data
        data['[8].ckboxync1[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you your spouse your child(ren) your parents or your siblings ever applied to the U_S_ Government for refugee status asylum or withholding of removal")
    await bot.send_message(callback_query.from_user.id,
                           "Explain the decision and what happened to any status you, your spouse, your child(ren), your parents, or your siblings received as a result of that decision. Indicate whether or not you were included in a parent or spouse's application. If so, include your parent or spouse's A-number in your response. If you have been denied asylum by an immigration judge or the Board of Immigration Appeals, describe any change(s) in conditions in your country or your own personal circumstances since the date of the denial that may affect your eligibility for asylum.")


@dp.message_handler(state=Form_I_589.C_PCL1_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[8].PCL1_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice()
    await bot.send_message(message.from_user.id,
                           "After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Family_Applied_For_USRefugee_Status",
                           state=Form_I_589.C_Family_Applied_For_USRefugee_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync1[1]'] = callback_query.data
        data['[8].ckboxync1[0]'] = ""
    await Form_I_589.C_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you your spouse your child(ren) your parents or your siblings have never applied to the U_S_ Government for refugee status asylum or withholding of removal")
    keyboard = Form_I_589_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Travel_Or_Reside_In_Other_Countries_Before_US",
                           state=Form_I_589.C_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2a[0]'] = callback_query.data
        data['[8].ckboxync2a[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your spouse or child(ren) who are now in the United States have traveled through or reside in any other country before entering the United States")
    keyboard = Form_I_589_Family_Recieved_Any_Lawful_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Family_Travel_Or_Reside_In_Other_Countries_Before_US",
                           state=Form_I_589.C_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2a[1]'] = callback_query.data
        data['[8].ckboxync2a[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or your spouse or child(ren) who are now in the United States have not traveled through or reside in any other country before entering the United States")
    keyboard = Form_I_589_Family_Recieved_Any_Lawful_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Recieved_Any_Lawful_Status",
                           state=Form_I_589.C_Family_Recieved_Any_Lawful_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2b[0]'] = callback_query.data
        data['[8].ckboxync2b[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you, your spouse, your child(ren), or other family members, such as your parents or siblings, ever applied for or received any lawful status in any country other than the one from which you are now claiming asylum")
    await bot.send_message(callback_query.from_user.id,
                           """Provide for each person the following: the name of each country and the length of stay, the
person's status while there, the reasons for leaving, whether or not the person is entitled to return for lawful residence purposes, and whether the
person applied for refugee status or for asylum while there, and if not, why he or she did not do so""")


@dp.callback_query_handler(text="no_Family_Recieved_Any_Lawful_Status",
                           state=Form_I_589.C_Family_Recieved_Any_Lawful_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2b[1]'] = callback_query.data
        data['[8].ckboxync2b[0]'] = ""
        answered_yes_in_previous_question = data['[8].ckboxync2a[0]']
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you, your spouse, your child(ren), or other family members, such as your parents or siblings, ever applied for or received any lawful status in any country other than the one from which you are now claiming asylum")
    if answered_yes_in_previous_question:
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id,
                               """Provide for each person the following: the name of each country and the length of stay, the
    person's status while there, the reasons for leaving, whether or not the person is entitled to return for lawful residence purposes, and whether the
    person applied for refugee status or for asylum while there, and if not, why he or she did not do so""")
    else:
        keyboard = Form_I_589_You_Or_Family_Caused_Harm_Or_Suffering_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Have you, your spouse or your child(ren) ever ordered, incited, assisted or otherwise participated in causing harm or suffering to any person because of his or her race, religion, nationality, membership in a particular social group or belief in a particular political opinion?",
                               reply_markup=keyboard.markup)


@dp.message_handler(state=Form_I_589.C_PCL2B_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[8].PCL2B_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Or_Family_Caused_Harm_Or_Suffering_Choice()
    await bot.send_message(message.from_user.id,
                           "Have you, your spouse or your child(ren) ever ordered, incited, assisted or otherwise participated in causing harm or suffering to any person because of his or her race, religion, nationality, membership in a particular social group or belief in a particular political opinion?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Or_Family_Caused_Harm_Or_Suffering",
                           state=Form_I_589.C_You_Or_Family_Caused_Harm_Or_Suffering_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync3[0]'] = callback_query.data
        data['[8].ckboxync3[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you, your spouse or your child(ren) ever ordered, incited, assisted or otherwise participated in causing harm or suffering to any person because of his or her race, religion, nationality, membership in a particular social group or belief in a particular political opinion")
    await bot.send_message(callback_query.from_user.id,
                           "Explain the decision and what happened to any status you, your spouse, your child(ren), your parents, or your siblings received as a result of that decision. Indicate whether or not you were included in a parent or spouse's application. If so, include your parent or spouse's A-number in your response. If you have been denied asylum by an immigration judge or the Board of Immigration Appeals, describe any change(s) in conditions in your country or your own personal circumstances since the date of the denial that may affect your eligibility for asylum.")


@dp.message_handler(state=Form_I_589.C_PCL3_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[8].PCL3_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Returned_To_Bad_Country_Choice()
    await bot.send_message(message.from_user.id,
                           "After you left the country where you were harmed or fear harm, did you return to that country?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Or_Family_Caused_Harm_Or_Suffering",
                           state=Form_I_589.C_You_Or_Family_Caused_Harm_Or_Suffering_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync1[1]'] = callback_query.data
        data['[8].ckboxync1[0]'] = ""
    await Form_I_589.C_Returned_To_Bad_Country_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you, your spouse or your child(ren) have never ordered, incited, assisted or otherwise participated in causing harm or suffering to any person because of his or her race, religion, nationality, membership in a particular social group or belief in a particular political opinion")
    keyboard = Form_I_589_Returned_To_Bad_Country_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "After you left the country where you were harmed or fear harm, did you return to that country?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Returned_To_Bad_Country",
                           state=Form_I_589.C_Returned_To_Bad_Country_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCckboxyn4[0]'] = callback_query.data
        data['[9].PCckboxyn4[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you have had returned to country where you have had feared to be mistreated or harmed")
    await bot.send_message(callback_query.from_user.id,
                           "Describe in detail the circumstances of your visit(s) (for example, the date(s) of the trip(s), the purpose(s) of the trip(s), and the length of time you remained in that country for the visit(s).)")


@dp.message_handler(state=Form_I_589.C_PCL4_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCL4_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Last_Arrival_To_US_More_Than_1_Year_Choice()
    await bot.send_message(message.from_user.id,
                           "Are you filing this application more than 1 year after your last arrival in the United States?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Returned_To_Bad_Country",
                           state=Form_I_589.C_Returned_To_Bad_Country_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCckboxyn4[1]'] = callback_query.data
        data['[9].PCckboxyn4[0]'] = ""
    await Form_I_589.C_Last_Arrival_To_US_More_Than_1_Year_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you did not return to country where you have had feared to be mistreated or harmed")
    keyboard = Form_I_589_Last_Arrival_To_US_More_Than_1_Year_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Are you filing this application more than 1 year after your last arrival in the United States?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Last_Arrival_To_US_More_Than_1_Year",
                           state=Form_I_589.C_Last_Arrival_To_US_More_Than_1_Year_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync5[0]'] = callback_query.data
        data['[9].ckboxync5[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you filing this application more than 1 year after your last arrival in the United States")
    await bot.send_message(callback_query.from_user.id,
                           "Explain why you did not file within the first year after you arrived. You must be prepared to explain at your interview or hearing why you did not file your asylum application within the first year after you arrived. For guidance in answering this question, see Instructions, Part 1: Filing Instructions, Section V.")


@dp.message_handler(state=Form_I_589.C_PCL5_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCL5_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Or_Family_Did_Crime_Choice()
    await bot.send_message(message.from_user.id,
                           "Have you or any member of your family included in the application ever committed any crime and/or been arrested, charged, convicted, or sentenced for any crimes in the United States (including for an immigration law violation)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Last_Arrival_To_US_More_Than_1_Year",
                           state=Form_I_589.C_Last_Arrival_To_US_More_Than_1_Year_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync5[1]'] = callback_query.data
        data['[9].ckboxync5[0]'] = ""
    await Form_I_589.C_You_Or_Family_Did_Crime_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you not filing this application more than 1 year after your last arrival in the United States")
    keyboard = Form_I_589_You_Or_Family_Did_Crime_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Have you or any member of your family included in the application ever committed any crime and/or been arrested, charged, convicted, or sentenced for any crimes in the United States (including for an immigration law violation)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Or_Family_Did_Crime",
                           state=Form_I_589.C_You_Or_Family_Did_Crime_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync6[0]'] = callback_query.data
        data['[9].ckboxync6[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or any member of your family included in the application ever committed any crime and/or been arrested, charged, convicted, or sentenced for any crimes in the United States (including for an immigration law violation)")
    await bot.send_message(callback_query.from_user.id,
                           """For each instance, specify in your response: what occurred and the circumstances, dates, length of sentence received, location, the
duration of the detention or imprisonment, reason(s) for the detention or conviction, any formal charges that were lodged against you or your
relatives included in your application, and the reason(s) for release. Attach documents referring to these incidents, if they are available, or an
explanation of why documents are not available.""")


@dp.message_handler(state=Form_I_589.C_PCL6_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCL6_TextField[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Print your complete name.",
                           )


@dp.callback_query_handler(text="no_You_Or_Family_Did_Crime",
                           state=Form_I_589.C_You_Or_Family_Did_Crime_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync6[1]'] = callback_query.data
        data['[9].ckboxync6[0]'] = ""
    await Form_I_589.D_TextField20_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you or any member of your family included in the application never committed any crime and/or been arrested, charged, convicted, or sentenced for any crimes in the United States (including for an immigration law violation)")
    await bot.send_message(callback_query.from_user.id,
                           "Print your complete name.")


@dp.message_handler(state=Form_I_589.D_TextField20_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField20[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Write your name in your native alphabet")


@dp.message_handler(state=Form_I_589.D_TextField20_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField20[1]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Helped_Complete_Application_Choice()
    await bot.send_message(message.from_user.id,
                           "Did your spouse, parent, or child(ren) assist you in completing this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Helped_Complete_Application",
                           state=Form_I_589.D_Family_Helped_Complete_Application)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ckboxynd1[0]'] = callback_query.data
        data['[10].PtD_ckboxynd1[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that your spouse, parent, or child(ren) assist you in completing this application")
    await bot.send_message(callback_query.from_user.id,
                           "Enter Name.")


@dp.message_handler(state=Form_I_589.D_PtD_ChildName1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ChildName1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Relationship.")


@dp.message_handler(state=Form_I_589.D_PtD_RelationshipOfChild1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ChildName1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Helped_Complete_Fill_Next_Member_Choice()
    await bot.send_message(message.from_user.id,
                           "Do you wish to list another assistant?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Helped_Complete_Fill_Next_Member_Choice",
                           state=Form_I_589.D_PtD_ChildName2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you had second family member help you to fill application")
    await bot.send_message(callback_query.from_user.id,
                           "Enter name.")


@dp.message_handler(state=Form_I_589.D_PtD_ChildName2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ChildName2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Enter Relationship.")


@dp.message_handler(state=Form_I_589.D_PtD_RelationshipOfChild2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_RelationshipOfChild2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Not_Family_Helped_Complete_Application_Choice()
    await bot.send_message(message.from_user.id,
                           "Did someone other than your spouse, parent, or child(ren) prepare this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Family_Helped_Complete_Fill_Next_Member_Choice",
                           state=Form_I_589.D_PtD_ChildName2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.D_Not_Family_Helped_Complete_Application.set()
    keyboard = Form_I_589_Not_Family_Helped_Complete_Application_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Did someone other than your spouse, parent, or child(ren) prepare this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Family_Helped_Complete_Application",
                           state=Form_I_589.D_Family_Helped_Complete_Application)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ckboxynd1[1]'] = callback_query.data
        data['[10].PtD_ckboxynd1[0]'] = ""
    await Form_I_589.D_Not_Family_Helped_Complete_Application.set()
    keyboard = Form_I_589_Not_Family_Helped_Complete_Application_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Did someone other than your spouse, parent, or child(ren) prepare this application?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Not_Family_Helped_Complete_Application",
                           state=Form_I_589.D_Not_Family_Helped_Complete_Application)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].ckboxynd2[0]'] = callback_query.data
        data['[10].ckboxynd2[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Provided_With_List_Of_Persons_Who_May_Assist_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Asylum applicants may be represented by counsel. Have you been provided with a list of persons who may be available to assist you, at little or no cost, with your asylum claim?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Not_Family_Helped_Complete_Application",
                           state=Form_I_589.D_Not_Family_Helped_Complete_Application)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].ckboxynd2[1]'] = callback_query.data
        data['[10].ckboxynd2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Provided_With_List_Of_Persons_Who_May_Assist_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Asylum applicants may be represented by counsel. Have you been provided with a list of persons who may be available to assist you, at little or no cost, with your asylum claim?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Provided_With_List_Of_Persons_Who_May_Assist",
                           state=Form_I_589.D_Provided_With_List_Of_Persons_Who_May_Assist_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].ckboxynd3[0]'] = callback_query.data
        data['[10].ckboxynd3[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Signature of Applicant (The person in Part. A.I.)")


@dp.callback_query_handler(text="no_Provided_With_List_Of_Persons_Who_May_Assist",
                           state=Form_I_589.D_Provided_With_List_Of_Persons_Who_May_Assist_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].ckboxynd3[1]'] = callback_query.data
        data['[10].ckboxynd3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Signature of Applicant (The person in Part. A.I.)")


@dp.message_handler(state=Form_I_589.D_TextField22_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField22[0]'] = message.text
        data['[10].DateTimeField48[0]'] = datetime.datetime.now().strftime("%d/%m/%Y")
        is_preparer = data['[10].ckboxynd2[0]']
    if is_preparer:
        await Form_I_589.next()
        await bot.send_message(message.from_user.id,
                               "Enter Signature of Preparer")
    else:
        async with state.proxy() as data:
            adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                             user_id=message.from_user.id,
                                             timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
            adapter.save_json(data)
            await bot.send_message(message.chat.id,
                                   "Your data for Form-I-589 form was successfully saved! Wait for pdf file.")
            await bot.send_chat_action(message.chat.id, "typing")
            pdf_file_path = adapter.fill_pdf()
            with open(pdf_file_path, 'rb') as file:
                await bot.send_document(message.chat.id, file)
        await state.finish()


@dp.message_handler(state=Form_I_589.E_PtE_PreparerSignature_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_PreparerSignature[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Print Complete Name of Preparer")


@dp.message_handler(state=Form_I_589.E_PtE_PreparerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_PreparerName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Daytime Telephone Number Code")


@dp.message_handler(state=Form_I_589.E_TextField25_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField25[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Daytime Telephone Number")


@dp.message_handler(state=Form_I_589.E_TextField25_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField25[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Address of Preparer: Street Number and Name")


@dp.message_handler(state=Form_I_589.E_PtE_StreetNumAndName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_StreetNumAndName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Address of Preparer: Apt. Number")


@dp.message_handler(state=Form_I_589.E_PtE_AptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Address of Preparer: City")


@dp.message_handler(state=Form_I_589.E_PtE_City_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_City[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Address of Preparer: State")


@dp.message_handler(state=Form_I_589.E_PtE_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Address of Preparer: Zip Code")


@dp.message_handler(state=Form_I_589.E_PtE_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_ZipCode[0]'] = message.text

        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        adapter.save_json(data)
        await bot.send_message(message.chat.id,
                               "Your data for Form-I-589 form was successfully saved! Wait for pdf file.")
        await bot.send_chat_action(message.chat.id, "typing")
        pdf_file_path = adapter.fill_pdf()
        with open(pdf_file_path, 'rb') as file:
            await bot.send_document(message.chat.id, file)
    await state.finish()
