from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from telegram_bot.form_i_485.f_i_485_keyboards import \
    FormI485DontNeedAlternateMailingAddressChoice, FormI485SSAChoice, FormI485SSACouldUseInformationChoice, \
    FormI485WasInspectedAtPortOfEntryChoice, FormI485SpecialCategoryEntryGrantedChoice, \
    FormI485CameIntoUSWithoutAdmissionOrParoleChoice, FormI485I94WasIssuedChoice, \
    FormI485ImmigrationStatusDontChangedChoice, FormI485ApplicationByFamilyCategoryChoice
from telegram_bot.form_i_765.f_i_765_keyboards import FormI765TypeOfBuildingChoice
from telegram_bot.form_i_589.form_i_589_handlers import escape_json_special_chars
from telegram_bot.form_i_485.form_i_485_state_group import FormI485
from telegram_bot import bot, dp, FillPdfFromJsonAdapter, datetime, FormI589IfAnyChoice, FormI589GenderChoice
from telegram_bot.form_i_765.f_i_765_keyboards import FormI765UsedOtherNamesChoice, FormI765WantSSACardToBeIssuedChoice


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


@dp.callback_query_handler(text="I-485")
async def i_485_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-485"
    await bot.send_message(callback_query.from_user.id, "Вы выбрали форму I-485. Давайте приступим к ее заполнению.")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 1. «Информация о вас.»\n"
                           "Раздел «Ваше ФИО.»"
                           "Укажите вашу фамилию:")
    await FormI485.S_0_Pt1Line1a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line1a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line1a_FamilyName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line1b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line1b_GivenName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line1c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line1c_MiddleName[0]'] = message.text
    await FormI485.next()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали иные имена (например, девичья фамилия и псевдоним)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_Yes", state=FormI485.UsedOtherNamesChoice_1)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что использовали иные имена.")
    await bot.send_message(callback_query.from_user.id, "Раздел «Иные имена.» Далее укажите информацию "
                                                        "о иных используемых вами именах. ")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу фамилию:")
    await FormI485.S_0_Pt1Line2a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line2a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line2a_FamilyName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line2b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line2b_GivenName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line2c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line2c_MiddleName[0]'] = message.text
    await FormI485.UsedOtherNamesChoice_2.set()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали еще какие-либо иные имена, помимо указанного выше?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI485.UsedOtherNamesChoice_1)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    await FormI485.S_0_Pt1Line5_DateofBirth_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Иная информация о вас.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу дату рождения (мм/дд/гггг):")


@dp.callback_query_handler(text="UsedOtherNames_Yes", state=FormI485.UsedOtherNamesChoice_2)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что использовали иные имена.")
    await bot.send_message(callback_query.from_user.id, "Раздел «Иные имена.» Далее укажите информацию "
                                                        "об следующем ином используемом вами имени. ")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу фамилию:")
    await FormI485.S_0_Pt1Line3a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line3a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line3a_FamilyName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line3b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line3b_GivenName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line3c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line3c_MiddleName[0]'] = message.text
    await FormI485.UsedOtherNamesChoice_3.set()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали еще какие-либо иные имена, помимо указанного выше?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI485.UsedOtherNamesChoice_2)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    await FormI485.S_0_Pt1Line5_DateofBirth_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Иная информация о вас.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу дату рождения (мм/дд/гггг):")


@dp.callback_query_handler(text="UsedOtherNames_Yes", state=FormI485.UsedOtherNamesChoice_3)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что использовали иные имена.")
    await bot.send_message(callback_query.from_user.id, "Раздел «Иные имена.» Далее укажите информацию "
                                                        "об следующем ином используемом вами имени. ")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу фамилию:")
    await FormI485.S_0_Pt1Line4a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line4a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line4a_FamilyName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line4b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line4b_GivenName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line4c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line4c_MiddleName[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Раздел «Иная информация о вас.»")
    await bot.send_message(message.from_user.id,
                           "Укажите вашу дату рождения (мм/дд/гггг):")


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI485.UsedOtherNamesChoice_3)
async def callback_query_handler_UsedOtherNames_No(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    await FormI485.S_0_Pt1Line5_DateofBirth_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Иная информация о вас.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу дату рождения (мм/дд/гггг):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line5_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line5_DateofBirth[0]'] = message.text
    await FormI485.next()
    keyboard = FormI589GenderChoice()
    await bot.send_message(message.from_user.id,
                           "Выберите свой пол:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="female",
                           state=FormI485.GenderChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line6_Gender[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите город, где вы родились:")
    await FormI485.next()


@dp.callback_query_handler(text="male",
                           state=FormI485.GenderChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line6_Gender[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите город, где вы родились:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line6_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Pt1Line6_CityOrTown[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну, где вы родились:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line8_CountryofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line8_CountryofBirth[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну вашего гражданства:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line9_CountryofCitizenship_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line9_CountryofCitizenship[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите Ваш регистрационный номер иностранца (A-number) (если имеется):",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_1_Pt1Line10_AlienNumber_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет регистрационного номера иностранца (A-number).")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер онлайн-аккаунта USCIS (если имеется):",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line10_AlienNumber_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line10_AlienNumber[2]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер онлайн-аккаунта USCIS (если имеется):",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_1_Pt1Line11_USCISELISAcctNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет номера онлайн-аккаунта USCIS.")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Почтовый адрес.» Далее укажите информацию о вашем почтовом адресе.")
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line11_USCISELISAcctNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line11_USCISELISAcctNumber[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Почтовый адрес.» Далее укажите информацию о вашем почтовом адресе.")
    await bot.send_message(message.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_1_Pt1Line12_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что иное лицо не будет получать корреспонденцию за вас.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_InCareofName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_StreetNumberName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_Unit[2]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    await FormI485.S_1_Pt1Line12_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_Unit[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    await FormI485.S_1_Pt1Line12_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_Unit[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    await FormI485.S_1_Pt1Line12_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_AptSteFlrNumber[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_CityOrTown[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_State[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (например, 123456).\n"
                           "Найти почтовый индекс можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line12_ZipCode[0]'] = message.text
    await FormI485.next()
    keyboard = FormI485DontNeedAlternateMailingAddressChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Альтернативный и/или безопасный почтовый адрес.»")
    await bot.send_message(message.from_user.id,
                           "Если вы подаете заявление на основании Закона о насилии в отношении женщин (VAWA) или в "
                           "качестве особого несовершеннолетнего иммигранта, жертвы торговли людьми "
                           "(T для неиммигрантов) или жертвы квалифицируемого преступления (U для неиммигрантов), и вы "
                           "не хотите, чтобы USCIS отправляла уведомления об этом заявлении к Вам домой, вы можете "
                           "предоставить альтернативный и/или безопасный почтовый адрес далее.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_need_alternate_mailing_address",
                           state=FormI485.AlternateMailingAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SSAChoice()
    await bot.send_message(callback_query.from_user.id, "Раздел «Карта социального обеспечения "
                                                        "(Ssocial Security Card).»")
    await bot.send_message(callback_query.from_user.id,
                           "Выдавало ли вам когда-либо Управление социального обеспечения (SSA) карту социального "
                           "обеспечения (social security card)?",
                           reply_markup=keyboard.markup)
    await FormI485.SSA_Choice.set()


@dp.callback_query_handler(text="need_alternate_mailing_address",
                           state=FormI485.AlternateMailingAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_1_Pt1Line13_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что иное лицо не будет получать корреспонденцию за вас.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_InCareofName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_StreetNumberName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_Unit[2]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    await FormI485.S_1_Pt1Line13_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_Unit[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    await FormI485.S_1_Pt1Line13_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_Unit[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    await FormI485.S_1_Pt1Line13_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_AptSteFlrNumber[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_CityOrTown[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_State[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (например, 123456).\n"
                           "Найти почтовый индекс можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line13_ZipCode[0]'] = message.text
    keyboard = FormI485SSAChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Карта социального обеспечения (Ssocial Security Card).»")
    await bot.send_message(message.from_user.id,
                           "Выдавало ли вам когда-либо Управление социального обеспечения (SSA) карту социального "
                           "обеспечения (social security card)?",
                           reply_markup=keyboard.markup)
    await FormI485.SSA_Choice.set()


@dp.callback_query_handler(text="SSAChoice_Yes",
                           state=FormI485.SSA_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line14_YN[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США (SSN):")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line15_SSN_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line15_SSN[0]'] = message.text
    keyboard = FormI765WantSSACardToBeIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы хотите, чтобы SSA выдало вам карту социального обеспечения?",
                           reply_markup=keyboard.markup)
    await FormI485.IssueSSCChoice.set()


@dp.callback_query_handler(text="SSAChoice_No",
                           state=FormI485.SSA_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line14_YN[0]'] = "x"
    keyboard = FormI765WantSSACardToBeIssuedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы хотите, чтобы SSA выдало вам карту социального обеспечения?",
                           reply_markup=keyboard.markup)
    await FormI485.IssueSSCChoice.set()


@dp.callback_query_handler(text="WantSSACardToBeIssued_Yes",
                           state=FormI485.IssueSSCChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line16_YN[1]'] = "x"
    keyboard = FormI485SSACouldUseInformationChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы разрешаете раскрытие информации из этого заявления Управлению социального обеспечения "
                           "(SSA)? Это необходимо для присвоения вам номера социального страхования (SSN) и выдачи "
                           "карты социального страхования.",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="SSACouldUseInformation_Yes",
                           state=FormI485.SSACouldUseInformationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line17_YN[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Недавняя иммиграционная история». Заполните данный раздел, если вы в последний раз "
                           "въезжали в Соединенные Штаты по паспорту или проездному документу.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта, использованного при вашем последнем въезде в США:")
    await FormI485.S_1_Pt1Line18_PassportNum_0.set()


@dp.callback_query_handler(text="SSACouldUseInformation_No",
                           state=FormI485.SSACouldUseInformationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line17_YN[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Недавняя иммиграционная история». Заполните данный раздел, если вы в последний раз "
                           "въезжали в Соединенные Штаты по паспорту или проездному документу.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта, использованного при вашем последнем въезде в США:")
    await FormI485.S_1_Pt1Line18_PassportNum_0.set()


@dp.callback_query_handler(text="WantSSACardToBeIssued_No",
                           state=FormI485.IssueSSCChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line16_YN[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Недавняя иммиграционная история». Заполните данный раздел, если вы в последний раз "
                           "въезжали в Соединенные Штаты по паспорту или проездному документу.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта, использованного при вашем последнем въезде в США:")
    await FormI485.S_1_Pt1Line18_PassportNum_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line18_PassportNum_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line18_PassportNum[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите номер проездного документа (travel document), использованного при вашем "
                           "последнем въезде в США:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt2Line19_TravelDoc_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt2Line19_TravelDoc[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату истечения срока действия паспорта или проездного документа (мм/дд/гггг):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line20_ExpDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line20_ExpDate[0]'] = message.text
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Какая страна выдала вам последний паспорт или проездной документ (travel document)?")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line21_Passport_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line21_Passport[0]'] = message.text
    await FormI485.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер неиммиграционной визы из этого паспорта (если имеется):",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_1_Pt1Line22_VisaNum_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите место вашего последнего въезда в США.\n"
                           "Укажите город:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line22_VisaNum_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line22_VisaNum[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите место вашего последнего въезда в США.\n"
                           "Укажите город:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line23a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line23a_CityTown[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line23b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line23b_State[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату вашего последнего въезда в США (мм/дд/гггг):")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line24_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Pt1Line24_Date[0]'] = message.text
    keyboard = FormI485WasInspectedAtPortOfEntryChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите верное.\n"
                           "Когда я в последний раз въехал в США:\n"
                           "1. Я был(-а) проверен в порту въезда и допущен в общем порядке (например, посетителя по "
                           "обмену; посетителя; временного работника; студента и тд).",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="WasInspectedAtPortOfEntry_Yes",
                           state=FormI485.S_2_Pt1Line25a_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line25a_CB[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы ответили «Да» на вопрос выше. Укажите, в каком статусе вы въехали в страну:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line25a_AdmissionEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line25a_AdmissionEntry[0]'] = message.text
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    await FormI485.S_2_P2Line26a_I94_0.set()


@dp.callback_query_handler(text="WasInspectedAtPortOfEntry_No",
                           state=FormI485.S_2_Pt1Line25a_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SpecialCategoryEntryGrantedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "2. Я был(-а) досмотрен в порту въезда, и мне был разрешен въезд по особой категории "
                           "(например, по гуманитарному разрешению на въезд (humanitarian parole) или как гражданину "
                           "Кубы (Cuban parole)).",
                           reply_markup=keyboard.markup)
    await FormI485.S_2_Pt1Line25b_CB_0.set()


@dp.callback_query_handler(text="SpecialCategoryEntryGranted_Yes",
                           state=FormI485.S_2_Pt1Line25b_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line25b_CB[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы ответили «Да» на вопрос выше. Укажите, на основании какого статуса вам разрешили въезд:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line25b_ParoleEntrance_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line25b_ParoleEntrance[0]'] = message.text
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    await FormI485.S_2_P2Line26a_I94_0.set()


@dp.callback_query_handler(text="SpecialCategoryEntryGranted_No",
                           state=FormI485.S_2_Pt1Line25b_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485CameIntoUSWithoutAdmissionOrParoleChoice()
    await bot.send_message(callback_query.from_user.id,
                           "3. Я въехал(-а) в Соединенные Штаты без допуска или разрешения на въезд.",
                           reply_markup=keyboard.markup)
    await FormI485.S_2_Pt1Line25c_CB_0.set()


@dp.callback_query_handler(text="CameIntoUSWithoutAdmissionOrParole_Yes",
                           state=FormI485.S_2_Pt1Line25c_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line25c_CB[0]'] = "x"
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    await FormI485.S_2_P2Line26a_I94_0.set()


@dp.callback_query_handler(text="CameIntoUSWithoutAdmissionOrParole_No",
                           state=FormI485.S_2_Pt1Line25c_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line25d_CB[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "4. Иное.\n"
                           "Если вы не выбрали ни один из вариантов, укажите, каким образом вы въехали в США:")
    await FormI485.S_2_Pt2Line25d_other_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt2Line25d_other_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line25b_ParoleEntrance[0]'] = message.text
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    await FormI485.S_2_P2Line26a_I94_0.set()


@dp.callback_query_handler(text="I94WasIssued_Yes",
                           state=FormI485.I94WasIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Форма I-94.» Далее укажите сведения, указанные в форме I-94.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер записи о прибытии и выезде (указан в форме I-94):")
    await FormI485.S_2_P2Line26a_I94_0.set()


@dp.callback_query_handler(text="I94WasIssued_No",
                           state=FormI485.I94WasIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Форма I-94.» Далее укажите сведения, указанные в форме I-94.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер записи о прибытии и выезде (указан в форме I-94):")
    await FormI485.S_2_Pt2Line1_CB_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_P2Line26a_I94_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].P2Line26a_I94[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите номер записи о прибытии и выезде (указан в форме I-94):")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line26b_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line26b_Date[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату истечения срока разрешенного пребывания, указанную в форме I-94 (мм/дд/гггг):")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line26c_Status_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line26c_Status[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите статус в форме I-94 (например, класс допуска или вид разрешения на въезд (parole):")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line27_Status_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line27_Status[0]'] = message.text
    keyboard = FormI485ImmigrationStatusDontChangedChoice()
    await bot.send_message(message.from_user.id,
                           "Каков ваш текущий иммиграционный статус (если он изменился с момента вашего прибытия)?",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="ImmigrationStatusDontChanged_No",
                           state=FormI485.ImmigrationStatusDontChangedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш иммиграционный статус не изменился.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свое ФИО так, как оно указано в вашей форме I-94.\n"
                           "Укажите фамилию:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line28a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line28a_FamilyName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line28b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line28b_GivenName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line28c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt1Line28c_MiddleName[0]'] = message.text
    keyboard = FormI485ApplicationByFamilyCategoryChoice()
    await bot.send_message(message.from_user.id,
                           "Часть 2. «Тип заявления или категория подачи.»")
    await bot.send_message(message.from_user.id,
                           "Вы подаете заявление по семейной категории?",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="ApplicationByFamilyCategory_Yes",
                           state=FormI485.S_2_Pt2Line1_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш иммиграционный статус не изменился.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свое ФИО так, как оно указано в вашей форме I-94.\n"
                           "Укажите фамилию:")
    await FormI485.next()