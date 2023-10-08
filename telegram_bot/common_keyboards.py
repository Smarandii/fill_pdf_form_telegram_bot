from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class AvailableFormsKeyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("AR-11 (30 вопросов)", callback_data="AR-11")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-131 (185 вопросов)", callback_data="I-131")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-485 (802 вопроса)", callback_data="I-485")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-589 (579 вопросов)", callback_data="I-589")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-765 (181 вопрос)", callback_data="I-765")
        keyboard_markup.add(button)
        self.keyboard_markup = keyboard_markup
