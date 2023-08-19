from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class Form_AR_11_Mailing_Address_Choice_Keyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button_yes = InlineKeyboardButton("Да", callback_data="MailingSameAsPhysical_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="MailingSameAsPhysical_No")
        keyboard_markup.add(button_no)
        button_empty = InlineKeyboardButton("Оставить пустым", callback_data="MailingEmpty")
        keyboard_markup.add(button_empty)
        self.keyboard_markup = keyboard_markup
