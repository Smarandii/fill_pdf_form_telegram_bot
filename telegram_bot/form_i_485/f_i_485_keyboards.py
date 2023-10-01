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


class FormI485ParentHasDifferentName:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ParentHasDifferentName_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ParentHasDifferentName_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ParentNotAlive:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Родитель 1 скончался(лась)", callback_data="ParentNotAlive_Yes")
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


class FormI485TypeOfEmploymentBasedCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Иностранный наемный работник, форма I-140",
                                      callback_data="TypeOfEmploymentBasedCategory_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Иностранный предприниматель, форма I-526",
                                      callback_data="TypeOfEmploymentBasedCategory_2")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ApplicationBySpecialImmigrantCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ApplicationBySpecialImmigrantCategory_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ApplicationBySpecialImmigrantCategory_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ApplicationByAsyleeOrRefugeeCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ApplicationByAsyleeOrRefugeeCategory_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ApplicationByAsyleeOrRefugeeCategory_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ApplicationByHumanTraffickingVictimCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ApplicationByHumanTraffickingVictimCategory_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ApplicationByHumanTraffickingVictimCategory_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ApplicationBySpecialProgramsBasedCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ApplicationBySpecialProgramsBasedCategory_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ApplicationBySpecialProgramsBasedCategory_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ApplicationByOtherCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ApplicationByOtherCategory_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ApplicationByOtherCategory_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form485SpouceApllyingTooChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="SpouceApllyingToo_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="SpouceApllyingToo_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485BeenMarriedBeforeChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="BeenMarriedBefore_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="BeenMarriedBefore_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485HaveKidsChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="HaveKids_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="HaveKids_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ChildApplyingTooChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ChildApplyingToo_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ChildApplyingToo_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485EthnicityChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("1.", callback_data="Ethnicity_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.", callback_data="Ethnicity_2")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485IChooseAllOfMyRaces:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Продолжить заполнение формы", callback_data="continue")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485RaceChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=5)
        button = InlineKeyboardButton("1.", callback_data="Race_Euro")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.", callback_data="Race_Asia")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.", callback_data="Race_Negro")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("4.", callback_data="Race_AmericanIndian")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("5.", callback_data="Race_HawaiiOrPacificOcean")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485EyeColorChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=9)
        button = InlineKeyboardButton("Черный", callback_data="Black")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Серый ", callback_data="Gray")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Темно-бордовый", callback_data="Maroon")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Синий", callback_data="Blue")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Зеленый", callback_data="Green")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Розовый", callback_data="Pink")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Коричневый", callback_data="Brown")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Светло-коричневый", callback_data="Hazel")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Иное", callback_data="Unknown/Other")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485IHairColorChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=9)
        button = InlineKeyboardButton("Лысый", callback_data="Bald (No hair)")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Черный", callback_data="Black")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Блонд", callback_data="Blond")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Коричневый", callback_data="Brown")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Серый", callback_data="Gray")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Рыжий", callback_data="Red")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Золотистый", callback_data="Sandy")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Белый", callback_data="White")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Иное", callback_data="Unknown/Other")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485IsYourSpouceInArmyChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="IsYourSpouceInArmy_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="IsYourSpouceInArmy_No")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Не обладаю информацией", callback_data="IsYourSpouceInArmy_DoNotKnow")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485TypeOfSpecialImmigrantCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=5)
        button = InlineKeyboardButton("1.",
                                      callback_data="TypeOfSpecialImmigrantCategory_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.",
                                      callback_data="TypeOfSpecialImmigrantCategory_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.",
                                      callback_data="TypeOfSpecialImmigrantCategory_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("4.",
                                      callback_data="TypeOfSpecialImmigrantCategory_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("5.",
                                      callback_data="TypeOfSpecialImmigrantCategory_5")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485MaritalStatusChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=5)
        button = InlineKeyboardButton("1.",
                                      callback_data="MaritalStatus_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.",
                                      callback_data="MaritalStatus_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.",
                                      callback_data="MaritalStatus_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("4.",
                                      callback_data="MaritalStatus_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("5.",
                                      callback_data="MaritalStatus_5")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("6.",
                                      callback_data="MaritalStatus_6")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485TypeOfOtherCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=5)
        button = InlineKeyboardButton("1.",
                                      callback_data="TypeOfOtherCategory_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.",
                                      callback_data="TypeOfOtherCategory_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.",
                                      callback_data="TypeOfOtherCategory_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("4.",
                                      callback_data="TypeOfOtherCategory_4")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485TypeOfSpecialProgramsCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=7)
        button = InlineKeyboardButton("1.",
                                      callback_data="TypeOfSpecialProgramsCategory_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.",
                                      callback_data="TypeOfSpecialProgramsCategory_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.",
                                      callback_data="TypeOfSpecialProgramsCategory_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("4.",
                                      callback_data="TypeOfSpecialProgramsCategory_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("5.",
                                      callback_data="TypeOfSpecialProgramsCategory_5")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("6.",
                                      callback_data="TypeOfSpecialProgramsCategory_6")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("7.",
                                      callback_data="TypeOfSpecialProgramsCategory_7")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485IndicateEducationLevel:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=9)
        button = InlineKeyboardButton("1.",
                                      callback_data="IndicateEducationLevel_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.",
                                      callback_data="IndicateEducationLevel_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.",
                                      callback_data="IndicateEducationLevel_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("4.",
                                      callback_data="IndicateEducationLevel_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("5.",
                                      callback_data="IndicateEducationLevel_5")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("6.",
                                      callback_data="IndicateEducationLevel_6")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("7.",
                                      callback_data="IndicateEducationLevel_7")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("8.",
                                      callback_data="IndicateEducationLevel_8")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("9.",
                                      callback_data="IndicateEducationLevel_9")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485AnnualHouseHoldIncome:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=7)
        button = InlineKeyboardButton("$0-27,000",
                                      callback_data="AnnualHouseHoldIncome_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$27,001-52,000",
                                      callback_data="AnnualHouseHoldIncome_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$52,001-85,000",
                                      callback_data="AnnualHouseHoldIncome_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$85,001-141,000",
                                      callback_data="AnnualHouseHoldIncome_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Более $141,000",
                                      callback_data="AnnualHouseHoldIncome_5")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485HouseHoldNetWorth:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=7)
        button = InlineKeyboardButton("$0-18,400",
                                      callback_data="HouseHoldNetWorth_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$18,401-136,000",
                                      callback_data="HouseHoldNetWorth_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$136,001-321,400",
                                      callback_data="HouseHoldNetWorth_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$321,401-707,100",
                                      callback_data="HouseHoldNetWorth_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Более $707,100",
                                      callback_data="HouseHoldNetWorth_5")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485HouseHoldDebt:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=7)
        button = InlineKeyboardButton("$0",
                                      callback_data="HouseHoldDebt_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$1-10,100",
                                      callback_data="HouseHoldDebt_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$10,101-57,700",
                                      callback_data="HouseHoldDebt_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("$57,701-186,800",
                                      callback_data="HouseHoldDebt_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Более $186,800",
                                      callback_data="HouseHoldDebt_5")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485TypeOfAsyleeOrRefugeeCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("1.",
                                      callback_data="TypeOfAsyleeOrRefugeeCategory_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.",
                                      callback_data="TypeOfAsyleeOrRefugeeCategory_2")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485TypeOfHumanTraffickingVictimCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("1.",
                                      callback_data="TypeOfHumanTraffickingVictimCategory_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.",
                                      callback_data="TypeOfHumanTraffickingVictimCategory_2")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485AddressWasProvidedAbove:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Адрес был указан выше",
                                      callback_data="AddressWasProvidedAbove")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485RecentEmploymentListedAbove:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Место работы было указано выше",
                                      callback_data="AddressWasProvidedAbove")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ImmigrantVisaDecisionStatusChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        button = InlineKeyboardButton("Заявление утверждено",
                                      callback_data="ImmigrantVisaDecisionStatus_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Заявление отклонено",
                                      callback_data="ImmigrantVisaDecisionStatus_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Заявление отозвано",
                                      callback_data="ImmigrantVisaDecisionStatus_3")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ApplicationByWorkingCategoryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ApplicationByWorkingCategory_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ApplicationByWorkingCategory_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485IGeneralEligibilityChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="GeneralEligibility_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="GeneralEligibility_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485WasEverRefusedToEnterUSAChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="WasEverRefusedToEnterUSA_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="WasEverRefusedToEnterUSA_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485SimpleYesOrNoChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="SimpleYesOrNo_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="SimpleYesOrNo_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485ImmigrationAndNationalityActChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="ImmigrationAndNationalityAct_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="ImmigrationAndNationalityAct_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485PrincipalApplicantChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="PrincipalApplicant_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="PrincipalApplicant_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485DerivativeApplicantChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="DerivativeApplicant_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="DerivativeApplicant_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485AppliedForImmigrationVisaInOtherCountriesChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="AppliedForImmigrationVisaInOtherCountries_Yes")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="AppliedForImmigrationVisaInOtherCountries_No")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI485TypeOfFamilyCategoryApplicationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=5)
        button = InlineKeyboardButton("1.", callback_data="TypeOfFamilyCategoryApplication_1")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.", callback_data="TypeOfFamilyCategoryApplication_2")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.", callback_data="TypeOfFamilyCategoryApplication_3")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("4.", callback_data="TypeOfFamilyCategoryApplication_4")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("5.", callback_data="TypeOfFamilyCategoryApplication_5")
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
