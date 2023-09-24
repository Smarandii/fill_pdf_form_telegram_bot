from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class FormI589GenderChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Женский", callback_data="female")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Мужской", callback_data="male")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589IfAnyChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Отсутствуют запрашиваемые сведения", callback_data="don't_have_it")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589IfPreviouslyInUs:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Ранее не был в США", callback_data="not_previously_in_us")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589IfApplicable:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Не применимо", callback_data="not_applicable")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589MailingAddressChoiceKeyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Не отличается", callback_data="MailingSameAsResidence_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Отличается", callback_data="MailingSameAsResidence_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class FormI589MaritalStatusChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        button = InlineKeyboardButton("Не состою в браке", callback_data="ms_single")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("В браке", callback_data="ms_married")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("В разводе", callback_data="ms_divorced")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Вдова(-ец)", callback_data="ms_widowed")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589ImmigrationCourtChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button = InlineKeyboardButton("1.", callback_data="never_been_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.", callback_data=f"now_in_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("3.", callback_data="not_now_but_been_in_imc")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589SpouseImmigrationCourtChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_spouse_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_spouse_imc")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589ChildImmigrationCourtChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_child_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_child_imc")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589IncludeSpouseChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_include_spouse")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_include_spouse")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589IncludeChildChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_include_child")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_include_child")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FillNextChildChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_fill_next_child")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_fill_next_child")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589HaveChildrenChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("1.",
                                      callback_data="dont_have_children")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("2.", callback_data="have_children")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI94NumberChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("У меня нет номера I-94", callback_data="blank_i_94")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589EnglishFluencyChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_eng_fluent")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_eng_fluent")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589LocationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_location")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_location")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589MotherDeceasedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_mother_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_mother_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FatherDeceasedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_father_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_father_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI5891siblingDeceasedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_1sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_1sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI5892siblingDeceasedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_2sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_2sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI5893siblingDeceasedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_3sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_3sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI5894siblingDeceasedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_4sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_4sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589AsylumReasonChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Расы", callback_data="race_asylum_reason")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Религии", callback_data="religion_asylum_reason")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Национальности", callback_data="nationality_asylum_reason")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Политического мнения", callback_data="political_asylum_reason")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Принадлежности к определенной социальной группе", callback_data="membership_asylum_reason")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Конвенции против пыток", callback_data="torture_asylum_reason")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FamilyExperiencedHarmChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_family_harm")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_family_harm")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589YouFearHarmOrMistreatmentChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_you_fear_harm")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_you_fear_harm")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589YouOrFamilyAccusedChargedArrestedDetainedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_violated_law")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_violated_law")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589YouBeenAssociatedWithAnyOrganizationsChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Been_Associated_With_Any_Organizations")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Been_Associated_With_Any_Organizations")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589YouContinueToParticipateInOrganizationsChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Continue_To_Participate_In_Organizations")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Continue_To_Participate_In_Organizations")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589YouAfraidOfBeingSubjectedToTortureChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Afraid_Of_Being_Subjected_To_Torture")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Afraid_Of_Being_Subjected_To_Torture")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FamilyAppliedForUsrefugeeStatusChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Applied_For_USRefugee_Status")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Applied_For_USRefugee_Status")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FamilyTravelOrResideInOtherCountriesBeforeUsChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Travel_Or_Reside_In_Other_Countries_Before_US")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Travel_Or_Reside_In_Other_Countries_Before_US")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FamilyRecievedAnyLawfulStatusChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Recieved_Any_Lawful_Status")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Recieved_Any_Lawful_Status")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589YouOrFamilyCausedHarmOrSufferingChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Or_Family_Caused_Harm_Or_Suffering")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Or_Family_Caused_Harm_Or_Suffering")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589ReturnedToBadCountryChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Returned_To_Bad_Country")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Returned_To_Bad_Country")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589LastArrivalToUsMoreThan1YearChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Last_Arrival_To_US_More_Than_1_Year")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Last_Arrival_To_US_More_Than_1_Year")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589YouOrFamilyDidCrimeChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Or_Family_Did_Crime")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Or_Family_Did_Crime")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FamilyHelpedCompleteApplicationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FamilyHelpedCompleteFillNextMemberChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Helped_Complete_Fill_Next_Member_Choice")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Helped_Complete_Fill_Next_Member_Choice")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589NotFamilyHelpedCompleteApplicationChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Not_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Not_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589ProvidedWithListOfPersonsWhoMayAssistChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Provided_With_List_Of_Persons_Who_May_Assist")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Provided_With_List_Of_Persons_Who_May_Assist")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589FormG28AttachedChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Form_G_28_Attached")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Form_G_28_Attached")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589AllTrueOrNotTrueApplication:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_All_True_Or_Not_True_Application")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_All_True_Or_Not_True_Application")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class FormI589HaveSiblingsChoice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("братья/сестры отсутствуют", callback_data="have_no_siblings")
        keyboard_markup.add(button)
        self.markup = keyboard_markup