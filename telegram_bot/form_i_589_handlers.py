from aiogram import types
from aiogram.dispatcher import FSMContext
from form_i_589 import Form_I_589
from telegram_bot import bot, dp, FillPdfFromJsonAdapter, datetime


@dp.callback_query_handler(text="I-589")
async def i_589_form_chosen(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['form_identifier'] = "I-589"
    await bot.send_message(callback_query.from_user.id, "You've chosen the I-589 form. Let's start filling it.")
    await bot.send_message(callback_query.from_user.id, "Enter your Alien Registration Number(s) (A-Number) (if any):")
    await Form_I_589.A_I_PtAILine1_ANumber_0.set()


@dp.message_handler(state=Form_I_589.A_I_PtAILine1_ANumber_0)
async def process_A_I_PtAILine1_ANumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine1_ANumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your U.S. Social Security Number (if any):")


@dp.message_handler(state=Form_I_589.A_I_TextField1_0)
async def process_A_I_TextField1_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "USCIS Online Account Number (if any)")


@dp.message_handler(state=Form_I_589.A_I_TextField1_8)
async def process_A_I_TextField1_8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[8]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Complete Last Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine4_LastName_0)
async def process_A_I_PtAILine4_LastName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine4_LastName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "First Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine5_FirstName_0)
async def process_A_I_PtAILine5_FirstName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine5_FirstName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Middle Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine6_MiddleName_0)
async def process_A_I_PtAILine6_MiddleName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine6_MiddleName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "What other names have you used (include maiden name and aliases)?")


@dp.message_handler(state=Form_I_589.A_I_TextField1_1)
async def process_A_I_TextField1_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Street Number and Name:")

# 8. Residence in the U.S. (where you physically reside)
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_StreetNumandName_0)
async def process_A_I_PtAILine8_StreetNumandName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Apt. Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AptNumber_0)
async def process_A_I_PtAILine8_AptNumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AptNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your City:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_City_0)
async def process_A_I_PtAILine9_City_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].TextField1[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your State:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_State_0)
async def process_A_I_PtAILine8_State_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_State[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Zip Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_Zipcode_0)
async def process_A_I_PtAILine8_Zipcode_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_Zipcode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Area Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_AreaCode_0)
async def process_A_I_PtAILine8_AreaCode_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Number:")


# 9. Mailing Address in the U.S. (if different than the address in Item Number 8)
@dp.message_handler(state=Form_I_589.A_I_PtAILine8_TelephoneNumber_0)
async def process_A_I_PtAILine8_TelephoneNumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_TelephoneNumber[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter In Care Of (if applicable):")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_InCareOf_0)
async def process_A_I_PtAILine9_InCareOf_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_InCareOf[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Area Code:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_AreaCode_0)
async def process_A_I_PtAILine9_AreaCode_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine8_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Telephone Number:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine9_TelephoneNumber_0)
async def process_A_I_PtAILine8_TelephoneNumber_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_AreaCode[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Street Number and Name:")


@dp.message_handler(state=Form_I_589.A_I_PtAILine8_TelephoneNumber_0)
async def process_A_I_PtAILine9_StreetNumandName_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PtAILine9_StreetNumandName[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter Street Number and Name:")


@dp.message_handler(state=Form_I_589.A_I_PartALine9Gender_1)
async def process_A_I_PartALine9Gender_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].PartALine9Gender[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "Enter your Marital Status:")


@dp.message_handler(state=Form_I_589.A_I_Marital_0)
async def process_A_I_Marital_0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[0]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "You have indicated that you are single.")


@dp.message_handler(state=Form_I_589.A_I_Marital_1)
async def process_A_I_Marital_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[1]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "You have indicated that you are married.")


@dp.message_handler(state=Form_I_589.A_I_Marital_2)
async def process_A_I_Marital_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[2]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "You have indicated that you are divorced.")


@dp.message_handler(state=Form_I_589.A_I_Marital_3)
async def process_A_I_Marital_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['[0].Marital[3]'] = message.text
    await Form_I_589.next()
    await bot.send_message(message.from_user.id, "You have indicated that you are widowed.")














