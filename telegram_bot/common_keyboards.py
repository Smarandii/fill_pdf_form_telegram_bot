from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class AvailableFormsKeyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("AR-11", callback_data="AR-11")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-131", callback_data="I-131")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-485", callback_data="I-485")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-589", callback_data="I-589")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-765", callback_data="I-765")
        keyboard_markup.add(button)
        self.keyboard_markup = keyboard_markup
