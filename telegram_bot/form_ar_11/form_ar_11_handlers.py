import os
import time
from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from telegram_bot.form_i_765.f_i_765_keyboards import FormI765TypeOfBuildingChoice
from telegram_bot.phrases import AR_11_START_PHRASE
from telegram_bot.form_ar_11.form_ar_11_state_group import Form_AR_11
from telegram_bot import bot, dp, datetime, Form_AR_11_Mailing_Address_Choice_Keyboard, strapi_client
from telegram_bot.common_form_elements.functions import final_stage, save_json_to_strapi


@dp.message_handler(filters.Command("end"), state='*')
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await final_stage(data, message, state, bot, strapi_client)


@dp.callback_query_handler(text="AR-11", state='*')
async def ar_11_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "AR-11"
        response = await save_json_to_strapi(strapi_client, message=callback_query, state=state)
        data['json_input_strapi_id'] = response['data']['id']
    await bot.send_message(callback_query.from_user.id, AR_11_START_PHRASE)
    await bot.send_message(callback_query.from_user.id, "Укажите Вашу фамилию:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S1_FamilyName.set()


@dp.message_handler(state=Form_AR_11.S1_FamilyName)
async def process_s1_family_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S1_FamilyName[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше имя:")


@dp.message_handler(state=Form_AR_11.S1_GivenName)
async def process_s1_given_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S1_GivenName[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите Ваше отчество:")


@dp.message_handler(state=Form_AR_11.S1_MiddleName)
async def process_s1_middle_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S1_MiddleName[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите Вашу дату рождения:")


@dp.message_handler(state=Form_AR_11.S1_DateOfBirth)
async def process_s1_date_of_birth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S1_DateOfBirth[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите Ваш регистрационный номер иностранца (alien number):")


@dp.message_handler(state=Form_AR_11.AlienNumber)
async def process_alien_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].AlienNumber[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы, на которой Вы проживаете в настоящий момент:")


@dp.message_handler(state=Form_AR_11.S2B_StreetNumberName)
async def process_s2b_street_number_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2B_StreetNumberName[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@dp.message_handler(state=Form_AR_11.S2B_CityOrTown)
async def process_s2b_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2B_CityOrTown[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2B__Unit[0]"] = "x"
        data["[0].S2B__Unit[1]"] = ""
        data["[0].S2B__Unit[2]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2B_AptSteFlrNumber.set()


@dp.callback_query_handler(text="Apt",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2B__Unit[1]"] = "x"
        data["[0].S2B__Unit[0]"] = ""
        data["[0].S2B__Unit[2]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2B_AptSteFlrNumber.set()


@dp.callback_query_handler(text="Flr",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2B__Unit[2]"] = "x"
        data["[0].S2B__Unit[0]"] = ""
        data["[0].S2B__Unit[1]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2B_AptSteFlrNumber.set()


@dp.message_handler(state=Form_AR_11.S2B_AptSteFlrNumber)
async def process_s2b_apt_ste_flr_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2B_AptSteFlrNumber[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@dp.message_handler(state=Form_AR_11.S2B_State)
async def process_s2b_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2B_State[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Введите свой почтовый индекс (например, 123456). "
                                                 "Найти почтовый индекс можно по ссылке: "
                                                 "https://tools.usps.com/go/ZipLookupAction_input")


@dp.message_handler(state=Form_AR_11.S2B_ZipCode)
async def process_s2b_zip_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2B_ZipCode[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Отлично! Теперь давайте заполним предыдущий адрес фактического проживания. ")
    await bot.send_message(message.from_user.id, "Укажите название и номер улицы:")


@dp.message_handler(state=Form_AR_11.S2A_StreetNumberName)
async def process_s2a_street_number_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2A_StreetNumberName[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@dp.message_handler(state=Form_AR_11.S2A_CityOrTown)
async def process_s2a_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2A_CityOrTown[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2A_Unit[0]"] = "x"
        data["[0].S2A_Unit[1]"] = ""
        data["[0].S2A_Unit[2]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2A_AptSteFlrNumber.set()


@dp.callback_query_handler(text="Apt",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2A_Unit[1]"] = "x"
        data["[0].S2A_Unit[0]"] = ""
        data["[0].S2A_Unit[2]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2A_AptSteFlrNumber.set()


@dp.callback_query_handler(text="Flr",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice_2)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2A_Unit[2]"] = "x"
        data["[0].S2A_Unit[0]"] = ""
        data["[0].S2A_Unit[1]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2A_AptSteFlrNumber.set()


@dp.message_handler(state=Form_AR_11.S2A_AptSteFlrNumber)
async def process_s2a_apt_ste_flr_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2A_AptSteFlrNumber[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@dp.message_handler(state=Form_AR_11.S2A_State)
async def process_s2a_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2A_State[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Введите свой почтовый индекс (например, 123456). "
                                                 "Найти почтовый индекс можно по ссылке: https://tools.usps.com/go/ZipLookupAction_input")


# Mailing address
@dp.message_handler(state=Form_AR_11.S2C_StreetNumberName)
async def process_s2c_street_number_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2C_StreetNumberName[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите город:")


@dp.message_handler(state=Form_AR_11.S2C_CityOrTown)
async def process_s2c_city_or_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2C_CityOrTown[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    keyboard = FormI765TypeOfBuildingChoice()
    await bot.send_message(message.from_user.id, "Укажите тип помещения:",
                           reply_markup=keyboard.markup)


@dp.callback_query_handler(text="Ste",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2C_Unit[0]"] = "x"
        data["[0].S2C_Unit[1]"] = ""
        data["[0].S2C_Unit[2]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер квартиры:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2C_AptSteFlrNumber.set()


@dp.callback_query_handler(text="Apt",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2C_Unit[1]"] = "x"
        data["[0].S2C_Unit[0]"] = ""
        data["[0].S2C_Unit[2]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер апартаментов:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2C_AptSteFlrNumber.set()


@dp.callback_query_handler(text="Flr",
                           state=Form_AR_11.Page1_TypeOfBuildingChoice_3)
async def process(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["[0].S2C_Unit[2]"] = "x"
        data["[0].S2C_Unit[0]"] = ""
        data["[0].S2C_Unit[1]"] = ""
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    await bot.send_message(callback_query.from_user.id,
                           "Укажите номер этажа:")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2C_AptSteFlrNumber.set()


@dp.message_handler(state=Form_AR_11.S2C_AptSteFlrNumber)
async def process_s2c_apt_ste_flr_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2C_AptSteFlrNumber[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Укажите штат (например, CA, NY, AZ и т.д.):")


@dp.message_handler(state=Form_AR_11.S2C_State)
async def process_s2c_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2C_State[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Введите свой почтовый индекс (например, 123456). "
                                                 "Найти почтовый индекс можно по ссылке: "
                                                 "https://tools.usps.com/go/ZipLookupAction_input")


@dp.message_handler(state=Form_AR_11.S2C_ZipCode)
async def process_s2b_zip_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2C_ZipCode[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.next()
    await bot.send_message(message.from_user.id, "Отлично! Единственное, что осталось, это ваша подпись:")


@dp.message_handler(state=Form_AR_11.S2A_ZipCode)
async def process_s2a_zip_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S2A_ZipCode[0]'] = message.text
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
    keyboard = Form_AR_11_Mailing_Address_Choice_Keyboard()
    await message.answer("Отлично! Давайте сейчас заполним ваш почтовый адрес. "
                         "Перед этим небольшой вопрос: совпадает ли Ваш текущий фактический адрес  проживания с Вашим почтовым адресом?", reply_markup=keyboard.keyboard_markup)


@dp.callback_query_handler(text="MailingSameAsPhysical_Yes", state="*")
async def callback_query_handler_mailing_same_as_physical_yes(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку «Да», я скопирую и перенесу информацию из графы фактического адреса в графу почтового адреса. ")
    async with state.proxy() as data:
        data['[0].S2C_StreetNumberName[0]'] = data['[0].S2B_StreetNumberName[0]']
        data['[0].S2C_CityOrTown[0]'] = data['[0].S2B_CityOrTown[0]']
        data['[0].S2C_Unit[0]'] = data['[0].S2B__Unit[0]']
        data['[0].S2C_Unit[1]'] = data['[0].S2B__Unit[1]']
        data['[0].S2C_Unit[2]'] = data['[0].S2B__Unit[2]']
        data['[0].S2C_AptSteFlrNumber[0]'] = data['[0].S2B_AptSteFlrNumber[0]']
        data['[0].S2C_State[0]'] = data['[0].S2B_State[0]']
        data['[0].S2C_CityOrTown[0]'] = data['[0].S2B_CityOrTown[0]']
        data['[0].S2C_ZipCode[0]'] = data['[0].S2B_ZipCode[0]']
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)

    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S3_SignatureApplicant.set()
    await bot.send_message(callback_query.from_user.id, "Укажите свою подпись:")


@dp.callback_query_handler(text="MailingSameAsPhysical_No", state="*")
async def callback_query_handler_mailing_same_as_physical_no(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку «Нет», давайте продолжим заполнять форму с Вашим почтовым адресом. ")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S2C_StreetNumberName.set()
    await bot.send_message(callback_query.from_user.id, "Укажите название и номер улицы:")


@dp.callback_query_handler(text="MailingEmpty", state="*")
async def callback_query_handler_mailing_empty(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "Вы не будете заполнять почтовый адрес. "
                                                        "Осталась только ваша подпись. ")
    time.sleep(float(os.getenv('RESPONSE_DELAY', default="0.1")))
    await Form_AR_11.S3_SignatureApplicant.set()
    await bot.send_message(callback_query.from_user.id, "Укажите свою подпись:")


@dp.message_handler(state=Form_AR_11.S3_SignatureApplicant)
async def process_s3_signature_applicant(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].S3_SignatureApplicant[0]'] = message.text
        data['[0].S3_DateofSignature[0]'] = datetime.datetime.now().strftime("%d/%m/%Y")
        json_data = await state.get_data()
        strapi_client.update_json_input_by_id(id_=data['json_input_strapi_id'], json_data=json_data)
        await final_stage(data, message, state, bot, strapi_client)
