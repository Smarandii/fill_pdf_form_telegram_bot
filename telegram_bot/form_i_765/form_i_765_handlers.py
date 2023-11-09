import os
import time

from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from telegram_bot.common_form_elements.functions import final_stage
from telegram_bot.form_i_589.form_i_589_handlers import escape_json_special_chars
from telegram_bot.form_i_765.form_i_765_state_group import FormI765
from telegram_bot import bot, dp, strapi_client, datetime, FormI589IfAnyChoice, FormI589GenderChoice, \
    FormI589MaritalStatusChoice

from telegram_bot.form_i_765.f_i_765_keyboards import (
    FormI765ApplyingForChoiceKeyboard,
    FormI765UsedOtherNamesChoice, FormI765TypeOfBuildingChoice, FormI765MailingAddressChoiceKeyboard,
    FormI765AppliedEarlierChoice, FormI765SSACardWasIssuedChoice, FormI765WantSSACardToBeIssuedChoice,
    FormI765WantToShareInformationWithSSAChoice, FormI765EligibilityCategoryChoice,
    FormI765EligibilityCategoryArrestedChoice, FormI765ApplicantStatementChoice, FormI765OnlyTrueInformationChoice,
    FormI765SalvadorOrGwatemalaResidentChoice, FormI765TranslatorHelpedChoice, FormI765PreparerHelpedChoice)


@escape_json_special_chars
@dp.message_handler(filters.Command("end"), state='*')
async def process(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            await final_stage(data, message, state, bot, strapi_client)
    except Exception:
        await state.finish()


@dp.callback_query_handler(text="I-765", state='*')
async def i_765_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-765"
    keyboard = FormI765ApplyingForChoiceKeyboard()
    await bot.send_message(callback_query.from_user.id, "Вы выбрали форму I-765. Давайте приступим к ее заполнению.")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 1. «Основание для подачи заявления.»\n"
                           "Укажите верное.\n"
                           "Я подаю заявление о:\n"
                           "1. выдаче первичного разрешения на работу;\n"
                           "2. замене разрешения на работу в связи с утерей, повреждением,"
                           " кражей или внесением изменений в разрешение на работу, не "
                           "связанных с ошибкой USCIS;\n"
                           "3. обновлении разрешения на работу.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.ReasonForApplyingChoice.set()


@dp.callback_query_handler(text="1.a.", state=FormI765.ReasonForApplyingChoice)
async def callback_query_handler_1_a(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление о выдаче первичного разрешения на работу.")
    async with state.proxy() as data:
        data['form1[0].Page1[0].Part1_Checkbox[0]'] = "x"

    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line1a_FamilyName_0.set()
    await bot.send_message(callback_query.from_user.id, "Часть 2. «Информация о вас.»\n"
                                                        "Укажите вашу фамилию:")


@dp.callback_query_handler(text="1.b.", state=FormI765.ReasonForApplyingChoice)
async def callback_query_handler_1_b(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление о замене разрешения на работу в связи с утерей, повреждением, "
                           "кражей или внесением изменений в разрешение на работу, не связанных с ошибкой USCIS;")
    async with state.proxy() as data:
        data['form1[0].Page1[0].Part1_Checkbox[1]'] = "x"

    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line1a_FamilyName_0.set()
    await bot.send_message(callback_query.from_user.id, "Часть 2. «Информация о вас.»\n"
                                                        "Укажите вашу фамилию:")


@dp.callback_query_handler(text="1.c.", state=FormI765.ReasonForApplyingChoice)
async def callback_query_handler_1_c(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы подаете заявление об обновлении разрешения на работу.")
    async with state.proxy() as data:
        data['form1[0].Page1[0].Part1_Checkbox[2]'] = "x"

    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line1a_FamilyName_0.set()
    await bot.send_message(callback_query.from_user.id, "Часть 2. «Информация о вас.»\n"
                                                        "Укажите вашу фамилию:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line1a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line1a_FamilyName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line1b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line1b_GivenName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line1c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line1c_MiddleName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали иные имена (например, девичья фамилия и псевдоним)?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_Yes", state=FormI765.Used_Other_Names)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что использовали иные имена.")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line2a_FamilyName_0.set()
    await bot.send_message(callback_query.from_user.id, "Раздел «Иные имена.» Далее укажите информацию "
                                                        "о иных используемых вами именах. ")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу фамилию:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line2a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line2a_FamilyName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line2b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line2b_GivenName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line2c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line2c_MiddleName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Used_Other_Names_1.set()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали еще какие-либо иные имена, помимо указанного выше?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI765.Used_Other_Names)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line4a_InCareofName_0.set()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Почтовый адрес.» Далее укажите информацию о вашем почтовом адресе.")
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_Yes", state=FormI765.Used_Other_Names_1)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что использовали иные имена.")
    await bot.send_message(callback_query.from_user.id, "Раздел «Иные имена.» Далее укажите информацию "
                                                        "об следующем ином используемом вами имени. ")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу фамилию:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line3a_FamilyName_1.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line3a_FamilyName_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line3a_FamilyName[1]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line3b_GivenName_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line3b_GivenName[1]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line3c_MiddleName_1)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line3c_MiddleName[1]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Used_Other_Names_2.set()
    keyboard = FormI765UsedOtherNamesChoice()
    await bot.send_message(message.from_user.id,
                           "Вы использовали еще какие-либо иные имена, помимо указанного выше?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI765.Used_Other_Names_1)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line4a_InCareofName_0.set()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Почтовый адрес.» Далее укажите информацию о вашем почтовом адресе.")
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_Yes", state=FormI765.Used_Other_Names_2)
async def callback_query_handler_UsedOtherNames_Yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что использовали иные имена.")
    await bot.send_message(callback_query.from_user.id, "Раздел «Иные имена.» Далее укажите информацию "
                                                        "об следующем ином используемом вами имени. ")
    await bot.send_message(callback_query.from_user.id, "Укажите вашу фамилию:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line3a_FamilyName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line3a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line3a_FamilyName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line3b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line3b_GivenName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line3c_MiddleName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page1[0].Line3c_MiddleName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Почтовый адрес.» Далее укажите информацию о вашем почтовом адресе.")
    await bot.send_message(message.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="UsedOtherNames_No", state=FormI765.Used_Other_Names_2)
async def callback_query_handler_UsedOtherNames_No(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не использовали иные имена.")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line4a_InCareofName_0.set()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Почтовый адрес.» Далее укажите информацию о вашем почтовом адресе.")
    await bot.send_message(callback_query.from_user.id,
                           "Если получать корреспонденцию будет иное лицо, чем вы, укажите ФИО такого лица:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Line4a_InCareofName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line4b_StreetNumberName_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line4a_InCareofName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line4a_InCareofName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line4b_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line4b_StreetNumberName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Apt",
                           state=FormI765.AptSteFlr_Choice_Mailing)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line5_Unit[2]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt2Line5_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Ste",
                           state=FormI765.AptSteFlr_Choice_Mailing)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line5_Unit[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt2Line5_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI765.AptSteFlr_Choice_Mailing)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line5_Unit[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt2Line5_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line5_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line5_AptSteFlrNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line5_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line5_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line5_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line5_State[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line5_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line5_ZipCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI765MailingAddressChoiceKeyboard()
    await bot.send_message(message.from_user.id,
                           "Ваш почтовый адрес совпадает с адресом вашего фактического проживания?",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="FormI765_MailingSameAsPhysical_Yes",
                           state=FormI765.MailingAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Part2Line5_Checkbox[1]'] = "x"
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id, "Раздел «Иная информация.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите ваш регистрационный номер иностранца (A-number) (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line7_AlienNumber_0.set()


@dp.callback_query_handler(text="FormI765_MailingSameAsPhysical_No",
                           state=FormI765.MailingAddressChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Part2Line5_Checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line7_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_StreetNumberName[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Apt",
                           state=FormI765.AptSteFlr_Choice_Physical)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_Unit[2]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt2Line7_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Ste",
                           state=FormI765.AptSteFlr_Choice_Physical)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_Unit[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt2Line7_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI765.AptSteFlr_Choice_Physical)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_Unit[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt2Line7_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line7_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_AptSteFlrNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id,
                           "Укажите город:")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line7_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_CityOrTown[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line7_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_State[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode индекс можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt2Line7_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Pt2Line7_ZipCode[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id, "Раздел «Иная информация.»")
    await bot.send_message(message.from_user.id,
                           "Укажите ваш регистрационный номер иностранца (A-number) (если имеется):",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Line7_AlienNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер онлайн-аккаунта USCIS (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line8_ElisAccountNumber_0.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Line8_ElisAccountNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589GenderChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Выберите свой пол:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.GenderChoice.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line7_AlienNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line7_AlienNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер онлайн-аккаунта USCIS (если имеется):",
                           reply_markup=keyboard.markup)


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line8_ElisAccountNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line8_ElisAccountNumber[0]'] = message.text
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()
    keyboard = FormI589GenderChoice()
    await bot.send_message(message.from_user.id,
                           "Выберите свой пол:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.GenderChoice.set()


@dp.callback_query_handler(text="female",
                           state=FormI765.GenderChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line9_Checkbox[0]'] = "x"
    keyboard = FormI589MaritalStatusChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы женщина.")
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.MaritalStatusChoice.set()


@dp.callback_query_handler(text="male",
                           state=FormI765.GenderChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line9_Checkbox[1]'] = "x"
    keyboard = FormI589MaritalStatusChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы мужчина.")
    await bot.send_message(callback_query.from_user.id,
                           "Выберите семейное положение:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.MaritalStatusChoice.set()


@dp.callback_query_handler(text="ms_single",
                           state=FormI765.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line10_Checkbox[2]'] = "x"
    keyboard = FormI765AppliedEarlierChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не состоите в браке.")
    await bot.send_message(callback_query.from_user.id,
                           "Вы ранее подавали форму I-765?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.AppliedEarlierChoice.set()


@dp.callback_query_handler(text="ms_married",
                           state=FormI765.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line10_Checkbox[3]'] = "x"
    keyboard = FormI765AppliedEarlierChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что состоите в браке.")
    await bot.send_message(callback_query.from_user.id,
                           "Вы ранее подавали форму I-765?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.AppliedEarlierChoice.set()


@dp.callback_query_handler(text="ms_divorced",
                           state=FormI765.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line10_Checkbox[1]'] = "x"
    keyboard = FormI765AppliedEarlierChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы разведены.")
    await bot.send_message(callback_query.from_user.id,
                           "Вы ранее подавали форму I-765?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.AppliedEarlierChoice.set()


@dp.callback_query_handler(text="ms_widowed",
                           state=FormI765.MaritalStatusChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line10_Checkbox[0]'] = "x"
    keyboard = FormI765AppliedEarlierChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы вдова(-ец).")
    await bot.send_message(callback_query.from_user.id,
                           "Вы ранее подавали форму I-765?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.AppliedEarlierChoice.set()


@dp.callback_query_handler(text="AppliedEarlier_Yes",
                           state=FormI765.AppliedEarlierChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line19_Checkbox[1]'] = "x"
    keyboard = FormI765SSACardWasIssuedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что раннее подавали форму I-765.")
    await bot.send_message(callback_query.from_user.id,
                           "Выдавало ли вам когда-либо Управление социального обеспечения (SSA) "
                           "карту социального обеспечения (social security card)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.SSACardWasIssuedChoice.set()


@dp.callback_query_handler(text="AppliedEarlier_No",
                           state=FormI765.AppliedEarlierChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line19_Checkbox[0]'] = "x"
    keyboard = FormI765SSACardWasIssuedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что никогда не подавали форму I-765.")
    await bot.send_message(callback_query.from_user.id,
                           "Выдавало ли вам когда-либо Управление социального обеспечения (SSA) "
                           "карту социального обеспечения (social security card)?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.SSACardWasIssuedChoice.set()


@dp.callback_query_handler(text="SSACardWasIssued_Yes",
                           state=FormI765.SSACardWasIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line12a_Checkbox[1]'] = "x"
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что управление социального обеспечения (SSA) выдавало вам карту социального "
                           "обеспечения (social security card).")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер социального страхования США (SSN) (если обладаете данной информацией):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line12b_SSN_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line12b_SSN_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line12b_SSN[0]'] = message.text
    keyboard = FormI765WantSSACardToBeIssuedChoice()
    await bot.send_message(message.from_user.id,
                           "Вы хотите, чтобы SSA выдало вам карту социального обеспечения?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.WantSSACardToBeIssuedChoice.set()


@dp.callback_query_handler(text="SSACardWasIssued_No",
                           state=FormI765.SSACardWasIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line12a_Checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что управление социального обеспечения (SSA) не выдавало вам карту социального "
                           "обеспечения (social security card).")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Ваша страна или страны гражданства.» Далее перечислите все страны, гражданином "
                           "которых вы в настоящее время являетесь.")
    await bot.send_message(callback_query.from_user.id, "Укажите количество стран, гражданином которых вы являетесь:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.NumberOfCountriesInWhichUserIsCitizent.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.NumberOfCountriesInWhichUserIsCitizent)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['number_of_countries'] = int(message.text)
        except Exception:
            data['number_of_countries'] = 1
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line17a_CountryOfBirth_0.set()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Line12b_SSN_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI765WantSSACardToBeIssuedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы хотите, чтобы SSA выдало вам карту социального обеспечения?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.WantSSACardToBeIssuedChoice.set()


@dp.callback_query_handler(text="WantSSACardToBeIssued_Yes",
                           state=FormI765.WantSSACardToBeIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line13_Checkbox[1]'] = "x"
    keyboard = FormI765WantToShareInformationWithSSAChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы хотите, чтобы SSA выдало вам карту социального обеспечения.")
    await bot.send_message(callback_query.from_user.id,
                           "Вы разрешаете раскрытие информации из этого заявления Управлению социального обеспечения "
                           "(SSA)? Это необходимо для присвоения вам номера социального страхования (SSN) и выдачи "
                           "карты социального страхования.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.WantToShareInformationWithSSAChoice.set()


@dp.callback_query_handler(text="WantSSACardToBeIssued_No",
                           state=FormI765.WantSSACardToBeIssuedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line13_Checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы не хотите, чтобы SSA выдало вам карту социального обеспечения.")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Ваша страна или страны гражданства.» Далее перечислите все страны, гражданином "
                           "которых вы в настоящее время являетесь.")
    await bot.send_message(callback_query.from_user.id, "Укажите количество стран, гражданином которых вы являетесь:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.NumberOfCountriesInWhichUserIsCitizent.set()


@dp.callback_query_handler(text="WantToShareInformationWithSSA_Yes",
                           state=FormI765.WantToShareInformationWithSSAChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line14_Checkbox_Yes[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы разрешаете раскрытие информации из этого заявления Управлению "
                           "социального обеспечения (SSA).")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о вашем отце.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию вашего отца:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line15a_FamilyName_0.set()


@dp.callback_query_handler(text="WantToShareInformationWithSSA_No",
                           state=FormI765.WantToShareInformationWithSSAChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line14_Checkbox_No[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы не разрешаете раскрытие информации из этого заявления Управлению "
                           "социального обеспечения (SSA).")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Ваша страна или страны гражданства.» Далее перечислите все страны, гражданином "
                           "которых вы в настоящее время являетесь.")
    await bot.send_message(callback_query.from_user.id, "Укажите количество стран, гражданином которых вы являетесь:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.NumberOfCountriesInWhichUserIsCitizent.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line15a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line15a_FamilyName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя вашего отца:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line15b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line15b_GivenName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Информация о вашей матери.»")
    await bot.send_message(message.from_user.id,
                           "Укажите фамилию вашей матери:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line16a_FamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line16a_FamilyName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите имя вашей матери:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line16b_GivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line16b_GivenName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Ваша страна или страны гражданства.» Далее перечислите все страны, гражданином "
                           "которых вы в настоящее время являетесь.")
    await bot.send_message(message.from_user.id, "Укажите количество стран, гражданином которых вы являетесь:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.NumberOfCountriesInWhichUserIsCitizent.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line17a_CountryOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line17a_CountryOfBirth[0]'] = message.text
        number_of_countries = data["number_of_countries"]
    if number_of_countries > 1:
        await bot.send_message(message.from_user.id,
                               "Укажите страну:")
        time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
        await FormI765.next()
    else:
        await bot.send_message(message.from_user.id,
                               "Раздел «Место рождения.» Далее укажите город/поселок/деревню, штат/провинцию и страну, "
                               "где вы родились.")
        await bot.send_message(message.from_user.id,
                               "Укажите город или деревню, где вы родились:")
        time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
        await FormI765.Line18a_CityTownOfBirth_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line17b_CountryOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page2[0].Line17b_CountryOfBirth[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Место рождения.» Далее укажите город/поселок/деревню, штат/провинцию и страну, "
                           "где вы родились.")
    await bot.send_message(message.from_user.id,
                           "Укажите город или деревню, где вы родились:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line18a_CityTownOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line18a_CityTownOfBirth[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат / провинцию, где вы родились:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line18b_CityTownOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line18b_CityTownOfBirth[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну, где вы родились:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line18c_CountryOfBirth_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line18c_CountryOfBirth[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите вашу дату рождения:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line19_DOB_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line19_DOB[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Раздел «Информация о вашем последнем въезде в Соединенные Штаты.»")
    await bot.send_message(message.from_user.id,
                           "Укажите ваш текущий номер I-94, (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Line20a_I94Number_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет номера I-94.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер последнего выданного вам паспорта:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line20a_I94Number_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line20a_I94Number[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите номер последнего выданного вам паспорта:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line20b_Passport_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line20b_Passport[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер проездного документа (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Line20c_TravelDoc_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет номера проездного документа.")
    await bot.send_message(callback_query.from_user.id,
                           "Какая страна выдала вам последний паспорт или проездной документ (travel document)?")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line20c_TravelDoc_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line20c_TravelDoc[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Какая страна выдала вам последний паспорт или проездной документ (travel document)?")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line20d_CountryOfIssuance_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line20d_CountryOfIssuance[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату истечения срока действия паспорта или проездного документа (мм/дд/гггг):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line20e_ExpDate_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line20e_ExpDate[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите дату вашего последнего въезда в США (мм/дд/гггг):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line21_DateOfLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line21_DateOfLastEntry[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите место вашего последнего въезда в США:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Place_OfLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].place_entry[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите ваш законный статус при вашем последнем въезде в США "
                           "(например, B-2 посетитель, F-1 студент):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line23_StatusLastEntry_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line23_StatusLastEntry[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите ваш текущий законный статус в США (например, B-2 посетитель, F-1 студент):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line24_CurrentStatus_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line24_CurrentStatus[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите ваш номер информационной системы для студентов и посетителей по обмену (SEVIS) "
                           "(если имеется):", reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Line26_SEVISnumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что у вас нет номера информационной системы для студентов и посетителей по "
                           "обмену (SEVIS) .")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Информация о вашей категории соответствия требования для получения разрешения "
                           "на работу.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу категорию соответствии согласно инструкции к форме I-765 "
                           "(https://www.uscis.gov/sites/default/files/document/forms/i-765instr.pdf) "
                           "(например, (a)(8), (c)(17) (i11)):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line26_SEVISnumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line26_SEVISnumber[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Информация о вашей категории соответствия требования для получения разрешения "
                           "на работу.»")
    await bot.send_message(message.from_user.id,
                           "Укажите вашу категорию соответствии согласно инструкции к форме I-765 "
                           "(https://www.uscis.gov/sites/default/files/document/forms/i-765instr.pdf) "
                           "(например, (a)(8), (c) (17) (iii)):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.EligibilityCategory)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        input_data = message.text.split()
        try:
            data['form1[0].Page3[0].#area[1].section_1[0]'] = input_data[0]
            data['form1[0].Page3[0].#area[1].section_2[0]'] = input_data[1]
            data['form1[0].Page3[0].#area[1].section_3[0]'] = input_data[2]
        except IndexError:
            pass
    keyboard = FormI765EligibilityCategoryChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы указали категорию соответствия (с)(3)(С), предоставьте следующую информацию:\n"
                           "Укажите ученую степень (бакалавр, магистр, доктор и так далее):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="did_not_entered_category",
                           state=FormI765.Line27a_Degree_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не указывали категорию (с)(3)(С).")
    keyboard = FormI765EligibilityCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если вы указали категорию соответствия (с)(26), укажите номер последнего "
                           "уведомления по форме I-797 вашего супруга по форме Н-1В для формы І-129 «Петиция для "
                           "работника-неиммигранта»:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Line28_ReceiptNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line27a_Degree_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line27a_Degree[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите наименование работодателя как оно указано в E-Verify:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line27b_Everify_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line27b_Everify[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите идентификационный номер компании работодателя E-Verify или действующий "
                           "идентификационный номер компании клиента E-Verify:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line27c_EverifyIDNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line27c_EverifyIDNumber[0]'] = message.text
    keyboard = FormI765EligibilityCategoryChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы указали категорию соответствия (с)(26), укажите номер квитанции последнего "
                           "уведомления по форме I-797 вашего супруга по форме Н-1В для формы І-129 «Петиция для "
                           "работника-неиммигранта»:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="did_not_entered_category",
                           state=FormI765.Line28_ReceiptNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не указывали категорию (с)(26).")
    keyboard = FormI765EligibilityCategoryArrestedChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если вы указали категорию соответствия (с)(8), были ли вы когда-либо были арестованы "
                           "и/или осуждены за какое-либо преступление?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line28_ReceiptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line28_ReceiptNumber[0]'] = message.text
    keyboard = FormI765EligibilityCategoryArrestedChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы указали категорию соответствия (с)(8), были ли вы когда-либо были арестованы "
                           "и/или осуждены за какое-либо преступление?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="EligibilityCategoryArrested_Yes",
                           state=FormI765.EligibilityCategoryArrestedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].PtLine29_YesNo[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы были арестованы и/или осуждены за какое-либо преступление.")
    keyboard = FormI765EligibilityCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если вы указали категорию соответствия (с)(35), укажите номер квитанции вашего уведомления "
                           "по форме 1-797 для формы I-140 «Петиция иммигранта для иностранного работника». Если вы "
                           "указали категорию соответствия (с) (36), укажите номер квитанции вашего супруга или "
                           "родителя по форме 1-797 с уведомлением по форме 1-140:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="EligibilityCategoryArrested_No",
                           state=FormI765.EligibilityCategoryArrestedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].PtLine29_YesNo[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы никогда не были арестованы и/или осуждены за какое-либо преступление.")
    keyboard = FormI765EligibilityCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если вы указали категорию соответствия (с)(35), укажите номер квитанции вашего уведомления "
                           "по форме 1-797 для формы I-140 «Петиция иммигранта для иностранного работника». Если вы "
                           "указали категорию соответствия (с) (36), укажите номер квитанции вашего супруга или "
                           "родителя по форме 1-797 с уведомлением по форме 1-140:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="EligibilityCategoryArrested_DidNotEntered",
                           state=FormI765.EligibilityCategoryArrestedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не указывали категорию (с)(8).")
    keyboard = FormI765EligibilityCategoryChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Если вы указали категорию соответствия (с)(35), укажите номер квитанции вашего уведомления "
                           "по форме 1-797 для формы I-140 «Петиция иммигранта для иностранного работника». Если вы "
                           "указали категорию соответствия (с) (36), укажите номер квитанции вашего супруга или "
                           "родителя по форме 1-797 с уведомлением по форме 1-140:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Line18a_Receipt_0_Line30a_ReceiptNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].Line18a_Receipt[0].Line30a_ReceiptNumber[0]'] = message.text
    keyboard = FormI765EligibilityCategoryArrestedChoice()
    await bot.send_message(message.from_user.id,
                           "Если вы указали категорию соответствия (с) (35) или (с)(36), были ли вы когда-либо "
                           "арестованы и/или осуждены за какое-либо преступление?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="EligibilityCategoryArrested_Yes",
                           state=FormI765.EligibilityCategoryArrestedChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].PtLine30b_YesNo[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы были арестованы и/или осуждены за какое-либо преступление.")
    keyboard = FormI765ApplicantStatementChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 3. Заверения заявителя, контактная информация, декларация, сертификация и подпись")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Заверения заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите верное:\n"
                           "1. Я могу читать и понимать по-английски, я прочитал и понял каждый вопрос и инструкцию к "
                           "этому заявлению, а также свои ответы на все вопросы.\n"
                           "2. Переводчик зачитал мне все вопросы и инструкцию к этому заявлению, а также мои ответы "
                           "на каждый вопрос на языке, которым я свободно владею, и я все понял.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.ApplicantStatementChoice.set()


@dp.callback_query_handler(text="EligibilityCategoryArrested_No",
                           state=FormI765.EligibilityCategoryArrestedChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page3[0].PtLine30b_YesNo[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы никогда не были арестованы и/или осуждены за какое-либо преступление.")
    keyboard = FormI765ApplicantStatementChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Часть 3. Заверения заявителя, контактная информация, декларация, сертификация и подпись")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Заверения заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите верное:\n"
                           "1. Я могу читать и понимать по-английски, я прочитал и понял каждый вопрос и инструкцию к "
                           "этому заявлению, а также свои ответы на все вопросы.\n"
                           "2. Переводчик зачитал мне все вопросы и инструкцию к этому заявлению, а также мои ответы "
                           "на каждый вопрос на языке, которым я свободно владею, и я все понял.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.ApplicantStatementChoice.set()


@dp.callback_query_handler(text="EligibilityCategoryArrested_DidNotEntered",
                           state=FormI765.EligibilityCategoryArrestedChoice_1)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI765ApplicantStatementChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не указывали категорию (с)(35) или (с)(36).")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 3. Заверения заявителя, контактная информация, декларация, сертификация и подпись")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Заверения заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите верное:\n"
                           "1. Я могу читать и понимать по-английски, я прочитал и понял каждый вопрос и инструкцию к "
                           "этому заявлению, а также свои ответы на все вопросы.\n"
                           "2. Переводчик зачитал мне все вопросы и инструкцию к этому заявлению, а также мои ответы "
                           "на каждый вопрос на языке, которым я свободно владею, и я все понял.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.ApplicantStatementChoice.set()


@dp.callback_query_handler(text="did_not_entered_category",
                           state=FormI765.Line18a_Receipt_0_Line30a_ReceiptNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI765ApplicantStatementChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не указывали категорию (с)(35) или (с)(36).")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 3. Заверения заявителя, контактная информация, декларация, сертификация и подпись")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Заверения заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите верное:\n"
                           "1. Я могу читать и понимать по-английски, я прочитал и понял каждый вопрос и инструкцию к "
                           "этому заявлению, а также свои ответы на все вопросы.\n"
                           "2. Переводчик зачитал мне все вопросы и инструкцию к этому заявлению, а также мои ответы "
                           "на каждый вопрос на языке, которым я свободно владею, и я все понял.",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.ApplicantStatementChoice.set()


@dp.callback_query_handler(text="ApplicantStatement_1",
                           state=FormI765.ApplicantStatementChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line1Checkbox[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что вы можете читать и понимать по-английски, я прочитал и понял каждый вопрос "
                           "и инструкцию к этому заявлению, а также свои ответы на все вопросы.")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="ApplicantStatement_2",
                           state=FormI765.ApplicantStatementChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line1Checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что переводчик зачитал вам все вопросы и инструкцию к этому заявлению, "
                           "а также ваши ответы на каждый вопрос на языке, которым вы свободно владеете, "
                           "и вы все поняли.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите язык, на который переводчик переводил это заявление и инструкцию к нему, и "
                           "которым вы свободно владеете:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt3Line1b_Language_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line1b_Language[0]'] = message.text
    keyboard = FormI765OnlyTrueInformationChoice()
    await bot.send_message(message.from_user.id,
                           "Верно ли следующее: по моей просьбе составитель (третье лицо) заполнил за меня это "
                           "заявление исключительно на основе информации, которую я предоставил или "
                           "разрешил использовать?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="OnlyTrueInformation_Yes",
                           state=FormI765.Part3_Checkbox_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Part3_Checkbox[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите имя третьего лица, которое по вашей просьбе заполнило это заявление:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt3Line2_RepresentativeName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line2_RepresentativeName[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Контактная информация заявителя.»")
    await bot.send_message(message.from_user.id,
                           "Укажите дневной номер телефона заявителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="OnlyTrueInformation_No",
                           state=FormI765.Part3_Checkbox_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Контактная информация заявителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите дневной номер телефона заявителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt3Line3_DaytimePhoneNumber1_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt3Line3_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line3_DaytimePhoneNumber1[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер мобильного телефона заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt3Line4_MobileNumber1_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес электронной почты заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt3Line5_Email_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt3Line4_MobileNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line4_MobileNumber1[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес электронной почты заявителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt3Line5_Email_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI765SalvadorOrGwatemalaResidentChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Вы являетесь гражданином Сальвадора или Гватемалы и имеете право на получение льгот по"
                           " мировому соглашению АВС?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt4Line6_Checkbox_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt3Line5_Email_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line5_Email[0]'] = message.text
    keyboard = FormI765SalvadorOrGwatemalaResidentChoice()
    await bot.send_message(message.from_user.id,
                           "Вы являетесь гражданином Сальвадора или Гватемалы и имеете право на получение льгот по"
                           " мировому соглашению АВС?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt4Line6_Checkbox_0.set()


@dp.callback_query_handler(text="SalvadorOrGwatemalaResident_Yes",
                           state=FormI765.Pt4Line6_Checkbox_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt4Line6_Checkbox[0]'] = ""
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что являетесь гражданином Сальвадора или Гватемалы и имеете право на получение "
                           "льгот по мировому соглашению АВС.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу подпись:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt3Line7a_Signature_0.set()


@dp.callback_query_handler(text="SalvadorOrGwatemalaResident_No",
                           state=FormI765.Pt4Line6_Checkbox_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не являетесь гражданином Сальвадора или Гватемалы и имеете право на "
                           "получение льгот по мировому соглашению АВС.")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите вашу подпись:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt3Line7a_Signature_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt3Line7a_Signature_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt3Line7a_Signature[0]'] = message.text
        data['form1[0].Page4[0].Pt3Line7b_DateofSignature[0]'] = datetime.datetime.now().strftime('%m/%d%/Y')

    keyboard = FormI765TranslatorHelpedChoice()
    await bot.send_message(message.from_user.id,
                           "Вам помогал переводчик при заполнении этого заявления?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.TranslatorHelpedChoice.set()


@dp.callback_query_handler(text="TranslatorHelped_Yes",
                           state=FormI765.TranslatorHelpedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что переводчик помогал вам при заполнении этого заявления.")
    await bot.send_message(callback_query.from_user.id,
                           "Часть 4. «Контактная информация, сертификация и подпись переводчика.»")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Имя переводчика.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию переводчика:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt4Line1a_InterpreterFamilyName_0.set()


@dp.callback_query_handler(text="TranslatorHelped_No",
                           state=FormI765.TranslatorHelpedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что переводчик не помогал вам при заполнении этого заявления.")
    async with state.proxy() as data:
        await final_stage(data, callback_query, state, bot)


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt4Line1a_InterpreterFamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt4Line1a_InterpreterFamilyName[0]'] = message.text

    await bot.send_message(message.from_user.id,
                           "Укажите имя переводчика:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt4Line1b_InterpreterGivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt4Line1b_InterpreterGivenName[0]'] = message.text

    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите название компании или организации, где работает переводчик (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt4Line2_InterpreterBusinessorOrg_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не знаете название компании или организации, где работает переводчик.")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Почтовый адрес переводчик.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt4Line2_InterpreterBusinessorOrg_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page4[0].Pt4Line2_InterpreterBusinessorOrg[0]'] = message.text

    await bot.send_message(message.from_user.id,
                           "Раздел «Почтовый адрес переводчика.»")
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3a_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3a_StreetNumberName[0]'] = message.text

    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.AptSteFlr_Choice_Mailing_Translator.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI765.AptSteFlr_Choice_Mailing_Translator)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3b_Unit[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt5Line3b_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Ste",
                           state=FormI765.AptSteFlr_Choice_Mailing_Translator)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3b_Unit[2]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt5Line3b_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI765.AptSteFlr_Choice_Mailing_Translator)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3b_Unit[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt5Line3b_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3b_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3b_AptSteFlrNumber[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите город:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3c_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3c_CityOrTown[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3d_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3d_State[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти Zipcode можно по ссылке:\n"
                           "https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3e_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3e_ZipCode[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3f_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3f_Province[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (postal code) (например, 12345-1234):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3g_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3g_PostalCode[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line3h_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line3h_Country[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Контактная информация переводчика.»")
    await bot.send_message(message.from_user.id,
                           "Укажите дневной номер телефона переводчика:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt4Line4_InterpreterDaytimeTelephone_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt4Line4_InterpreterDaytimeTelephone[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер мобильного телефона переводчика (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt4Line5_MobileNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес электронной почты переводчика (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt4Line5_MobileNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt4Line5_MobileNumber[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес электронной почты переводчика (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt4Line6_Email_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите подпись переводчика:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt4Line6_Email_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt4Line6_Email[0]'] = message.text
        data['form1[0].Page5[0].Part4_NameofLanguage[0]'] = message.text

    await bot.send_message(message.from_user.id,
                           "Укажите подпись переводчика:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt4Line6a_Signature_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt4Line6a_Signature[0]'] = message.text
        data['form1[0].Page5[0].Pt4Line6b_DateofSignature[0]'] = datetime.datetime.now().strftime('%m/%d%/Y')
    keyboard = FormI765PreparerHelpedChoice()
    await bot.send_message(message.from_user.id,
                           "Вам помогал какое-либо третье лицо (составитель) в заполнении этого заявления?",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="PreparerHelped_Yes",
                           state=FormI765.PreparerHelpedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Часть 5. «Контактная информация, сертификация и подпись составителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Имя составителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите фамилию составителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt5Line1a_PreparerFamilyName_0.set()


@dp.callback_query_handler(text="PreparerHelped_No",
                           state=FormI765.PreparerHelpedChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что составитель не помогал вам при заполнении этого заявления.")
    async with state.proxy() as data:
        await final_stage(data, callback_query, state, bot)


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line1a_PreparerFamilyName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line1a_PreparerFamilyName[0]'] = message.text

    await bot.send_message(message.from_user.id,
                           "Укажите имя составителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line1b_PreparerGivenName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line1b_PreparerGivenName[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите название компании или организации, где работает составитель (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt5Line2_BusinessName_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Вы указали, что не знаете название компании или организации, где работает составитель.")
    await bot.send_message(callback_query.from_user.id,
                           "Раздел «Почтовый адрес составителя.»")
    await bot.send_message(callback_query.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line2_BusinessName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line2_BusinessName[0]'] = message.text

    await bot.send_message(message.from_user.id,
                           "Раздел «Почтовый адрес составителя.»")
    await bot.send_message(message.from_user.id,
                           "Укажите название и номер улицы:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3a_StreetNumberName_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3a_StreetNumberName[0]'] = message.text

    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите тип помещения:",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.AptSteFlr_Choice_Mailing_Preparer.set()


@dp.callback_query_handler(text="Apt",
                           state=FormI765.AptSteFlr_Choice_Mailing_Preparer)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3b_Unit[1]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt6Line3b_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Ste",
                           state=FormI765.AptSteFlr_Choice_Mailing_Preparer)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3b_Unit[0]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt6Line3b_AptSteFlrNumber_0.set()


@dp.callback_query_handler(text="Flr",
                           state=FormI765.AptSteFlr_Choice_Mailing_Preparer)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3b_Unit[2]'] = "x"
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.Pt6Line3b_AptSteFlrNumber_0.set()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3b_AptSteFlrNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3b_AptSteFlrNumber[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите город:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3c_CityOrTown_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3c_CityOrTown[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите штат (например, CA, NY, AZ и т. д.):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3d_State_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3d_State[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите Zipcode (например, 123456).\n"
                           "Найти почтовый индекс можно по ссылке:\n"
                           "https://tools.usps.com/go/ZipLookupAction_input")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3e_ZipCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3e_ZipCode[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите провинцию:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3f_Province_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3f_Province[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите почтовый индекс (postal code) (например, 12345-1234):")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3g_PostalCode_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3g_PostalCode[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Укажите страну:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt6Line3h_Country_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt6Line3h_Country[0]'] = message.text
    await bot.send_message(message.from_user.id,
                           "Раздел «Контактная информация составителя.»")
    await bot.send_message(message.from_user.id,
                           "Укажите дневной номер телефона составителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line4_DaytimePhoneNumber1_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line4_DaytimePhoneNumber1[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите номер мобильного телефона составителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt5Line5_PreparerFaxNumber_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(callback_query.from_user.id,
                           "Укажите адрес электронной почты составителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line5_PreparerFaxNumber_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line5_PreparerFaxNumber[0]'] = message.text
    keyboard = FormI589IfAnyChoice()
    await bot.send_message(message.from_user.id,
                           "Укажите адрес электронной почты составителя (если имеется):",
                           reply_markup=keyboard.markup)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@dp.callback_query_handler(text="don't_have_it",
                           state=FormI765.Pt5Line6_Email_0)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id,
                           "Укажите подпись составителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line6_Email_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page5[0].Pt5Line6_Email[0]'] = message.text

    await bot.send_message(message.from_user.id,
                           "Укажите подпись составителя:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await FormI765.next()


@escape_json_special_chars
@dp.message_handler(state=FormI765.Pt5Line8a_Signature_0)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['form1[0].Page6[0].Pt5Line8a_Signature[0]'] = message.text
        data['form1[0].Page6[0].Pt5Line8b_DateofSignature[0]'] = datetime.datetime.now().strftime('%m/%d%/Y')
    async with state.proxy() as data:
        await final_stage(data, message, state, bot, strapi_client)
