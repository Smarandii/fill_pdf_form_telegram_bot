from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class Form_I_589_Gender_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Female", callback_data="female")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Male", callback_data="male")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Marital_Status_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        button = InlineKeyboardButton("Marital Status Single", callback_data="ms_single")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Marital Status Married", callback_data="ms_married")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Marital Status Divorced", callback_data="ms_divorced")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Marital Status Widowed", callback_data="ms_widowed")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Immigration_Court_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button = InlineKeyboardButton("I have never been in Immigration Court proceedings.", callback_data="never_been_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I am now in Immigration Court proceedings.", callback_data=f"now_in_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("I am not now in Immigration Court proceedings, but I have been in the past.", callback_data=f"not_now_but_been_in_imc")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_94_Number_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("I don't have an I-94 number", callback_data="blank_i_94")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_English_Fluency_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Yes", callback_data="yes_eng_fluent")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("No", callback_data="no_eng_fluent")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Marriage_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Yes", callback_data="yes_married")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("No", callback_data="no_married")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Location_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Yes", callback_data="yes_location")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("No", callback_data="no_location")
        keyboard_markup.add(button)
        self.markup = keyboard_markup
