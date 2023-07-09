from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class Form_AR_11_Mailing_Address_Choice_Keyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button_yes = InlineKeyboardButton("MailingSameAsPhysical_Yes", callback_data="MailingSameAsPhysical_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("MailingSameAsPhysical_No", callback_data="MailingSameAsPhysical_No")
        keyboard_markup.add(button_no)
        button_empty = InlineKeyboardButton("MailingEmpty", callback_data="MailingEmpty")
        keyboard_markup.add(button_empty)
        self.keyboard_markup = keyboard_markup
