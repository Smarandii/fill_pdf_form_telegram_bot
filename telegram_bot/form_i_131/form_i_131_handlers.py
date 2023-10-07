from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from telegram_bot.form_i_131.f_i_131_keyboards import FormI131ApplicationTypeChoice, \
    FormI131PeopleIncludedInApplicationAreInExclusion, FormI131HadBeenPermitedReentryChoice, \
    FormI131WhereToSendTravelDocumentChoice, FormI131NoticeAddressChoice
from telegram_bot.form_i_131.form_i_131_state_group import FormI131
from telegram_bot import bot, dp, FillPdfFromJsonAdapter, datetime, FormI589IfAnyChoice, FormI589GenderChoice


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


@dp.callback_query_handler(text="I-131")
async def ar_11_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-131"
    await bot.send_message(callback_query.from_user.id, "Вы выбрали форму I-131. Давайте приступим к ее заполнению.\n"
                                                        "Часть 1. «Информация о вас.»")
    await bot.send_message(callback_query.from_user.id, "Укажите Вашу фамилию:")
    await FormI131.Page1_1a_FamilyName_0.set()


@dp.message_handler(state=FormI131.Page1_1a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line1a_FamilyName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@dp.message_handler(state=FormI131.Page1_1b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line1b_GivenName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@dp.message_handler(state=FormI131.Page1_1c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line1c_MiddleName[0]'] = message.text
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
    await FormI131.next()


@dp.message_handler(state=FormI131.Page1_2a_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2a_InCareofName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@dp.message_handler(state=FormI131.Page1_2b_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2b_StreetNumberName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:")


@dp.callback_query_handler(text="Ste",
                           state=FormI131.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Line2c_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    await FormI131.Page1_2c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI131.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Line2c_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    await FormI131.Page1_2c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI131.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Line2c_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    await FormI131.Page1_2c_AptSteFlrNumber_0.set()


@dp.message_handler(state=FormI131.Page1_2c_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2c_AptSteFlrNumber[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@dp.message_handler(state=FormI131.Page1_2d_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2d_CityOrTown[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@dp.message_handler(state=FormI131.Page1_2e_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2e_State[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш zip код (например, 123456).\nНайти zip код можно по "
                                                 "ссылке:\nhttps://tools.usps.com/go/ZipLookupAction_input")


@dp.message_handler(state=FormI131.Page1_2f_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2f_ZipCode[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш почтовый индекс:")


@dp.message_handler(state=FormI131.Page1_2g_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2g_PostalCode[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите провинцию (субъект, штат):")


@dp.message_handler(state=FormI131.Page1_2h_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2h_Province[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@dp.message_handler(state=FormI131.Page1_2i_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2i_Country[0]'] = ""
    await FormI131.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id, "Раздел «Иная информация.»\n"
                                                 "Укажите Ваш регистрационный номер иностранца (A-number) "
                                                 "(если имеется):", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page1_3_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите страну, где вы родились:")
    await FormI131.next()


@dp.message_handler(state=FormI131.Page1_3_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].#area[1].Line3_AlienNumber[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну, где вы родились:")


@dp.message_handler(state=FormI131.Page1_4_CountryOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line4_CountryOfBirth[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну гражданства:")


# Mailing address
@dp.message_handler(state=FormI131.Page1_5_CountryOfCitizenship_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line5_CountryOfCitizenship[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш класс допуска (категорию визы, по которой вы были "
                                                 "допущены в США, например, постоянный житель, условный постоянный "
                                                 "житель и др.):")


@dp.message_handler(state=FormI131.Page1_6_ClassofAdmission_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line6_ClassofAdmission[0]'] = message.text
    await FormI131.next()
    keyboard = FormI589GenderChoice()
    await bot.send_message(message.from_user.id, "Выберите свой пол:", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="male",
                           state=FormI131.Page1_ChooseGenderChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line7_Male[0]'] = "x"
    await FormI131.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что вы мужчина.")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу дату рождения:")


@dp.callback_query_handler(text="female",
                           state=FormI131.Page1_ChooseGenderChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line7_Female[0]'] = "x"
    await FormI131.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что вы женщина.")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу дату рождения:")


@dp.message_handler(state=FormI131.Page1_8_DateOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line8_DateOfBirth[0]'] = message.text
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
                                                        "3) Я являюсь постоянным жителем в результате получения статуса"
                                                        "беженца или лица, получившего убежище, и подаю заявление на "
                                                        "получение проездного документа беженца.\n"
                                                        "4) Я подаю на разрешение на обратный въезд (Advance Parole "
                                                        "Document), чтобы мне позволили вернуться в Соединенные Штаты "
                                                        "после временной поездки за границу.\n"
                                                        "5) Я нахожусь за пределами США и подаю на Advance Parole "
                                                        "Document.\n"
                                                        "6) Я подаю на Advance Parole Document от имени лица, "
                                                        "находящегося за пределами США.", reply_markup=keyboard.markup)
    await FormI131.Page2_ApplicationTypeChoice.set()


@dp.message_handler(state=FormI131.Page1_9_SSN_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].#area[2].Line9_SSN[0]'] = message.text
    await FormI131.next()
    keyboard = FormI131ApplicationTypeChoice()
    await bot.send_message(message.from_user.id, "Часть 2. «Тип заявления.»")
    await bot.send_message(message.from_user.id, "Укажите верное:\n"
                                                 "1) Я являюсь постоянным или условным постоянным жителем США и "
                                                 "подаю заявление на получение разрешения на повторный въезд.\n"
                                                 "2) У меня есть статус беженца или лица, получившего убежище"
                                                 " в США, и я подаю заявление на получение проездного документа "
                                                 "беженца.\n"
                                                 "3) Я являюсь постоянным жителем в результате получения статуса"
                                                 "беженца или лица, получившего убежище, и подаю заявление на "
                                                 "получение проездного документа беженца.\n"
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
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_2",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1b_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_3",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1c_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_4",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1d_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_5",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1e_checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(callback_query.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")
    await FormI131.Page2_1_DateIntendedDeparture_0.set()


@dp.callback_query_handler(text="ApplicationType_6",
                           state=FormI131.Page2_ApplicationTypeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1f_checkbox[0]'] = "x"
    await FormI131.next()
    await bot.send_message(callback_query.from_user.id, "Вы указали, что подаете на Advance Parole Document от имени "
                                                        "лица, находящегося за пределами США. Далее укажите "
                                                        "информацию о таком лице.")
    await bot.send_message(callback_query.from_user.id, "Укажите фамилию:")


@dp.message_handler(state=FormI131.Page2_2a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2a_FamilyName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите имя:")


@dp.message_handler(state=FormI131.Page2_2b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2b_GivenName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите отчество:")


@dp.message_handler(state=FormI131.Page2_2c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2c_MiddleName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите дату рождения:")


@dp.message_handler(state=FormI131.Page2_2d_DateOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2d_DateOfBirth[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну, где вы родились:")


@dp.message_handler(state=FormI131.Page2_2f_CountryOfCitizenship_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2e_CountryOfBirth[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну гражданства:")


@dp.message_handler(state=FormI131.Page2_2f_CountryOfCitizenship_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2f_CountryOfCitizenship[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите код номера телефона:")


@dp.message_handler(state=FormI131.Page2_2g_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].#area[4].Line2g_DaytimePhoneNumber1[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите номер телефона:")


@dp.message_handler(state=FormI131.Page2_2g_DaytimePhoneNumber2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].#area[4].Line2g_DaytimePhoneNumber2[0]'] = message.text[:3:]
        data['[1].#area[4].Line2g_DaytimePhoneNumber3[0]'] = message.text[:4:]
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
    await FormI131.next()


@dp.message_handler(state=FormI131.Page2_2h_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2h_InCareofName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@dp.message_handler(state=FormI131.Page2_2i_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Line2b_StreetNumberName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:")


@dp.callback_query_handler(text="Ste",
                           state=FormI131.Page2_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line2j_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    await FormI131.Page2_2j_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI131.Page2_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line2j_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    await FormI131.Page2_2j_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI131.Page2_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line2j_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    await FormI131.Page2_2j_AptSteFlrNumber_0.set()


@dp.message_handler(state=FormI131.Page2_2j_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2j_AptSteFlrNumber[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@dp.message_handler(state=FormI131.Page2_2k_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2k_CityOrTown[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@dp.message_handler(state=FormI131.Page2_2l_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2l_State[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш zip код (например, 123456).\nНайти zip код можно по "
                                                 "ссылке:\nhttps://tools.usps.com/go/ZipLookupAction_input")


@dp.message_handler(state=FormI131.Page2_2m_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2m_ZipCode[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш почтовый индекс:")


@dp.message_handler(state=FormI131.Page2_2n_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2n_PostalCode[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите провинцию (субъект, штат):")


@dp.message_handler(state=FormI131.Page2_2o_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2o_Province[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@dp.message_handler(state=FormI131.Page2_2p_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2p_Country[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Часть 3. «Обработка информации.»")
    await bot.send_message(message.from_user.id, "Укажите дату предполагаемого отъезда за границу (мм/дд/гггг):")


@dp.message_handler(state=FormI131.Page2_1_DateIntendedDeparture_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line1_DateIntendedDeparture[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ожидаемую длительность поездки (количество дней):")


@dp.message_handler(state=FormI131.Page2_2_ExpectedLengthTrip_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line2_ExpectedLengthTrip[0]'] = message.text
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
    await FormI131.Page2_3b_NameDHSOffice_0.set()


@dp.callback_query_handler(text="PeopleIncludedInApplicationAreInExclusion_No",
                           state=FormI131.PeopleIncludedInApplicationAreInExclusionChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line3a_No[0]"] = "x"
    keyboard = FormI131WhereToSendTravelDocumentChoice()
    await bot.send_message(callback_query.from_user.id, "Куда вы хотите, чтобы проездной документ был отправлен? "
                                                        "(укажите 1 вариант)\n"
                                                        "1. По вашему адресу фактического проживания.\n"
                                                        "2. В посольство или консульство США.\n"
                                                        "3. В DHS office за рубежом.", reply_markup=keyboard.markup)
    await FormI131.Page3_WhereToSendTravelDocumentChoice.set()


@dp.message_handler(state=FormI131.Page2_3b_NameDHSOffice_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line3b_NameDHSOffice[0]'] = message.text
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
    await FormI131.Page2_4b_DateIssued_0.set()


@dp.callback_query_handler(text="HadBeenPermitedReentry_No",
                           state=FormI131.Page2_HadBeenPermitedReentryChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Line4a_No[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату выдачи такого документа (мм/дд/гггг).:")
    await FormI131.Page2_4b_DateIssued_0.set()


@dp.message_handler(state=FormI131.Page2_4b_DateIssued_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line4b_DateIssued[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите состояние документа (приложен, утерян, иное):")


@dp.message_handler(state=FormI131.Page2_4c_Disposition_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[1].Line4c_Disposition[0]'] = message.text
    await FormI131.next()
    keyboard = FormI131WhereToSendTravelDocumentChoice()
    await bot.send_message(message.from_user.id, "Куда вы хотите, чтобы проездной документ был отправлен? "
                                                 "(укажите 1 вариант)\n"
                                                 "1. По вашему адресу фактического проживания.\n"
                                                 "2. В посольство или консульство США.\n"
                                                 "3. В DHS office за рубежом.", reply_markup=keyboard.markup)


@dp.callback_query_handler(text="WhereToSendTravelDocument_1",
                           state=FormI131.Page2_HadBeenPermitedReentryChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line5_USAddress[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Часть 4. «Информация о предполагаемой поездке.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите цель поездки:")
    await FormI131.Page3_1a_Purpose_0.set()


@dp.callback_query_handler(text="WhereToSendTravelDocument_2",
                           state=FormI131.Page2_HadBeenPermitedReentryChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line6_USEmbassy[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес такого посольства или консульства.\n"
                           "Укажите город:")
    await FormI131.Page3_6a_CityOrTown_0.set()


@dp.message_handler(state=FormI131.Page3_6a_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line6a_CityOrTown[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@dp.message_handler(state=FormI131.Page3_6b_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line6b_Country[0]'] = message.text
    await FormI131.Page3_NoticeAddressChoice.set()
    keyboard = FormI131NoticeAddressChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите, куда следует отправить уведомление о получении проездного "
                           "документа:\n"
                           "1. По адресу лица, находящегося за пределами США, от имени которого вы подаете на Advance "
                           "Parole Document (часть 2).\n"
                           "2. По иному адресу.",
                           reply_markup=keyboard)


@dp.callback_query_handler(text="WhereToSendTravelDocument_3",
                           state=FormI131.Page2_HadBeenPermitedReentryChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line7_DHSOffice[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес такого DHS office.\n"
                           "Укажите город:")
    await FormI131.Page3_7a_CityOrTown_0.set()


@dp.message_handler(state=FormI131.Page3_7a_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line7a_CityOrTown[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@dp.message_handler(state=FormI131.Page3_7b_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line7b_Country[0]'] = message.text
    await FormI131.Page3_NoticeAddressChoice.set()
    keyboard = FormI131NoticeAddressChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите, куда следует отправить уведомление о получении проездного "
                           "документа:\n"
                           "1. По адресу лица, находящегося за пределами США, от имени которого вы подаете на Advance "
                           "Parole Document (часть 2).\n"
                           "2. По иному адресу.",
                           reply_markup=keyboard)


@dp.callback_query_handler(text="NoticeAddress_1",
                           state=FormI131.Page3_NoticeAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line8_AddressPart2[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Часть 4. «Информация о предполагаемой поездке.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите цель поездки:")
    await FormI131.Page3_1a_Purpose_0.set()


@dp.callback_query_handler(text="NoticeAddress_2",
                           state=FormI131.Page3_NoticeAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line9_AddressBelow[0]"] = "x"
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем укаазано в заявлении, "
                           "укажите ФИО такого лица:", reply_markup=keyboard.markup)
    await FormI131.Page3_10a_InCareofName_0.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI131.Page3_10a_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    await FormI131.next()


@dp.message_handler(state=FormI131.Page3_10b_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10a_InCareofName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@dp.message_handler(state=FormI131.Page2_2i_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10b_StreetNumberName[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:")


@dp.callback_query_handler(text="Ste",
                           state=FormI131.Page3_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line10c_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    await FormI131.Page3_10c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI131.Page3_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line10c_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    await FormI131.Page3_10c_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI131.Page3_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Line10c_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    await FormI131.Page3_10c_AptSteFlrNumber_0.set()


@dp.message_handler(state=FormI131.Page3_10c_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10c_AptSteFlrNumber[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@dp.message_handler(state=FormI131.Page3_10d_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10d_CityOrTown[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@dp.message_handler(state=FormI131.Page3_10e_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10e_State[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш zip код (например, 123456).\nНайти zip код можно по "
                                                 "ссылке:\nhttps://tools.usps.com/go/ZipLookupAction_input")


@dp.message_handler(state=FormI131.Page3_10f_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10f_ZipCode[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите ваш почтовый индекс:")


@dp.message_handler(state=FormI131.Page3_10g_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10g_PostalCode[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите провинцию (субъект, штат):")


@dp.message_handler(state=FormI131.Page3_10h_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10h_Province[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите страну:")


@dp.message_handler(state=FormI131.Page3_10i_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line10i_Country[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите код номера телефона:")


@dp.message_handler(state=FormI131.Page3_10j_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].#area[5].Line10j_DaytimePhoneNumber1[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Укажите номер телефона:")


@dp.message_handler(state=FormI131.Page3_10j_DaytimePhoneNumber2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].#area[5].Line10j_DaytimePhoneNumber2[0]'] = message.text[:3:]
        data['[2].#area[5].Line10j_DaytimePhoneNumber3[0]'] = message.text[:4:]
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Часть 4. «Информация о предполагаемой поездке.»")
    await bot.send_message(message.from_user.id, "Укажите цель поездки:")


@dp.message_handler(state=FormI131.Page3_1a_Purpose_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line1a_Purpose[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Перечислите страны, которые вы собираетесь посетить:")


@dp.message_handler(state=FormI131.Page3_1b_ListCountries_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[2].Line1b_ListCountries[0]'] = message.text
    await FormI131.next()
    await bot.send_message(message.from_user.id, "Перечислите страны, которые вы собираетесь посетить:")