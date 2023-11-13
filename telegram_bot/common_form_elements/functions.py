import datetime
import os
from telegram_bot import FillPdfFromJsonAdapter
import logging

async def final_stage(data, message, state, bot, strapi_client):
    try:
        adapter = FillPdfFromJsonAdapter(data=data, form_identifier=data['form_identifier'],
                                         user_id=message.from_user.id,
                                         timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    except KeyError:
        bot.send_message(message.chat.id, "form_identifier is not set")
        return None
    adapter.save_json()
    try:
        client_model = strapi_client.find_client(message.from_user.id)
        json_data = await state.get_data()
        strapi_client.create_json_input(json_data, client_model['id'])
    except Exception as e:
        logger = logging.getLogger("Final Stage")
        logger.setLevel(logger.INFO)
        logger.error(f"Error trying to save json: {e}")
    await state.finish()
    await bot.send_message(message.chat.id,
                           f"Ваши данные для формы {data['form_identifier']} успешно сохранены! С вами свяжется наш оператор для получения предоплаты, отправки заполненной формы и создания чата с юристом-консультантом.")
    await bot.send_chat_action(message.chat.id, "typing")
    file_path = adapter.fill_pdf()
    if os.getenv("RUNNING_ENV", default="PROD") == "PROD":
        with open(file_path, 'rb') as file:
            await bot.send_document(int(os.getenv("DOCUMENTS_RECEIVER")), file)
            await bot.send_message(int(os.getenv("DOCUMENTS_RECEIVER")), f"From user: {message.from_user.mention}")
    with open(file_path, 'rb') as file:
        await bot.send_document(int(os.getenv("DEVELOPER_TELEGRAM_ID")), file)
        await bot.send_message(int(os.getenv("DEVELOPER_TELEGRAM_ID")), f"From user: {message.from_user.mention}")                                                                                                      
