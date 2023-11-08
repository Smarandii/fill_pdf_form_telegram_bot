import os
import time

from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from telegram_bot.common_form_elements.functions import final_stage
from telegram_bot.form_i_131.f_i_131_keyboards import FormI131ApplicationTypeChoice, \
    FormI131PeopleIncludedInApplicationAreInExclusion, FormI131HadBeenPermitedReentryChoice, \
    FormI131WhereToSendTravelDocumentChoice, FormI131NoticeAddressChoice, FormI131ApplyingForReentryPermitChoice, \
    FormI131HowMuchTimeSpentOutsideUSChoice, FormI131HaveEverFiledFederalIncomeTaxReturnChoice, \
    FormI131ApplyingForTravelDocumentOfRefugeeChoice, FormI131ApplyingForAdvancedParoleChoice, \
    FormI131IntendToComebackChoice, FormI131HaveEverCameBackChoice, FormI131HaveEverIssuedPassportChoice, \
    FormI131HaveEverGotHelpFromGovernmentChoice, FormI131RestoredCitizenshipOfLeftCountryChoice, \
    FormI131GotNewCitizenshipChoice, FormI131GotRefugeeStatusElsewhereChoice, FormI131HowManyTripsChoice, \
    FormI131AddressOfNotificationChoice, \
    FormI131EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOperationAlliesWelcomeChoice, \
    FormI131UnderFearOfPunishmentForDisinformationChoice, FormI131RecieverOutsideOfUSIntendToGetThisDocument
from telegram_bot.form_i_131.form_i_131_state_group import FormI131
from telegram_bot import bot, dp, FillPdfFromJsonAdapter, datetime, FormI589IfAnyChoice, FormI589GenderChoice
from telegram_bot.form_i_589.form_i_589_handlers import escape_json_special_chars
from telegram_bot.form_i_765.f_i_765_keyboards import FormI765TypeOfBuildingChoice


@escape_json_special_chars
@dp.message_handler(filters.Command("end"), state='*')
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await final_stage(data, message, state, bot)


@dp.callback_query_handler(text="I-131", state='*')
async def ar_11_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-131"
    await bot.send_message(callback_query.from_user.id, "Вы выбрали форму I-131. Давайте приступим к ее заполнению.\n"
                                                        "Часть 1. «Информация о вас.»")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу фамилию:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page1_1a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_1a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line1a_FamilyName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_1b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line1b_GivenName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_1c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line1c_MiddleName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id, "Раздел «Адрес фактического проживания.» Далее укажите информацию о "
                                                 "вашем адресе фактического проживания.\n"
                                                 "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО "
                                                 "такого лица:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page1_2a_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2a_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2a_InCareofName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2b_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2b_StreetNumberName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI131.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Line2c_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page1_2c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI131.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Line2c_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page1_2c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI131.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Line2c_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page1_2c_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2c_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2c_AptSteFlrNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2d_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2d_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2e_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2e_State[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш zip код (например, 123456).\nНайти zip код можно по "
                                                 "ссылке:\nhttps://tools.usps.com/go/ZipLookupAction_input")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2f_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2f_ZipCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш почтовый индекс:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2g_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2g_PostalCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите провинцию (субъект, штат):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2h_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2h_Province[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_2i_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2i_Country[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id, "Раздел «Иная информация.»\n"
                                                 "Укажите ваш регистрационный номер иностранца (A-number) "
                                                 "(если имеется):", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page1_3_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите страну, где вы родились:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_3_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].#area[1].Line3_AlienNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну, где вы родились:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_4_CountryOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line4_CountryOfBirth[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну гражданства:")


# Mailing address
@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_5_CountryOfCitizenship_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line5_CountryOfCitizenship[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш класс допуска (категорию визы, по которой вы были "
                                                 "допущены в США, например, постоянный житель, условный постоянный "
                                                 "житель и др.):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_6_ClassofAdmission_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line6_ClassofAdmission[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI589GenderChoice()
    await bot.send_message(message.from_user.id, "Выберите свой пол:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=FormI131.Page1_ChooseGenderChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line7_Male[0]'] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что вы мужчина.")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу дату рождения:")


@dp.callback_query_handler(text="female",
                           state=FormI131.Page1_ChooseGenderChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line7_Female[0]'] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что вы женщина.")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу дату рождения:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_8_DateOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line8_DateOfBirth[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите номер социального страхования США (SSN) (если имеется):")


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page1_9_SSN_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI131ApplicationTypeChoice()
    await bot.send_message(callback_query.from_user.id, "Часть 2. «Тип заявления.»")
    await bot.send_message(callback_query.from_user.id, "Укажите верное:\n"
                                                        "1) Я являюсь постоянным или условным постоянным жителем США и "
                                                        "подаю заявление на получение разрешения на повторный въезд.\n"
                                                        "2) У меня есть статус беженца или лица, получившего убежище"
                                                        " в США, и я подаю заявление на получение проездного документа "
                                                        "беженца.\n"
                                                        "3) Я являюсь постоянным жителем в результате получения "
                                                        "статуса  беженца или получения "
                                                        "убежища, и подаю заявление на получение проездного документа беженца.\n"
                                                        "4) Я подаю на разрешение на обратный въезд (Advance Parole "
                                                        "Document), чтобы мне позволили вернуться в Соединенные Штаты "
                                                        "после временной поездки за границу.\n"
                                                        "5) Я нахожусь за пределами США и подаю на Advance Parole "
                                                        "Document.\n"
                                                        "6) Я подаю на Advance Parole Document от имени лица, "
                                                        "находящегося за пределами США.", reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_ApplicationTypeChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page1_9_SSN_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].#area[2].Line9_SSN[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131ApplicationTypeChoice()
    await bot.send_message(message.from_user.id, "Часть 2. «Тип заявления.»")
    await bot.send_message(message.from_user.id, "Укажите верное:\n"
                                                 "1) Я являюсь постоянным или условным постоянным жителем США и "
                                                 "подаю заявление на получение разрешения на повторный въезд.\n"
                                                 "2) У меня есть статус беженца или лица, получившего убежище"
                                                 " в США, и я подаю заявление на получение проездного документа "
                                                 "беженца.\n"
                                                 "3) Я являюсь постоянным жителем в результате получения статуса  беженца или получения убежища, и подаю заявление на получение проездного документа беженца.\n"
                                                 "4) Я подаю на разрешение на обратный въезд (Advance Parole "
                                                 "Document), чтобы мне позволили вернуться в Соединенные Штаты "
                                                 "после временной поездки за границу.\n"
                                                 "5) Я нахожусь за пределами США и подаю на Advance Parole "
                                                 "Document.\n"
                                                 "6) Я подаю на Advance Parole Document от имени лица, "
                                                 "находящегося за пределами США.", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ApplicationType_1",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1a_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_2",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1b_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_3",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1c_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_4",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1d_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_5",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1e_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_6",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1f_checkbox[0]'] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что подаете на Advance Parole Document от имени "
                                                        "лица, находящегося за пределами США. Далее укажите "
                                                        "информацию о таком лице.")
    await bot.send_message(callback_query.from_user.id, "Укажите фамилию:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2a_FamilyName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2b_GivenName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2c_MiddleName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2d_DateOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2d_DateOfBirth[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну рождения:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2e_CountryOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2e_CountryOfBirth[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну гражданства:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2f_CountryOfCitizenship_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2f_CountryOfCitizenship[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите код номера телефона:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2g_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].#area[4].Line2g_DaytimePhoneNumber1[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите номер телефона:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2g_DaytimePhoneNumber2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].#area[4].Line2g_DaytimePhoneNumber2[0]'] = message.text[:3:]
        data['[1].#area[4].Line2g_DaytimePhoneNumber3[0]'] = message.text[:4:]
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id, "Далее укажите адрес фактического проживания такого лица.")
    await bot.send_message(message.from_user.id, "Если получать корреспонденцию будет иное лицо, чем указано в "
                                                 "заявлении, укажите ФИО такого лица:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page2_2h_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2h_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2h_InCareofName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2i_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2b_StreetNumberName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI131.Page2_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line2j_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_2j_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI131.Page2_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line2j_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_2j_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI131.Page2_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line2j_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_2j_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2j_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2j_AptSteFlrNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2k_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2k_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2l_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2l_State[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите zip код (например, 123456).\nНайти zip код можно по "
                                                 "ссылке:\nhttps://tools.usps.com/go/ZipLookupAction_input")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2m_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2m_ZipCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите почтовый индекс:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2n_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2n_PostalCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите провинцию (субъект, штат):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2o_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2o_Province[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2p_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2p_Country[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(message.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_1_DateIntendedDeparture_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1_DateIntendedDeparture[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ожидаемую длительность поездки (количество дней):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_2_ExpectedLengthTrip_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2_ExpectedLengthTrip[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131PeopleIncludedInApplicationAreInExclusion()
    await bot.send_message(message.from_user.id, "Находится ли ваше дело или дело иного человека, включенного в "
                                                 "заявку, в иммиграционном суде в связи с депортацией, высылкой, "
                                                 "иное?", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="PeopleIncludedInApplicationAreInExclusion_Yes",
                           state=FormI131.PeopleIncludedInApplicationAreInExclusionChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line3a_Yes[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите наименование DHS office:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_3b_NameDHSOffice_0.set()


@dp.callback_query_handler(text="PeopleIncludedInApplicationAreInExclusion_No",
                           state=FormI131.PeopleIncludedInApplicationAreInExclusionChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line3a_No[0]"] = "x"
    keyboard = FormI131HadBeenPermitedReentryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вам ранее выдавали разрешение на повторный въезд (re-entry permit) "
                           "или проездной документ беженца (refugee travel document)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_HadBeenPermitedReentryChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_3b_NameDHSOffice_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line3b_NameDHSOffice[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131HadBeenPermitedReentryChoice()
    await bot.send_message(message.from_user.id,
                           "Вам ранее выдавали разрешение на повторный въезд (re-entry permit) "
                           "или проездной документ беженца (refugee travel document)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HadBeenPermitedReentry_Yes",
                           state=FormI131.Page2_HadBeenPermitedReentryChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line4a_Yes[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату выдачи такого документа (мм/дд/гггг).:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page2_4b_DateIssued_0.set()


@dp.callback_query_handler(text="HadBeenPermitedReentry_No",
                           state=FormI131.Page2_HadBeenPermitedReentryChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line4a_No[0]"] = "x"
    keyboard = FormI131WhereToSendTravelDocumentChoice()
    await bot.send_message(callback_query.from_user.id, "Куда вы хотите, чтобы проездной документ был отправлен? "
                                                        "(укажите 1 вариант)\n"
                                                        "1. По вашему адресу фактического проживания.\n"
                                                        "2. В посольство или консульство США.\n"
                                                        "3. В DHS office за рубежом.", reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_WhereToSendTravelDocumentChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_4b_DateIssued_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line4b_DateIssued[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите состояние документа (приложен, утерян, иное):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page2_4c_Disposition_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line4c_Disposition[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131WhereToSendTravelDocumentChoice()
    await bot.send_message(message.from_user.id, "Куда вы хотите, чтобы проездной документ был отправлен? "
                                                 "(укажите 1 вариант)\n"
                                                 "1. По вашему адресу фактического проживания.\n"
                                                 "2. В посольство или консульство США.\n"
                                                 "3. В DHS office за рубежом.", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="WhereToSendTravelDocument_1",
                           state=FormI131.Page3_WhereToSendTravelDocumentChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line5_USAddress[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Часть 4. «Информация о предполагаемой поездке.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите цель поездки:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_1a_Purpose_0.set()


@dp.callback_query_handler(text="WhereToSendTravelDocument_2",
                           state=FormI131.Page3_WhereToSendTravelDocumentChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line6_USEmbassy[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес такого посольства или консульства.\n"
                           "Укажите город:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_6a_CityOrTown_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_6a_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line6a_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_6b_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line6b_Country[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_NoticeAddressChoice.set()
    keyboard = FormI131NoticeAddressChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите, куда следует отправить уведомление о получении проездного "
                           "документа:\n"
                           "1. По адресу лица, находящегося за пределами США, от имени которого вы подаете на Advance "
                           "Parole Document (часть 2).\n"
                           "2. По иному адресу.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="WhereToSendTravelDocument_3",
                           state=FormI131.Page3_WhereToSendTravelDocumentChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line7_DHSOffice[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес такого DHS office.\n"
                           "Укажите город:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_7a_CityOrTown_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_7a_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line7a_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_7b_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line7b_Country[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_NoticeAddressChoice.set()
    keyboard = FormI131NoticeAddressChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите, куда следует отправить уведомление о получении проездного "
                           "документа:\n"
                           "1. По адресу лица, находящегося за пределами США, от имени которого вы подаете на Advance "
                           "Parole Document (часть 2).\n"
                           "2. По иному адресу.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="NoticeAddress_1",
                           state=FormI131.Page3_NoticeAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line8_AddressPart2[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Часть 4. «Информация о предполагаемой поездке.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите цель поездки:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_1a_Purpose_0.set()


@dp.callback_query_handler(text="NoticeAddress_2",
                           state=FormI131.Page3_NoticeAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line9_AddressBelow[0]"] = "x"
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем указано в заявлении, "
                           "укажите ФИО такого лица:", reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_10a_InCareofName_0.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page3_10a_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10a_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10a_InCareofName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10b_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10b_StreetNumberName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI131.Page3_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line10c_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_10c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI131.Page3_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line10c_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_10c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI131.Page3_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line10c_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_10c_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10c_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10c_AptSteFlrNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10d_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10d_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10e_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10e_State[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите zip код (например, 123456).\nНайти zip код можно по "
                                                 "ссылке:\nhttps://tools.usps.com/go/ZipLookupAction_input")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10f_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10f_ZipCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите почтовый индекс:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10g_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10g_PostalCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите провинцию (субъект, штат):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10h_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10h_Province[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10i_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10i_Country[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите код номера телефона:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10j_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].#area[5].Line10j_DaytimePhoneNumber1[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите номер телефона:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_10j_DaytimePhoneNumber2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].#area[5].Line10j_DaytimePhoneNumber2[0]'] = message.text[:3:]
        data['[2].#area[5].Line10j_DaytimePhoneNumber3[0]'] = message.text[:4:]
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Часть 4. «Информация о предполагаемой поездке.»")
    await bot.send_message(message.from_user.id, "Укажите цель поездки:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_1a_Purpose_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line1a_Purpose[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Перечислите страны, которые вы собираетесь посетить:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_1b_ListCountries_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line1b_ListCountries[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131ApplyingForReentryPermitChoice()
    await bot.send_message(message.from_user.id, "Вы подаете на разрешение на повторный въезд (re-entry permit)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ApplyingForReentryPermit_Yes",
                           state=FormI131.Page3_ApplyingForReentryPermitChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI131HowMuchTimeSpentOutsideUSChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 5. «Информация, заполняемая лицом, подающим на повторный въезд.»")
    await bot.send_message(callback_query.from_user.id,
                           "С момента получения статуса постоянного жителя США или за последние 5 лет "
                           "(в зависимости от того, что меньше) какое количество времени вы провели за пределами "
                           "США?", reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="ApplyingForReentryPermit_No",
                           state=FormI131.Page3_ApplyingForReentryPermitChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI131HaveEverFiledFederalIncomeTaxReturnChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о "
                           "федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о "
                           "федеральном подоходном налоге, потому что считали себя нерезидентом?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="HowMuchTimeSpentOutsideUS_1",
                           state=FormI131.Page3_HowMuchTotalTimeSpentOutsideUSChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line1a_Lessthan6[0]"] = "x"
    keyboard = FormI131HaveEverFiledFederalIncomeTaxReturnChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о "
                           "федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о "
                           "федеральном подоходном налоге, потому что считали себя нерезидентом?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="HowMuchTimeSpentOutsideUS_2",
                           state=FormI131.Page3_HowMuchTotalTimeSpentOutsideUSChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line1b_6months[0]"] = "x"
    keyboard = FormI131HaveEverFiledFederalIncomeTaxReturnChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о "
                           "федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о "
                           "федеральном подоходном налоге, потому что считали себя нерезидентом?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="HowMuchTimeSpentOutsideUS_3",
                           state=FormI131.Page3_HowMuchTotalTimeSpentOutsideUSChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line1c_1to2[0]"] = "x"
    keyboard = FormI131HaveEverFiledFederalIncomeTaxReturnChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о "
                           "федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о "
                           "федеральном подоходном налоге, потому что считали себя нерезидентом?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="HowMuchTimeSpentOutsideUS_4",
                           state=FormI131.Page3_HowMuchTotalTimeSpentOutsideUSChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line1d_2to3[0]"] = "x"
    keyboard = FormI131HaveEverFiledFederalIncomeTaxReturnChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о "
                           "федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о "
                           "федеральном подоходном налоге, потому что считали себя нерезидентом?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="HowMuchTimeSpentOutsideUS_5",
                           state=FormI131.Page3_HowMuchTotalTimeSpentOutsideUSChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line1e_3to4[0]"] = "x"
    keyboard = FormI131HaveEverFiledFederalIncomeTaxReturnChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о "
                           "федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о "
                           "федеральном подоходном налоге, потому что считали себя нерезидентом?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="HowMuchTimeSpentOutsideUS_6",
                           state=FormI131.Page3_HowMuchTotalTimeSpentOutsideUSChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line1f_morethan[0]"] = "x"
    keyboard = FormI131HaveEverFiledFederalIncomeTaxReturnChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о "
                           "федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о "
                           "федеральном подоходном налоге, потому что считали себя нерезидентом?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="HaveEverFiledFederalIncomeTaxReturn_Yes",
                           state=FormI131.Page3_HaveEverFiledFederalIncomeTaxReturnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line2_Yes[0]"] = "x"

    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page3_HaveEverFiledFederalIncomeTaxReturnReason)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['HaveEverFiledFederalIncomeTaxReturnReason'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131ApplyingForTravelDocumentOfRefugeeChoice()
    await bot.send_message(message.from_user.id, "Вы подаете на проездной документ беженца (refugee travel document)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HaveEverFiledFederalIncomeTaxReturn_No",
                           state=FormI131.Page3_HaveEverFiledFederalIncomeTaxReturnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line2_No[0]"] = "x"
    keyboard = FormI131ApplyingForTravelDocumentOfRefugeeChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете на проездной документ беженца (refugee travel document)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page3_ApplyingForTravelDocumentOfRefugeeChoice.set()


@dp.callback_query_handler(text="ApplyingForTravelDocumentOfRefugee_Yes",
                           state=FormI131.Page3_ApplyingForTravelDocumentOfRefugeeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Часть 6. «Информация, заполняемая лицом, подающим на проездной документ беженца "
                           "(refugee travel document).»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите страну, от которой вы запрашивали убежище:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="ApplyingForTravelDocumentOfRefugee_No",
                           state=FormI131.Page3_ApplyingForTravelDocumentOfRefugeeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI131ApplyingForAdvancedParoleChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете на обратный въезд (advance parole)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_ApplyingForAdvancedParoleChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_1_CountryRefugee_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line1_CountryRefugee[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131IntendToComebackChoice()
    await bot.send_message(message.from_user.id, "Если вы ответите «Да» на любой из следующих вопросов, "
                                                 "вы должны разъяснить ситуацию в деталях.")
    await bot.send_message(message.from_user.id, "Вы собираетесь вернуться в страну, названную выше?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="IntendToComeback_Yes",
                           state=FormI131.Page4_IntendToComebackChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line2_Yes1[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_IntendToComebackExplanation)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['IntendToComeBackExplanation'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131HaveEverCameBackChoice()
    await bot.send_message(message.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                 "получившего убежище, вы возвращались в эту страну?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="IntendToComeback_No",
                           state=FormI131.Page4_IntendToComebackChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line2_No1[0]"] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_HaveEverCameBackChoice.set()
    keyboard = FormI131HaveEverCameBackChoice()
    await bot.send_message(callback_query.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                        "получившего убежище, вы возвращались в эту страну?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HaveEverCameBack_Yes",
                           state=FormI131.Page4_HaveEverCameBackChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line3a_Yes1[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_ReasonOfComebackExplanation)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ReasonOfComeBackExplanation'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131HaveEverIssuedPassportChoice()
    await bot.send_message(message.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                 "получившего убежище, вы подавали заявку на получение или получали "
                                                 "национальный паспорт, подавали заявку на обновление или обновляли "
                                                 "имеющийся паспорт, подавали заявку или получали разрешение на въезд в эту страну?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HaveEverCameBack_No",
                           state=FormI131.Page4_HaveEverCameBackChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line3a_No1[0]"] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_HaveEverIssuedPassport.set()
    keyboard = FormI131HaveEverIssuedPassportChoice()
    await bot.send_message(callback_query.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                        "получившего убежище, вы подавали заявку на получение или получали "
                                                        "национальный паспорт, подавали заявку на обновление или обновляли "
                                                        "имеющийся паспорт, подавали заявку или получали разрешение на въезд в эту страну?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HaveEverIssuedPassport_Yes",
                           state=FormI131.Page4_HaveEverIssuedPassport)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line3b_Yes[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_ReasonOfIssuedPassport)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ReasonOfIssuedPassport'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131HaveEverGotHelpFromGovernmentChoice()
    await bot.send_message(message.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                 "получившего убежище, вы подавали заявку на получение или получали "
                                                 "какие-либо выплаты или пособия в этой стране? (например, "
                                                 "выплаты по медицинской страховке)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HaveEverIssuedPassport_No",
                           state=FormI131.Page4_HaveEverIssuedPassport)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line3b_No[0]"] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_HaveEverGotHelpFromGovernmentChoice.set()
    keyboard = FormI131HaveEverGotHelpFromGovernmentChoice()
    await bot.send_message(callback_query.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                        "получившего убежище, вы подавали заявку на получение или получали "
                                                        "какие-либо выплаты или пособия в этой стране? (например, "
                                                        "выплаты по медицинской страховке)",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HaveEverGotHelpFromGovernment_Yes",
                           state=FormI131.Page4_HaveEverGotHelpFromGovernmentChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line3c_Yes[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_TellAboutHelpFromGovernment)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['TellAboutHelpFromGovernment'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131RestoredCitizenshipOfLeftCountryChoice()
    await bot.send_message(message.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                 "получившего убежище, вы восстанавливали гражданство вышеназванной "
                                                 "страны?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="HaveEverGotHelpFromGovernment_No",
                           state=FormI131.Page4_HaveEverGotHelpFromGovernmentChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line3c_No[0]"] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_RestoredCitizenshipOfLeftCountry.set()
    keyboard = FormI131RestoredCitizenshipOfLeftCountryChoice()
    await bot.send_message(callback_query.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                        "получившего убежище, вы восстанавливали гражданство вышеназванной "
                                                        "страны?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="RestoredCitizenshipOfLeftCountry_Yes",
                           state=FormI131.Page4_RestoredCitizenshipOfLeftCountry)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4a_Yes[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_RestoredCitizenshipOfLeftCountryReason)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['RestoredCitizenshipOfLeftCountryReason'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131GotNewCitizenshipChoice()
    await bot.send_message(message.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                 "получившего убежище, вы приобрели новое гражданство?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="RestoredCitizenshipOfLeftCountry_No",
                           state=FormI131.Page4_RestoredCitizenshipOfLeftCountry)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4a_No[0]"] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_GotNewCitizenshipChoice.set()
    keyboard = FormI131GotNewCitizenshipChoice()
    await bot.send_message(callback_query.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                        "получившего убежище, вы приобрели новое гражданство?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="GotNewCitizenship_Yes",
                           state=FormI131.Page4_GotNewCitizenshipChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4b_Yes[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_GotNewCitizenshipReason)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['GotNewCitizenshipReason'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131GotRefugeeStatusElsewhereChoice()
    await bot.send_message(message.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                 "получившего убежище, вам был предоставлен статус беженца или лица, "
                                                 "получившего убежище, в любой другой стране?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="GotNewCitizenship_No",
                           state=FormI131.Page4_GotNewCitizenshipChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4b_No[0]"] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_GotRefugeeStatusElsewhereChoice.set()
    keyboard = FormI131GotRefugeeStatusElsewhereChoice()
    await bot.send_message(callback_query.from_user.id, "После того как вам был предоставлен статус беженца/лица, "
                                                        "получившего убежище, вам был предоставлен статус беженца или "
                                                        "лица, получившего убежище, в любой другой стране?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="GotRefugeeStatusElsewhere_Yes",
                           state=FormI131.Page4_GotRefugeeStatusElsewhereChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4c_Yes[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Разъясните ситуацию в деталях:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_GotRefugeeStatusElsewhereReason)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['GotRefugeeStatusElsewhereReason'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131ApplyingForAdvancedParoleChoice()
    await bot.send_message(message.from_user.id, "Вы подаете на обратный въезд (advance parole)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="GotRefugeeStatusElsewhere_No",
                           state=FormI131.Page4_GotRefugeeStatusElsewhereChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4c_No[0]"] = "x"
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_ApplyingForAdvancedParoleChoice.set()
    keyboard = FormI131ApplyingForAdvancedParoleChoice()
    await bot.send_message(callback_query.from_user.id, "Вы подаете на обратный въезд (advance parole)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ApplyingForAdvancedParole_Yes",
                           state=FormI131.Page4_ApplyingForAdvancedParoleChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131HowManyTripsChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 7. «Информация, заполняемая лицом, подающим на обратный въезд (advance parole).»")
    await bot.send_message(callback_query.from_user.id,
                           "Для какого количества поездок вы собираетесь использовать данный документ?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="ApplyingForAdvancedParole_No",
                           state=FormI131.Page4_ApplyingForAdvancedParoleChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI131EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOperationAlliesWelcomeChoice()
    await bot.send_message(callback_query.from_user.id, "Часть 8. «Разрешение на работу по программе OAW для граждан "
                                                        "Афганистана.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы запрашиваете разрешение на работу при получении одобрения на въезд по программе OAW ("
                           "для граждан Афганистана)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOAWChoice.set()


@dp.callback_query_handler(text="HowManyTrips_1",
                           state=FormI131.Page4_HowManyTripsChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line1_OneTrip[0]"] = "x"
    keyboard = FormI131RecieverOutsideOfUSIntendToGetThisDocument()
    await bot.send_message(callback_query.from_user.id,
                           "Лицо, намеревающееся получить данный документ, находится за пределами США?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="RecieverOutsideOfUSIntendToGetThisDocument_Yes",
                           state=FormI131.Page4_RecieverOutsideOfUSIntendToGetThisDocumentChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес посольства, консульства или DHS Office США.\nУкажите город:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="RecieverOutsideOfUSIntendToGetThisDocument_No",
                           state=FormI131.Page4_RecieverOutsideOfUSIntendToGetThisDocumentChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line1_OneTrip[0]"] = "x"
    keyboard = FormI131AddressOfNotificationChoice()
    await bot.send_message(callback_query.from_user.id, "Если проездной документ будет направляться в офис за рубежом, "
                                                        "укажите адрес, куда должно прийти уведомление о готовности "
                                                        "документа?\n\n"
                                                        "1. По адресу лица, находящегося за пределами США, от имени "
                                                        "которого"
                                                        "вы подаете на Advance Parole Document (часть 2).\n"
                                                        "2. По иному адресу.", reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_AddressOfNotificationChoice.set()


@dp.callback_query_handler(text="HowManyTrips_2",
                           state=FormI131.Page4_HowManyTripsChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line1_MoreThanOne[0]"] = "x"
    keyboard = FormI131RecieverOutsideOfUSIntendToGetThisDocument()
    await bot.send_message(callback_query.from_user.id,
                           "Лицо, намеревающееся получить данный документ, находится за пределами США?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_2a_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line2a_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_2b_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line2b_Country[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI131AddressOfNotificationChoice()
    await bot.send_message(message.from_user.id, "Если проездной документ будет направляться в офис за рубежом, "
                                                 "укажите адрес, куда должно прийти уведомление о готовности "
                                                 "документа?\n\n"
                                                 "1. По адресу лица, находящегося за пределами США, от имени которого "
                                                 "вы подаете на Advance Parole Document (часть 2).\n"
                                                 "2. По иному адресу.", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="AddressOfNotification_1",
                           state=FormI131.Page4_AddressOfNotificationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line3_AddressPart2[0]"] = "x"
    keyboard = FormI131EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOperationAlliesWelcomeChoice()
    await bot.send_message(callback_query.from_user.id, "Часть 8. «Разрешение на работу по программе OAW для граждан "
                                                        "Афганистана.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы запрашиваете разрешение на работу при получении одобрения на въезд по программе OAW ("
                           "для граждан Афганистана)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOAWChoice.set()


@dp.callback_query_handler(text="AddressOfNotification_2",
                           state=FormI131.Page4_AddressOfNotificationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4_AddressBelow[0]"] = "x"
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем указано в заявлении, "
                           "укажите ФИО такого лица:", reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page4_4a_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4a_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4a_InCareofName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4b_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4b_StreetNumberName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI131.Page4_TypeOfBuilding)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4c_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="Apt",
                           state=FormI131.Page4_TypeOfBuilding)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4c_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="Flr",
                           state=FormI131.Page4_TypeOfBuilding)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line4c_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4c_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4c_AptSteFlrNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4d_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4d_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4e_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4e_State[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите zip код (например, 123456).\nНайти zip код можно по "
                                                 "ссылке:\nhttps://tools.usps.com/go/ZipLookupAction_input")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4f_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4f_ZipCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите почтовый индекс:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4g_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4g_PostalCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите провинцию (субъект, штат):")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4h_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4h_Province[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4i_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].Line4i_Country[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите код номера телефона:")


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4j_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].#area[6].Line4j_DaytimePhoneNumber1[0]'] = message.text
    await bot.send_message(message.from_user.id, "Укажите номер телефона:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page4_4j_DaytimePhoneNumber2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[3].#area[6].Line4j_DaytimePhoneNumber2[0]'] = message.text[:3:]
        data['[3].#area[6].Line4j_DaytimePhoneNumber3[0]'] = message.text[:4:]
    keyboard = FormI131EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOperationAlliesWelcomeChoice()
    await bot.send_message(message.from_user.id, "Часть 8. «Разрешение на работу по программе OAW для граждан "
                                                 "Афганистана.»")
    await bot.send_message(message.from_user.id,
                           "Вы запрашиваете разрешение на работу при получении одобрения на въезд по программе OAW ("
                           "для граждан Афганистана)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.Page4_EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOAWChoice.set()


@dp.callback_query_handler(text="OperationAlliesWelcome_Yes",
                           state=FormI131.Page4_EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOAWChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line1_OAW[1]"] = "x"
    keyboard = FormI131UnderFearOfPunishmentForDisinformationChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 9. «Подпись заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Под страхом наказания за дачу ложных показаний в соответствии с законодательством "
                           "Соединенных Штатов Америки я подтверждаю, что данное заявление и представленные вместе с "
                           "ним доказательства являются достоверными. Я разрешаю раскрыть любую информацию, "
                           "необходимую USCIS для определения права на получение услуги, которую я запрашиваю.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="OperationAlliesWelcome_No",
                           state=FormI131.Page4_EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOAWChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Line1_OAW[0]"] = "x"
    keyboard = FormI131UnderFearOfPunishmentForDisinformationChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 9. «Подпись заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Под страхом наказания за дачу ложных показаний в соответствии с законодательством "
                           "Соединенных Штатов Америки я подтверждаю, что данное заявление и представленные вместе с "
                           "ним доказательства являются достоверными. Я разрешаю раскрыть любую информацию, "
                           "необходимую USCIS для определения права на получение услуги, которую я запрашиваю.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="UnderFearOfPunishmentForDisinformation_Yes",
                           state=FormI131.Page5_UnderFearOfPunishmentForDisinformationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу подпись:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="UnderFearOfPunishmentForDisinformation_No",
                           state=FormI131.Page5_UnderFearOfPunishmentForDisinformationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу подпись:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page5_1a_SignatureofApplicant_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].Line1a_SignatureofApplicant[0]'] = message.text
        data['[4].Line1b_DateOfSignature[0]'] = datetime.datetime.now().strftime("%m/%d/%Y")
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите код номера мобильного телефона заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page5__2_DaytimePhoneNumber1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await final_stage(data, callback_query, state, bot)


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page5__2_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].#area[7].Line2_DaytimePhoneNumber1[0]'] = message.text
    await bot.send_message(message.from_user.id, "Укажите номер мобильного телефона заявителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI131.next()


@escape_json_special_chars
@dp.message_handler(state=FormI131.Page5__2_DaytimePhoneNumber2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[4].#area[7].Line2_DaytimePhoneNumber2[0]'] = message.text[:3:]
        data['[4].#area[7].Line2_DaytimePhoneNumber3[0]'] = message.text[:4:]
        await final_stage(data, message, state, bot)
