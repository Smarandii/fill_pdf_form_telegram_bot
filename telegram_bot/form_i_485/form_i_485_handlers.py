import os
import time

from aiogram import types
from aiogram.dispatcher import FSMContext, filters
from aiogram.types.message import ContentType

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
    FormI485TypeOfSpecialProgramsCategoryChoice, \
    FormI485TypeOfOtherCategoryChoice, FormI485DerivativeApplicantChoice, \
    FormI485AppliedForImmigrationVisaInOtherCountriesChoice, FormI485ImmigrantVisaDecisionStatusChoice, \
    FormI485AddressWasProvidedAbove, FormI485RecentEmploymentListedAbove, FormI485ParentHasDifferentName, \
    FormI485ParentNotAlive, FormI485MaritalStatusChoice, FormI485IsYourSpouceInArmyChoice, \
    Form485SpouceApllyingTooChoice, FormI485BeenMarriedBeforeChoice, FormI485HaveKidsChoice, FormI485EthnicityChoice, \
    FormI485ChildApplyingTooChoice, FormI485RaceChoice, FormI485IChooseAllOfMyRaces, FormI485EyeColorChoice, \
    FormI485IHairColorChoice, FormI485IGeneralEligibilityChoice, FormI485WasEverRefusedToEnterUSAChoice, \
    FormI485SimpleYesOrNoChoice, FormI485AnnualHouseHoldIncome, FormI485HouseHoldNetWorth, FormI485HouseHoldDebt, \
    FormI485IndicateEducationLevel
from telegram_bot.form_i_765.f_i_765_keyboards import FormI765TypeOfBuildingChoice, FormI765ApplicantStatementChoice, \
    FormI765OnlyTrueInformationChoice
from telegram_bot.form_i_589.form_i_589_handlers import escape_json_special_chars
from telegram_bot.form_i_485.form_i_485_state_group import FormI485
from telegram_bot import bot, dp, FillPdfFromJsonAdapter, datetime, FormI589IfAnyChoice, FormI589GenderChoice
from telegram_bot.form_i_765.f_i_765_keyboards import FormI765UsedOtherNamesChoice, FormI765WantSSACardToBeIssuedChoice


@escape_json_special_chars
@dp.message_handler(filters.Command("end"), state="*")
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        adapter.save_json()
        await bot.send_message(message.chat.id,
                               f"Ваши данные для формы {data['form_identifier']} успешно сохранены! Дождитесь pdf-файла.")
        await bot.send_chat_action(message.chat.id, "typing")
        file_path = adapter.fill_pdf()
        with open(file_path, 'rb') as file:
            await bot.send_document(int(os.getenv("DOCUMENTS_RECEIVER")), file)

        with open(file_path, 'rb') as file:
            await bot.send_document(int(os.getenv("DEVELOPER_TELEGRAM_ID")), file)
    await state.finish()


@dp.callback_query_handler(text="I-485")
async def i_485_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-485"
    await bot.send_message(callback_query.from_user.id, "Вы выбрали форму I-485. Давайте приступим к ее заполнению.")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 1. «Информация о вас.»\n"
                           "Раздел «Ваше ФИО.»\n"
                           "Укажите вашу фамилию:")
    time.sleep(0.5)
    await FormI485.S_0_Pt1Line1a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line1a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line1a_FamilyName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line1b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line1b_GivenName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line1c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line1c_MiddleName[0]"] = message.text
    time.sleep(0.5)
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
                                                        "об иных используемых вами именах. ")
    await bot.send_message(callback_query.from_user.id, "Укажите фамилию:")
    time.sleep(0.5)
    await FormI485.S_0_Pt1Line2a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line2a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line2a_FamilyName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line2b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line2b_GivenName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line2c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line2c_MiddleName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.UsedOtherNamesChoice_2.set()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали еще какие-либо иные имена, помимо указанного выше?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI485.UsedOtherNamesChoice_1)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.S_0_Pt1Line3a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line3a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line3a_FamilyName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line3b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line3b_GivenName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line3c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line3c_MiddleName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.UsedOtherNamesChoice_3.set()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали еще какие-либо иные имена, помимо указанного выше?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI485.UsedOtherNamesChoice_2)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.S_0_Pt1Line4a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line4a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line4a_FamilyName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line4b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line4b_GivenName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id, "Укажите ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line4c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line4c_MiddleName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Раздел «Иная информация о вас.»")
    await bot.send_message(message.from_user.id,
                           "Укажите вашу дату рождения (мм/дд/гггг):")


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI485.UsedOtherNamesChoice_3)
async def callback_query_handler_UsedOtherNames_No(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    time.sleep(0.5)
    await FormI485.S_0_Pt1Line5_DateofBirth_0.set()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Иная информация о вас.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу дату рождения (мм/дд/гггг):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line5_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line5_DateofBirth[0]"] = message.text
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="male",
                           state=FormI485.GenderChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line6_Gender[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите город, где вы родились:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_0_Pt1Line6_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[0].Pt1Line6_CityOrTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну, где вы родились:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line8_CountryofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line8_CountryofBirth[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну вашего гражданства:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line9_CountryofCitizenship_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line9_CountryofCitizenship[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите Ваш регистрационный номер иностранца (A-number) (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line10_AlienNumber_2)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line10_AlienNumber[2]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер онлайн-аккаунта USCIS (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line11_USCISELISAcctNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line11_USCISELISAcctNumber[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Почтовый адрес.» Далее укажите информацию о вашем почтовом адресе.")
    await bot.send_message(message.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_1_Pt1Line12_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что иное лицо не будет получать корреспонденцию за вас.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_InCareofName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_StreetNumberName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line12_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line12_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line12_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line12_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line12_ZipCode[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI485DontNeedAlternateMailingAddressChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Альтернативный и/или безопасный почтовый адрес.»")
    await bot.send_message(message.from_user.id,
                           "Если вы подаете заявление на основании Закона о насилии в отношении женщин (VAWA) или в "
                           "качестве особого несовершеннолетнего иммигранта, жертвы торговли людьми "
                           "(T для неиммигрантов) или жертвы квалифицируемого преступления (U для неиммигрантов), и вы "
                           "не хотите, чтобы USCIS отправляла уведомления об этом заявлении к вам домой, вы можете "
                           "предоставить альтернативный и/или безопасный почтовый адрес далее.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_need_alternate_mailing_address",
                           state=FormI485.AlternateMailingAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SSAChoice()
    await bot.send_message(callback_query.from_user.id, "Раздел «Карта социального обеспечения "
                                                        "(Social Security Card).»")
    await bot.send_message(callback_query.from_user.id,
                           "Выдавало ли вам когда-либо Управление социального обеспечения (SSA) карту социального "
                           "обеспечения (social security card)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.SSA_Choice.set()


@dp.callback_query_handler(text="need_alternate_mailing_address",
                           state=FormI485.AlternateMailingAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_1_Pt1Line13_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что иное лицо не будет получать корреспонденцию за вас.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_InCareofName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_StreetNumberName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line13_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line13_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line13_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line13_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line13_ZipCode[0]"] = message.text
    keyboard = FormI485SSAChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Карта социального обеспечения (Social Security Card).»")
    await bot.send_message(message.from_user.id,
                           "Выдавало ли вам когда-либо Управление социального обеспечения (SSA) карту социального "
                           "обеспечения (social security card)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.SSA_Choice.set()


@dp.callback_query_handler(text="SSAChoice_Yes",
                           state=FormI485.SSA_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line14_YN[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США (SSN):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line15_SSN_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line15_SSN[0]"] = message.text
    keyboard = FormI765WantSSACardToBeIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы хотите, чтобы SSA выдало вам карту социального обеспечения?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.IssueSSCChoice.set()


@dp.callback_query_handler(text="SSAChoice_No",
                           state=FormI485.SSA_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line14_YN[0]"] = "x"
    keyboard = FormI765WantSSACardToBeIssuedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы хотите, чтобы SSA выдало вам карту социального обеспечения?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.IssueSSCChoice.set()


@dp.callback_query_handler(text="WantSSACardToBeIssued_Yes",
                           state=FormI485.IssueSSCChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line16_YN[1]"] = "x"
    keyboard = FormI485SSACouldUseInformationChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы разрешаете раскрытие информации из этого заявления Управлению социального обеспечения "
                           "(SSA)? Это необходимо для присвоения вам номера социального страхования (SSN) и выдачи "
                           "карты социального страхования.",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SSACouldUseInformation_Yes",
                           state=FormI485.SSACouldUseInformationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line17_YN[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Недавняя иммиграционная история». Заполните данный раздел, если вы в последний раз "
                           "въезжали в Соединенные Штаты по паспорту или проездному документу.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта, использованного при вашем последнем въезде в США:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line18_PassportNum_0.set()


@dp.callback_query_handler(text="SSACouldUseInformation_No",
                           state=FormI485.SSACouldUseInformationChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line17_YN[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Недавняя иммиграционная история». Заполните данный раздел, если вы в последний раз "
                           "въезжали в Соединенные Штаты по паспорту или проездному документу.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта, использованного при вашем последнем въезде в США:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line18_PassportNum_0.set()


@dp.callback_query_handler(text="WantSSACardToBeIssued_No",
                           state=FormI485.IssueSSCChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line16_YN[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Недавняя иммиграционная история». Заполните данный раздел, если вы в последний раз "
                           "въезжали в Соединенные Штаты по паспорту или проездному документу.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер паспорта, использованного при вашем последнем въезде в США:")
    time.sleep(0.5)
    await FormI485.S_1_Pt1Line18_PassportNum_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line18_PassportNum_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line18_PassportNum[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите номер проездного документа (travel document), использованного при вашем "
                           "последнем въезде в США:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt2Line19_TravelDoc_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt2Line19_TravelDoc[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите дату истечения срока действия паспорта или проездного документа (мм/дд/гггг):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line20_ExpDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line20_ExpDate[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Какая страна выдала вам последний паспорт или проездной документ (travel document)?")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line21_Passport_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line21_Passport[0]"] = message.text
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line22_VisaNum_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line22_VisaNum[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите место вашего последнего въезда в США.\n"
                           "Укажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line23a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line23a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line23b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line23b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату вашего последнего въезда в США (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_1_Pt1Line24_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[1].Pt1Line24_Date[0]"] = message.text
    keyboard = FormI485WasInspectedAtPortOfEntryChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите верное.\n"
                           "Когда я в последний раз въехал в США:\n"
                           "1. Я был(-а) проверен(-a) в порту въезда и допущен(-a) в общем порядке (например, "
                           "посетителя по обмену; посетителя; временного работника; студента и тд).",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="WasInspectedAtPortOfEntry_Yes",
                           state=FormI485.S_2_Pt1Line25a_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line25a_CB[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы ответили «Да» на вопрос выше. Укажите, в каком статусе вы въехали в страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line25a_AdmissionEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line25a_AdmissionEntry[0]"] = message.text
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.I94WasIssuedChoice.set()


@dp.callback_query_handler(text="WasInspectedAtPortOfEntry_No",
                           state=FormI485.S_2_Pt1Line25a_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SpecialCategoryEntryGrantedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "2. Я был(-а) досмотрен(-a) в порту въезда, и мне был разрешен въезд по особой категории "
                           "(например, по гуманитарному разрешению на въезд (humanitarian parole) или как гражданину "
                           "Кубы (Cuban parole)).",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.S_2_Pt1Line25b_CB_0.set()


@dp.callback_query_handler(text="SpecialCategoryEntryGranted_Yes",
                           state=FormI485.S_2_Pt1Line25b_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line25b_CB[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы ответили «Да» на вопрос выше. Укажите, на основании какого статуса вам разрешили въезд:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line25b_ParoleEntrance_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line25b_ParoleEntrance[0]"] = message.text
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.I94WasIssuedChoice.set()


@dp.callback_query_handler(text="SpecialCategoryEntryGranted_No",
                           state=FormI485.S_2_Pt1Line25b_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485CameIntoUSWithoutAdmissionOrParoleChoice()
    await bot.send_message(callback_query.from_user.id,
                           "3. Я въехал(-а) в Соединенные Штаты без допуска или разрешения на въезд.",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.S_2_Pt1Line25c_CB_0.set()


@dp.callback_query_handler(text="CameIntoUSWithoutAdmissionOrParole_Yes",
                           state=FormI485.S_2_Pt1Line25c_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line25c_CB[0]"] = "x"
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.I94WasIssuedChoice.set()


@dp.callback_query_handler(text="CameIntoUSWithoutAdmissionOrParole_No",
                           state=FormI485.S_2_Pt1Line25c_CB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line25d_CB[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "4. Иное.\n"
                           "Если вы не выбрали ни один из вариантов, укажите, каким образом вы въехали в США:")
    time.sleep(0.5)
    await FormI485.S_2_Pt2Line25d_other_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt2Line25d_other_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line25d_other[0]"] = message.text
    keyboard = FormI485I94WasIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы получали форму I-94?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.I94WasIssuedChoice.set()


@dp.callback_query_handler(text="I94WasIssued_Yes",
                           state=FormI485.I94WasIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Форма I-94.» Далее укажите сведения, указанные в форме I-94.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер записи о прибытии и выезде (указан в форме I-94):")
    time.sleep(0.5)
    await FormI485.S_2_P2Line26a_I94_0.set()


@dp.callback_query_handler(text="I94WasIssued_No",
                           state=FormI485.I94WasIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationByFamilyCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 2. «Тип заявления или категория подачи.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление по семейной категории?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ApplicationByFamilyCategory.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_P2Line26a_I94_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].P2Line26a_I94[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату истечения срока разрешенного пребывания, указанную в форме I-94 (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line26b_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line26b_Date[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите статус в форме I-94 (например, класс допуска или вид разрешения на "
                           "въезд (parole):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line26c_Status_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line26c_Status[0]"] = message.text
    keyboard = FormI485ImmigrationStatusDontChangedChoice()
    await bot.send_message(message.from_user.id,
                           "Каков ваш текущий иммиграционный статус (если он изменился с момента вашего прибытия)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ImmigrationStatusDontChanged_No",
                           state=FormI485.S_2_Pt1Line27_Status_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш иммиграционный статус не изменился.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свое ФИО так, как оно указано в вашей форме I-94.\n"
                           "Укажите фамилию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line27_Status_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line27_Status[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите свое ФИО так, как оно указано в вашей форме I-94.\n"
                           "Укажите фамилию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line28a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line28a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line28b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line28b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_2_Pt1Line28c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt1Line28c_MiddleName[0]"] = message.text
    keyboard = FormI485ApplicationByFamilyCategoryChoice()
    await bot.send_message(message.from_user.id,
                           "Часть 2. «Тип заявления или категория подачи.»")
    await bot.send_message(message.from_user.id,
                           "Вы подаете заявление по семейной категории?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
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
                           "5. Заявитель VAWA, форма I-360",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.TypeOfFamilyCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_1",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[0]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_2",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[1]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_3",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[2]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_4",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[3]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfFamilyCategoryApplication_5",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[4]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByFamilyCategory_No",
                           state=FormI485.ApplicationByFamilyCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationByWorkingCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании трудовой занятости?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ApplicationByEmploymentBasedCategory.set()


@dp.callback_query_handler(text="ApplicationByWorkingCategory_Yes",
                           state=FormI485.ApplicationByEmploymentBasedCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfEmploymentBasedCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите тип вашей трудовой занятости:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.TypeOfEmploymentBasedCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfEmploymentBasedCategory_1",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[5]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfEmploymentBasedCategory_2",
                           state=FormI485.TypeOfFamilyCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[6]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByWorkingCategory_No",
                           state=FormI485.ApplicationByEmploymentBasedCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationBySpecialImmigrantCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании специальной категории иммиграции (религиозный деятель, "
                           "специальный несовершеннолетний иммигрант, определенный гражданин Ирана или Ирака и др.)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.TypeOfSpecialImmigrantCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_1",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[7]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_2",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[8]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_3",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[9]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_4",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[10]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialImmigrantCategory_5",
                           state=FormI485.TypeOfSpecialImmigrantCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[11]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationBySpecialImmigrantCategory_No",
                           state=FormI485.ApplicationBySpecialImmigrantCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationByAsyleeOrRefugeeCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление как соискатель убежища или беженец?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.TypeOfAsyleeOrRefugeeCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfAsyleeOrRefugeeCategory_1",
                           state=FormI485.TypeOfAsyleeOrRefugeeCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[12]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfAsyleeOrRefugeeCategory_2",
                           state=FormI485.TypeOfAsyleeOrRefugeeCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[13]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByAsyleeOrRefugeeCategory_No",
                           state=FormI485.ApplicationByAsyleeOrRefugeeCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationByHumanTraffickingVictimCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление как жертва торговли людьми или жертва преступления?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.TypeOfHumanTraffickingVictimCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfHumanTraffickingVictimCategory_1",
                           state=FormI485.TypeOfHumanTraffickingVictimCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[14]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfHumanTraffickingVictimCategory_2",
                           state=FormI485.TypeOfHumanTraffickingVictimCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[15]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationByHumanTraffickingVictimCategory_No",
                           state=FormI485.ApplicationByHumanTraffickingVictimCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485ApplicationBySpecialProgramsBasedCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании специальных программ, основанных на определенных "
                           "публичных законах? (Специальные Кубинские законы, программа Лаутенберга и др.)",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ApplicationBySpecialProgramsCategory.set()


@dp.callback_query_handler(text="ApplicationBySpecialProgramsBasedCategory_Yes",
                           state=FormI485.ApplicationBySpecialProgramsCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfSpecialProgramsCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу категорию:\n"
                           "1.	Кубинский закон об урегулировании\n"
                           "2.	Кубинский закон об урегулировании проблем супругов и детей, подвергшихся физическому насилию\n"
                           "3.	Статус иждивенца в соответствии с Законом о справедливости гаитянских беженцев-иммигра"
                           "нтов\n"
                           "4.	Статус иждивенца в соответствии с Законом о справедливости гаитянских беженцев-иммигра"
                           "нтов для супругов и детей, подвергшихся физическому насилию\n"
                           "5.	Программа Лаутенберга\n"
                           "6.	Дипломаты или высокопоставленные чиновники, не имеющие возможности вернуться домой "
                           "(статья 13 Закона от 11 сентября 1957 г.)\n"
                           "7.	Индокитайский закон об условно-досрочном освобождении от 2000 г.\n",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.TypeOfSpecialProgramsCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_1",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[16]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_2",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[17]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_3",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[18]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_4",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[19]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_5",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[20]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_6",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[21]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfSpecialProgramsCategory_7",
                           state=FormI485.TypeOfSpecialProgramsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[22]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ApplicationBySpecialProgramsBasedCategory_No",
                           state=FormI485.ApplicationBySpecialProgramsCategory)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485TypeOfOtherCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление на основании иных категорий.\n"
                           "Выберите тип иной категории:\n"
                           "1.	Диверсификационная визовая программа.\n"
                           "2.	Постоянное проживание в США до 1 января 1972 г. \n"
                           "3.	Лицо, родившееся в США с дипломатическим статусом.\n"
                           "4.	Иное\n",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.TypeOfAdditionalOptionsCategoryApplication.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_1",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[23]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_2",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[24]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_3",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[25]"] = "x"
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="TypeOfOtherCategory_4",
                           state=FormI485.TypeOfAdditionalOptionsCategoryApplication)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[2].Pt2Line1_CB[26]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали тип категории «Иное».\nВведите тип категории:")
    time.sleep(0.5)
    await FormI485.S_3_Pt2Line1g_OtherEligibility_0.set()


@dp.message_handler(state=FormI485.S_3_Pt2Line1g_OtherEligibility_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line1g_OtherEligibility[0]"] = message.text
    keyboard = FormI485ImmigrationAndNationalityActChoice()
    await bot.send_message(message.from_user.id,
                           "Вы подаете заявку на корректировку статуса на основании раздела 245(i) Закона об "
                           "иммиграции и гражданстве (INA)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ImmigrationAndNationalityActChoice.set()


@dp.callback_query_handler(text="ImmigrationAndNationalityAct_Yes",
                           state=FormI485.ImmigrationAndNationalityActChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line2_CB[1]"] = "x"
    keyboard = FormI485PrincipalApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о вашей иммиграционной категории.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь основным заявителем (не производным, то есть не супругом(-й) или не состоящим "
                           "в браке ребенком в возрасте до 21 года основного заявителя)? ",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.PrincipalApplicatnChoice.set()


@dp.callback_query_handler(text="ImmigrationAndNationalityAct_No",
                           state=FormI485.ImmigrationAndNationalityActChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line2_CB[0]"] = "x"
    keyboard = FormI485PrincipalApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о вашей иммиграционной категории.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь основным заявителем (не производным, то есть не супругом(-й) или не состоящим "
                           "в браке ребенком в возрасте до 21 года основного заявителя)? ",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.PrincipalApplicatnChoice.set()


@dp.callback_query_handler(text="PrincipalApplicant_Yes",
                           state=FormI485.PrincipalApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер основного заявления (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.S_3_Pt2Line3_Receipt_0.set()


@dp.callback_query_handler(text="PrincipalApplicant_No",
                           state=FormI485.PrincipalApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485DerivativeApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь производным заявителем (супругом(-й) или не состоящим в браке ребенком в "
                           "возрасте до 21 года основного заявителя)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.DerivativeApplicatnChoice.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_3_Pt2Line3_Receipt_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату приоритета из основного заявления (если имеется) (мм/дд/гггг):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line3_Receipt_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line3_Receipt[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите дату приоритета из основного заявления (если имеется) (мм/дд/гггг):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_3_Pt2Line4_Date_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485DerivativeApplicantChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь производным заявителем (супругом(-й) или не состоящим в браке ребенком в "
                           "возрасте до 21 года основного заявителя)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line4_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line4_Date[0]"] = message.text
    keyboard = FormI485DerivativeApplicantChoice()
    await bot.send_message(message.from_user.id,
                           "Вы являетесь производным заявителем (супругом(-й) или не состоящим в браке ребенком в "
                           "возрасте до 21 года основного заявителя)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="DerivativeApplicant_Yes",
                           state=FormI485.DerivativeApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию основного заявителя:")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="DerivativeApplicant_No",
                           state=FormI485.DerivativeApplicatnChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485AppliedForImmigrationVisaInOtherCountriesChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 3. «Дополнительная информация о вас.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-нибудь обращались за иммиграционной визой для получения статуса постоянного "
                           "жителя в посольство или консульство США за границей?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.AppliedForImmigrantVisaChoice.set()


@dp.message_handler(state=FormI485.S_3_Pt2Line5a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line5a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя основного заявителя:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line5b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line5b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество основного заявителя:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line5c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line5c_MiddleName[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите A-number основного заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_3_Pt1Line8_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения основного заявителя (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt1Line8_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt1Line8_AlienNumber[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения основного заявителя (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line7_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line7_Date[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите номер основного заявления основного заявителя:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt2Line8_ReceiptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line8_ReceiptNumber[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите дату приоритета основного заявления основного заявителя (если имеется) "
                           "(мм/дд/гггг):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
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
    time.sleep(0.5)
    await FormI485.AppliedForImmigrantVisaChoice.set()


@dp.message_handler(state=FormI485.S_3_Pt2Line9_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt2Line9_Date[0]"] = message.text
    keyboard = FormI485AppliedForImmigrationVisaInOtherCountriesChoice()
    await bot.send_message(message.from_user.id,
                           "Часть 3. «Дополнительная информация о вас.»")
    await bot.send_message(message.from_user.id,
                           "Вы когда-нибудь обращались за иммиграционной визой для получения статуса постоянного "
                           "жительства в посольстве или консульстве США за границей?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.AppliedForImmigrantVisaChoice.set()


@dp.callback_query_handler(text="AppliedForImmigrationVisaInOtherCountries_No",
                           state=FormI485.AppliedForImmigrantVisaChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «История адресов проживания.»\n"
                           "Далее укажите физические адреса мест, где вы жили в течение последних пяти лет, будь то в "
                           "Соединенных Штатах или за их пределами. Сначала укажите свой текущий адрес.")
    await bot.send_message(callback_query.from_user.id, "Укажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line5_StreetNumberName_0.set()


@dp.callback_query_handler(text="AppliedForImmigrationVisaInOtherCountries_Yes",
                           state=FormI485.AppliedForImmigrantVisaChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Местоположение посольства или консульства США.» Далее заполните информацию о "
                           "местоположении консульства или посольства США, куда вы подавали заявление о получении "
                           "иммиграционной визы.")
    await bot.send_message(callback_query.from_user.id, "Укажите город:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt3Line2a_City_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt3Line2a_City[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt3Line2b_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt3Line2b_Country[0]"] = message.text
    keyboard = FormI485ImmigrantVisaDecisionStatusChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите решение консульства или посольства "
                           "(например, заявление утверждено, отклонено, отозвано):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ImmigrantVisaDecisionStatus_1",
                           state=FormI485.S_3_Pt3Line3_Decision_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt3Line3_Decision[0]"] = "Утверждено"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату вынесения решения (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ImmigrantVisaDecisionStatus_2",
                           state=FormI485.S_3_Pt3Line3_Decision_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt3Line3_Decision[0]"] = "Отклонено"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату вынесения решения (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ImmigrantVisaDecisionStatus_3",
                           state=FormI485.S_3_Pt3Line3_Decision_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt3Line3_Decision[0]"] = "Отозвано"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату вынесения решения мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_3_Pt3Line4_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[3].Pt3Line4_Date[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «История адресов проживания.»\n"
                           "Далее укажите физические адреса мест, где вы жили в течение последних пяти лет, будь то в "
                           "Соединенных Штатах или за их пределами. Сначала укажите свой текущий адрес.")
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line5_StreetNumberName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_StreetNumberName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line5_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line5_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line5_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_ZipCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_Province[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (postal code):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_PostalCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line5_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line5_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы проживали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line6a_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line6a_Date[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы проживали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line6b_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line6b_Date[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите ваш второй адрес.\nУкажите название и номер улицы:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line7_StreetNumberName_0.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_4_Pt3Line7_StreetNumberName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485AddressWasProvidedAbove()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите свой последний адрес за пределами США, где вы проживали более одного года "
                           "(если он еще не указан выше).\nУкажите название и номер улицы:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.AddressWasProvidedAboveChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_StreetNumberName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line7_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line7_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line7_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_ZipCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_Province[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (postal code):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_PostalCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line7_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line7_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы проживали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line8a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line8a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы проживали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line8b_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line8b_DateTo[0]"] = message.text
    keyboard = FormI485AddressWasProvidedAbove()
    await bot.send_message(message.from_user.id,
                           "Укажите свой последний адрес за пределами США, где вы проживали более одного года "
                           "(если он еще не указан выше).\nУкажите название и номер улицы:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="AddressWasProvidedAbove",
                           state=FormI485.AddressWasProvidedAboveChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Трудовой стаж.»\nПредоставьте следующую информацию о вашей занятости за последние "
                           "5 лет. Сначала укажите свою текущую работу.\n"
                           "Укажите наименование работодателя:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line11_EmployerName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.AddressWasProvidedAboveChoice)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_StreetNumberName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line9_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line9_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line9_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line9_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line9_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line9_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line9_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_ZipCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line9_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_Province[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (postal code):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line9_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_PostalCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line9_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line9_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы проживали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line10a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line10a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы проживали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line10a_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line10a_DateTo[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Трудовой стаж.»")
    await bot.send_message(message.from_user.id,
                           "Предоставьте следующую информацию о вашей занятости за последние 5 лет. "
                           "Сначала укажите свою текущую работу.\nУкажите наименование работодателя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line11_EmployerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line11_EmployerName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите адрес работодателя.\nУкажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_StreetNumberName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line12_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line12_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_4_Pt3Line12_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_ZipCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_Province[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (postal code):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_PostalCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line12_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line12_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите должность:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_4_Pt3Line13_EmployerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[4].Pt3Line13_EmployerName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы начали работать в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line14a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line14a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы работали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line14b_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line14b_DateTo[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите наименование второго работодателя:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_5_Pt3Line4a_EmployerName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Часть 4. «Информация о ваших родителях.»\n"
                           "Раздел «Информация о вашем родителе 1.» Далее заполните информацию о вашем родителе 1.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ФИО в соответствии с действующим паспортом.\nУкажите фамилию:")
    time.sleep(0.5)
    await FormI485.S_5_Pt4Line1a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line4a_EmployerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line4a_EmployerName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите адрес работодателя.\nУкажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_StreetNumberName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_7)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_5_Pt3Line16_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_7)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_5_Pt3Line16_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_7)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_5_Pt3Line16_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_ZipCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_Province[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (postal code):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_PostalCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line16_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line16_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите должность:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line17_EmployerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line17_EmployerName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы начали работать в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line18a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line18a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы работали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line18a_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line18a_DateTo[0]"] = message.text
    keyboard = FormI485RecentEmploymentListedAbove()
    await bot.send_message(message.from_user.id,
                           "Укажите свое последнее место работы за пределами США "
                           "(если оно еще не указано выше).\nУкажите наименование работодателя:"
                           , reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="AddressWasProvidedAbove",
                           state=FormI485.S_5_Pt3Line19_EmployerName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Часть 4. «Информация о ваших родителях.»\n"
                           "Раздел «Информация о вашем родителе 1.» Далее заполните информацию о вашем родителе 1.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ФИО в соответствии с действующим паспортом.\nУкажите фамилию:")
    time.sleep(0.5)
    await FormI485.S_5_Pt4Line1a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line19_EmployerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line19_EmployerName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите адрес работодателя.\nУкажите название и номер улицы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_StreetNumberName[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=FormI485.TypeOfBuildingChoice_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_Unit[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(0.5)
    await FormI485.S_5_Pt3Line16_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI485.TypeOfBuildingChoice_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_Unit[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(0.5)
    await FormI485.S_5_Pt3Line16_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI485.TypeOfBuildingChoice_8)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_Unit[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(0.5)
    await FormI485.S_5_Pt3Line20_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_AptSteFlrNumber[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_CityOrTown[0]"] = message.text
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_ZipCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_Province[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (postal code):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_PostalCode[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите должность:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line20_EmployerName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line20_EmployerName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы начали работать в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line22a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line22a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы работали в этом месте (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt3Line22a_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt3Line22a_DateTo[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Часть 4. «Информация о ваших родителях.»\n"
                           "Раздел «Информация о вашем родителе 1.» Далее заполните информацию о вашем родителе 1.")
    await bot.send_message(message.from_user.id,
                           "Укажите ФИО в соответствии с действующим паспортом.\nУкажите фамилию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line1a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line1a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line1b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line1b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line1c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line1c_MiddleName[0]"] = message.text
    keyboard = FormI485ParentHasDifferentName()
    await bot.send_message(message.from_user.id,
                           "Имя, данное родителю 1 при рождении, отличается от имени, "
                           "указанном в действующем паспорте?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ParentHasDifferentName_Yes",
                           state=FormI485.ParentHasDifferentNameChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию:")
    time.sleep(0.5)
    await FormI485.S_5_Pt4Line2a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line2a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line2a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line2b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line2b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line2c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line2c_MiddleName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ParentHasDifferentName_No",
                           state=FormI485.ParentHasDifferentNameChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения:")
    time.sleep(0.5)
    await FormI485.S_5_Pt4Line3_DateofBirth_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line3_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line3_DateofBirth[0]"] = message.text
    keyboard = FormI589GenderChoice()
    await bot.send_message(message.from_user.id,
                           "Выберите пол родителя:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="female",
                           state=FormI485.Parent1_Gender_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line4_Gender[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш 1 родитель - женщина.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите город рождения:")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="male",
                           state=FormI485.Parent1_Gender_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line4_Gender[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш 1 родитель - мужчина.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите город рождения:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line5_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line5_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну рождения:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_5_Pt4Line6_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[5].Pt4Line6_Country[0]"] = message.text
    keyboard = FormI485ParentNotAlive()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий город или город проживания (если родитель 1 жив):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ParentNotAlive_Yes",
                           state=FormI485.S_6_Pt4Line7_CityTown_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о вашем родителе 2.» Далее заполните информацию о вашем родителе 2.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ФИО в соответствии с действующим паспортом.\nУкажите фамилию:")
    time.sleep(0.5)
    await FormI485.S_6_Pt4Line9a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line7_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line7_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите текущую страну проживания:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line8_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line8_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Информация о вашем родителе 2.» Далее заполните информацию о вашем родителе 2.")
    await bot.send_message(message.from_user.id,
                           "Укажите ФИО в соответствии с действующим паспортом.\nУкажите фамилию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line9a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line9a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line9b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line9b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line9c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line9c_MiddleName[0]"] = message.text
    keyboard = FormI485ParentHasDifferentName()
    await bot.send_message(message.from_user.id,
                           "Имя, данное родителю 2 при рождении отличается от имени, "
                           "указанном в действующем паспорте?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ParentHasDifferentName_Yes",
                           state=FormI485.ParentHasDifferentNameChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию:")
    time.sleep(0.5)
    await FormI485.S_6_Pt4Line10a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line10a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line10a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line10b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line10b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line10c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line10c_MiddleName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения:")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ParentHasDifferentName_No",
                           state=FormI485.ParentHasDifferentNameChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения:")
    time.sleep(0.5)
    await FormI485.S_6_Pt4Line11_DateofBirth_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line11_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line11_DateofBirth[0]"] = message.text
    keyboard = FormI589GenderChoice()
    await bot.send_message(message.from_user.id,
                           "Выберите пол родителя:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="female",
                           state=FormI485.Parent2_Gender_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line12_Gender[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш 2 родитель - женщина.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите город рождения:")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="male",
                           state=FormI485.Parent2_Gender_Choice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line12_Gender[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш 2 родитель - мужчина.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите город рождения:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line13_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line13_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну рождения:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line14_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line14_Country[0]"] = message.text
    keyboard = FormI485ParentNotAlive()
    await bot.send_message(message.from_user.id,
                           "Укажите текущий город или город проживания (если родитель 2 жив):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ParentNotAlive_Yes",
                           state=FormI485.S_6_Pt4Line15_CityTown_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485MaritalStatusChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 5. «Информация о вашем браке.»")
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение:\n"
                           "1. Не состою в браке\n"
                           "2. В браке\n"
                           "3. В разводе\n"
                           "4. Вдова (-ец)\n"
                           "5. Брак аннулирован\n"
                           "6. Юридически установленное раздельное проживание\n",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.MaritalStatusChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line15_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line15_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите текущую страну проживания:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt4Line16_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt4Line16_Country[0]"] = message.text
    keyboard = FormI485MaritalStatusChoice()
    await bot.send_message(message.from_user.id,
                           "Часть 5. «Информация о вашем браке.»")
    await bot.send_message(message.from_user.id,
                           "Выберите семейное положение:\n"
                           "1. Не состою в браке\n"
                           "2. В браке\n"
                           "3. В разводе\n"
                           "4. Вдова (-ец)\n"
                           "5. Брак аннулирован\n"
                           "6. Юридически установленное раздельное проживание\n",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="MaritalStatus_1",
                           state=FormI485.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line1_MaritalStatus[0]"] = "x"
    keyboard = FormI485IsYourSpouceInArmyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не состоите в браке.")
    await bot.send_message(callback_query.from_user.id,
                           "Ваш супруг является действующим лицом вооруженных сил США или береговой охраны США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.IsYourSpouceInArmyChoice.set()


@dp.callback_query_handler(text="MaritalStatus_2",
                           state=FormI485.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line1_MaritalStatus[1]"] = "x"
    keyboard = FormI485IsYourSpouceInArmyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что состоите в браке.")
    await bot.send_message(callback_query.from_user.id,
                           "Ваш супруг является действующим лицом вооруженных сил США или береговой охраны США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.IsYourSpouceInArmyChoice.set()


@dp.callback_query_handler(text="MaritalStatus_3",
                           state=FormI485.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line1_MaritalStatus[2]"] = "x"
    keyboard = FormI485IsYourSpouceInArmyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что разведены.")
    await bot.send_message(callback_query.from_user.id,
                           "Ваш супруг является действующим лицом вооруженных сил США или береговой охраны США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.IsYourSpouceInArmyChoice.set()


@dp.callback_query_handler(text="MaritalStatus_4",
                           state=FormI485.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line1_MaritalStatus[3]"] = "x"
    keyboard = FormI485BeenMarriedBeforeChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что являетесь вдовой(цом).")
    await bot.send_message(callback_query.from_user.id,
                           "Вы ранее состояли в браке?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.BeenMarriedBeforeChoice.set()


@dp.callback_query_handler(text="MaritalStatus_5",
                           state=FormI485.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line1_MaritalStatus[4]"] = "x"
    keyboard = FormI485IsYourSpouceInArmyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш брак аннулирован.")
    await bot.send_message(callback_query.from_user.id,
                           "Ваш супруг является действующим лицом вооруженных сил США или береговой охраны США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.IsYourSpouceInArmyChoice.set()


@dp.callback_query_handler(text="MaritalStatus_6",
                           state=FormI485.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line1_MaritalStatus[5]"] = "x"
    keyboard = FormI485IsYourSpouceInArmyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что юридически установленно раздельное проживание.")
    await bot.send_message(callback_query.from_user.id,
                           "Ваш супруг является действующим лицом вооруженных сил США или береговой охраны США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.IsYourSpouceInArmyChoice.set()


@dp.callback_query_handler(text="IsYourSpouceInArmy_Yes",
                           state=FormI485.IsYourSpouceInArmyChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line2_YNNA[1]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш супруг является действующим лицом вооруженных сил США или береговой "
                           "охраны США.")
    await bot.send_message(callback_query.from_user.id,
                           "Сколько раз вы состояли в браке "
                           "(включая аннулированные браки и браки с одним и тем же лицом)?")
    time.sleep(0.5)
    await FormI485.S_6_Pt5Line3_TimesMarried_0.set()


@dp.callback_query_handler(text="IsYourSpouceInArmy_No",
                           state=FormI485.IsYourSpouceInArmyChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line2_YNNA[0]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш супруг не является действующим лицом вооруженных сил США или береговой "
                           "охраны США.")
    await bot.send_message(callback_query.from_user.id,
                           "Сколько раз вы состояли в браке "
                           "(включая аннулированные браки и браки с одним и тем же лицом)?")
    time.sleep(0.5)
    await FormI485.S_6_Pt5Line3_TimesMarried_0.set()


@dp.callback_query_handler(text="IsYourSpouceInArmy_DoNotKnow",
                           state=FormI485.IsYourSpouceInArmyChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line2_YNNA[2]"] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не знаете является ли ваш супруг действующим лицом вооруженных сил США или "
                           "береговой охраны США.")
    await bot.send_message(callback_query.from_user.id,
                           "Сколько раз вы состояли в браке "
                           "(включая аннулированные браки и браки с одним и тем же лицом)?")
    time.sleep(0.5)
    await FormI485.S_6_Pt5Line3_TimesMarried_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line3_TimesMarried_0)
async def process_S_6_Pt5Line3_TimesMarried_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line3_TimesMarried[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Информация о вашем нынешнем браке.»")
    await bot.send_message(message.from_user.id,
                           "Укажите ФИО нынешнего супруга, как указано в паспорте.\nУкажите фамилию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line4a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line4a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line4b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line4b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line4c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line4c_MiddleName[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите A-number (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_6_Pt5Line5_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения вашего супруга (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.S_6_Pt5Line6_DateofBirth_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line5_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line5_AlienNumber[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения вашего супруга (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line6_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line6_DateofBirth[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату вступления в брак с нынешним супругом (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line7_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line7_Date[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите место рождения вашего нынешнего супруга.\nУкажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line8a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line8a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат или провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line8b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line8b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line8c_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line8c_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите место вступления в брак с нынешним супругом.\nУкажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line9a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line9a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат или провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line9b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line9b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_6_Pt5Line9c_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line9c_Country[0]"] = message.text
    keyboard = Form485SpouceApllyingTooChoice()
    await bot.send_message(message.from_user.id,
                           "Ваш нынешний супруг подает это заявление вместе с вами?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SpouceApllyingToo_Yes",
                           state=FormI485.SpouceApplyingTooChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line10_YN[1]"] = "x"
    keyboard = FormI485BeenMarriedBeforeChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш нынешний супруг подает это заявление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Вы ранее состояли в браке?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.BeenMarriedBeforeChoice.set()


@dp.callback_query_handler(text="SpouceApllyingToo_No",
                           state=FormI485.SpouceApplyingTooChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[6].Pt5Line10_YN[0]"] = "x"
    keyboard = FormI485BeenMarriedBeforeChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш нынешний супруг не подает это заявление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Вы ранее состояли в браке?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.BeenMarriedBeforeChoice.set()


@dp.callback_query_handler(text="BeenMarriedBefore_Yes",
                           state=FormI485.BeenMarriedBeforeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ранее состояли в браке.")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о предыдущих браках.» "
                           "Если вы уже состояли в браке в Соединенных Штатах или в любой другой стране, предоставьте "
                           "следующую информацию о вашем предыдущем супруге.\n")

    await bot.send_message(callback_query.from_user.id,
                           "Укажите ФИО прошлого супруга, как указано в паспорте.\n"
                           "Укажите фамилию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt511a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt511a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line11b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line11b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line11c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line11c_MiddleName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения вашего бывшего супруга (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line12_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line12_DateofBirth[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату вступления в брак с бывшим супругом (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line13_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line13_Date[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите место вступления в брак с прошлого супругом.\nУкажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line14a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line14a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат или провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line14b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line14b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line14c_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line14c_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату прекращения брака с предыдущим супругом (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line15_Date_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line15_Date[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите место законного прекращения брака с предыдущим супругом.\nУкажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line16a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line16a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат или провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line16b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line16b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt5Line16c_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt5Line16c_Country[0]"] = message.text
    keyboard = FormI485HaveKidsChoice()
    await bot.send_message(message.from_user.id,
                           "У вас есть дети?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="BeenMarriedBefore_No",
                           state=FormI485.BeenMarriedBeforeChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485HaveKidsChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ранее не состояли в браке.")
    await bot.send_message(callback_query.from_user.id,
                           "У вас есть дети?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveKidsChoice.set()


@dp.callback_query_handler(text="HaveKids_Yes",
                           state=FormI485.HaveKidsChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас есть дети.")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 6. Информация о ваших детях\n"
                           "Укажите количество ваших детей (включая тех, кому больше 21 года): ")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line1_TotalChildren_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line1_TotalChildren[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите фамилию вашего первого ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line2a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line2a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя вашего первого ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line2b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line2b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество вашего первого ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line2c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line2c_MiddleName[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите регистрационный номер иностранца вашего первого ребенка (A-Number) (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_7_Pt6Line3_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вашего первого ребенка нет A-Number.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения вашего первого ребенка (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line3_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line3_AlienNumber[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения вашего первого ребенка (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line4_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line4_DateofBirth[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну рождения вашего первого ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line6_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line6_Country[0]"] = message.text
    keyboard = FormI485ChildApplyingTooChoice()
    await bot.send_message(message.from_user.id,
                           "Этот ребенок подает заявление вместе с вами?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ChildApplyingToo_Yes",
                           state=FormI485.Child1ApplyingTooChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line6_YesNo[0]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш первый ребенок подает завяление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию вашего второго ребенка:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ChildApplyingToo_No",
                           state=FormI485.Child1ApplyingTooChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line6_YesNo[1]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш первый ребенок не подает завяление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию вашего второго ребенка:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_7_Pt6Line7a_FamilyName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет второго ребенка.")
    keyboard = FormI485EthnicityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 7. «Биографические сведения.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу этническую принадлежность (выберите только один вариант):\n"
                           "1.	Испанец или латиноамериканец\n"
                           "2.	Не испанец или латиноамериканец", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.EthicityChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line7a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line7a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя вашего второго ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line7b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line7b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество второго первого ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line7c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line7c_MiddleName[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите регистрационный номер иностранца вашего второго ребенка (A-Number) (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_7_Pt6Line8_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вашего второго ребенка нет A-Number.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения вашего второго ребенка (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line8_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line8_AlienNumber[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения вашего первого ребенка (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line9_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line9_DateofBirth[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну рождения вашего второго ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_7_Pt6Line10_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line10_Country[0]"] = message.text
    keyboard = FormI485ChildApplyingTooChoice()
    await bot.send_message(message.from_user.id,
                           "Этот ребенок подает заявление вместе с вами?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ChildApplyingToo_Yes",
                           state=FormI485.Child1ApplyingTooChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line11_YesNo[0]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш второй ребенок подает завяление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию вашего третьего ребенка:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ChildApplyingToo_No",
                           state=FormI485.Child1ApplyingTooChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[7].Pt6Line11_YesNo[1]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш второй ребенок не подает завяление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию вашего третьего ребенка:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_8_Pt6Line12a_FamilyName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет третьего ребенка.")
    keyboard = FormI485EthnicityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 7. «Биографические сведения.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу этническую принадлежность (выберите только один вариант):\n"
                           "1.	Испанец или латиноамериканец\n"
                           "2.	Не испанец или латиноамериканец", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.EthicityChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt6Line12a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line12a_FamilyName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя вашего третьего ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt6Line12b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line12b_GivenName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите отчество третьего ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt6Line12c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line12c_MiddleName[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите регистрационный номер иностранца вашего третьего ребенка (A-Number) (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_8_Pt6Line13_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вашего третьего ребенка нет A-Number.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дату рождения вашего третьего ребенка (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt6Line13_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line13_AlienNumber[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату рождения вашего третьего ребенка (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt6Line14_DateofBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line14_DateofBirth[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну рождения вашего третьего ребенка:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt6Line15_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line15_Country[0]"] = message.text
    keyboard = FormI485ChildApplyingTooChoice()
    await bot.send_message(message.from_user.id,
                           "Этот ребенок подает заявление вместе с вами?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="ChildApplyingToo_Yes",
                           state=FormI485.Child1ApplyingTooChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line16_YesNo[0]"] = 'x'
    keyboard = FormI485EthnicityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш третий ребенок подает завяление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 7. «Биографические сведения.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу этническую принадлежность (выберите только один вариант):\n"
                           "1.	Испанец или латиноамериканец\n"
                           "2.	Не испанец или латиноамериканец", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.EthicityChoice.set()


@dp.callback_query_handler(text="ChildApplyingToo_No",
                           state=FormI485.Child1ApplyingTooChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt6Line16_YesNo[1]"] = 'x'
    keyboard = FormI485EthnicityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что ваш третий ребенок не подает завяление вместе с вами.")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 7. «Биографические сведения.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу этническую принадлежность (выберите только один вариант):\n"
                           "1.	Испанец или латиноамериканец\n"
                           "2.	Не испанец или латиноамериканец", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.EthicityChoice.set()


@dp.callback_query_handler(text="HaveKids_No",
                           state=FormI485.HaveKidsChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет детей.")
    keyboard = FormI485EthnicityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 7. «Биографические сведения.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу этническую принадлежность (выберите только один вариант):\n"
                           "1.	Испанец или латиноамериканец\n"
                           "2.	Не испанец или латиноамериканец", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.EthicityChoice.set()


@dp.callback_query_handler(text="Ethnicity_1",
                           state=FormI485.EthicityChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line1_Ethnicity[0]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы испанец или латиноамериканец.")
    keyboard = FormI485RaceChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу расу (выберете все применимое):\n"
                           "1.	Европеоид\n"
                           "2.	Монголоид (азиат)\n"
                           "3.	Негроид или афроамериканец\n"
                           "4.	Американский индеец или коренной житель Аляски\n"
                           "5.	Уроженец Гавайских островов или других островов Тихого океана\n",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.RaceChoice.set()


@dp.callback_query_handler(text="Ethnicity_2",
                           state=FormI485.EthicityChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line1_Ethnicity[1]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы не испанец или латиноамериканец.")
    keyboard = FormI485RaceChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу расу (выберете все применимое):\n"
                           "1.	Европеоид\n"
                           "2.	Монголоид (азиат)\n"
                           "3.	Негроид или афроамериканец\n"
                           "4.	Американский индеец или коренной житель Аляски\n"
                           "5.	Уроженец Гавайских островов или других островов Тихого океана\n",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.RaceChoice.set()


@dp.callback_query_handler(text="Race_Euro",
                           state=FormI485.RaceChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line2_Race[0]"] = 'x'
    keyboard = FormI485IChooseAllOfMyRaces()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы европеоид.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Race_Asia",
                           state=FormI485.RaceChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line2_Race[1]"] = 'x'
    keyboard = FormI485IChooseAllOfMyRaces()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы монголоид (азиат).",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Race_Negro",
                           state=FormI485.RaceChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line2_Race[2]"] = 'x'
    keyboard = FormI485IChooseAllOfMyRaces()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы негроид или афроамериканец.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Race_AmericanIndian",
                           state=FormI485.RaceChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line2_Race[3]"] = 'x'
    keyboard = FormI485IChooseAllOfMyRaces()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы американский индеец или коренной житель Аляски.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Race_HawaiiOrPacificOcean",
                           state=FormI485.RaceChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line2_Race[4]"] = 'x'
    keyboard = FormI485IChooseAllOfMyRaces()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы уроженец Гавайских островов или других островов Тихого океана.",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="continue",
                           state=FormI485.RaceChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    time.sleep(0.5)
    await FormI485.next()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш рост (в сантиметрах):")


def cm_to_feet_inches(cm):
    # 1 inch is 2.54 cm
    total_inches = cm / 2.54

    # 1 foot is 12 inches
    feet = int(total_inches // 12)
    inches = round(total_inches % 12)

    return feet, inches


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt7Line3_HeightFeetAndInches)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            feet, inches = cm_to_feet_inches(int(message.text))
            data["[8].Pt7Line3_HeightFeet[0]"] = feet
            data["[8].Pt7Line3_HeightInches[0]"] = inches
        except ValueError:
            bot.send_message(message.from_user.id, "Укажите ваш рост ЦИФРОЙ (в сантиметрах):")
            return
    await bot.send_message(message.from_user.id,
                           "Укажите ваш вес (в килограмах): ")
    time.sleep(0.5)
    await FormI485.next()


def kg_to_pounds(kg):
    # 1 kg is approximately 2.20462 pounds
    pounds = kg * 2.20462
    return str(round(pounds, 2))  # rounding to 2 decimal places for simplicity


@escape_json_special_chars
@dp.message_handler(state=FormI485.WeightField)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pounds = kg_to_pounds(int(message.text))
        data["[8].Pt7Line4_Weight1[0]"] = pounds[0]
        data["[8].Pt7Line4_Weight2[0]"] = pounds[1]
        data["[8].Pt7Line4_Weight3[0]"] = pounds[2]
    keyboard = FormI485EyeColorChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите ваш цвет глаз (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Blue",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[0]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Black",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[1]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Brown",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[2]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Gray",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[3]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Green",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[4]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Hazel",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[5]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Maroon",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[6]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Pink",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[7]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Unknown/Other",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[8]"] = 'x'
    keyboard = FormI485IHairColorChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш цвет волос (выберите только один вариант):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Blue",
                           state=FormI485.EyeColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line5_Eyecolor[0]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Bald (No hair)",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[0]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Black",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[1]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Blond",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[2]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Brown",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[3]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Gray",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[4]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Red",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[5]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Sandy",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[6]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="White",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[7]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="Unknown/Other",
                           state=FormI485.HairColorChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt7Line6_Haircolor[8]"] = 'x'
    keyboard = FormI485IGeneralEligibilityChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 8. «Общие основания приемлемости и недопустимости.»")
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, вовлечены или каким-либо образом связаны с какой-либо "
                           "организацией, ассоциацией, фондом, партией, клубом, обществом или подобной "
                           "группой в Соединенных Штатах или в любом другом месте в мире, включая какую-либо "
                           "военную службу?", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="GeneralEligibility_Yes",
                           state=FormI485.WasOrIsMemberOfAnyOrganization)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line1_YesNo[1]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация об организации 1.» Далее укажите информацию об организации 1.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название организации:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line2_OrgName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line2_OrgName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line3a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line3a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат или провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line3b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line3b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line3c_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line3c_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите природу группы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line4_Group_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line4_Group[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату начала членства в организации (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line5a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line5a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату выхода из организации (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line5b_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line5b_DateTo[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Далее укажите информацию об организации 2.",
                           reply_markup=keyboard.markup)
    await bot.send_message(message.from_user.id,
                           "Укажите название организации:")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_8_Pt8Line6_OrgName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485WasEverRefusedToEnterUSAChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вам когда-либо было отказано во въезде в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.WasEverRefusedToEnterUSAChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line6_OrgName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line6_OrgName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line8a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line8a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат или провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line7b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line7b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line7c_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line7c_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите природу группы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_8_Pt8Line8_Group_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line8_Group[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату начала членства в организации (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line9a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line9a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату выхода из организации (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line9b_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line9b_DateTo[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Далее укажите информацию об организации 3.")
    await bot.send_message(message.from_user.id,
                           "Укажите название организации:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line10_OrgName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line10_OrgName[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите город:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line11a_CityTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line11a_CityTown[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат или провинцию:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line11b_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line11b_State[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line11c_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line11c_Country[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите природу группы:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line12_Group_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line12_Group[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату начала членства в организации (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line13a_DateFrom_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line13a_DateFrom[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату выхода из организации (мм/дд/гггг):")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_9_Pt8Line13b_DateTo_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line13b_DateTo[0]"] = message.text
    keyboard = FormI485WasEverRefusedToEnterUSAChoice()
    await bot.send_message(message.from_user.id,
                           "Вам когда-либо было отказано во въезде в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.WasEverRefusedToEnterUSAChoice.set()


@dp.callback_query_handler(text="GeneralEligibility_No",
                           state=FormI485.WasOrIsMemberOfAnyOrganization)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[8].Pt8Line1_YesNo[0]"] = 'x'
    keyboard = FormI485WasEverRefusedToEnterUSAChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вам когда-либо было отказано во въезде в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.WasEverRefusedToEnterUSAChoice.set()


@dp.callback_query_handler(text="WasEverRefusedToEnterUSA_Yes",
                           state=FormI485.WasEverRefusedToEnterUSAChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line14_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вам когда-либо было отказывали в визе в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverBeenDeniedVisaToTheUSA.set()


@dp.callback_query_handler(text="WasEverRefusedToEnterUSA_No",
                           state=FormI485.WasEverRefusedToEnterUSAChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line14_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вам когда-либо было отказывали в визе в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverBeenDeniedVisaToTheUSA.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenDeniedVisaToTheUSA)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line15_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо работали в США без разрешения на работу?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverWorkedWithoutAuthorization.set()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenDeniedVisaToTheUSA)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line15_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо работали в США без разрешения на работу?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverWorkedWithoutAuthorization.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverWorkedWithoutAuthorization)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line16_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо нарушали условия вашего неиммиграционного статуса?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverWorkedWithoutAuthorization)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line16_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо нарушали условия вашего неиммиграционного статуса?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverViolatedConditionsOfNonimmigrantStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line17_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы в настоящее время или когда-либо находились в процессе выдворения, исключения, "
                           "отмены или депортации?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverViolatedConditionsOfNonimmigrantStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line17_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы в настоящее время или когда-либо находились в процессе выдворения, исключения, "
                           "отмены или депортации?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenInRemoval)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line18_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "В отношении вас когда-либо был издан окончательный приказ об исключении, депортации "
                           "или выдворении?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenInRemoval)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line18_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "В отношении вас когда-либо был издан окончательный приказ об исключении, депортации "
                           "или выдворении?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenIssuedAFinalOrder)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line19_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "В отношении вас было восстановлено предыдущее окончательное решение суда об исключении, "
                           "депортации или выдворении?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenIssuedAFinalOrder)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line19_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "В отношении вас было восстановлено предыдущее окончательное решение суда об исключении, "
                           "депортации или выдворении?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverHadPriorFinalOrder)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line20_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо имели статус законного постоянного жителя, который впоследствии был "
                           "аннулирован?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverHadPriorFinalOrder)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line20_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо имели статус законного постоянного жителя, который впоследствии был "
                           "аннулирован?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverHeldLawfulPermanentResidentStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line21_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Разрешал ли вам когда-либо сотрудник иммиграционной службы или иммиграционный судья "
                           "добровольный выезд, но вы не выезжали в отведенное время?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverHeldLawfulPermanentResidentStatus)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line21_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Разрешал ли вам когда-либо сотрудник иммиграционной службы или иммиграционный судья "
                           "добровольный выезд, но вы не выезжали в отведенное время?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverFailedToDepart)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line22_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо обращались за какой-либо помощью или защитой от выдворения, исключения или "
                           "депортации?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverFailedToDepart)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line22_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо обращались за какой-либо помощью или защитой от выдворения, исключения или "
                           "депортации?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverAppliedForProtection)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line23_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были неиммигрантом по обмену категории J, в отношении которого наличествовало"
                           " требование о  двухлетнем проживании за границей?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverAppliedForProtection)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line23_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были неиммигрантом по обмену категории J, в отношении которого наличествовало"
                           " требование о  двухлетнем проживании за границей?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenAJNonImmigrantExchange)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line24a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы выполнили требование о проживании за границей?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverCompliedWithForeignResidenceRequirement.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverCompliedWithForeignResidenceRequirement)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line24b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставляли ли вам право не соблюдать это условие?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveBeenGrantedAWaiver.set()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverCompliedWithForeignResidenceRequirement)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line24b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Предоставляли ли вам право не соблюдать это условие?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveBeenGrantedAWaiver.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveBeenGrantedAWaiver)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line24c_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были арестованы, обвинены или задержаны по любой причине любым сотрудником "
                           "правоохранительных органов (включая, помимо прочего, любого сотрудника иммиграционной "
                           "службы США или любого сотрудника вооруженных сил США или береговой охраны США)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveBeenGrantedAWaiver)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line24c_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были арестованы, обвинены или задержаны по любой причине любым сотрудником "
                           "правоохранительных органов (включая, помимо прочего, любого сотрудника иммиграционной "
                           "службы США или любого сотрудника вооруженных сил США или береговой охраны США)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenAJNonImmigrantExchange)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line24a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были арестованы, обвинены или задержаны по любой причине любым сотрудником "
                           "правоохранительных органов (включая, помимо прочего, любого сотрудника иммиграционной "
                           "службы США или любого сотрудника вооруженных сил США или береговой охраны США)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverBeenArrested.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenArrested)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line25_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо совершали какое-либо преступление (даже если вас не арестовывали, не "
                           "привлекали к суду, не обвиняли и не судили за это преступление)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenArrested)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line25_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо совершали какое-либо преступление (даже если вас не арестовывали, не "
                           "привлекали к суду, не обвиняли и не судили за это преступление)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line26_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо признавали себя виновным в совершении преступления или правонарушения или "
                           "были осуждены за него (даже если ответственность за нарушение была впоследствии была "
                           "отменена судом, или если вы получили помилование, амнистию, постановление о реабилитации "
                           "или иной акт помилования)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[9].Pt8Line26_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо признавали себя виновным в совершении преступления или правонарушения или "
                           "были осуждены за него (даже если ответственность за нарушение была впоследствии была "
                           "отменена судом, или если вы получили помилование, амнистию, постановление о реабилитации "
                           "или иной акт помилования)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverPledGuilty)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line27_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Судья когда-нибудь выносил в отношении вас обвинительный приговор, или к вам были "
                           "применены условия, которые ограничивали вашу свободу (например, тюремное заключение, "
                           "условный срок, домашний арест, альтернативное "
                           "наказание, лечение от наркомании или алкоголизма, реабилитационные программы, "
                           "испытательный срок или общественные работы)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverPledGuilty)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line27_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Судья когда-нибудь выносил в отношении вас обвинительный приговор, или к вам были "
                           "применены условия, которые ограничивали вашу свободу (например, тюремное заключение, "
                           "условный срок, домашний арест, альтернативное "
                           "наказание, лечение от наркомании или алкоголизма, реабилитационные программы, "
                           "испытательный срок или общественные работы)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenOrderedPunishedByAJudge)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line28_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были подсудимым или обвиняемым в уголовном процессе?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenOrderedPunishedByAJudge)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line28_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были подсудимым или обвиняемым в уголовном процессе?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenDefendantOrTheAccused)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line29_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо нарушали (или пытались или сговорились нарушить) какой-либо закон или "
                           "постановление штата, Соединенных Штатов или иностранного государства о контролируемых "
                           "веществах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenDefendantOrTheAccused)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line29_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо нарушали (или пытались или сговорились нарушить) какой-либо закон или "
                           "постановление штата, Соединенных Штатов или иностранного государства о контролируемых "
                           "веществах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverViolatedAnyControlledSubstanceLaw)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line30_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были осуждены за два или более правонарушения (кроме чисто политических "
                           "правонарушений), за которые совокупные приговоры к лишению свободы составляли пять "
                           "лет или более?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverViolatedAnyControlledSubstanceLaw)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line30_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были осуждены за два или более правонарушения (кроме чисто политических правонарушений), за которые совокупные приговоры к лишению свободы составляли пять лет или более?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenConvictedOfTwoOrMoreOffenses)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line31_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо незаконно продавали или получали выгоду от торговли любыми контролируемыми веществами, такими как химические вещества, запрещенные наркотики?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenConvictedOfTwoOrMoreOffenses)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line31_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо незаконно продавали или получали выгоду от торговли любыми контролируемыми веществами, такими как химические вещества, запрещенные наркотики?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverIllicitlyTraffickedOrBenefitedFromNarcotics)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line32_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо сознательно помогали, подстрекали, участвовали в сговоре о незаконном обороте любых наркотиков или других контролируемых веществ?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverIllicitlyTraffickedOrBenefitedFromNarcotics)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line32_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо сознательно помогали, подстрекали, участвовали в сговоре о незаконном обороте любых наркотиков или других контролируемых веществ?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverAssistedInTraffickingSubstances)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line33_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом, сыном или дочерью иностранца, который незаконно торговал или помогал (или иным образом подстрекал, участвовал в сговоре) в незаконном обороте контролируемых веществ, таких как химические вещества, запрещенные лекарства или наркотики, и получали ли вы в течение последних пяти лет какую-либо финансовую или иную выгоду от незаконной деятельности вашего супруга или родителя, хотя вы знали или разумно должны были знать, что финансовая или иная выгода была получена в результате незаконной деятельности вашего супруга или родителя?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverAssistedInTraffickingSubstances)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line33_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом, сыном или дочерью иностранца, который незаконно торговал или помогал (или иным образом подстрекал, участвовал в сговоре) в незаконном обороте контролируемых веществ, таких как химические вещества, запрещенные лекарства или наркотики, и получали ли вы в течение последних пяти лет какую-либо финансовую или иную выгоду от незаконной деятельности вашего супруга или родителя, хотя вы знали или разумно должны были знать, что финансовая или иная выгода была получена в результате незаконной деятельности вашего супруга или родителя?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.YourFamilyIllicitlyTrafickedSubstances)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line34_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо занимались проституцией или ездили в Соединенные Штаты, чтобы заниматься проституцией?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.YourFamilyIllicitlyTrafickedSubstances)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line34_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо занимались проституцией или ездили в Соединенные Штаты, чтобы заниматься проституцией?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverEngagedInProstitution)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line35_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо прямо или косвенно приобретали (или пытались приобрести) или импортировали проституток или лиц с целью проституции?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverEngagedInProstitution)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line35_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо прямо или косвенно приобретали (или пытались приобрести) или импортировали проституток или лиц с целью проституции?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverProcuredProstitutes)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line36_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо получали какие-либо доходы или деньги от проституции?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverProcuredProstitutes)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line36_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо получали какие-либо доходы или деньги от проституции?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverReceivedMoneyFromProstitution)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line37_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Собираетесь ли вы заниматься незаконными азартными играми или любой другой формой коммерциализации порока, такой как проституция, бутлегерство или продажа детской порнографии, находясь в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverReceivedMoneyFromProstitution)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line37_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Собираетесь ли вы заниматься незаконными азартными играми или любой другой формой коммерциализации порока, такой как проституция, бутлегерство или продажа детской порнографии, находясь в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IllegalGambling)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line38_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо использовали иммунитет (дипломатический или иной), чтобы избежать судебного преследования за уголовное преступление в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IllegalGambling)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line38_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо использовали иммунитет (дипломатический или иной), чтобы избежать судебного преследования за уголовное преступление в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverExercisedImmunityForCriminalOffense)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line39_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо будучи должностным лицом иностранного правительства, отвечали или непосредственно нарушали религиозные свободы?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverExercisedImmunityForCriminalOffense)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line39_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо будучи должностным лицом иностранного правительства, отвечали или непосредственно нарушали религиозные свободы?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverServingForeignGovernment)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line40_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо провоцировали силой, обманом или принуждением или иным образом были вовлечены в торговлю людьми для целей коммерциализации секса?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverServingForeignGovernment)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line40_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо провоцировали силой, обманом или принуждением или иным образом были вовлечены в торговлю людьми для целей коммерциализации секса?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverInductedByForce)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line41_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо продавали человека в принудительное рабство, долговую кабалу? Торговля "
                           "людьми включает в себя вербовку, укрывательство, перевозку, предоставление или "
                           "приобретение человека для работ или услуг с применением силы, мошенничества или "
                           "принуждения.",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverInductedByForce)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line41_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо продавали человека в принудительное рабство, долговую кабалу? Торговля "
                           "людьми включает в себя вербовку, укрывательство, перевозку, предоставление или "
                           "приобретение человека для работ или услуг с применением силы, мошенничества или "
                           "принуждения.",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverTraffickedPersonInvoluntary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line42_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо сознательно помогали, подстрекали, содействовали, вступали в сговор с "
                           "другими в торговле людьми для целей коммерциализации секса, рабства, пеонажа или долговой "
                           "кабалы?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverTraffickedPersonInvoluntary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line42_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо сознательно помогали, подстрекали, содействовали, вступали в сговор с "
                           "другими в торговле людьми для целей коммерциализации секса, рабства, пеонажа или долговой "
                           "кабалы?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverKnowinglyAidedTraffickingPersonInvoluntary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line43_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом, сыном или дочерью иностранного гражданина, который занимался "
                           "торговлей людьми, и получали ли вы в течение последних пяти лет какие-либо финансовые или "
                           "иные выгоды от незаконной деятельности вашего супруга или вашего родителя, хотя вы знали "
                           "или разумно должны были знать, что эти денежные средства были результатом незаконной "
                           "деятельности вашего супруга или родителя?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverKnowinglyAidedTraffickingPersonInvoluntary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line43_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом, сыном или дочерью иностранного гражданина, который занимался "
                           "торговлей людьми, и получали ли вы в течение последних пяти лет какие-либо финансовые или "
                           "иные выгоды от незаконной деятельности вашего супруга или вашего родителя, хотя вы знали "
                           "или разумно должны были знать, что эти денежные средства были результатом незаконной "
                           "деятельности вашего супруга или родителя?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.FamilyEngagedInTraffickingPersonInvoluntary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line44_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо занимались отмыванием денег или сознательно помогали, участвовали в сговоре с другими лицами в отмывании денег, или пытались въехать в Соединенные Штаты, чтобы участвовать в такой деятельности?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.FamilyEngagedInTraffickingPersonInvoluntary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line44_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо занимались отмыванием денег или сознательно помогали, участвовали в сговоре с другими лицами в отмывании денег, или пытались въехать в Соединенные Штаты, чтобы участвовать в такой деятельности?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverEngagedInMoneyLaundering)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line45_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в какой-либо деятельности, которая нарушает или обходит любой закон, касающийся шпионажа или саботажа в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverEngagedInMoneyLaundering)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[10].Pt8Line45_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в какой-либо деятельности, которая нарушает или обходит любой закон, касающийся шпионажа или саботажа в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IntendToEngageInEspionage)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в любой деятельности в Соединенных Штатах, которая нарушает любой закон, запрещающий экспорт из Соединенных Штатов товаров, технологий или конфиденциальной информации?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IntendToEngageInEspionage)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в любой деятельности в Соединенных Штатах, которая нарушает любой закон, запрещающий экспорт из Соединенных Штатов товаров, технологий или конфиденциальной информации?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IntendToEngageInProhibitedExport)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в любой деятельности, целью которой является противостояние, "
                           "контроль или свержение правительства США, насилием или другими незаконными средствами?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IntendToEngageInProhibitedExport)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в любой деятельности, целью которой является противостояние, "
                           "контроль или свержение правительства США, насилием или другими незаконными средствами?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IntendToOwerthrowUSGovernment)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46c_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в любой деятельности, которая может поставить под угрозу благополучие или безопасность Соединенных Штатов?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IntendToOwerthrowUSGovernment)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46c_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены участвовать в любой деятельности, которая может поставить под угрозу благополучие или безопасность Соединенных Штатов?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IntendToEndangerWelfare)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46d_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены заниматься какой-либо другой незаконной деятельностью?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IntendToEndangerWelfare)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46d_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы намерены заниматься какой-либо другой незаконной деятельностью?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IntendToEngageInAnyUnlawfulActivity)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46e_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Занимаетесь ли вы или после вашего въезда в Соединенные Штаты намерены заниматься какой-либо деятельностью, которая потенциально может иметь серьезные негативные последствия для внешней политики США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IntendToEngageInAnyUnlawfulActivity)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line46e_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Занимаетесь ли вы или после вашего въезда в Соединенные Штаты намерены заниматься какой-либо деятельностью, которая потенциально может иметь серьезные негативные последствия для внешней политики США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IntendToAdverseForeignPolicy)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line47_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо совершали, грозились совершить, пытались совершить, сговаривались с целью совершения, подстрекали, одобряли, пропагандировали, планировали или подготавливали любое из следующих действий: угон самолета, саботаж, похищение, политическое убийство или использование оружия или взрывчатых веществ с целью причинения вреда другому лицу или нанесения существенного материального ущерба? (далее – вопрос А)",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IntendToAdverseForeignPolicy)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line47_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо совершали, грозились совершить, пытались совершить, сговаривались с целью совершения, подстрекали, одобряли, пропагандировали, планировали или подготавливали любое из следующих действий: угон самолета, саботаж, похищение, политическое убийство или использование оружия или взрывчатых веществ с целью причинения вреда другому лицу или нанесения существенного материального ущерба? (далее – вопрос А)",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverCommitedACrime_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо участвовали или был членом группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverCommitedACrime_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо участвовали или был членом группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenInOrganizationThatCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо набирали членов или собирали денежные средства или ценные вещи для группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenInOrganizationThatCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо набирали членов или собирали денежные средства или ценные вещи для группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverDoneServiceToOrganizationThatCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48c_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо предоставляли денежные средства, ценные вещи, услуги или труд, "
                           "или любую другую помощь или поддержку для любого из видов деятельности, описанной в "
                           "вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverDoneServiceToOrganizationThatCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48c_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо предоставляли денежные средства, ценные вещи, услуги или труд, "
                           "или любую другую помощь или поддержку для любого из видов деятельности, описанной в "
                           "вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverProvidedToOrganizationThatCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48d_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо предоставляли денежные средства, ценные вещи, услуги или труд, или любую другую помощь или поддержку для человека, группы лиц или организации, занимающейся деятельностью, описанной в номере вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverProvidedToOrganizationThatCommitedACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48d_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо предоставляли денежные средства, ценные вещи, услуги или труд, или любую другую помощь или поддержку для человека, группы лиц или организации, занимающейся деятельностью, описанной в номере вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverProvidedToOrganizationThatCommitedACrime_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48e_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо проходили какую-либо военную, военизированную или боевую подготовку?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverProvidedToOrganizationThatCommitedACrime_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line48e_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо проходили какую-либо военную, военизированную или боевую подготовку?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverReceivedMilitaryTraining)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line49_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Собираетесь ли вы заниматься какой-либо деятельностью, перечисленной в вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverReceivedMilitaryTraining)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line49_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Собираетесь ли вы заниматься какой-либо деятельностью, перечисленной в вопросе А?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.IntendToEngageInCommitingACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line50_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое когда-либо совершало, грозилось совершить, пыталось совершить, сговаривалось с целью совершения, подстрекало, одобряло, пропагандировало, планировало или подготавливало любое из следующих действий: угон самолета, саботаж, похищение, политическое убийство или использование оружия или взрывчатых веществ с целью причинения вреда другому лицу или нанесения существенного материального ущерба? (далее - вопрос Б)",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.IntendToEngageInCommitingACrime)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line50_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое когда-либо совершало, грозилось совершить, пыталось совершить, сговаривалось с целью совершения, подстрекало, одобряло, пропагандировало, планировало или подготавливало любое из следующих действий: угон самолета, саботаж, похищение, политическое убийство или использование оружия или взрывчатых веществ с целью причинения вреда другому лицу или нанесения существенного материального ущерба? (далее - вопрос Б)",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.SpouceOfCriminalChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое участвовало или было членом группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.SpouceOfCriminalChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое участвовало или было членом группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.SpouceOfCriminalChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое набирало членов или собирало денежные средства или ценные вещи для группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.SpouceOfCriminalChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое набирало членов или собирало денежные средства или ценные вещи для группы или организации, которые занимались какой-либо деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.SpouceOfCriminalChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51c_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое предоставляло денежные средства, ценные вещи, услуги или труд, или любую другую помощь или поддержку для любого из видов деятельности, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.SpouceOfCriminalChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51c_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое предоставляло денежные средства, ценные вещи, услуги или труд, или любую другую помощь или поддержку для любого из видов деятельности, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.SpouceOfCriminalChoice_4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51d_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое предоставляло денежные средства, ценные вещи, услуги или труд, или любую другую помощь или поддержку физическому лицу, группе лиц или организации, которые занимаются деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.SpouceOfCriminalChoice_4)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51d_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое предоставляло денежные средства, ценные вещи, услуги или труд, или любую другую помощь или поддержку физическому лицу, группе лиц или организации, которые занимаются деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.SpouceOfCriminalChoice_5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51e_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое проходило какую-либо военную, военизированную или боевую подготовку от группы или организации, которая занималась какой-либо деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.SpouceOfCriminalChoice_5)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51e_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Являетесь ли вы супругом или ребенком лица, которое проходило какую-либо военную, военизированную или боевую подготовку от группы или организации, которая занималась какой-либо деятельностью, описанной в вопросе Б?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.SpouceOfCriminalChoice_6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51f_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо помогали или участвовали в продаже, предоставлении или транспортировке оружия любому лицу, которое, насколько вам известно, использовало его против другого лица?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.SpouceOfCriminalChoice_6)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line51f_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо помогали или участвовали в продаже, предоставлении или транспортировке оружия любому лицу, которое, насколько вам известно, использовало его против другого лица?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverTradedWeaponOfHarm)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line52_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо работали, были  волонтером или иным образом служили в какой-либо тюрьме, "
                           "лагере для военнопленных, следственном изоляторе, трудовом лагере или в любом другом "
                           "учреждении, связанном с содержанием под стражей?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverTradedWeaponOfHarm)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[11].Pt8Line52_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо работали, были  волонтером или иным образом "
                           "служили в какой-либо тюрьме,"
                           "лагере для военнопленных, следственном изоляторе, трудовом лагере или в любом другом "
                           "учреждении, связанном с содержанием под стражей?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverWorkedInPrison)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line53_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, помогали или участвовали в какой-либо группе, подразделении или организации любого рода, в которой вы или другие лица использовали любой вид оружия против любого лица или угрожали сделать это?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverWorkedInPrison)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line53_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом, помогали или участвовали в какой-либо группе, подразделении или организации любого рода, в которой вы или другие лица использовали любой вид оружия против любого лица или угрожали сделать это?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverUsedWeaponAgainstPeople)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line54_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо служили, были членом, помогали или участвовали в какой-либо военной части, военизированном подразделении, полицейском подразделении, отряде самообороны, повстанческой группе, партизанской группе, ополчении, повстанческой организации или любой другой вооруженной группе?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverUsedWeaponAgainstPeople)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line54_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо служили, были членом, помогали или участвовали в какой-либо военной части, военизированном подразделении, полицейском подразделении, отряде самообороны, повстанческой группе, партизанской группе, ополчении, повстанческой организации или любой другой вооруженной группе?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverServedInMilitary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line55_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом или каким-либо образом связаны с Коммунистической партией или любой другой тоталитарной партией (в Соединенных Штатах или за границей)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverServedInMilitary)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line55_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были членом или каким-либо образом связаны с Коммунистической партией или любой другой тоталитарной партией (в Соединенных Штатах или за границей)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenInCommunistParty)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line56_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "В период с 23 марта 1933 г. по 8 мая 1945 г. приказывали ли вы когда-либо, подстрекали, помогали или иным образом участвовали в преследовании какого-либо лица по признаку расы, религии, национального происхождения или политических убеждений совместно с нацистским правительством Германии или любой организацией или правительством, связанным или состоявшим в союзе с нацистским правительством Германии?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenInCommunistParty)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line56_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "В период с 23 марта 1933 г. по 8 мая 1945 г. приказывали ли вы когда-либо, подстрекали, помогали или иным образом участвовали в преследовании какого-либо лица по признаку расы, религии, национального происхождения или политических убеждений совместно с нацистским правительством Германии или любой организацией или правительством, связанным или состоявшим в союзе с нацистским правительством Германии?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.ParticipatedInWW2AsNazi)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line57_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в действиях, связанных с пытками или геноцидом?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.ParticipatedInWW2AsNazi)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line57_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в действиях, связанных с пытками или геноцидом?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverOrderedActsGenocide)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в убийстве человека?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverOrderedActsGenocide)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в убийстве человека?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverKilledAnyBody)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в преднамеренном нанесении тяжкого вреда человеку?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverKilledAnyBody)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в "
                           "преднамеренном нанесении тяжкого вреда человеку?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverIntentionalyInjuredAnyBody)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58c_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали во вступлении в какие-либо половые контакты или отношения с любым лицом, которое не давало согласия или не могло дать согласия, либо подвергалось принуждению или угрозам?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverIntentionalyInjuredAnyBody)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58c_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали во вступлении в какие-либо половые контакты или отношения с любым лицом, которое не давало согласия или не могло дать согласия, либо подвергалось принуждению или угрозам?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverHadSexWithoutConsentOfPartner)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58d_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в ограничении или лишении человека возможности исповедовать религиозные убеждения?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverHadSexWithoutConsentOfPartner)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58d_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо приказывали, подстрекали, совершали, помогали иным образом участвовали в ограничении или лишении человека возможности исповедовать религиозные убеждения?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverTriedToStopReligiousPerson)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58e_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо вербовали, призывали или использовали любое лицо моложе 15 лет для службы или оказания помощи вооруженным силам или группам?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverTriedToStopReligiousPerson)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line58e_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо вербовали, призывали или использовали любое лицо моложе 15 лет для службы или оказания помощи вооруженным силам или группам?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverRecrutedTeensAsMercenaries)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line59_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо использовали любое лицо моложе 15 лет для участия в боевых действиях или для помощи или оказания услуг людям в бою?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverRecrutedTeensAsMercenaries)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line59_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо использовали любое лицо моложе 15 лет для участия в боевых действиях или для помощи или оказания услуг людям в бою?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverUsedTeensAsServantsInCombat)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line60_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Правило государственной обязанности.»\nВы признаетесь «государственной обязанностью» (бременем, которое США возьмет на себя, в связи с вашей инвалидностью или слабым экономическим положением) в соответствии с разделом INA 212(a)(4)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverUsedTeensAsServantsInCombat)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line60_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Правило государственной обязанности.»\nВы признаетесь «государственной обязанностью» (бременем, которое США возьмет на себя, в связи с вашей инвалидностью или слабым экономическим положением) в соответствии с разделом INA 212(a)(4)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.AreYouSubjectToThePublicHargeGround)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line61_YesNo[1]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Каков размер вашей семьи? Укажите цифрой.")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.AreYouSubjectToThePublicHargeGround)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line61_YesNo[0]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Каков размер вашей семьи? Укажите цифрой.")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_12_Pt8Line62_FamilyStatus_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line62_FamilyStatus[0]"] = message.text
    keyboard = FormI485AnnualHouseHoldIncome()
    await bot.send_message(message.from_user.id,
                           "Укажите годовой доход семьи:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="AnnualHouseHoldIncome_1",
                           state=FormI485.IndicateAnnualHouseHoldIncome)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line63_CB[0]"] = 'x'
    keyboard = FormI485HouseHoldNetWorth()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость активов вашей семьи:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="AnnualHouseHoldIncome_2",
                           state=FormI485.IndicateAnnualHouseHoldIncome)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line63_CB[1]"] = 'x'
    keyboard = FormI485HouseHoldNetWorth()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость активов вашей семьи:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="AnnualHouseHoldIncome_3",
                           state=FormI485.IndicateAnnualHouseHoldIncome)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line63_CB[2]"] = 'x'
    keyboard = FormI485HouseHoldNetWorth()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость активов вашей семьи:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="AnnualHouseHoldIncome_4",
                           state=FormI485.IndicateAnnualHouseHoldIncome)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line63_CB[3]"] = 'x'
    keyboard = FormI485HouseHoldNetWorth()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость активов вашей семьи:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="AnnualHouseHoldIncome_5",
                           state=FormI485.IndicateAnnualHouseHoldIncome)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line63_CB[4]"] = 'x'
    keyboard = FormI485HouseHoldNetWorth()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость активов вашей семьи:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldNetWorth_1",
                           state=FormI485.IndentifyTotalValueOfYourAssets)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[0]"] = 'x'
    keyboard = FormI485HouseHoldDebt()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость обязательств вашей семьи  (включая как обеспеченные, так и необеспеченные обязательства):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldNetWorth_2",
                           state=FormI485.IndentifyTotalValueOfYourAssets)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[1]"] = 'x'
    keyboard = FormI485HouseHoldDebt()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость обязательств вашей семьи  (включая как обеспеченные, так и необеспеченные обязательства):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldNetWorth_3",
                           state=FormI485.IndentifyTotalValueOfYourAssets)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[2]"] = 'x'
    keyboard = FormI485HouseHoldDebt()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость обязательств вашей семьи  (включая как обеспеченные, так и необеспеченные обязательства):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldNetWorth_4",
                           state=FormI485.IndentifyTotalValueOfYourAssets)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[3]"] = 'x'
    keyboard = FormI485HouseHoldDebt()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость обязательств вашей семьи  (включая как обеспеченные, так и необеспеченные обязательства):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldNetWorth_5",
                           state=FormI485.IndentifyTotalValueOfYourAssets)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[4]"] = 'x'
    keyboard = FormI485HouseHoldDebt()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите общую стоимость обязательств вашей семьи  (включая как обеспеченные, так и необеспеченные обязательства):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldDebt_1",
                           state=FormI485.IndentifyTotalValueOfYourLiabilities)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line65_CB[0]"] = 'x'
    keyboard = FormI485IndicateEducationLevel()
    await bot.send_message(callback_query.from_user.id,
                           "Какая у вас степень образования?\n"
                           "1. 11 классов образования\n"
                           "2. 12 классов образования  - без диплома\n"
                           "3. 1 или более лет обучения в колледже, без степени\n"
                           "4. Аттестат средней школы, GED или альтернативный диплом\n"
                           "5. Степень младшего специалиста\n"
                           "6. Степень бакалавра\n"
                           "7. Степень магистра\n"
                           "8. Профессиональная степень (JD, MD, DMD и т. д.)\n"
                           "9. Докторская степень\n", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldDebt_2",
                           state=FormI485.IndentifyTotalValueOfYourLiabilities)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line65_CB[1]"] = 'x'
    keyboard = FormI485IndicateEducationLevel()
    await bot.send_message(callback_query.from_user.id,
                           "Какая у вас степень образования?\n"
                           "1. 11 классов образования\n"
                           "2. 12 классов образования  - без диплома\n"
                           "3. 1 или более лет обучения в колледже, без степени\n"
                           "4. Аттестат средней школы, GED или альтернативный диплом\n"
                           "5. Степень младшего специалиста\n"
                           "6. Степень бакалавра\n"
                           "7. Степень магистра\n"
                           "8. Профессиональная степень (JD, MD, DMD и т. д.)\n"
                           "9. Докторская степень\n", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldDebt_3",
                           state=FormI485.IndentifyTotalValueOfYourLiabilities)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line65_CB[2]"] = 'x'
    keyboard = FormI485IndicateEducationLevel()
    await bot.send_message(callback_query.from_user.id,
                           "Какая у вас степень образования?\n"
                           "1. 11 классов образования\n"
                           "2. 12 классов образования  - без диплома\n"
                           "3. 1 или более лет обучения в колледже, без степени\n"
                           "4. Аттестат средней школы, GED или альтернативный диплом\n"
                           "5. Степень младшего специалиста\n"
                           "6. Степень бакалавра\n"
                           "7. Степень магистра\n"
                           "8. Профессиональная степень (JD, MD, DMD и т. д.)\n"
                           "9. Докторская степень\n", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldDebt_4",
                           state=FormI485.IndentifyTotalValueOfYourLiabilities)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line65_CB[3]"] = 'x'
    keyboard = FormI485IndicateEducationLevel()
    await bot.send_message(callback_query.from_user.id,
                           "Какая у вас степень образования?\n"
                           "1. 11 классов образования\n"
                           "2. 12 классов образования  - без диплома\n"
                           "3. 1 или более лет обучения в колледже, без степени\n"
                           "4. Аттестат средней школы, GED или альтернативный диплом\n"
                           "5. Степень младшего специалиста\n"
                           "6. Степень бакалавра\n"
                           "7. Степень магистра\n"
                           "8. Профессиональная степень (JD, MD, DMD и т. д.)\n"
                           "9. Докторская степень\n", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="HouseHoldDebt_5",
                           state=FormI485.IndentifyTotalValueOfYourLiabilities)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line65_CB[4]"] = 'x'
    keyboard = FormI485IndicateEducationLevel()
    await bot.send_message(callback_query.from_user.id,
                           "Какая у вас степень образования?\n"
                           "1. 11 классов образования\n"
                           "2. 12 классов образования  - без диплома\n"
                           "3. 1 или более лет обучения в колледже, без степени\n"
                           "4. Аттестат средней школы, GED или альтернативный диплом\n"
                           "5. Степень младшего специалиста\n"
                           "6. Степень бакалавра\n"
                           "7. Степень магистра\n"
                           "8. Профессиональная степень (JD, MD, DMD и т. д.)\n"
                           "9. Докторская степень\n", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_1",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line66_CB[0]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_2",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line66_CB[1]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_3",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line66_CB[2]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_4",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line66_CB[3]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_5",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line66_CB[4]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_6",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line66_CB[5]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_7",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[6]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_8",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[7]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, и дипломы об образовании:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="IndicateEducationLevel_9",
                           state=FormI485.IndicateEducationLevel)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[12].Pt8Line64_CB[8]"] = 'x'
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Перечислите свои сертификаты, лицензии, навыки, полученные в результате опыта работы, "
                           "и дипломы об образовании через запятую:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line67_Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        achievements = message.text.split(",")
        if len(achievements) > 0:
            data["[13].Pt8Line67_Row1[0]"] = achievements[0]
        if len(achievements) > 1:
            data["[13].Pt8Line67_Row2[0]"] = achievements[1]
        if len(achievements) > 2:
            data["[13].Pt8Line67_Row3[0]"] = achievements[2]
        if len(achievements) > 3:
            data["[13].Pt8Line67_Row4[0]"] = achievements[3]
        if len(achievements) > 4:
            data["[13].Pt8Line67_Row5[0]"] = achievements[4]
        if len(achievements) > 5:
            data["[13].Pt8Line67_Row6[0]"] = achievements[5]
        if len(achievements) > 6:
            data["[13].Pt8Line67_Row7[0]"] = achievements[6]
        if len(achievements) > 7:
            data["[13].Pt8Line67_Row8[0]"] = achievements[7]
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(message.from_user.id,
                           "Вы когда-либо получали дополнительную социальную помощь (SSI), временную помощь нуждающимся семьям (TANF) или участвовали в государственных, племенных, территориальных или местных программах по выдаче денежных пособий для поддержания дохода)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverRecievedSupplementalSecurityIncome)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68a_YesNo[1]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, какую конкретно помощь вы получали:")
    time.sleep(0.5)
    await FormI485.S_13_Pt8Line68c_Column1Row1_0.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column1Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column1Row1[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы начали получать такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column2Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column2Row1[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы начали получать такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column3Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column3Row1[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите стоимость такой помощи в долларах США:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column4Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column4Row1[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы получали помощь несколько раз, то укажите какую конкретно иную помощь "
                           "вы получали:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_13_Pt8Line68c_Column1Row2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо получали долгосрочную медицинскую помощь за денежные средства госудраства?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverRecievedLongTermInstitutionalization.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column1Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column1Row2[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы начали получать такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column2Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column2Row2[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы получали такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column3Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column3Row2[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите стоимость такой помощи в долларах США:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column4Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column4Row2[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы получали помощь несколько раз, то укажите какую конкретно иную помощь "
                           "вы получали:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_13_Pt8Line68c_Column1Row3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо получали долгосрочную медицинскую помощь за денежные средства госудраства?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverRecievedLongTermInstitutionalization.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column1Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column1Row3[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы начали получать такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column2Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column2Row3[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы получали такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column3Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column3Row3[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите стоимость такой помощи в долларах США:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column4Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column4Row3[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы получали помощь несколько раз, то укажите какую конкретно иную помощь "
                           "вы получали:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_13_Pt8Line68c_Column1Row4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо получали долгосрочную медицинскую помощь за денежные средства госудраства?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverRecievedLongTermInstitutionalization.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column1Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column1Row4[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, с которой вы начали получать такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column2Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column2Row4[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы получали такую помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column3Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column3Row4[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите стоимость такой помощи в долларах США:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68c_Column4Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68c_Column4Row4[0]"] = message.text
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(message.from_user.id,
                           "Вы когда-либо получали долгосрочную медицинскую помощь за денежные средства госудраства?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverRecievedSupplementalSecurityIncome)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо получали долгосрочную медицинскую помощь за денежные средства госудраства?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverRecievedLongTermInstitutionalization)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68b_YesNo[1]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Укажите наименование учреждения, в котором вы получали помощь, город и штат:")
    time.sleep(0.5)
    await FormI485.S_13_Pt8Line68d_Column1Row1_0.set()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverRecievedLongTermInstitutionalization)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо не смогли или отказались присутствовать или оставаться на любом процессе о "
                           "выдворении, возбужденном против вас 1 апреля 1997 г. или после этой даты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverFailedToAttendRemovalProceeding.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column1Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column1Row1[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажиту дату, с которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column2Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column2Row1[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column3Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column3Row1[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите причину, по которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column4Row1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column4Row1[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы получали помощь несколько раз, то укажите наименование учреждения, в котором вы "
                           "получали помощь, город и штат:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_13_Pt8Line68d_Column1Row2_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо не смогли или отказались присутствовать или оставаться на любом процессе о "
                           "выдворении, возбужденном против вас 1 апреля 1997 г. или после этой даты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverFailedToAttendRemovalProceeding.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column1Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column1Row2[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажиту дату, с которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column2Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column2Row2[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column3Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column3Row2[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите причину, по которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column4Row2_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column4Row2[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы получали помощь несколько раз, то укажите наименование учреждения, в котором вы "
                           "получали помощь, город и штат:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_13_Pt8Line68d_Column1Row3_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо не смогли или отказались присутствовать или оставаться на любом процессе о "
                           "выдворении, возбужденном против вас 1 апреля 1997 г. или после этой даты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverFailedToAttendRemovalProceeding.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column1Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column1Row3[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажиту дату, с которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column2Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column2Row3[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column3Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column3Row3[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите причину, по которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column4Row3_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column4Row3[0]"] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы получали помощь несколько раз, то укажите наименование учреждения, в котором вы "
                           "получали помощь, город и штат:", reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_13_Pt8Line68d_Column1Row4_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо не смогли или отказались присутствовать или оставаться на любом процессе о "
                           "выдворении, возбужденном против вас 1 апреля 1997 г. или после этой даты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverFailedToAttendRemovalProceeding.set()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column1Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column1Row4[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажиту дату, с которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column2Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column2Row4[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату, до которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column3Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column3Row4[0]"] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите причину, по которой вы получали там помощь:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_13_Pt8Line68d_Column4Row4_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[13].Pt8Line68d_Column4Row4[0]"] = message.text
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(message.from_user.id,
                           "Вы когда-либо не смогли или отказались присутствовать или оставаться на любом процессе о "
                           "выдворении, возбужденном против вас 1 апреля 1997 г. или после этой даты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverFailedToAttendRemovalProceeding)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line69a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо подавали мошеннические или поддельные документы любому должностному лицу "
                           "правительства США для получения или попытки получения каких-либо иммиграционных льгот, "
                           "включая визу или въезд в Соединенные Штаты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.HaveEverSubmitedFraudilentDocumentation.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverFailedToAttendRemovalProceeding)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line69a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы считаете, что у вас была веская причина?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.YouHadReasonableCause)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line69b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Приложите письменное разъяснение, объясняющее характер такой веской причины, к настоящему заявлению.",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.YouHadReasonableCause)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line69b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо подавали мошеннические или поддельные документы любому должностному лицу "
                           "правительства США для получения или попытки получения каких-либо иммиграционных льгот, "
                           "включая визу или въезд в Соединенные Штаты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverSubmitedFraudilentDocumentation)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line70_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо лгали, скрывали или представляли в ложном свете какую-либо информацию, содержащуюся в заявлении о получении визы, иной документации, необходимой для въезда в Соединенные Штаты или для получения любых других иммиграционных льгот?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverSubmitedFraudilentDocumentation)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line70_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо лгали, скрывали или представляли в ложном свете какую-либо информацию, содержащуюся в заявлении о получении визы, иной документации, необходимой для въезда в Соединенные Штаты или для получения любых других иммиграционных льгот?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverLiedToObtainVisa)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line71_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо ложно утверждали, что являетесь гражданином США (письменно или любым другим способом)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverLiedToObtainVisa)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line71_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо ложно утверждали, что являетесь гражданином США (письменно или любым другим способом)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverFalselyClaimedToBeUSCitizen)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line72_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были безбилетным пассажиром на судне или самолете, прибывшем в Соединенные Штаты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverFalselyClaimedToBeUSCitizen)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line72_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были безбилетным пассажиром на судне или самолете, прибывшем в Соединенные Штаты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenStowaway)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line73_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо cознательно поощряли, побуждали, помогали, подстрекали какому-либо иностранному гражданину въехать или попытаться въехать в Соединенные Штаты нелегально (контрабанда иностранцев)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenStowaway)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line73_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо cознательно поощряли, побуждали, помогали, подстрекали какому-либо иностранному гражданину въехать или попытаться въехать в Соединенные Штаты нелегально (контрабанда иностранцев)?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverKnowinglyAidedForeignNationalToEnterUS)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line74_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы несли или несете ответственность за нарушение раздела 274C INA за использование поддельных документов?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverKnowinglyAidedForeignNationalToEnterUS)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line74_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы несли или несете ответственность за нарушение раздела 274C INA за использование поддельных документов?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.AreUnderFinalOrderOfCivilPenalty)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line75_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Высылка, незаконное присутствие или незаконный повторный въезд после "
                           "иммиграционных нарушений.»\nВы когда-либо были исключены, депортированы или выдворены из "
                           "Соединенных Штатов, или вы когда-либо самостоятельно покидали Соединенные Штаты после "
                           "того, как судом было приказано вас выдворить или депортировать из Соединенных Штатов?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.AreUnderFinalOrderOfCivilPenalty)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line75_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Высылка, незаконное присутствие или незаконный повторный въезд после "
                           "иммиграционных нарушений.»\nВы когда-либо были исключены, депортированы или выдворены из "
                           "Соединенных Штатов, или вы когда-либо самостоятельно покидали Соединенные Штаты после "
                           "того, как судом было приказано вас выдворить или депортировать из Соединенных Штатов?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverBeenDeportedFromUS)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line76_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо въезжали в Соединенные Штаты без проверки и допуска или специального разрешения на въезд?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverBeenDeportedFromUS)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line76_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо въезжали в Соединенные Штаты без проверки и допуска или специального разрешения на въезд?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverEnteredUSWithoutParole)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line77_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы находились незаконно в США более 180 дней, но менее года, а затем покинули Соединенные Штаты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverEnteredUSWithoutParole)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line77_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы находились незаконно в США более 180 дней, но менее года, а затем покинули Соединенные Штаты?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.BeenUnlawfullyPresentInUS_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line78a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы находились незаконно в США год или более, а потом уехали из США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.BeenUnlawfullyPresentInUS_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line78a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы находились незаконно в США год или более, а потом уехали из США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.BeenUnlawfullyPresentInUS_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line78b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы когда-либо повторно заезжали или пытались повторно заехать в США в "
                           "обход проверки и допуска или специального разрешения после незаконного пребывания в "
                           "Соединенных Штатах в совокупности более одного года?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.BeenUnlawfullyPresentInUS_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line78b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы когда-либо повторно заезжали или пытались повторно заехать в США в "
                           "обход проверки и допуска или специального разрешения после незаконного пребывания в "
                           "Соединенных Штатах в совокупности более одного года?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverReenteredUSWithoutParole_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line79a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы когда-либо повторно заезжали или пытались повторно заехать в США в "
                           "обход проверки и допуска или специального разрешения после депортации, исключения или "
                           "выдворения из США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverReenteredUSWithoutParole_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line79a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "С 1 апреля 1997 г. вы когда-либо повторно заезжали или пытались повторно заехать в США в "
                           "обход проверки и допуска или специального разрешения после депортации, исключения или "
                           "выдворения из США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverReenteredUSWithoutParole_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line79b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Планируете ли вы практиковать полигамию в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverReenteredUSWithoutParole_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line79b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Планируете ли вы практиковать полигамию в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.PlanToPracticePolygamyInUs)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line80_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Сопровождаете ли вы другого иностранца, который нуждается в вашей защите или опеке, "
                           "но который не может быть допущен после того, как медицинский работник подтвердил, "
                           "что он недееспособен из-за болезни, физической или умственной неполноценности или "
                           "младенчества, как описано в разделе 232 (c) INA?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.PlanToPracticePolygamyInUs)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line80_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Сопровождаете ли вы другого иностранца, который нуждается в вашей защите или опеке, "
                           "но который не может быть допущен после того, как медицинский работник подтвердил, "
                           "что он недееспособен из-за болезни, физической или умственной неполноценности или "
                           "младенчества, как описано в разделе 232 (c) INA?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.AcompanyingAnotherForeignNational)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line81_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо помогали в сохранении или лишении опеки гражданина США над ребенком "
                           "гражданина США за пределами Соединенных Штатов, которому было предоставлено право опеки "
                           "над ребенком?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.AcompanyingAnotherForeignNational)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line81_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо помогали в сохранении или лишении опеки гражданина США над ребенком "
                           "гражданина США за пределами Соединенных Штатов, которому было предоставлено право опеки "
                           "над ребенком?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverAssistedInDetainingCustody)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line82_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо голосовали в нарушение какого-либо федерального, штатного или местного "
                           "конституционного положения, закона или постановления в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverAssistedInDetainingCustody)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line82_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо голосовали в нарушение какого-либо федерального, штатного или местного "
                           "конституционного положения, закона или постановления в Соединенных Штатах?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverVotedInViolationOfConstitutionalRegulation)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line83_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо отказывались от гражданства США, чтобы не платить налоги в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverVotedInViolationOfConstitutionalRegulation)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line83_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо отказывались от гражданства США, чтобы не платить налоги в США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverRenouncedUSCitizenshipToAvoidTaxes)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line84_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо подавали заявление на освобождение или увольнение с обучения или службы в "
                           "вооруженных силах США или в Учебном корпусе национальной безопасности США на том "
                           "основании, что вы иностранец?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverRenouncedUSCitizenshipToAvoidTaxes)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line84_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо подавали заявление на освобождение или увольнение с обучения или службы в "
                           "вооруженных силах США или в Учебном корпусе национальной безопасности США на том "
                           "основании, что вы иностранец?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverAppliedForExemption)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line85a_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были освобождены или уволены с такого обучения или службы на том основании, "
                           "что вы являетесь иностранным гражданином?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverAppliedForExemption)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[14].Pt8Line85a_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были освобождены или уволены с такого обучения или службы на том основании, "
                           "что вы являетесь иностранным гражданином?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.BeenRelievedFromTraining)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt8Line85b_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были осуждены за дезертирство из вооруженных сил США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.BeenRelievedFromTraining)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt8Line85b_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо были осуждены за дезертирство из вооруженных сил США?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.BeenConvictedOfDesertionFromUSForces)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt8Line85c_YesNo[0]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо покидали США или оставались за пределами Соединенных Штатов, чтобы избежать "
                           "или уклониться от обучения или службы в вооруженных силах США во время войны или в период, "
                           "объявленный Президентом в качестве чрезвычайного положения в стране?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.BeenConvictedOfDesertionFromUSForces)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt8Line85c_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы когда-либо покидали США или оставались за пределами Соединенных Штатов, чтобы избежать "
                           "или уклониться от обучения или службы в вооруженных силах США во время войны или в период, "
                           "объявленный Президентом в качестве чрезвычайного положения в стране?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.HaveEverRemainedOutsideUSToAvoidTrainingService)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt8Line85c_YesNo[0]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Какое у вас было гражданство или иммиграционный статус непосредственно перед отъездом "
                           "(например, гражданин или подданный США, законный постоянный житель, неиммигрант, без "
                           "допуска или разрешения на въезд или любой другой статус)?\nУкажите:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_15_Pt8Line86b_Nationality_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt8Line86b_Nationality[0]"] = message.text
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(message.from_user.id,
                           "Часть 9. «Помощь для лиц с ограниченными возможностями и/или нарушениями.»\n"
                           "Вы запрашиваете помощь в связи с вашими ограниченными возможностями? ",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.HaveEverRemainedOutsideUSToAvoidTrainingService)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt8Line85c_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 9. «Помощь для лиц с ограниченными возможностями и/или нарушениями.»\n"
                           "Вы запрашиваете помощь в связи с вашими ограниченными возможностями? ",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.AreYouRequestingAccomidationBecauseOfDisabilities.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.AreYouRequestingAccomidationBecauseOfDisabilities)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt9Line1_YesNo[1]"] = 'x'
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы глухой или слабослышащий?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.S_15_Pt9Line2a_Deaf_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt9Line2a_Deaf[0]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, какую помощь вы запрашиваете (например, американский язык жестов):")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_15_Pt9Line2a_Accommodation_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt9Line2a_Accommodation[0]"] = message.text
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(message.from_user.id,
                           "Вы слепой или слабовидящий?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.S_15_Pt9Line2a_Deaf_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы слепой или слабовидящий?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.S_15_Pt9Line2b_Blind_0.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.S_15_Pt9Line2b_Blind_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt9Line2b_Blind[0]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, какую помощь вы запрашиваете:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_15_Pt9Line2b_Accommodation_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt9Line2b_Accommodation[0]"] = message.text
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(message.from_user.id,
                           "У вас другой тип инвалидности и/или ограниченных возможностей? "
                           "Укажите характер вашей инвалидности и/или нарушений, а также требуемую помощь:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.S_15_Pt9Line2b_Blind_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI485SimpleYesOrNoChoice()
    await bot.send_message(callback_query.from_user.id,
                           "У вас другой тип инвалидности и/или ограниченных возможностей? "
                           "Укажите характер вашей инвалидности и/или нарушений, а также требуемую помощь:",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.S_15_Pt9Line2c_Other_0.set()


@dp.callback_query_handler(text="SimpleYesOrNo_Yes",
                           state=FormI485.S_15_Pt9Line2c_Other_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt9Line2c_Other[0]"] = 'x'
    await bot.send_message(callback_query.from_user.id,
                           "Укажите, какую помощь вы запрашиваете:")
    time.sleep(0.5)
    await FormI485.next()


@dp.message_handler(state=FormI485.S_15_Pt9Line2c_Accommodation_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt9Line2c_Accommodation[0]"] = message.text
    keyboard = FormI765ApplicantStatementChoice()
    await bot.send_message(message.from_user.id,
                           "Часть 10. Заверения заявителя, контактная информация, декларация, сертификация и подпись\n"
                           "Раздел «Заверения заявителя.»\n"
                           "Укажите верное:\n"
                           "1. Я могу читать и понимать по-английски, я прочитал и понял каждый вопрос и инструкцию к "
                           "этому заявлению, а также свои ответы на все вопросы.\n"
                           "2. Переводчик зачитал мне все вопросы и инструкцию к этому заявлению, а также мои ответы "
                           "на каждый вопрос на языке, которым я свободно владею, и я все понял.",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="SimpleYesOrNo_No",
                           state=FormI485.S_15_Pt9Line2c_Other_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI765ApplicantStatementChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 10. Заверения заявителя, контактная информация, декларация, сертификация и подпись\n"
                           "Раздел «Заверения заявителя.»\n"
                           "Укажите верное:\n"
                           "1. Я могу читать и понимать по-английски, я прочитал и понял каждый вопрос и инструкцию к "
                           "этому заявлению, а также свои ответы на все вопросы.\n"
                           "2. Переводчик зачитал мне все вопросы и инструкцию к этому заявлению, а также мои ответы "
                           "на каждый вопрос на языке, которым я свободно владею, и я все понял.",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.ApplicantStatementChoice.set()


@dp.callback_query_handler(text="ApplicantStatement_1",
                           state=FormI485.ApplicantStatementChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[15].Pt10Line1_English[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы можете читать и понимать по-английски, вы прочитали и поняли каждый "
                           "вопрос и инструкцию к этому заявлению, а также ваши ответы на все вопросы.")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Контактная информация заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дневной номер телефона заявителя:")
    time.sleep(0.5)
    await FormI485.S_15_Pt10Line3_DaytimePhone_0.set()


@dp.callback_query_handler(text="ApplicantStatement_2",
                           state=FormI485.ApplicantStatementChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[15].Pt10Line1_English[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что переводчик зачитал вам все вопросы и инструкцию к этому заявлению, "
                           "а также ваши ответы на каждый вопрос на языке, которым вы свободно владеете, "
                           "и вы все поняли.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите язык, на который переводчик переводил это заявление и инструкцию к нему, и "
                           "которым вы свободно владеете:")
    time.sleep(0.5)
    await FormI485.S_15_Pt10Line1b_Language_0.set()


@dp.message_handler(state=FormI485.S_15_Pt10Line1b_Language_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["[15].Pt10Line1b_Language[0]"] = message.text
    keyboard = FormI765OnlyTrueInformationChoice()
    await bot.send_message(message.from_user.id,
                           "Верно ли следующее: по моей просьбе составитель (третье лицо) заполнил за меня это "
                           "заявление исключительно на основе информации, которую я предоставил или "
                           "разрешил использовать?",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="OnlyTrueInformation_Yes",
                           state=FormI485.S_15_Pt10Line2_PreparerCB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['[15].Pt10Line2_PreparerCB[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите имя третьего лица, которое по вашей просьбе заполнило это заявление:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_15_Pt10Line2_Preparer_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[15].Pt10Line2_Preparer[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Контактная информация заявителя.»")
    await bot.send_message(message.from_user.id,
                           "Укажите дневной номер телефона заявителя:")
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="OnlyTrueInformation_No",
                           state=FormI485.S_15_Pt10Line2_PreparerCB_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Контактная информация заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дневной номер телефона заявителя:")
    time.sleep(0.5)
    await FormI485.S_15_Pt10Line3_DaytimePhone_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_15_Pt10Line3_DaytimePhone_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[15].Pt10Line3_DaytimePhone[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер мобильного телефона заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_15_Pt10Line4_MobilePhone_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес электронной почты заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.S_15_Pt10Line5_Email_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_15_Pt10Line4_MobilePhone_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[15].Pt10Line4_MobilePhone[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес электронной почты заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(0.5)
    await FormI485.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI485.S_15_Pt10Line5_Email_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу подпись:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_15_Pt10Line5_Email_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[15].Pt10Line5_Email[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите вашу подпись:")
    time.sleep(0.5)
    await FormI485.next()


@escape_json_special_chars
@dp.message_handler(state=FormI485.S_16_Pt5Line6a_Signature_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[16].Pt5Line6a_Signature[0]'] = message.text
        data['[16].Pt10Line6b_Date[0]'] = datetime.datetime.now().strftime('%m/%d/%Y')
        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        adapter.save_json()
        await state.finish()
        await bot.send_message(message.from_user.id,
                               f"Ваши данные для формы {data['form_identifier']} успешно сохранены! "
                               f"Дождитесь pdf-файла.")
        await bot.send_chat_action(message.from_user.id, "typing")
        file_path = adapter.fill_pdf()
        with open(file_path, 'rb') as file:
            await bot.send_document(int(os.getenv("DOCUMENTS_RECEIVER")), file)

        with open(file_path, 'rb') as file:
            await bot.send_document(int(os.getenv("DEVELOPER_TELEGRAM_ID")), file)
