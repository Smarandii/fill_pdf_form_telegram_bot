from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class FormI765EligibilityCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Я не указывал(-а) данную категорию", callback_data="did_not_entered_category")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765ApplicantStatementChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("1.", callback_data="ApplicantStatement_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.", callback_data="ApplicantStatement_2")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765OnlyTrueInformationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="OnlyTrueInformation_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="OnlyTrueInformation_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765SalvadorOrGwatemalaResidentChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="SalvadorOrGwatemalaResident_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="SalvadorOrGwatemalaResident_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765EligibilityCategoryArrestedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button = InlineKeyboardButton("Да", callback_data="EligibilityCategoryArrested_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="EligibilityCategoryArrested_No")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Я не указывал(-а) данную категорию",
                                      callback_data="EligibilityCategoryArrested_DidNotEntered")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765ApplyingForChoiceKeyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button = InlineKeyboardButton("1.a.", callback_data="1.a.")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("1.b.", callback_data="1.b.")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("1.c.", callback_data="1.c.")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765UsedOtherNamesChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="UsedOtherNames_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="UsedOtherNames_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765TranslatorHelpedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="TranslatorHelped_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="TranslatorHelped_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765PreparerHelpedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="PreparerHelped_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="PreparerHelped_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765AppliedEarlierChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="AppliedEarlier_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="AppliedEarlier_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765SSACardWasIssuedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="SSACardWasIssued_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="SSACardWasIssued_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765WantSSACardToBeIssuedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="WantSSACardToBeIssued_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="WantSSACardToBeIssued_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765WantToShareInformationWithSSAChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="WantToShareInformationWithSSA_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="WantToShareInformationWithSSA_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765TypeOfBuildingChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button = InlineKeyboardButton("Квартира", callback_data="Ste")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Апартаменты", callback_data="Apt")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Этаж", callback_data="Flr")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI765MailingAddressChoiceKeyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button_yes = InlineKeyboardButton("Да", callback_data="FormI765_MailingSameAsPhysical_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="FormI765_MailingSameAsPhysical_No")
        keyboard_markup.add(button_no)
        # button_empty = InlineKeyboardButton("Оставить пустым", callback_data="MailingEmpty")
        # keyboard_markup.add(button_empty)
        self.markup = keyboard_markup
