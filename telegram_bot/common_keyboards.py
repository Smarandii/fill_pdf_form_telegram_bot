from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class AvailableFormsKeyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("AR-11 form", callback_data="AR-11")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I-589 form", callback_data="I-589")
        keyboard_markup.add(button)
        self.keyboard_markup = keyboard_markup
