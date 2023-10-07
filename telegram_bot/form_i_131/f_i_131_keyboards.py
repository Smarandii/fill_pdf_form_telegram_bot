from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class FormI131ApplicationTypeChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=6)
        button_yes = InlineKeyboardButton("1.", callback_data="ApplicationType_1")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("2.", callback_data="ApplicationType_2")
        keyboard_markup.add(button_no)
        button_empty = InlineKeyboardButton("3.", callback_data="ApplicationType_3")
        keyboard_markup.add(button_empty)
        button_yes = InlineKeyboardButton("4.", callback_data="ApplicationType_4")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("5.", callback_data="ApplicationType_5")
        keyboard_markup.add(button_no)
        button_empty = InlineKeyboardButton("6.", callback_data="ApplicationType_6")
        keyboard_markup.add(button_empty)
        self.markup = keyboard_markup


class FormI131WhereToSendTravelDocumentChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=6)
        button_yes = InlineKeyboardButton("1.", callback_data="WhereToSendTravelDocument_1")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("2.", callback_data="WhereToSendTravelDocument_2")
        keyboard_markup.add(button_no)
        button_empty = InlineKeyboardButton("3.", callback_data="WhereToSendTravelDocument_3")
        keyboard_markup.add(button_empty)
        self.markup = keyboard_markup


class FormI131PeopleIncludedInApplicationAreInExclusion:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="PeopleIncludedInApplicationAreInExclusion_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="PeopleIncludedInApplicationAreInExclusion_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131NoticeAddressChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("1.", callback_data="NoticeAddress_1")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("2.", callback_data="NoticeAddress_2")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131HadBeenPermitedReentryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="HadBeenPermitedReentry_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="HadBeenPermitedReentry_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup
