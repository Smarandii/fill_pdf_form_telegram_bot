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


class FormI131HowMuchTimeSpentOutsideUSChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=6)
        button_yes = InlineKeyboardButton("Менее 6 месяцев.", callback_data="HowMuchTimeSpentOutsideUS_1")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("От 6 месяцев до 1 года.", callback_data="HowMuchTimeSpentOutsideUS_2")
        keyboard_markup.add(button_no)
        button_empty = InlineKeyboardButton("От 1 до 2 лет.", callback_data="HowMuchTimeSpentOutsideUS_3")
        keyboard_markup.add(button_empty)
        button_yes = InlineKeyboardButton("От 2 до 3 лет.", callback_data="ApplicationType_4")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("От 3 до 4 лет.", callback_data="HowMuchTimeSpentOutsideUS_5")
        keyboard_markup.add(button_no)
        button_empty = InlineKeyboardButton("Более 4 лет.", callback_data="HowMuchTimeSpentOutsideUS_6")
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


class FormI131HaveEverFiledFederalIncomeTaxReturnChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="HaveEverFiledFederalIncomeTaxReturn_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="HaveEverFiledFederalIncomeTaxReturn_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131ApplyingForTravelDocumentOfRefugeeChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="ApplyingForTravelDocumentOfRefugee_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="ApplyingForTravelDocumentOfRefugee_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131ApplyingForAdvancedParoleChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="ApplyingForAdvancedParole_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="ApplyingForAdvancedParole_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131HowManyTripsChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("1 поездка", callback_data="HowManyTrips_1")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Более 1 поездки", callback_data="HowManyTrips_2")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131AddressOfNotificationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("1.", callback_data="AddressOfNotification_1")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("2.", callback_data="AddressOfNotification_2")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131EmploymentAuthorizationDocumentForNewPeriodOfParoleUnderOperationAlliesWelcomeChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да",
                                          callback_data="OperationAlliesWelcome_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет",
                                         callback_data="OperationAlliesWelcome_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131UnderFearOfPunishmentForDisinformationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да",
                                          callback_data="UnderFearOfPunishmentForDisinformation_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет",
                                         callback_data="UnderFearOfPunishmentForDisinformation_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131IntendToComebackChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="IntendToComeback_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="IntendToComeback_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131HaveEverCameBackChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="HaveEverCameBack_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="HaveEverCameBack_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131HaveEverIssuedPassportChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="HaveEverIssuedPassport_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="HaveEverIssuedPassport_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131HaveEverGotHelpFromGovernmentChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="HaveEverGotHelpFromGovernment_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="HaveEverGotHelpFromGovernment_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131RestoredCitizenshipOfLeftCountryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="RestoredCitizenshipOfLeftCountry_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="RestoredCitizenshipOfLeftCountry_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131GotNewCitizenshipChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="GotNewCitizenship_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="GotNewCitizenship_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI131GotRefugeeStatusElsewhereChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="GotRefugeeStatusElsewhere_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="GotRefugeeStatusElsewhere_No")
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


class FormI131ApplyingForReentryPermitChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Да", callback_data="ApplyingForReentryPermit_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Нет", callback_data="ApplyingForReentryPermit_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup
