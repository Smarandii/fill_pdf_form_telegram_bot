from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from telegram_bot.form_i_485.f_i_485_keyboards import \
    FormI485DontNeedAlternateMailingAddressChoice, FormI485SSAChoice, FormI485SSACouldUseInformationChoice, \
    FormI485WasInspectedAtPortOfEntryChoice, FormI485SpecialCategoryEntryGrantedChoice, \
    FormI485CameIntoUSWithoutAdmissionOrParoleChoice, FormI485I94WasIssuedChoice, \
    FormI485ImmigrationStatusDontChangedChoice, FormI485ApplicationByFamilyCategoryChoice, \
    FormI485TypeOfFamilyCategoryApplicationChoice, FormI485ApplicationByWorkingCategoryChoice, \
    FormI485ImmigrationAndNationalityActChoice, FormI485PrincipalApplicantChoice, \
    FormI485TypeOfEmploymentBasedCategoryChoice, FormI485TypeOfSpecialImmigrantCategoryChoice, \
    FormI485ApplicationBySpecialImmigrantCategoryChoice, FormI485ApplicationByAsyleeOrRefugeeCategoryChoice, \
    FormI485TypeOfAsyleeOrRefugeeCategoryChoice, FormI485ApplicationByHumanTraffickingVictimCategoryChoice, \
    FormI485TypeOfHumanTraffickingVictimCategoryChoice, FormI485ApplicationBySpecialProgramsBasedCategoryChoice, \
    FormI485TypeOfSpecialProgramsCategoryChoice, FormI485ApplicationByOtherCategoryChoice, \
    FormI485TypeOfOtherCategoryChoice, FormI485DerivativeApplicantChoice, \
    FormI485AppliedForImmigrationVisaInOtherCountriesChoice
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
                           state=FormI485.ApplicationByFamilyCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfFamilyCategoryApplicationChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите тип вашей семейной категории:\n"
                           "1. Ближайший родственник гражданина США, форма I-130\n"
                           "2. Иной родственник гражданина США или законного постоянного жителя, форма I-130.\n"
                           "3. Лицо, допущенное в Соединенные Штаты в качестве невесты (невесты) или ребенка невесты "
                           "гражданина США, форма I-129F (K-1 / K-2, неиммиграция)\n"
                           "4. Вдова или вдовец гражданина США, форма I-360\n"
                           "5. заявитель VAWA, форма I-360",
                           reply_markup=keyboard.markup)
    await FormI485.TypeOfFamilyCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_1",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[0]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_2",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[1]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_3",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[2]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_4",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[3]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_5",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[4]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByFamilyCategory_No",
                           state=FormI485.ApplicationByFamilyCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationByWorkingCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании трудовой занятости?",
                           reply_markup=keyboard.markup)
    await FormI485.ApplicationByEmploymentBasedCategory.set()


@dp.callback_query_handler(text="ApplicationByWorkingCategory_Yes",
                           state=FormI485.ApplicationByEmploymentBasedCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfEmploymentBasedCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите тип вашей трудовой занятости:",
                           reply_markup=keyboard.markup)
    await FormI485.TypeOfEmploymentBasedCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfEmploymentBasedCategory_1",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[5]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfEmploymentBasedCategory_2",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[6]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByWorkingCategory_No",
                           state=FormI485.ApplicationByEmploymentBasedCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationBySpecialImmigrantCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании специальной категории иммиграции (религиозный деятель, "
                           "специальный несовершеннолетний иммигрант, определенный гражданин Ирана или Ирака и др.)?",
                           reply_markup=keyboard.markup)
    await FormI485.ApplicationBySpecialImmigrantCategory.set()


@dp.callback_query_handler(text="ApplicationBySpecialImmigrantCategory_Yes",
                           state=FormI485.ApplicationBySpecialImmigrantCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfSpecialImmigrantCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите тип вашей специальной категории:\n"
                           "1.	Религиозный деятель, форма I-360\n"
                           "2. Специальный несовершеннолетний иммигрант, форма I-360\n"
                           "3. Определенный гражданин Афганистана или Ирака, форма I-360 или форма DS-157\n"
                           "4. Определенный международный вещатель, форма I-360\n"
                           "5. Определенная международная организация G-4 или член семьи, сотрудник или член семьи "
                           "НАТО-6, форма I-360\n",
                           reply_markup=keyboard.markup)
    await FormI485.TypeOfSpecialImmigrantCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_1",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[7]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_2",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[8]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_3",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[9]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_4",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[10]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_5",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[11]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationBySpecialImmigrantCategory_No",
                           state=FormI485.ApplicationBySpecialImmigrantCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationByAsyleeOrRefugeeCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление как соискатель убежища или беженец?",
                           reply_markup=keyboard.markup)
    await FormI485.ApplicationByAsyleeOrRefugeeCategory.set()


@dp.callback_query_handler(text="ApplicationByAsyleeOrRefugeeCategory_Yes",
                           state=FormI485.ApplicationByAsyleeOrRefugeeCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfAsyleeOrRefugeeCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите тип вашего статуса:\n"
                           "1.	Статус соискателя убежища (раздел 208 INA), форма I-589 или форма I-730\n"
                           "2.	Статус беженца (раздел 207 INA), форма I-590 или форма I-730",
                           reply_markup=keyboard.markup)
    await FormI485.TypeOfAsyleeOrRefugeeCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfAsyleeOrRefugeeCategory_1",
                           state=FormI485.TypeOfAsyleeOrRefugeeCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[12]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfAsyleeOrRefugeeCategory_2",
                           state=FormI485.TypeOfAsyleeOrRefugeeCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[13]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByAsyleeOrRefugeeCategory_No",
                           state=FormI485.ApplicationByAsyleeOrRefugeeCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationByHumanTraffickingVictimCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление как жертва торговли людьми или жертва преступления?",
                           reply_markup=keyboard.markup)
    await FormI485.ApplicationByHumanTraffickingVictimCategory.set()


@dp.callback_query_handler(text="ApplicationByHumanTraffickingVictimCategory_Yes",
                           state=FormI485.ApplicationByHumanTraffickingVictimCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfHumanTraffickingVictimCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите категорию жертв торговли людьми и жертв преступлений, к которой вы относитесь:\n"
                           "1.	Жертва торговли людьми (неиммигрант T), форма I-914 или производный член семьи, форма "
                           "I-914A\n"
                           "2.	Жертва преступления (U неиммигрант), форма I-918, производный член семьи, форма I-918A"
                           ", или соответствующий член семьи, форма I-929",
                           reply_markup=keyboard.markup)
    await FormI485.TypeOfHumanTraffickingVictimCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfHumanTraffickingVictimCategory_1",
                           state=FormI485.TypeOfHumanTraffickingVictimCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[14]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfHumanTraffickingVictimCategory_2",
                           state=FormI485.TypeOfHumanTraffickingVictimCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[15]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByHumanTraffickingVictimCategory_No",
                           state=FormI485.ApplicationByHumanTraffickingVictimCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationBySpecialProgramsBasedCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании специальных программ, основанных на определенных "
                           "публичных законах? (Специальные Кубинские законы, программа Лаутенберга и др.)",
                           reply_markup=keyboard.markup)
    await FormI485.ApplicationBySpecialProgramsCategory.set()


@dp.callback_query_handler(text="ApplicationBySpecialProgramsBasedCategory_Yes",
                           state=FormI485.ApplicationBySpecialProgramsCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfSpecialProgramsCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу категорию:\n"
                           "1.	Кубинский закон об урегулировании\n"
                           "2.	Кубинский закон об урегулировании проблем супругов и детей, подвергшихся побоям\n"
                           "3.	Статус иждивенца в соответствии с Законом о справедливости гаитянских беженцев-иммигра"
                           "нтов\n"
                           "4.	Статус иждивенца в соответствии с Законом о справедливости гаитянских беженцев-иммигра"
                           "нтов для супругов и детей, подвергшихся побоям\n"
                           "5.	Программа Лаутенберга\n"
                           "6.	Дипломаты или высокопоставленные чиновники, не имеющие возможности вернуться домой "
                           "(статья 13 Закона от 11 сентября 1957 г.)\n"
                           "7.	Индокитайский закон об условно-досрочном освобождении от 2000 г.\n",
                           reply_markup=keyboard.markup)
    await FormI485.TypeOfSpecialProgramsCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_1",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[16]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_2",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[17]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_3",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[18]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_4",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[19]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_5",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[20]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_6",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[21]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_7",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[22]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationBySpecialProgramsBasedCategory_No",
                           state=FormI485.ApplicationBySpecialProgramsCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfOtherCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании иных категорий.\n"
                           "Выберите тип иной категории:"
                           "1.	Диверсификационная визовая программа.\n"
                           "2.	Постоянное проживание в США до 1 января 1972 г. \n"
                           "3.	Лицо, родившееся в США с дипломатическим статусом.\n"
                           "4.	Иное\n",
                           reply_markup=keyboard.markup)
    await FormI485.TypeOfAdditionalOptionsCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_1",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[23]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_2",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[24]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_3",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[25]'] = 'x'
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_4",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Pt2Line1_CB[26]'] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали тип категории «Иное».\nВведите тип категории:")
    await FormI485.S_3_Pt2Line1g_OtherEligibility_0.set()


@dp.message_handler(state=FormI485.S_3_Pt2Line1g_OtherEligibility_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line1g_OtherEligibility[0]'] = message.text
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(message.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ImmigrationAndNationalityAct_Yes",
                           state=FormI485.ImmigrationAndNationalityActChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line2_CB[1]'] = 'x'
    keyboard = FormI485PrincipalApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о вашей иммиграционной категории.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь основным заявителем (не производным, то есть не супругом(-й) или не состоящим "
                           "в браке ребенком в возрасте до 21 года основного заявителя)? ",
                           reply_markup=keyboard.markup)
    await FormI485.PrincipalApplicatnChoice.set()


@dp.callback_query_handler(text="ImmigrationAndNationalityAct_No",
                           state=FormI485.ImmigrationAndNationalityActChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line2_CB[0]'] = 'x'
    keyboard = FormI485PrincipalApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о вашей иммиграционной категории.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь основным заявителем (не производным, то есть не супругом(-й) или не состоящим "
                           "в браке ребенком в возрасте до 21 года основного заявителя)? ",
                           reply_markup=keyboard.markup)
    await FormI485.PrincipalApplicatnChoice.set()


@dp.callback_query_handler(text="PrincipalApplicant_Yes",
                           state=FormI485.PrincipalApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер основного заявления (если имеется):",
                           reply_markup=keyboard.markup)
    await FormI485.S_3_Pt2Line3_Receipt_0.set()


@dp.callback_query_handler(text="PrincipalApplicant_No",
                           state=FormI485.PrincipalApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485DerivativeApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь производным заявителем (супругом(-й) или не состоящим в браке ребенком в "
                           "возрасте до 21 года основного заявителя)?",
                           reply_markup=keyboard.markup)
    await FormI485.DerivativeApplicatnChoice.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_3_Pt2Line3_Receipt_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату приоритета из основного заявления (если имеется) (мм/дд/гггг):",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line3_Receipt_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line3_Receipt[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите дату приоритета из основного заявления (если имеется) (мм/дд/гггг):",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_3_Pt2Line4_Date_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485DerivativeApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь производным заявителем (супругом(-й) или не состоящим в браке ребенком в "
                           "возрасте до 21 года основного заявителя)?",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line4_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line4_Date[0]'] = message.text
    keyboard = FormI485DerivativeApplicantChoice()
    await bot.send_message(message.from_user.id,
                           "Вы являетесь производным заявителем (супругом(-й) или не состоящим в браке ребенком в "
                           "возрасте до 21 года основного заявителя)?",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="DerivativeApplicant_Yes",
                           state=FormI485.DerivativeApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию основного заявителя:")
    await FormI485.next()


@dp.callback_query_handler(text="DerivativeApplicant_No",
                           state=FormI485.DerivativeApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485AppliedForImmigrationVisaInOtherCountriesChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 3. «Дополнительная информация о вас.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-нибудь обращались за иммиграционной визой для получения статуса постоянного "
                           "жительства в посольстве или консульстве США за границей?",
                           reply_markup=keyboard.markup)
    await FormI485.AppliedForImmigrantVisaChoice.set()


@dp.message_handler(state=FormI485.S_3_Pt2Line5a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line5a_FamilyName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя основного заявителя:")
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line5b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line5b_GivenName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество основного заявителя:")
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line5c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line5c_MiddleName[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите A-number основного заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_3_Pt1Line8_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения основного заявителя (мм/дд/гггг):")
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt1Line8_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt1Line8_AlienNumber[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения основного заявителя (мм/дд/гггг):")
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line7_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line7_Date[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите номер основного заявления основного заявителя:")
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line8_ReceiptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line8_ReceiptNumber[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите дату приоритета основного заявления основного заявителя (если имеется) "
                           "(мм/дд/гггг):",
                           reply_markup=keyboard.markup)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_3_Pt2Line9_Date_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485AppliedForImmigrationVisaInOtherCountriesChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 3. «Дополнительная информация о вас.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-нибудь обращались за иммиграционной визой для получения статуса постоянного "
                           "жительства в посольстве или консульстве США за границей?",
                           reply_markup=keyboard.markup)
    await FormI485.AppliedForImmigrantVisaChoice.set()


@dp.message_handler(state=FormI485.S_3_Pt2Line9_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Pt2Line9_Date[0]'] = message.text
    keyboard = FormI485AppliedForImmigrationVisaInOtherCountriesChoice()
    await bot.send_message(message.from_user.id,
                           "Часть 3. «Дополнительная информация о вас.»")
    await bot.send_message(message.from_user.id,
                           "Вы когда-нибудь обращались за иммиграционной визой для получения статуса постоянного "
                           "жительства в посольстве или консульстве США за границей?",
                           reply_markup=keyboard.markup)
    await FormI485.AppliedForImmigrantVisaChoice.set()
