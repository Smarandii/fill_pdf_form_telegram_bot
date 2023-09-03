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
    Form_I_589_Family_Experienced_Harm_Choice, \
    Form_I_589_You_Been_Associated_With_Any_Organizations_Choice, \
    Form_I_589_You_Continue_To_Participate_In_Organizations_Choice, \
    Form_I_589_You_Afraid_Of_Being_Subjected_To_Torture_Choice, \
    Form_I_589_Family_Applied_For_USRefugee_Status_Choice, \
    Form_I_589_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice, \
    Form_I_589_Family_Recieved_Any_Lawful_Status_Choice, \
    Form_I_589_You_Or_Family_Caused_Harm_Or_Suffering_Choice, \
    Form_I_589_Returned_To_Bad_Country_Choice, \
    Form_I_589_Last_Arrival_To_US_More_Than_1_Year_Choice, \
    Form_I_589_You_Or_Family_Did_Crime_Choice, \
    Form_I_589_Family_Helped_Complete_Application_Choice, \
    Form_I_589_Family_Helped_Complete_Fill_Next_Member_Choice, \
    Form_I_589_Not_Family_Helped_Complete_Application_Choice, \
    Form_I_589_Provided_With_List_Of_Persons_Who_May_Assist_Choice, \
    Form_I_589_If_Any_Choice, \
    Form_I_589_Mailing_Address_Choice_Keyboard, \
    Form_I_589_If_Applicable, \
    Form_I_589_Child_Immigration_Court_Choice, \
    Form_I_589_If_Previously_In_US, Form_I_589_Include_Child_Choice, \
    Form_I_589_4Sibling_Deceased_Choice

from telegram_bot.form_i_589.form_i_589_state_group import Form_I_589

from telegram_bot import \
    bot, \
    dp, \
    FillPdfFromJsonAdapter, \
    datetime


import json


def escape_json_special_chars(func):
    def wrapper(message, *args, **kwargs):
        message.text.replace("\\", "\\\\")
        return func(message, *args, **kwargs)
    return wrapper


@escape_json_special_chars
@dp.message_handler(filters.Command("end"), state='*')
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        adapter.save_json()
        await bot.send_message(message.chat.id,
                               f"Ваши данные для формы {data['form_identifier']} успешно сохранены! Дождитесь pdf-файла.")
        await bot.send_chat_action(message.chat.id, "typing")
        pdf_file_path = adapter.fill_pdf()
        with open(pdf_file_path, 'rb') as file:
            await bot.send_document(message.chat.id, file)
    await state.finish()


@dp.callback_query_handler(text="I-589")
async def i_589_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-589"
    await bot.send_message(callback_query.from_user.id, "Вы выбрали форму I-589. Давайте приступим к ее заполнению.")
    await bot.send_message(callback_query.from_user.id, "Часть A.I. Информация о вас")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите Ваш регистрационный номер иностранца ( A-number) (если имеется):",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_PtAILine1_ANumber_0.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_PtAILine1_ANumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine1_ANumber[0]'] = ""
    await bot.send_message(callback_query.from_user.id,
                           "Вы решили оставить поле регистрационного номера иностранца (A-Number) пустым")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id, "Укажите номер социального страхования США (SSN) (если есть)",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_TextField1_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine1_ANumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите номер социального страхования США (SSN) (если есть)")


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[0]'] = ""
    await bot.send_message(callback_query.from_user.id,
                           "Вы решили оставить поле номера социального страхования (SSN) пустым")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id, "Укажите номер онлайн-аккаунта USCIS (если есть)",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_TextField1_8.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите номер онлайн-аккаунта USCIS (если есть)")


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField1_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[8]'] = ""
    await bot.send_message(callback_query.from_user.id, "Вы решили оставить поле номера онлайн-аккаунта USCIS пустым")
    await bot.send_message(callback_query.from_user.id, "Укажите Вашу фамилию")
    await Form_I_589.A_I_PtAILine4_LastName_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_8)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[8]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите Вашу фамилию:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine4_LastName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine4_LastName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine5_FirstName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine5_FirstName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine6_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine6_MiddleName[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Какие еще имена вы использовали (включая девичью фамилию и псевдонимы)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField1_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[1]'] = ""
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали другие фамилии или имена (включая девичью фамилию и псевдонимы)")
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы в США, где Вы фактически проживаете")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы в США, где Вы фактически проживаете")


# 8. Residence in the U.S. (where you physically reside)
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_StreetNumandName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите номер вашей квартиры:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите Ваш город:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_City_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите Ваш штат (например, CA, NY, AZ и т.д.):")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите свой почтовый индекс (например, 123456).\nНайти почтовый индекс можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_Zipcode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_Zipcode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите код Вашего номера телефона:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AreaCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите ваш номер телефона:")


# 9. Mailing Address in the U.S. (if different than the address in Item Number 8)
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_TelephoneNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_TelephoneNumber[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Mailing_Address_Choice_Keyboard()
    await bot.send_message(message.from_user.id,
                           "Ваш почтовый адрес отличается от адреса фактического проживания в США?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="MailingSameAsResidence_Yes",
                           state=Form_I_589.A_I_Mailing_Address_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(callback_query.from_user.id, "Выберите свой пол",
                           reply_markup=keyboard.markup)
    await Form_I_589.A_I_ChooseGender.set()


@dp.callback_query_handler(text="MailingSameAsResidence_No",
                           state=Form_I_589.A_I_Mailing_Address_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = Form_I_589_If_Applicable()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите имя человека, на попечении которого находится данный адресс (если это применимо)",
                           reply_markup=keyboard.markup)
    await Form_I_589.next()


@dp.callback_query_handler(text="not_applicable",
                           state=Form_I_589.A_I_PtAILine9_InCareOf_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "Укажите код номера телефона")
    await Form_I_589.A_I_PtAILine9_AreaCode_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_InCareOf_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_InCareOf[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите код номера телефона:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_AreaCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите номер телефона:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_TelephoneNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы в США, куда вы получаете корреспонденцию:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_StreetNumandName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите номер квартиры:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_AptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите штат:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите почтовый индекс (например, 123456).\nНайти почтовый индекс можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_PtAILine9_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_ZipCode[0]'] = message.text
    keyboard = Form_I_589_Gender_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Выберите свой пол:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_I_ChooseGender)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = "Male"
        data['[0].PartALine9Gender[1]'] = ""
    keyboard = Form_I_589_Marital_Status_Choice()
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что вы мужчина")
    await bot.send_message(callback_query.from_user.id, "Выберите семейное положение:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_I_ChooseGender)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[0]'] = ""
        data['[0].PartALine9Gender[1]'] = "Female"
    keyboard = Form_I_589_Marital_Status_Choice()
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что вы женщина")
    await bot.send_message(callback_query.from_user.id, "Выберите семейное положение:", reply_markup=keyboard.markup)


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
    await bot.send_message(callback_query.from_user.id, "Вы указали, что вы не состоите в браке")
    await bot.send_message(callback_query.from_user.id, "Укажите дату рождения (мм/дд/гггг):")


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
    await bot.send_message(callback_query.from_user.id, "Вы указали, что состоите в браке")
    await bot.send_message(callback_query.from_user.id, "Укажите дату рождения (мм/дд/гггг):")


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
    await bot.send_message(callback_query.from_user.id, "Вы указали, что разведены")
    await bot.send_message(callback_query.from_user.id, "Укажите дату рождения (мм/дд/гггг):")


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
    await bot.send_message(callback_query.from_user.id, "Вы указали, что овдовели")
    await bot.send_message(callback_query.from_user.id, "Укажите дату рождения (мм/дд/гггг):")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_DateTimeField1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите текущее гражданство:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство при рождении:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите Вашу расу, этническую или племенную группу:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[6]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id, "Укажите Вашу религию:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField1_7)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[7]'] = ""
    await bot.send_message(callback_query.from_user.id, "Вы указали, что у вас нет религии")
    keyboard = Form_I_589_Immigration_Court_Choice()
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Отметьте верное:", reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField1_7)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[7]'] = message.text
    keyboard = Form_I_589_Immigration_Court_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Отметьте верное:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="never_been_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = callback_query.data
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что никогда не участвовали в разбирательствах в иммиграционном суде.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, Когда вы в последний раз покидали свою страну? (мм/дд/гггг):")


@dp.callback_query_handler(text="now_in_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = callback_query.data
        data['[0].CheckBox3[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что сейчас учавствуете в разбирательствах в иммиграционном суде.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, Когда вы в последний раз покидали свою страну? (мм/дд/гггг):")


@dp.callback_query_handler(text="not_now_but_been_in_imc",
                           state=Form_I_589.A_I_ChooseImmigrationCourtProceedingsStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox3[0]'] = ""
        data['[0].CheckBox3[1]'] = ""
        data['[0].CheckBox3[2]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что сейчас не участвуете в разбирательстве в иммиграционном суде, но участвовали ранее.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, Когда вы в последний раз покидали свою страну? (мм/дд/гггг):")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_DateTimeField6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите Ваш текущий номер I-94, если он есть?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_I_TextField3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField3[0]'] = ""
    await Form_I_589.A_I_DateTimeField2_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что у вас нет номера I-94")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, все случаи, когда вы въезжали в США, начиная с самого последнего")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату вашего последнего въезда в США:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату вашего последнего въезда в США:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите место вашего последнего въезда в США:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите статус при вашем последнем въезде в США:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField4_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания Вашего статуса при вашем последнем въезде в США:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите второй по времени въезд в США. Укажите дату:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_DateTimeField3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите второй по времени въезд в США. Укажите место:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField4_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите второй по времени въезд в США. Укажите статус:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField4_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите третий по времени въезд в США. Введите дату:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_DateTimeField4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите третий по времени въезд в США. Укажите место:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField4_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите третий по времени въезд в США. Укажите статус:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField4_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField4[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Какая страна выдала вам последний паспорт или проездной документ (travel document)?")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите номер паспорта")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField5_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите номер проездного документа")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField5_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField5[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите срок действия проездного документа (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_DateTimeField2_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].DateTimeField2[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите Ваш родной язык (укажите диалект, если применимо)?")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField7_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField7[0]'] = message.text
    keyboard = Form_I_589_English_Fluency_Choice()
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Вы свободно владеете английским?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_eng_fluent",
                           state=Form_I_589.A_I_EngFluencyChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox4[1]'] = callback_query.data
        data['[0].CheckBox4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что свободно владеете английским языком")
    await bot.send_message(callback_query.from_user.id, "Укажите, какими еще языками Вы свободно владеете")


@dp.callback_query_handler(text="no_eng_fluent",
                           state=Form_I_589.A_I_EngFluencyChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].CheckBox4[0]'] = callback_query.data
        data['[0].CheckBox4[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что не владеете английским языком")
    await bot.send_message(callback_query.from_user.id, "Укажите, какими языками Вы свободно владеете")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_I_TextField7_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField7[1]'] = message.text
        is_married = data['[0].Marital[1]']
        is_not_married = not data['[0].Marital[1]']
    await bot.send_message(message.from_user.id, "Вы заполнили часть A.I. Информация о Вас полностью, далее:")
    await bot.send_message(message.from_user.id, "Часть А.II. Информация о вашем супруге и детях")
    if is_married:
        await Form_I_589.next()
        await bot.send_message(message.from_user.id, "Вы указали, что состоите в браке")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(message.from_user.id,
                               "Укажите Alien Registration Number вашего супруга (A-Number)\n(если есть)?",
                               reply_markup=keyboard.markup)
    if is_not_married:
        await Form_I_589.A_II_HaveChildrenChoice.set()
        await bot.send_message(message.from_user.id, "Вы указали, что не состоите в браке")
        keyboard = Form_I_589_Have_Children_Choice()
        await bot.send_message(message.from_user.id,
                               "У вас есть дети?",
                               reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine1_ANumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine1_ANumber[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего супруга (если есть)?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine1_ANumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего супруга (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_TextField10_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения супруга (мм/дд/гггг)?")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения супруга (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_DateTimeField7_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].DateTimeField7[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер социального страхования (SSN) вашего супруга (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_TextField10_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию Вашего супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите фамилию Вашего супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine5_LastName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine5_LastName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя Вашего супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine6_FirstName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine6_FirstName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество Вашего супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine7_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine7_MiddleName[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите другие использованные имена вашего супруга (включая девичью фамилию и псевдонимы)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_TextField10_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[3]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Укажите дату вступления в брак с супругом (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату вступления в брак с супругом (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_DateTimeField8_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].DateTimeField8[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите место вступления в брак")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите расу, этническую или племенную группу супруга ")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_TextField10_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[6]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Укажите пол вашего супруга:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_TextField10_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].TextField10[2]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию вашего супруга")


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = ""
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш супруг — женщина")
    await bot.send_message(callback_query.from_user.id, "Ваш супруг находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].CheckBox14_Gender[0]'] = callback_query.data
        data['[1].NotMarried[0].CheckBox14_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш супруг — мужчина")
    await bot.send_message(callback_query.from_user.id, "Ваш супруг находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_IsInUSChoiceSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[0]'] = ""
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[1]'] = callback_query.data
    await Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш супруг находится в США")
    await bot.send_message(callback_query.from_user.id, "Укажите место его последнего визита в США")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_IsInUSChoiceSpouse)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[0]'] = callback_query.data
        data['[1].NotMarried[0].PtAIILine15_CheckBox15[1]'] = ""
    await Form_I_589.A_II_NotMarried_0_PtAIILine15_Specify_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш супруг не находится в США")
    await bot.send_message(callback_query.from_user.id, "Укажите местонахождение вашего супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine15_Specify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine15_Specify[0]'] = message.text
    keyboard = Form_I_589_Have_Children_Choice()
    await Form_I_589.A_II_HaveChildrenChoice.set()
    await bot.send_message(message.from_user.id,
                           "У вас есть дети?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine16_PlaceofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату последнего визита США вашего супруга (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine17_DateofLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine17_DateofLastEntry[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "I-94 номер вашего супруга (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine18_I94Number_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите статус вашего супруга, когда его в последний раз впустили в США (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine18_I94Number_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine18_I94Number[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите статус вашего супруга, когда его в последний раз впустили в США (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущий статус вашего супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine19_StatusofLastAdmission[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите текущий статус вашего супруга")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine20_SpouseCurrentStatus_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine20_SpouseCurrentStatus[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания разрешенного пребывания в США вашего супруга, если таковая имеется? (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Spouse_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Является ли ваш супруг участником разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine21_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Spouse_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Является ли ваш супруг участником разбирательства в иммиграционном суде?",
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
                           "Вы указали, что ваш супруг является участником разбирательства в иммиграционном суде")
    await bot.send_message(callback_query.from_user.id,
                           "Если ранее находились в США, укажите дату предыдущего прибытия (мм/дд/гггг)",
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
                           "Вы указали, что ваш супруг не является участником разбирательств в иммиграционном суде.")
    await bot.send_message(callback_query.from_user.id,
                           "Если супруг ранее находился в США, укажите дату предыдущего прибытия (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="not_previously_in_us",
                           state=Form_I_589.A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Spouse_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш супруг ранее не был в США")
    await bot.send_message(callback_query.from_user.id,
                           "Если супруг находится в США, должен ли ваш супруг быть включен в это заявление?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].NotMarried[0].PtAIILine23_PreviousArrivalDate[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Include_Spouse_Choice()
    await bot.send_message(message.from_user.id,
                           "Если супруг находится в США, должен ли ваш супруг быть включен в это заявление?",
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
                           "Вы указали, что ваш супруг должен быть включен в это завяление")
    await bot.send_message(callback_query.from_user.id,
                           "У вас есть дети?",
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
                           "Вы указали, что ваш супруг не должен быть включен в это завяление")
    await bot.send_message(callback_query.from_user.id,
                           "У вас есть дети?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="dont_have_children",
                           state=Form_I_589.A_II_HaveChildrenChoice)
async def process(callback_query: types.CallbackQuery,
                  state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildrenCheckbox[0]'] = ""
        data['[1].ChildrenCheckbox[1]'] = callback_query.data
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что у Вас нет детей")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")


@dp.callback_query_handler(text="have_children",
                           state=Form_I_589.A_II_HaveChildrenChoice)
async def process(callback_query: types.CallbackQuery,
                  state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildrenCheckbox[0]'] = callback_query.data
        data['[1].ChildrenCheckbox[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у Вас есть дети")
    await bot.send_message(callback_query.from_user.id, "Общее количество детей:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_TotalChild_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].TotalChild[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите регистрационный номер иностранца вашего первого ребенка (номер A) (если есть)",
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
                           "Укажите номер паспорта/удостоверения личности вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildAlien1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport1[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение Вашего первого ребенка:",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildPassport1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(message.from_user.id,
                           "Выберите семейное положение Вашего первого ребенка:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_single",
                           state=Form_I_589.A_II_ChildMarital1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital1[0]'] = "Single"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш первый ребенок не состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_married",
                           state=Form_I_589.A_II_ChildMarital1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital1[0]'] = "Married"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш первый ребенок состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_divorced",
                           state=Form_I_589.A_II_ChildMarital1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital1[0]'] = "Divorced"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш первый ребенок разведен")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_widowed",
                           state=Form_I_589.A_II_ChildMarital1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital1[0]'] = "Widowed"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш первый ребенок вдова(-ец)")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildMarital1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMarital1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер социального страхования США вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN1[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildSSN1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите фамилию Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildLast1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildLast1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildFirst1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildFirst1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildMiddle1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildMiddle1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения Вашего первого ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildDOB1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildDOB1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildCity1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildCity1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildNat1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildNat1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите расу, этническую или племенную группу Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildRace1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildRace1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Укажите пол Вашего первого ребенка:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox16[1]'] = callback_query.data
        data['[1].CheckBox16[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш первый ребенок — женщина")
    await bot.send_message(callback_query.from_user.id, "Ваш первый ребенок находится в США?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild1
                           )
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox16[0]'] = callback_query.data
        data['[1].CheckBox16[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш первый ребенок — мужчина")
    await bot.send_message(callback_query.from_user.id, "Ваш первый ребенок находится в США?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox17[0]'] = callback_query.data
        data['[1].CheckBox17[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш первый ребенок находится в США.")
    await bot.send_message(callback_query.from_user.id, "Укажите место его последнего въезда в США")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].CheckBox17[1]'] = callback_query.data
        data['[1].CheckBox17[0]'] = ""
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш первый ребенок не находится в США.")
    total_number_of_children = int(data["[1].TotalChild[0]"])

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(callback_query.from_user.id,
                               "Хотите ли вы заполнить данные для вашего второго ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine13_Specify[0]'] = message.text
        total_number_of_children = int(data["[1].TotalChild[0]"])

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(message.from_user.id,
                               "Хотите ли вы заполнить данные для вашего второго ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine14_PlaceofLastEntry[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату последнего въезда в США Вашего первого ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_ExpirationDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine15_ExpirationDate[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер I-94 вашего первого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите статус при последнем въезде вашего первого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine16_I94Number[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите статус при последнем въезде вашего первого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущий статус Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine17_StatusofLastAdmission[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий статус Вашего первого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_CurrentStatusofChild_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine18_CurrentStatusofChild[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите, когда заканчивается срок законного пребывания Вашего шестого в стране (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ваш первый ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine19_ExpDateofAuthorizedStay[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Ваш первый ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = callback_query.data
        data['[1].PtAIILine20_No[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш первый ребенок находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine20_Yes[0]'] = ""
        data['[1].PtAIILine20_No[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш первый ребенок не находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes[0]'] = callback_query.data
        data['[1].PtAIILine21_No[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш первый первый ребенок должен быть включен в это приложение")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего второго ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боялись преследования. Сначала укажите номер и название улицы:")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].PtAIILine21_Yes[0]'] = ""
        data['[1].PtAIILine21_No[0]'] = callback_query.data
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш первый ребенок не должен быть включен в это приложение")

    if total_number_of_children > 1:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild2.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего второго ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боялись преследования. Сначала укажите номер и название улицы:")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите регистрационный номер иностранца вашего второго ребенка (номер A) (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боялись преследования. Сначала укажите номер и название улицы:")


# Child 2
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildAlien2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего второго ребенка (если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildAlien2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего второго ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildPassport2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение Вашего второго ребенка:",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildPassport2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildPassport2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(message.from_user.id,
                           "Выберите семейное положение Вашего второго ребенка:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_single",
                           state=Form_I_589.A_II_ChildMarital2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMarital2[0]'] = "Single"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш второй ребенок не состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего второго ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_married",
                           state=Form_I_589.A_II_ChildMarital2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMarital2[0]'] = "Married"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш второй ребенок состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего второго ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_divorced",
                           state=Form_I_589.A_II_ChildMarital2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMarital2[0]'] = "Divorced"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш второй ребенок разведен")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего второго ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_widowed",
                           state=Form_I_589.A_II_ChildMarital2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMarital2[0]'] = "Widowed"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш второй ребенок вдова(-ец)")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США вашего второго ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildSSN2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите фамилию Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildLast2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildLast2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildFirst2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildFirst2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildMiddle2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMiddle2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения Вашего второго ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildDOB2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildDOB2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildCity2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildCity2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildNat2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildNat2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите расу, этническую или племенную группу Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildRace2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildRace2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Укажите пол Вашего второго ребенка:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox26_Gender[0]'] = callback_query.data
        data['[3].CheckBox26_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш второй ребенок — женщина")
    await bot.send_message(callback_query.from_user.id, "Ваш второй ребенок находится в США?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox26_Gender[1]'] = callback_query.data
        data['[3].CheckBox26_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш второй ребенок — мужчина")
    await bot.send_message(callback_query.from_user.id, "Ваш второй ребенок находится в США?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox27[0]'] = callback_query.data
        data['[3].CheckBox27[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry2_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш второй ребенок находится в США.")
    await bot.send_message(callback_query.from_user.id, "Укажите место его последнего въезда в США")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox27[1]'] = callback_query.data
        data['[3].CheckBox27[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])

    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш второй ребенок не находится в США")

    if total_number_of_children > 2:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(callback_query.from_user.id,
                               "Хотите ли вы заполнить данные для вашего третьего ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine13_Specify2[0]'] = message.text
        total_number_of_children = int(data["[1].TotalChild[0]"])

    if total_number_of_children > 2:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(message.from_user.id,
                               "Хотите ли вы заполнить данные для вашего третьего ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine14_PlaceofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату последнего въезда в США Вашего второго ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер I-94 Вашего второго ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите статус при последнем въезде вашего второго ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите статус при последнем въезде вашего второго ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущий статус Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий статус Вашего второго ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите, когда заканчивается срок законного пребывания Вашего второго ребенка в стране (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ваш второй ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ваш второй ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Ваш второй ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes2[0]'] = callback_query.data
        data['[3].PtAIILine20_No2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш второй ребенок находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes2[0]'] = ""
        data['[3].PtAIILine20_No2[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш второй ребенок не находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
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
                           "Вы указали, что ваш второй ребенок должен быть включен в это приложение")

    if total_number_of_children > 2:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего третьего ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
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
                           "Вы указали, что ваш второй ребенок должен быть включен в это приложение")

    if total_number_of_children > 2:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild3.set()
        await bot.send_message(callback_query.from_user.id,
                               "Хотите ли вы заполнить данные для вашего третьего ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите регистрационный номер иностранца вашего третьего ребенка (номер A) (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")


# Child 3
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildAlien3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien3[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего третьего ребенка (если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildAlien3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildAlien3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего третьего ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport3[0]'] = ""
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение Вашего третьего ребенка",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildPassport3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport3[0]'] = message.text
        await Form_I_589.next()
        keyboard = Form_I_589_Marital_Status_Choice()
        await bot.send_message(message.from_user.id,
                               "Выберите семейное положение Вашего третьего ребенка",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_single",
                               state=Form_I_589.A_II_ChildMarital3_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital3[0]'] = "Single"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш третий ребенок не состоит в браке")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США вашего третьего ребенка (если есть)",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_married",
                               state=Form_I_589.A_II_ChildMarital3_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital3[0]'] = "Married"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш третий ребенок состоит в браке")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США вашего третьего ребенка (если есть)",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_divorced",
                               state=Form_I_589.A_II_ChildMarital3_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital3[0]'] = "Divorced"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш третий ребенок разведен")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США вашего третьего ребенка (если есть)",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_widowed",
                               state=Form_I_589.A_II_ChildMarital3_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital3[0]'] = "Widowed"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что ваш третий ребенок вдова(-ец)")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США вашего третьего ребенка (если есть)",
                               reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildSSN3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите фамилию Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildLast3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildLast3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildFirst3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildFirst3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildMiddle3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMiddle3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения Вашего третьего ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildDOB3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildDOB3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildCity3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildCity3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildNat3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildNat3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите расу, этническую или племенную группу Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildRace3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildRace3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Укажите пол Вашего третьего ребенка:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox36_Gender[0]'] = callback_query.data
        data['[3].CheckBox36_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш третий ребенок — женщина")
    await bot.send_message(callback_query.from_user.id, "Этот ребенок находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox36_Gender[1]'] = callback_query.data
        data['[3].CheckBox36_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш третий ребенок — мужчина")
    await bot.send_message(callback_query.from_user.id, "Этот ребенок находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox37[0]'] = callback_query.data
        data['[3].CheckBox37[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry3_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш третий ребенок находится в США")
    await bot.send_message(callback_query.from_user.id, "Укажите место его последнего въезда в США")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox37[1]'] = callback_query.data
        data['[3].CheckBox37[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш третий ребенок находится в США")

    if total_number_of_children > 3:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего четвертого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine13_Specify3[0]'] = message.text
        total_number_of_children = int(data["[1].TotalChild[0]"])

    if total_number_of_children > 3:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(message.from_user.id,
                               "Вы хотите заполнить данные для вашего следующего ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(message.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine14_PlaceofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату последнего въезда в США Вашего шестого (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер I-94 Вашего третьего ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number3[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите статус при последнем въезде Вашего третьего ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите статус при последнем въезде Вашего третьего ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущий статус Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission3[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий статус Вашего третьего ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите, когда заканчивается срок законного пребывания Вашего третьего ребенка в стране (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay3[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ваш третий ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay3[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Ваш третий ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes3[0]'] = callback_query.data
        data['[3].PtAIILine20_No3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш третий ребенок находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes3[0]'] = ""
        data['[3].PtAIILine20_No3[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш третий ребенок не находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
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
                           "Вы указали, что Ваш третий ребенок должен быть включен в это приложение")

    if total_number_of_children > 3:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего четвертого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
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
                           "Вы указали, что Ваш третий ребенок должен быть включен в это приложение")

    if total_number_of_children > 3:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.A_II_IsFillChild4.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего четвертого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите регистрационный номер иностранца вашего четвертого ребенка (номер A) (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.A_II_IsFillChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")


# Child 4
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildAlien4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien4[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего четвертого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildAlien4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildAlien4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер паспорта/удостоверения личности вашего четвертого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildPassport4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildPassport4[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение Вашего четвертого ребенка",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildPassport4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].ChildPassport4[0]'] = message.text
        await Form_I_589.next()
        keyboard = Form_I_589_Marital_Status_Choice()
        await bot.send_message(message.from_user.id,
                               "Выберите семейное положение Вашего четвертого ребенка",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_single",
                               state=Form_I_589.A_II_ChildMarital4_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital4[0]'] = "Single"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертого ребенок не состоит в браке")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США Вашего четвертого ребенка (если есть)",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_married",
                               state=Form_I_589.A_II_ChildMarital4_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital4[0]'] = "Married"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертого ребенок состоит в браке")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США Вашего четвертого ребенка (если есть)",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_divorced",
                               state=Form_I_589.A_II_ChildMarital4_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital4[0]'] = "Divorced"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертый ребенок разведен")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США Вашего четвертого ребенка (если есть)",
                               reply_markup=keyboard.markup)

    @dp.callback_query_handler(text="ms_widowed",
                               state=Form_I_589.A_II_ChildMarital4_0)
    async def process(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['[3].ChildMarital4[0]'] = "Widowed"
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертый ребенок вдова(-ец)")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Укажите номер социального страхования США Вашего четвертого ребенка (если есть)",
                               reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_ChildSSN4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildSSN4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildSSN4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите фамилию Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildLast4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildLast4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildFirst4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildFirst4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildMiddle4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildMiddle4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения Вашего четвертого ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildDOB4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildDOB4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildCity4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildCity4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildNat4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildNat4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите расу, этническую или племенную группу Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_ChildRace4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].ChildRace4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Укажите пол Вашего четвертого ребенка:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.A_II_ChooseGenderChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox46_Gender[0]'] = callback_query.data
        data['[3].CheckBox46_Gender[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертый ребенок — женщина")
    await bot.send_message(callback_query.from_user.id, "Этот ребенок находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.A_II_ChooseGenderChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox46_Gender[1]'] = callback_query.data
        data['[3].CheckBox46_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертый ребенок — мужчина")
    await bot.send_message(callback_query.from_user.id, "Этот находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.A_II_ChooseLocationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox47[0]'] = callback_query.data
        data['[3].CheckBox47[1]'] = ""
    await Form_I_589.A_II_PtAIILine14_PlaceofLastEntry4_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертый ребенок находится в США")
    await bot.send_message(callback_query.from_user.id, "Укажите место его последнего въезда в США")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.A_II_ChooseLocationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].CheckBox47[1]'] = callback_query.data
        data['[3].CheckBox47[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])

    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш четвертый ребенок находится в США")

    if total_number_of_children > 4:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild5.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для Вашего пятого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine13_Specify4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine13_Specify4[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
    await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine14_PlaceofLastEntry4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine14_PlaceofLastEntry4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату последнего въезда в США Вашего четвертого ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine15_DateofLastEntry4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine15_DateofLastEntry4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер I-94 Вашего четвертого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine16_I94Number4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number4[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите статус при последнем въезде Вашего четвертого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine16_I94Number4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine16_I94Number4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите статус при последнем въезде Вашего четвертого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущий статус Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine17_StatusofLastAdmission4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine17_StatusofLastAdmission4[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий статус Вашего четвертого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine18_ChildCurrentStatus4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine18_ChildCurrentStatus4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите, когда заканчивается срок законного пребывания Вашего четвертого ребенка в стране (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay4[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ваш четвертый ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_II_PtAIILine19_ExpDateofAuthorizedStay4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine19_ExpDateofAuthorizedStay4[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Ваш четвертый ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes4[0]'] = callback_query.data
        data['[3].PtAIILine20_No4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш четвертый ребенок находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.A_II_IsImmigrationCourtProceedingsChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine20_Yes4[0]'] = ""
        data['[3].PtAIILine20_No4[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш четвертый ребенок не находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine21_Yes4[0]'] = callback_query.data
        data['[3].PtAIILine21_No4[0]'] = ""
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш четвертый ребенок должен быть включен в это приложение")

    if total_number_of_children > 4:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild5.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего пятого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.A_II_IsIncludedInApplicationChild4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].PtAIILine21_Yes4[0]'] = ""
        data['[3].PtAIILine21_No4[0]'] = callback_query.data
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш четвертый ребенок должен быть включен в это приложение")

    if total_number_of_children > 4:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild5.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего пятого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите регистрационный номер иностранца Вашего пятого ребенка (номер A) (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")


# Child 5
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[6]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта/удостоверения личности Вашего пятого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[6]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер паспорта/удостоверения личности Вашего пятого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_7)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[7]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение Вашего пятого ребенка",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_7)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[7]'] = message.text
        await Form_I_589.next()
        keyboard = Form_I_589_Marital_Status_Choice()
        await bot.send_message(message.from_user.id,
                               "Выберите семейное положение Вашего пятого ребенка",
                               reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_single",
                           state=Form_I_589.Supplement_A_TextField12_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[8]'] = "Single"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок не состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего пятого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_married",
                           state=Form_I_589.Supplement_A_TextField12_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[8]'] = "Married"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего пятого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_divorced",
                           state=Form_I_589.Supplement_A_TextField12_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[8]'] = "Divorced"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок разведен")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего пятого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_widowed",
                           state=Form_I_589.Supplement_A_TextField12_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[8]'] = "Widowed"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок вдова(-ец)")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего пятого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_9)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[9]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_9)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[9]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите фамилию Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения Вашего пятого ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_DateTimeField14_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].DateTimeField14[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите расу, этническую или племенную группу Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[5]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Укажите пол Вашего пятого ребенка:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.Supplement_A_ChooseGenderChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox12_Gender[1]'] = callback_query.data
        data['[12].CheckBox12_Gender[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок — женщина")
    await bot.send_message(callback_query.from_user.id, "Этот ребенок находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.Supplement_A_ChooseGenderChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox12_Gender[1]'] = ""
        data['[12].CheckBox12_Gender[0]'] = callback_query.data
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок — мужчина")
    await bot.send_message(callback_query.from_user.id, "Этот ребенок находится в США?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox57[0]'] = callback_query.data
        data['[12].CheckBox57[1]'] = ""
    await Form_I_589.Supplement_A_ChildEntry5_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок находится в США")
    await bot.send_message(callback_query.from_user.id, "Укажите место его последнего въезда в США")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].CheckBox57[0]'] = ""
        data['[12].CheckBox57[1]'] = callback_query.data
        total_number_of_children = int(data["[1].TotalChild[0]"])
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш пятый ребенок находится в США")

    if total_number_of_children > 5:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild6.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего шестого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_SuppLALine13_Specify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppLALine13_Specify[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
    await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildEntry5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildEntry5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату последнего въезда в США Вашего пятого ребенка (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildExp5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExp5[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер I-94 Вашего пятого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildINum5_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum5[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите статус при последнем въезде Вашего пятого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildINum5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum5[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите статус при последнем въезде Вашего пятого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildStatus5_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus5[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущий статус Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildStatus5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus5[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий статус Вашего пятого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildCurrent5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildCurrent5[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите, когда заканчивается срок законного пребывания Вашего пятого ребенка в стране (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildExpAuth5_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth5[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ваш пятый ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildExpAuth5_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth5[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Ваш пятый ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[0]'] = callback_query.data
        data['[12].SuppA_CheckBox20[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш пятый ребенок находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_child_imc",
                           state=Form_I_589.Supplement_A_IsImmigrationCourtProceedingsChild5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppA_CheckBox20[1]'] = callback_query.data
        data['[12].SuppA_CheckBox20[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш пятый ребенок не находится в процессе судебного разбирательства в иммиграционном суде")
    keyboard = Form_I_589_Include_Child_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
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
                           "Вы указали, что Ваш пятый ребенок должен быть включен в это приложение")

    if total_number_of_children > 5:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild6.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для Вашего шестого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
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
                           "Вы указали, что Ваш пятый ребенок должен быть включен в это приложение")

    if total_number_of_children > 5:
        keyboard = Form_I_589_Fill_Next_Child_Choice()
        await Form_I_589.Supplement_A_IsFillChild6.set()
        await bot.send_message(callback_query.from_user.id,
                               "Вы хотите заполнить данные для вашего шестого ребенка?",
                               reply_markup=keyboard.markup)
    else:
        await bot.send_message(callback_query.from_user.id,
                               "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
        await Form_I_589.A_III_TextField13_0.set()


@dp.callback_query_handler(text="yes_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите регистрационный номер иностранца Вашего шестого ребенка (номер A) (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_fill_next_child",
                           state=Form_I_589.Supplement_A_IsFillChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")


# Child 6
@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_16)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[16]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта/удостоверения личности Вашего шестого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_16)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[16]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер паспорта/удостоверения личности Вашего шестого (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_17)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[17]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Marital_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение Вашего шестого",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_17)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[17]'] = message.text
        await Form_I_589.next()
        keyboard = Form_I_589_Marital_Status_Choice()
        await bot.send_message(message.from_user.id,
                               "Выберите семейное положение Вашего шестого",
                               reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_single",
                           state=Form_I_589.Supplement_A_TextField12_18)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[18]'] = "Single"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок не состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего шестого (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_married",
                           state=Form_I_589.Supplement_A_TextField12_18)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[18]'] = "Married"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок состоит в браке")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего шестого (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_divorced",
                           state=Form_I_589.Supplement_A_TextField12_18)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[18]'] = "Divorced"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок разведен")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего шестого (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ms_widowed",
                           state=Form_I_589.Supplement_A_TextField12_18)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[18]'] = "Widowed"
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок вдова(-ец)")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США Вашего шестого (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_TextField12_19)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[19]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию Вашего шестого")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_19)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[19]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите фамилию Вашего шестого")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_10)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[10]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите имя Вашего шестого")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_12)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[12]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите отчество Вашего шестого")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_13)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[13]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения Вашего шестого (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_DateTimeField14_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].DateTimeField14[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите город и страну рождения Вашего шестого")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_11)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[11]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите гражданство Вашего шестого")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_14)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[14]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Укажите расу, этническую или племенную группу Вашего шестого")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_TextField12_15)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].TextField12[15]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Gender_Choice()
    await bot.send_message(message.from_user.id, "Укажите пол Вашего шестого:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=Form_I_589.Supplement_A_ChooseGenderChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL12_CheckBox[1]'] = callback_query.data
        data['[12].SuppAL12_CheckBox[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок — женщина")
    await bot.send_message(callback_query.from_user.id, "Ваш шестой ребенок находится в США?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=Form_I_589.Supplement_A_ChooseGenderChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL12_CheckBox[0]'] = callback_query.data
        data['[12].SuppAL12_CheckBox[1]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Location_Choice()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок — мужчина")
    await bot.send_message(callback_query.from_user.id, "Ваш шестой ребенок находится в США?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL13_CheckBox[0]'] = callback_query.data
        data['[12].SuppAL13_CheckBox[1]'] = ""
    await Form_I_589.Supplement_A_ChildEntry6_0.set()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок находится в США")
    await bot.send_message(callback_query.from_user.id, "Укажите место его последнего въезда в США")


@dp.callback_query_handler(text="no_location",
                           state=Form_I_589.Supplement_A_ChooseLocationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppAL13_CheckBox[1]'] = callback_query.data
        data['[12].SuppAL13_CheckBox[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш шестой ребенок находится в США")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")
    await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_SuppLALine13_Specify2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppLALine13_Specify2[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боялись преследования.")
    await Form_I_589.A_III_TextField13_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildEntry6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildEntry6[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату последнего въезда в США Вашего шестого (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildExp6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExp6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер I-94 Вашего шестого ребенка (если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildINum6_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum6[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите статус при последнем въезде Вашего шестого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildINum6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildINum6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите статус при последнем въезде Вашего шестого ребенка (тип визы, если есть)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildStatus6_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus6[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущий статус Вашего шестого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildStatus6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildStatus6[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий статус Вашего шестого ребенка")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildCurrent6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildCurrent6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите, когда заканчивается срок законного пребывания Вашего шестого в стране (мм/дд/гггг)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.Supplement_A_ChildExpAuth6_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth6[0]'] = ""
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ваш шестой ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.Supplement_A_ChildExpAuth6_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[12].ChildExpAuth6[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Child_Immigration_Court_Choice()
    await bot.send_message(message.from_user.id,
                           "Ваш шестой ребенок находится в процессе судебного разбирательства в иммиграционном суде?",
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
                           "Вы указали, что Ваш шестой ребенок находится в процессе судебного разбирательства в иммиграционном суде")
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
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
                           "Вы указали, что Ваш шестой ребенок не находится в процессе судебного разбирательства в иммиграционном суде")
    await bot.send_message(callback_query.from_user.id,
                           "Если этот ребенок находится в США, должен ли он быть включен в это приложение?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_include_child",
                           state=Form_I_589.Supplement_A_IsIncludedInApplicationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppALine21_CheckBox[0]'] = callback_query.data
        data['[12].SuppALine21_CheckBox[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш шестой ребенок должен быть включен в это приложение")

    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боитесь преследований. Сначала укажите номер и улицу")


@dp.callback_query_handler(text="no_include_child",
                           state=Form_I_589.Supplement_A_IsIncludedInApplicationChild6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[12].SuppALine21_CheckBox[1]'] = callback_query.data
        data['[12].SuppALine21_CheckBox[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что Ваш шестой ребенок должен быть включен в это приложение")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боялись преследования."
                           "\n"
                           "Сначала укажите номер и название улицы:")


# Last address with no fear of persecution
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы не боялись преследования."
                           "\n"
                           "Укажите город, где Вы жили до приезда в Соединенные Штаты и не боялись преследования:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите округ, провинцию или штат, где Вы жили до приезда в Соединенные Штаты и не боялись преследования")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите страну, где Вы жили до приезда в Соединенные Штаты и не боялись преследования")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_6)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[6]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату (мм/гггг), с которой Вы проживали в этом месте")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField21_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField21[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату (мм/гггг) до которой Вы проживали в этом месте.")


# Address Where Fear Persecution
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField20_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField20[0]'] = message.text
    await Form_I_589.next()

    await bot.send_message(message.from_user.id,
                           "Укажите свой последний адрес, по которому вы жили до приезда в Соединенные Штаты, где вы опасались преследований."
                           "\n"
                           "Сначала введите название и номер улицы:")


# Last address with fear of persecution
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город, где вы жили до приезда в Соединенные Штаты, где вы опасались преследований. ")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите округ, провинцию или штат, где вы жили до приезда в Соединенные Штаты, где вы опасались преследований.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[5]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите страну, где вы жили до приезда в Соединенные Штаты, где вы опасались преследований.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_7)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[7]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату (мм/гггг), с которой Вы проживали в этом месте.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField22_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField22[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату (мм/гггг) до которой Вы проживали в этом месте")


# Present Address
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField23_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField23[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свой нынешний фактический адрес проживания.")
    await bot.send_message(message.from_user.id, "Сначала введите название и номер улицы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_8)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[8]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свой нынешний фактический адрес проживания.")
    await bot.send_message(message.from_user.id, "Укажите город")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_10)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[10]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свой нынешний фактический адрес проживания.")
    await bot.send_message(message.from_user.id, "Укажите округ, провинцию или штат")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_12)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[12]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свой нынешний фактический адрес проживания.")
    await bot.send_message(message.from_user.id, "Укажите страну")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_14)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[14]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свой нынешний фактический адрес проживания.")
    await bot.send_message(message.from_user.id, "Введите дату, когда вы въехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField24_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField24[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свой нынешний фактический адрес проживания.")
    await bot.send_message(message.from_user.id, "Введите дату, когда вы планируете выехать (мм/дд/гггг)")


# First Residence
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField26_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField26[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашем месте жительства за последние 5 лет.")
    await bot.send_message(message.from_user.id, "Укажите номер и название улицы первого места жительства:")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_9)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[9]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_11)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[11]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите округ, провинцию или штат")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_13)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[13]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите страну")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_15)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[15]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы въехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField25_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField25[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы выехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField27_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField27[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашем месте жительства за последние 5 лет.")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер и название улицы первого места жительства:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_16)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_28.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте следующую информацию о своем образовании, начиная с самой последней школы, которую вы посещали.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название школы:")


# Second Residence
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_16)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[16]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашем месте жительства за последние 5 лет.")
    await bot.send_message(message.from_user.id,
                           "Укажите город второго места жительства")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_17)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[17]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите округ, провинцию или штат")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_18)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[18]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите страну")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_19)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[19]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы въехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField28_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField28[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы съехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField29_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField29[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашем месте жительства за последние 5 лет.")
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер и название улицы третьего места жительства:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_20)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_28.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте следующую информацию о своем образовании, начиная с самой последней школы, которую вы посещали.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название школы:")


# Third Residence
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_20)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[20]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_21)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[21]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите округ, провинцию или штатe")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_22)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[23]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите страну")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_23)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[22]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы въехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField30_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField30[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы съехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField31_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField31[0]'] = message.text
        await Form_I_589.next()
        await bot.send_message(message.from_user.id,
                               "Предоставьте следующую информацию о вашем месте жительства за последние 5 лет.")
        keyboard = Form_I_589_If_Any_Choice()
        await bot.send_message(message.from_user.id,
                               "Укажите номер и название улицы четвертого места жительства:",
                               reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_24)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_28.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте следующую информацию о своем образовании, начиная с самой последней школы, которую вы посещали.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название школы:")


# Fourth Residence
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_24)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[24]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_25)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[25]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите округ, провинцию или штат")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_26)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[26]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите страну")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_27)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[27]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы въехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField32_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField32[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Введите дату, когда вы съехали (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField33_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField33[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о своем образовании, начиная с самой последней школы, которую вы посещали.")
    await bot.send_message(message.from_user.id,
                           "Укажите название вашей первой школы:")


# First School
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_28)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[28]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите тип вашей первой школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_30)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[30]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес вашей первой школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_32)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[32]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой Вы посещали школу (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField41_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField41[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания школы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField40_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField40[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о своем образовании.")
    await bot.send_message(message.from_user.id,
                           "Укажите название Вашей второй школы:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_29)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_40.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. "
                           "Сначала укажите свою нынешнюю работу.")
    await bot.send_message(callback_query.from_user.id, "Введите наименование и адрес работодателя")


# Second School
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_29)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[29]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите тип Вашей второй школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_31)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[31]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес Вашей второй школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_33)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[33]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой Вы посещали школу (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField38_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField38[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания школы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField39_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField39[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о своем образовании")
    await bot.send_message(message.from_user.id,
                           "Укажите название третьей школы: ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_34)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_40.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Сначала укажите свою нынешнюю работу.")
    await bot.send_message(callback_query.from_user.id, "Введите наименование и адрес работодателя")


# Third School
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_34)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[34]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите тип Вашей третьей школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_35)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[35]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес Вашей третьей школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_36)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[36]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой Вы посещали школу (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField37_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField37[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания школы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField36_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField36[0]'] = message.text

    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о своем образовании")
    await bot.send_message(message.from_user.id,
                           "Укажите название Вашей четвертой школы: ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_34)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_40.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Сначала укажите свою нынешнюю работу.")
    await bot.send_message(callback_query.from_user.id, "Введите наименование и адрес работодателя")


# Fourth School
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_37)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[37]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите тип вашей четвертой школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_38)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[38]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес вашей четвертой школы")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_39)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[39]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой Вы посещали школу (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField34_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField34[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания школы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField35_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField35[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Сначала укажите свою нынешнюю работу.")
    await bot.send_message(message.from_user.id, "Введите наименование и адрес работодателя")


# First Employer
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_40)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[40]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Сначала укажите свою нынешнюю работу.")
    await bot.send_message(message.from_user.id, "Укажите Вашу должность")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_42)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[42]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Сначала укажите свою нынешнюю работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите дату начала работы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField42_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField42[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Сначала укажите свою нынешнюю работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания работы (мм/дд/гггг)")


# Second Employer
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField44_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField44[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу вторую работу.",
                           reply_markup=keyboard.markup)
    await bot.send_message(message.from_user.id,
                           "Введите наименование и адрес работодателя")


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_41)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_46.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя матери")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_41)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[41]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу вторую работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите Вашу должность")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_43)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[43]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу вторую работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите дату начала работы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField43_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField43[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу вторую работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания работы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField45_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField45[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу вторую работу.",
                           reply_markup=keyboard.markup)
    await bot.send_message(message.from_user.id,
                           "Введите наименование и адрес работодателя")


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_41)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_46.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя матери")


# Third Employer
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_44)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[44]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу третюю работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите Вашу должность")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_45)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[45]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу третюю работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите дату начала работы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField46_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField46[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. Укажите вашу третюю работу.")
    await bot.send_message(message.from_user.id,
                           "Укажите дату окончания работы (мм/дд/гггг)")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_DateTimeField47_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].DateTimeField47[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_If_Any_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.",
                           reply_markup=keyboard.markup)
    await bot.send_message(message.from_user.id,
                           "Укажите полное имя матери")


@dp.callback_query_handler(text="don't_have_it",
                           state=Form_I_589.A_III_TextField13_46)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.A_III_TextField13_47.set()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя отца")


# Mother
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_46)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[46]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите город и страну рождения матери")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_49)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[49]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Mother_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "На данный момент, Ваша мать скончалась?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_mother_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_m_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].CheckBoxAIII5\\\\.m[0]"] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваша Мать скончалась")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя отца")
    await Form_I_589.A_III_TextField13_47.set()


@dp.callback_query_handler(text="no_mother_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_m_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.m[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что ваша Мать не скончалась")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущее местонахождение матери")
    await Form_I_589.A_III_TextField35_0.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField35_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите полное имя отца")


# Father
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_47)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[47]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите город и страну рождения отца")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_50)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[50]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Father_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "На данный момент, Ваш отец скончался?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_father_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_f_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.f[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш отец скончался")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя брата или сестры")
    await Form_I_589.A_III_TextField13_48.set()


@dp.callback_query_handler(text="no_father_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_f_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.f[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваш отец не скончался")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущее местонахождение отца")
    await Form_I_589.A_III_TextField35_1.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField35_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите полное имя брата или сестры")


# Sibling 1
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_48)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[48]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите город и страну рождения брата или сестры")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_51)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[51]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_1Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Ваша сестра или брат скончалась(-лся)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_1sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s1[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат скончалась(-лся)")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя брата или сестры")
    await Form_I_589.A_III_TextField13_52.set()


@dp.callback_query_handler(text="no_1sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s1[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат не скончалась(-лся)")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущее местоположение брата или сестры")
    await Form_I_589.A_III_TextField35_2.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField35_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите полное имя брата или сестры")


# Sibling 2
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_52)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[52]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите город и страну рождения брата или сестры")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_53)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[53]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_2Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Ваша сестра или брат скончалась(-лся)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_2sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s2[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат скончалась(-лся)")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя брата или сестры")
    await Form_I_589.A_III_TextField13_54.set()


@dp.callback_query_handler(text="no_2sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s2[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат не скончалась(-лся)")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущее местоположение брата или сестры")
    await Form_I_589.A_III_TextField35_3.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField35_3)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите полное имя брата или сестры")


# Sibling 3
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_54)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[54]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите город и страну рождения брата или сестры")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_55)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[55]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_3Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Ваша сестра или брат скончалась(-лся)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_3sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s3[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат скончалась(-лся)")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите полное имя брата или сестры")
    await Form_I_589.A_III_TextField13_56.set()


@dp.callback_query_handler(text="no_3sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат не скончалась(-лся)")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущее местоположение брата или сестры")
    await Form_I_589.A_III_TextField35_4.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField35_4)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[4]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите полное имя брата или сестры")


# Sibling 4
@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_56)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[56]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Укажите город и страну рождения брата или сестры")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField13_57)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField13[57]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_4Sibling_Deceased_Choice()
    await bot.send_message(message.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(message.from_user.id,
                           "Ваша сестра или брат скончалась(-лся)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_4sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s4[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат скончалась(-лся)")
    keyboard = Form_I_589_Asylum_Reason_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите верное:\nЯ прошу убежища или приостановления депортации  на основании:",
                           reply_markup=keyboard.markup)
    await Form_I_589.B_Asylum_Reason_Choice.set()


@dp.callback_query_handler(text="no_4sibling_deceased",
                           state=Form_I_589.A_III_CheckBoxAIII5_s4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[4].CheckBoxAIII5\\\\.s4[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что Ваша сестра или брат не скончалась(-лся)")
    await bot.send_message(callback_query.from_user.id,
                           "Предоставьте информацию о ваших родителях, братьях и сестрах.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите текущее местоположение брата или сестры")
    await Form_I_589.A_III_TextField35_5.set()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.A_III_TextField35_5)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].TextField35[5]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Asylum_Reason_Choice()
    await bot.send_message(message.from_user.id,
                           "Укажите верное:\nЯ прошу убежища или приостановления депортации  на основании:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="race_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxrace[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что просите убежища или приостановления депортации по признаку расы")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Испытывали ли Вы, ваша семья, близкие друзья, коллеги вред или жестокое обращение в прошлом от кого-либо?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="religion_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxreligion[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что просите убежища или приостановления депортации по признаку религии")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Испытывали ли Вы, ваша семья, близкие друзья, коллеги вред или жестокое обращение в прошлом от кого-либо?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="nationality_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxnationality[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что просите убежища или приостановления депортации по национальному признаку")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Испытывали ли Вы, ваша семья, близкие друзья, коллеги вред или жестокое обращение в прошлом от кого-либо?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="political_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxpolitics[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что просите убежища или приостановления депортации на основании политических убеждений.")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Испытывали ли Вы, ваша семья, близкие друзья, коллеги вред или жестокое обращение в прошлом от кого-либо?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="membership_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxsocial[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что просите убежища или приостановления депортации на основании членства в определенной социальной группе.")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Испытывали ли Вы, ваша семья, близкие друзья, коллеги вред или жестокое обращение в прошлом от кого-либо?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="torture_asylum_reason",
                           state=Form_I_589.B_Asylum_Reason_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].CheckBoxtorture[0]'] = callback_query.data
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что просите убежища или приостановления депортации на основании "
                           "Конвенции против пыток.")
    keyboard = Form_I_589_Family_Experienced_Harm_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Испытывали ли Вы, ваша семья, близкие друзья, коллеги вред или жестокое обращение "
                           "в прошлом от кого-либо?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_family_harm",
                           state=Form_I_589.B_Family_Experienced_Harm_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1a[0]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1a[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваша семья, близкие друзья или коллеги когда-либо подвергались "
                           "в прошлом вреду, жестокому обращению или угрозам со стороны кого-либо.")
    await bot.send_message(callback_query.from_user.id,
                           "Опишите:\n"
                           "1) что произошло; \n"
                           "2) какой конкретно вред или жестокое обращение вы перенесли; \n"
                           "3) кто выступал обидчиком; \n"
                           "4) причины нанесения вреда и жестокого обращения по вашему мнению")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.B_TextField14_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].TextField14[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Fear_Harm_Or_Mistreatment_Choice()
    await bot.send_message(message.from_user.id,
                           "Боитесь ли вы потенциального вреда или жестокого обращения при возвращении на родину?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_family_harm",
                           state=Form_I_589.B_Family_Experienced_Harm_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1a[1]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1a[0]'] = ""
    await Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваша семья, близкие друзья или коллеги когда-либо в прошлом "
                           "подвергались вреду, жестокому обращению или угрозам со стороны кого-либо.")
    keyboard = Form_I_589_You_Fear_Harm_Or_Mistreatment_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Боитесь ли вы причинения вреда или плохого обращения, если вернетесь на родину?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_you_fear_harm",
                           state=Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1b[0]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1b[1]'] = ""
    await Form_I_589.B_TextField15_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что опасаетесь причинения вреда или плохого обращения, если вернетесь "
                           "в свою родную страну.")
    await bot.send_message(callback_query.from_user.id,
                           "Если да, объясните подробно:\n"
                           "1. Какого вреда или жестокого обращения вы опасаетесь;\n"
                           "2. Кто, по вашему мнению, может причинить вам вред или плохо с вами обращаться; и\n"
                           "3. Почему вы считаете, что вам могут или могут причинить вред или плохо с вами обращаться.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.B_TextField15_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].TextField15[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice()
    await bot.send_message(message.from_user.id,
                           "Были ли вы или члены вашей семьи когда-либо "
                           "обвинены, обвинены, арестованы, задержаны, допрошены, осуждены и приговорены"
                           " или заключены в тюрьму в какой-либо стране, кроме Соединенных Штатов "
                           "(в том числе за нарушение иммиграционного законодательства)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_you_fear_harm",
                           state=Form_I_589.B_You_Fear_Harm_Or_Mistreatment_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[5].#subform[6].ckboxyn1b[1]'] = callback_query.data
        data['[5].#subform[6].ckboxyn1b[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не боитесь причинения вреда или плохого обращения, "
                           "если вернетесь в свою родную страну.")
    keyboard = Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Были ли вы или члены вашей семьи когда-либо "
                           "обвинены, обвинены, арестованы, задержаны, допрошены, осуждены и приговорены"
                           " или заключены в тюрьму в какой-либо стране, кроме Соединенных Штатов "
                           "(в том числе за нарушение иммиграционного законодательства)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_violated_law",
                           state=Form_I_589.B_You_Or_Family_Accused_Charged_Arrested_Detained_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn2[0]'] = callback_query.data
        data['[7].ckboxyn2[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы или члены вашей семьи были обвинены, арестованы, задержаны, допрошены, "
                           "осуждены и приговорены или заключены в тюрьму в любой стране, кроме Соединенных Штатов.")
    await bot.send_message(callback_query.from_user.id,
                           "Объясните обстоятельства и причины поступка.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.B_PBL2_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PBL2_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Been_Associated_With_Any_Organizations_Choice()
    await bot.send_message(message.from_user.id,
                           "Вы или члены вашей семьи когда-либо принадлежали или были связаны с какими-либо "
                           "организациями или группами в вашей стране, такими как, помимо прочего, политическая партия, "
                           "студенческая группа, профсоюз, религиозная организация, военная или военизированная группа, "
                           "гражданский патруль, партизанская организация, этническая группа, правозащитная группа, "
                           "пресса или средства массовой информации? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_violated_law",
                           state=Form_I_589.B_You_Or_Family_Accused_Charged_Arrested_Detained_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn2[1]'] = callback_query.data
        data['[7].ckboxyn2[0]'] = ""
    await Form_I_589.B_Been_Associated_With_Any_Organizations_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы или члены вашей семьи не были обвинены, арестованы, задержаны, "
                           "допрошены, "
                           "осуждены и приговорены или заключены в тюрьму в любой стране, кроме Соединенных Штатов.")
    keyboard = Form_I_589_You_Been_Associated_With_Any_Organizations_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы или члены вашей семьи когда-либо принадлежали или были связаны с какими-либо "
                           "организациями или группами в вашей стране, такими как, помимо прочего, политическая партия,"
                           " "
                           "студенческая группа, профсоюз, религиозная организация, военная или военизированная группа,"
                           " "
                           "гражданский патруль, партизанская организация, этническая группа, правозащитная группа, "
                           "пресса или средства массовой информации? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Been_Associated_With_Any_Organizations",
                           state=Form_I_589.B_Been_Associated_With_Any_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3a[0]'] = callback_query.data
        data['[7].ckboxyn3a[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Опишите для каждого человека уровень участия, какие-либо руководящие или другие должности, "
                           "а также продолжительность времени, в течение которого вы или ваши члены семьи "
                           "были вовлечены в каждую организацию.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.B_PBL3A_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PBL3A_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Continue_To_Participate_In_Organizations_Choice()
    await bot.send_message(message.from_user.id,
                           "Продолжаете ли вы или члены вашей семьи каким-либо образом участвовать "
                           "в этих организациях или группах?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Been_Associated_With_Any_Organizations",
                           state=Form_I_589.B_Been_Associated_With_Any_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3a[1]'] = callback_query.data
        data['[7].ckboxyn3a[0]'] = ""
    await Form_I_589.B_Continue_To_Participate_In_Organizations_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы или члены вашей семьи никогда не принадлежали и не были связаны "
                           "с какими-либо организациями или группами в вашей родной стране, такими как, помимо "
                           "прочего, политическая партия, студенческая группа, профсоюз, религиозная организация, "
                           "военная или военизированная группа, гражданский патруль, партизанская организация, "
                           "этническая группа, человек. правозащитная группа или пресса или СМИ?")
    keyboard = Form_I_589_You_Continue_To_Participate_In_Organizations_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Продолжаете ли вы или члены вашей семьи каким-либо образом участвовать "
                           "в этих организациях или группах? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Continue_To_Participate_In_Organizations",
                           state=Form_I_589.B_Continue_To_Participate_In_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3b[0]'] = callback_query.data
        data['[7].ckboxyn3b[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Опишите для каждого человека текущий уровень вашего участия или участия членов вашей "
                           "семьи, какие-либо руководящие или другие должности, занимаемые в настоящее время, "
                           "и как долго вы или члены вашей семьи были вовлечены в каждую организацию или группу.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.B_PBL3B_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PBL3B_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Afraid_Of_Being_Subjected_To_Torture_Choice()
    await bot.send_message(message.from_user.id,
                           "Боитесь ли вы подвергнуться пыткам в своей родной стране или в любой другой стране, "
                           "куда вас могут вернуть? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Continue_To_Participate_In_Organizations",
                           state=Form_I_589.B_Continue_To_Participate_In_Organizations_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn3b[1]'] = callback_query.data
        data['[7].ckboxyn3b[0]'] = ""
    await Form_I_589.B_Afraid_Of_Being_Subjected_To_Torture_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы или члены вашей семьи не продолжаете каким-либо образом участвовать в этих организациях или группах.")
    keyboard = Form_I_589_You_Afraid_Of_Being_Subjected_To_Torture_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Боитесь ли вы подвергнуться пыткам в своей родной стране или в любой другой стране, "
                           "куда вас могут вернуть?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Afraid_Of_Being_Subjected_To_Torture",
                           state=Form_I_589.B_Afraid_Of_Being_Subjected_To_Torture_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn4[0]'] = callback_query.data
        data['[7].ckboxyn4[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Объясните, почему вы боитесь, и опишите характер пыток, которых вы опасаетесь, "
                           "кем и почему они могут быть применены.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.B_PB4_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[7].PB4_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Applied_For_USRefugee_Status_Choice()
    await bot.send_message(message.from_user.id,
                           "Ходатайствовали ли ранее вы, ваш супруг, ваш ребенок (дети), ваши родители или братья и "
                           "сестры когда-либо перед правительством США о предоставлении статуса беженца, убежища или "
                           "о приостановлении депортации? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Afraid_Of_Being_Subjected_To_Torture",
                           state=Form_I_589.B_Afraid_Of_Being_Subjected_To_Torture_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[7].ckboxyn4[1]'] = callback_query.data
        data['[7].ckboxyn4[0]'] = ""
    await Form_I_589.C_Family_Applied_For_USRefugee_Status_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не боитесь подвергнуться пыткам в своей родной стране или в "
                           "любой другой стране, куда вас могут вернуть.")
    keyboard = Form_I_589_Family_Applied_For_USRefugee_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Ходатайствовали ли ранее вы, ваш супруг, ваш ребенок (дети), ваши родители или братья и "
                           "сестры когда-либо перед правительством США о предоставлении статуса беженца, убежища или "
                           "о приостановлении депортации? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Applied_For_USRefugee_Status",
                           state=Form_I_589.C_Family_Applied_For_USRefugee_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync1[0]'] = callback_query.data
        data['[8].ckboxync1[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you ваш spouse ваш child(ren) ваш parents or ваш siblings ever applied to the U_S_ Government for refugee status asylum or withholding of removal")
    await bot.send_message(callback_query.from_user.id,
                           "Опишите решение и то, что случилось с любым статусом, который вы, ваш супруг, ваш ребенок "
                           "(дети), ваши родители или ваши братья и сестры получили в результате этого решения. "
                           "Укажите, были ли вы включены в заявление родителя или супруга. Если да, включите в свой "
                           "ответ A-number вашего родителя или супруга. Если вам было отказано в убежище "
                           "иммиграционным судьей или Иммиграционным апелляционным советом, опишите любые изменения "
                           "в условиях в вашей стране или ваших личных обстоятельствах с момента отказа, которые "
                           "могут повлиять на ваше право на получение убежища.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.C_PCL1_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[8].PCL1_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice()
    await bot.send_message(message.from_user.id,
                           "После отъезда из страны, от которой вы просите убежища, вы, ваш супруг или ребенок "
                           "(дети), которые в настоящее время находятся в Соединенных Штатах, путешествовали "
                           "или проживали в какой-либо другой стране до въезда в Соединенные Штаты?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Family_Applied_For_USRefugee_Status",
                           state=Form_I_589.C_Family_Applied_For_USRefugee_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync1[1]'] = callback_query.data
        data['[8].ckboxync1[0]'] = ""
    await Form_I_589.C_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы, ваш супруг, ваш ребенок (дети), ваши родители или ваши братья и "
                           "сестры никогда не обращались к правительству США за предоставлением статуса беженца "
                           "или приостановлением департации.")
    keyboard = Form_I_589_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "После отъезда из страны, от которой вы просите убежища, вы, ваш супруг или ребенок "
                           "(дети), которые в настоящее время находятся в Соединенных Штатах, путешествовали или "
                           "проживали в какой-либо другой стране до въезда в Соединенные Штаты?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Travel_Or_Reside_In_Other_Countries_Before_US",
                           state=Form_I_589.C_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2a[0]'] = callback_query.data
        data['[8].ckboxync2a[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы, ваш супруг или ребенок (дети), которые сейчас находятся в "
                           "Соединенных Штатах, путешествовали или проживали в любой другой стране до въезда "
                           "в Соединенные Штаты.")
    keyboard = Form_I_589_Family_Recieved_Any_Lawful_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы, ваш супруг, ваш ребенок (дети) или другие члены семьи, такие как ваши родители или "
                           "братья и сестры, когда-либо обращались или получали какой-либо законный статус в "
                           "какой-либо стране, кроме той, в которой вы сейчас запрашиваете убежище?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Family_Travel_Or_Reside_In_Other_Countries_Before_US",
                           state=Form_I_589.C_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2a[1]'] = callback_query.data
        data['[8].ckboxync2a[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы, ваш супруг или ребенок (дети), которые сейчас находятся в "
                           "Соединенных Штатах, не путешествовали и не проживали в какой-либо другой стране "
                           "до въезда в Соединенные Штаты.")
    keyboard = Form_I_589_Family_Recieved_Any_Lawful_Status_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы, ваш супруг, ваш ребенок (дети) или другие члены семьи, такие как ваши родители или "
                           "братья и сестры, когда-либо обращались или получали какой-либо законный статус в "
                           "какой-либо стране, кроме той, в которой вы сейчас запрашиваете убежище?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Recieved_Any_Lawful_Status",
                           state=Form_I_589.C_Family_Recieved_Any_Lawful_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2b[0]'] = callback_query.data
        data['[8].ckboxync2b[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите для каждого лица следующее: название каждой страны и продолжительность пребывания, "
                           "статус лица во время пребывания в стране, причины выезда, и обращалось ли это лицо за "
                           "статусом беженца или за убежищем, находясь там, и если нет, то почему оно этого не сделало.")


@dp.callback_query_handler(text="no_Family_Recieved_Any_Lawful_Status",
                           state=Form_I_589.C_Family_Recieved_Any_Lawful_Status_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync2b[1]'] = callback_query.data
        data['[8].ckboxync2b[0]'] = ""
        answered_yes_in_previous_question = data['[8].ckboxync2a[0]']

    if answered_yes_in_previous_question:
        await Form_I_589.next()
        await bot.send_message(callback_query.from_user.id,
                            "Укажите для каждого лица следующее: название каждой страны и продолжительность пребывания, "
                           "статус лица во время пребывания в стране, причины выезда, и обращалось ли это лицо за "
                           "статусом беженца или за убежищем, находясь там, и если нет, то почему оно этого не сделало.")
    else:
        keyboard = Form_I_589_You_Or_Family_Caused_Harm_Or_Suffering_Choice()
        await bot.send_message(callback_query.from_user.id,
                               "Вы, ваш супруг или ваш ребенок (дети) когда-либо подстрекали, помогали или иным "
                               "образом участвовали в причинении вреда или страданий какому-либо лицу из-за его или "
                               "ее расы, религии, национальности, принадлежности к определенной социальной группе "
                               "или политических убеждений? ",
                               reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.C_PCL2B_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[8].PCL2B_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Or_Family_Caused_Harm_Or_Suffering_Choice()
    await bot.send_message(message.from_user.id,
                           "Вы, ваш супруг или ваш ребенок (дети) когда-либо подстрекали, помогали или иным образом "
                           "участвовали в причинении вреда или страданий какому-либо лицу из-за его или ее расы, "
                           "религии, национальности, принадлежности к определенной социальной группе или "
                           "политических убеждений? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Or_Family_Caused_Harm_Or_Suffering",
                           state=Form_I_589.C_You_Or_Family_Caused_Harm_Or_Suffering_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync3[0]'] = callback_query.data
        data['[8].ckboxync3[1]'] = ""
    await Form_I_589.next()

    await bot.send_message(callback_query.from_user.id,
                           "Подробно опишите каждый такой случай и участие в нем Вас, вашего супруга или "
                           "вашего ребенка (детей).")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.C_PCL3_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[8].PCL3_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Returned_To_Bad_Country_Choice()
    await bot.send_message(message.from_user.id,
                           "После того, как вы покинули страну, где вам причинили вред или вы "
                           "опасались вреда, вы возвращались в эту страну? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_You_Or_Family_Caused_Harm_Or_Suffering",
                           state=Form_I_589.C_You_Or_Family_Caused_Harm_Or_Suffering_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[8].ckboxync1[1]'] = callback_query.data
        data['[8].ckboxync1[0]'] = ""
    await Form_I_589.C_Returned_To_Bad_Country_Choice.set()
    await bot.send_message(callback_query.from_user.id,
                           "You indicated that you, ваш spouse or ваш child(ren) have never ordered, incited, assisted or otherwise participated in causing harm or suffering to any person because of his or her race, religion, nationality, membership in a particular social group or belief in a particular political opinion")
    keyboard = Form_I_589_Returned_To_Bad_Country_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "После того, как вы покинули страну, где вам причинили вред или вы "
                           "опасались вреда, вы возвращались в эту страну? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Returned_To_Bad_Country",
                           state=Form_I_589.C_Returned_To_Bad_Country_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCckboxyn4[0]'] = callback_query.data
        data['[9].PCckboxyn4[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Подробно опишите обстоятельства вашего визита(ов) (например, дату(ы) поездки(ей), цель(и) "
                           "поездки(ок) и продолжительность вашего визита(ов) и время, в течение которого вы "
                           "оставались в этой стране во время визита(ов).")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.C_PCL4_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCL4_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Last_Arrival_To_US_More_Than_1_Year_Choice()
    await bot.send_message(message.from_user.id,
                           "Вы подаете это заявление более чем через год после вашего последнего прибытия "
                           "в Соединенные Штаты?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Returned_To_Bad_Country",
                           state=Form_I_589.C_Returned_To_Bad_Country_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCckboxyn4[1]'] = callback_query.data
        data['[9].PCckboxyn4[0]'] = ""
    await Form_I_589.C_Last_Arrival_To_US_More_Than_1_Year_Choice.set()
    keyboard = Form_I_589_Last_Arrival_To_US_More_Than_1_Year_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете это заявление более чем через год после вашего последнего прибытия "
                           "в Соединенные Штаты?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Last_Arrival_To_US_More_Than_1_Year",
                           state=Form_I_589.C_Last_Arrival_To_US_More_Than_1_Year_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync5[0]'] = callback_query.data
        data['[9].ckboxync5[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Объясните, почему вы не подали заявление в течение первого года после прибытия. "
                           "Вы должны быть готовы объяснить на собеседовании или слушании, почему вы не подали "
                           "заявление о предоставлении убежища в течение первого года после прибытия.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.C_PCL5_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCL5_TextField[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_You_Or_Family_Did_Crime_Choice()
    await bot.send_message(message.from_user.id,
                           "Совершали ли вы или кто-либо из членов вашей семьи, включенных в заявку, какое-либо "
                           "преступление и/или были ли арестованы, обвинены или осуждены за какие-либо преступления "
                           "в Соединенных Штатах (в том числе за нарушение иммиграционного законодательства)? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Last_Arrival_To_US_More_Than_1_Year",
                           state=Form_I_589.C_Last_Arrival_To_US_More_Than_1_Year_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync5[1]'] = callback_query.data
        data['[9].ckboxync5[0]'] = ""
    await Form_I_589.C_You_Or_Family_Did_Crime_Choice.set()
    keyboard = Form_I_589_You_Or_Family_Did_Crime_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Совершали ли вы или кто-либо из членов вашей семьи, включенных в заявку, какое-либо "
                           "преступление и/или были ли арестованы, обвинены или осуждены за какие-либо преступления "
                           "в Соединенных Штатах (в том числе за нарушение иммиграционного законодательства)? ",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_You_Or_Family_Did_Crime",
                           state=Form_I_589.C_You_Or_Family_Did_Crime_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync6[0]'] = callback_query.data
        data['[9].ckboxync6[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Для каждого случая укажите в своем ответе: что произошло и обстоятельства, даты, "
                           "срок вынесения приговора, местонахождение, продолжительность задержания или заключения, "
                           "причину (причины) задержания или осуждения, любые формальные обвинения. которые были "
                           "поданы против вас или ваших родственников, включенных в ваше заявление, и причину(ы) "
                           "освобождения.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.C_PCL6_TextField_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[9].PCL6_TextField[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите Ваше полное имя",
                           )


@dp.callback_query_handler(text="no_You_Or_Family_Did_Crime",
                           state=Form_I_589.C_You_Or_Family_Did_Crime_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[9].ckboxync6[1]'] = callback_query.data
        data['[9].ckboxync6[0]'] = ""
    await Form_I_589.D_TextField20_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите Ваше полное имя")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.D_TextField20_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField20[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите свое имя на родном алфавите")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.D_TextField20_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField20[1]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Helped_Complete_Application_Choice()
    await bot.send_message(message.from_user.id,
                           "Помогал ли Вам ваш супруг, родитель или ребенок (дети) в заполнении этого заявления?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Helped_Complete_Application",
                           state=Form_I_589.D_Family_Helped_Complete_Application)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ckboxynd1[0]'] = callback_query.data
        data['[10].PtD_ckboxynd1[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш супруг, родитель или ребенок (дети) помогают вам заполнить это заявление.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите имя того, кто помог вам заполнить это заявление.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.D_PtD_ChildName1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ChildName1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите Ваши отношения с этим человеком.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.D_PtD_RelationshipOfChild1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ChildName1[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Family_Helped_Complete_Fill_Next_Member_Choice()
    await bot.send_message(message.from_user.id,
                           "Вы хотите указать еще одного помощника?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Family_Helped_Complete_Fill_Next_Member_Choice",
                           state=Form_I_589.D_PtD_ChildName2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что второй член семьи помог вам заполнить заявление.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите имя того, кто помог вам заполнить это заявление.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.D_PtD_ChildName2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_ChildName2[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите Ваши отношения с этим человеком.")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.D_PtD_RelationshipOfChild2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtD_RelationshipOfChild2[0]'] = message.text
    await Form_I_589.next()
    keyboard = Form_I_589_Not_Family_Helped_Complete_Application_Choice()
    await bot.send_message(message.from_user.id,
                           "Подготовил ли это заявление кто-то, кроме Вашего супруга, родителя или ребенка (детей)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="no_Family_Helped_Complete_Fill_Next_Member_Choice",
                           state=Form_I_589.D_PtD_ChildName2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await Form_I_589.D_Not_Family_Helped_Complete_Application.set()
    keyboard = Form_I_589_Not_Family_Helped_Complete_Application_Choice()
    await bot.send_message(callback_query.from_user.id,
                           "Подготовил ли это заявление кто-то, кроме Вашего супруга, родителя или ребенка (детей)?",
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
                           "Подготовил ли это заявление кто-то, кроме Вашего супруга, родителя или ребенка (детей)?",
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
                           "Заявители могут быть представлены адвокатом. Был ли вам предоставлен список лиц, которые"
                           " могут помочь вам, за небольшую плату или бесплатно, с Вашим заявлением о "
                           "предоставлении убежища?",
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
                           "Заявители могут быть представлены адвокатом. Был ли вам предоставлен список лиц, которые"
                           " могут помочь вам, за небольшую плату или бесплатно, с Вашим заявлением о "
                           "предоставлении убежища?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="yes_Provided_With_List_Of_Persons_Who_May_Assist",
                           state=Form_I_589.D_Provided_With_List_Of_Persons_Who_May_Assist_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].ckboxynd3[0]'] = callback_query.data
        data['[10].ckboxynd3[1]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите Вашу подпись")


@dp.callback_query_handler(text="no_Provided_With_List_Of_Persons_Who_May_Assist",
                           state=Form_I_589.D_Provided_With_List_Of_Persons_Who_May_Assist_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[10].ckboxynd3[1]'] = callback_query.data
        data['[10].ckboxynd3[0]'] = ""
    await Form_I_589.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите Вашу подпись")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.D_TextField22_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField22[0]'] = message.text
        data['[10].DateTimeField48[0]'] = datetime.datetime.now().strftime("%d/%m/%Y")
        is_preparer = data['[10].ckboxynd2[0]']
    if is_preparer:
        await Form_I_589.next()
        await bot.send_message(message.from_user.id,
                               "Укажите Подпись составителя")
    else:
        async with state.proxy() as data:
            adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                             user_id=message.from_user.id,
                                             timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
            adapter.save_json()
            await bot.send_message(message.chat.id,
                                   f"Ваши данные для формы {data['form_identifier']} успешно сохранены! Дождитесь pdf-файла.")
            await bot.send_chat_action(message.chat.id, "typing")
            pdf_file_path = adapter.fill_pdf()
            with open(pdf_file_path, 'rb') as file:
                await bot.send_document(message.chat.id, file)
        await state.finish()


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_PtE_PreparerSignature_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_PreparerSignature[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Укажите полное имя составителя")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_PtE_PreparerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_PreparerName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Код номера телефона составителя")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_TextField25_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField25[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Номер телефона составителя")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_TextField25_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].TextField25[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Адрес составителя: Номер улицы и имя")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_PtE_StreetNumAndName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_StreetNumAndName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Адрес составителя: номер квартиры")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_PtE_AptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Адрес составителя: Город")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_PtE_City_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_City[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Адрес составителя: Штат")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_PtE_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id,
                           "Адрес составителя: почтовый индекс")


@escape_json_special_chars
@dp.message_handler(state=Form_I_589.E_PtE_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[10].PtE_ZipCode[0]'] = message.text

        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        adapter.save_json()
        await bot.send_message(message.chat.id,
                               f"Ваши данные для формы {data['form_identifier']} успешно сохранены! Дождитесь pdf-файла.")
        await bot.send_chat_action(message.chat.id, "typing")
        pdf_file_path = adapter.fill_pdf()
        with open(pdf_file_path, 'rb') as file:
            await bot.send_document(message.chat.id, file)
    await state.finish()
