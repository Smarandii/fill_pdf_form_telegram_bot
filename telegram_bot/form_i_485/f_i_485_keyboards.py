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


class FormI485SSACouldUseInformationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="SSACouldUseInformation_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="SSACouldUseInformation_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485WasInspectedAtPortOfEntryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="WasInspectedAtPortOfEntry_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="WasInspectedAtPortOfEntry_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485SpecialCategoryEntryGrantedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="SpecialCategoryEntryGranted_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="SpecialCategoryEntryGranted_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485I94WasIssuedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="I94WasIssued_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="I94WasIssued_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ImmigrationStatusDontChangedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Иммиграционный статус не изменился",
                                      callback_data="ImmigrationStatusDontChanged_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485CameIntoUSWithoutAdmissionOrParoleChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="CameIntoUSWithoutAdmissionOrParole_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="CameIntoUSWithoutAdmissionOrParole_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ApplicationByFamilyCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ApplicationByFamilyCategory_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ApplicationByFamilyCategory_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485SSAChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="SSAChoice_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="SSAChoice_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485DontNeedAlternateMailingAddressChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Не нуждаюсь в альтернативном адресе",
                                      callback_data="don't_need_alternate_mailing_address")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нуждаюсь в альтернативном адресе",
                                      callback_data="need_alternate_mailing_address")
        keyboard_markup.add(button)
        self.markup = keyboard_markup
