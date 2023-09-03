from telegram_bot import InlineKeyboardMarkup, InlineKeyboardButton


class Form_I_589_Gender_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Женский", callback_data="female")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Мужской", callback_data="male")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_If_Any_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("У меня этого нет", callback_data="don't_have_it")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_If_Previously_In_US:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Ранее не был в США", callback_data="not_previously_in_us")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_If_Applicable:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Не применимо", callback_data="not_applicable")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Mailing_Address_Choice_Keyboard:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button_yes = InlineKeyboardButton("Почтовый адрес тот же", callback_data="MailingSameAsResidence_Yes")
        keyboard_markup.add(button_yes)
        button_no = InlineKeyboardButton("Почтовый адрес другой", callback_data="MailingSameAsResidence_No")
        keyboard_markup.add(button_no)
        self.markup = keyboard_markup


class Form_I_589_Marital_Status_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        button = InlineKeyboardButton("Не в браке", callback_data="ms_single")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("В браке", callback_data="ms_married")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("В разводе", callback_data="ms_divorced")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Вдова(-ец)", callback_data="ms_widowed")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Immigration_Court_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        button = InlineKeyboardButton("Я никогда не участвовал в разбирательствах в иммиграционном суде.", callback_data="never_been_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Сейчас я нахожусь на рассмотрении иммиграционного суда.", callback_data=f"now_in_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("В прошлом я участвовал в разбирательствах в иммиграционном суде.", callback_data="not_now_but_been_in_imc")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Spouse_Immigration_Court_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_spouse_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_spouse_imc")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Child_Immigration_Court_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_child_imc")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_child_imc")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Include_Spouse_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_include_spouse")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_include_spouse")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Include_Child_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_include_child")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_include_child")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Fill_Next_Child_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_fill_next_child")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_fill_next_child")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Have_Children_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("У меня нет детей. (Перейдите к части A.III. «Информация о вашем прошлом».)",
                                      callback_data="dont_have_children")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("У меня есть дети", callback_data="have_children")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_94_Number_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("У меня нет номера I-94", callback_data="blank_i_94")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_English_Fluency_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_eng_fluent")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_eng_fluent")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Location_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_location")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_location")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Mother_Deceased_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_mother_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_mother_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Father_Deceased_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_father_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_father_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_1Sibling_Deceased_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_1sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_1sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_2Sibling_Deceased_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_2sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_2sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_3Sibling_Deceased_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_3sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_3sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_4Sibling_Deceased_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_4sibling_deceased")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_4sibling_deceased")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Asylum_Reason_Choice:
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


class Form_I_589_Family_Experienced_Harm_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_family_harm")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_family_harm")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_You_Fear_Harm_Or_Mistreatment_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_you_fear_harm")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_you_fear_harm")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_You_Or_Family_Accused_Charged_Arrested_Detained_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_violated_law")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_violated_law")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_You_Been_Associated_With_Any_Organizations_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Been_Associated_With_Any_Organizations")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Been_Associated_With_Any_Organizations")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_You_Continue_To_Participate_In_Organizations_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Continue_To_Participate_In_Organizations")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Continue_To_Participate_In_Organizations")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_You_Afraid_Of_Being_Subjected_To_Torture_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Afraid_Of_Being_Subjected_To_Torture")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Afraid_Of_Being_Subjected_To_Torture")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Family_Applied_For_USRefugee_Status_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Applied_For_USRefugee_Status")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Applied_For_USRefugee_Status")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Travel_Or_Reside_In_Other_Countries_Before_US")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Travel_Or_Reside_In_Other_Countries_Before_US")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Family_Recieved_Any_Lawful_Status_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Recieved_Any_Lawful_Status")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Recieved_Any_Lawful_Status")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_You_Or_Family_Caused_Harm_Or_Suffering_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Or_Family_Caused_Harm_Or_Suffering")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Or_Family_Caused_Harm_Or_Suffering")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Returned_To_Bad_Country_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Returned_To_Bad_Country")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Returned_To_Bad_Country")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Last_Arrival_To_US_More_Than_1_Year_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Last_Arrival_To_US_More_Than_1_Year")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Last_Arrival_To_US_More_Than_1_Year")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_You_Or_Family_Did_Crime_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_You_Or_Family_Did_Crime")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_You_Or_Family_Did_Crime")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Family_Helped_Complete_Application_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Family_Helped_Complete_Fill_Next_Member_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Family_Helped_Complete_Fill_Next_Member_Choice")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Family_Helped_Complete_Fill_Next_Member_Choice")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Not_Family_Helped_Complete_Application_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Not_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Not_Family_Helped_Complete_Application")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Provided_With_List_Of_Persons_Who_May_Assist_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Provided_With_List_Of_Persons_Who_May_Assist")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Provided_With_List_Of_Persons_Who_May_Assist")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_Form_G_28_Attached_Choice:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_Form_G_28_Attached")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_Form_G_28_Attached")
        keyboard_markup.add(button)
        self.markup = keyboard_markup


class Form_I_589_All_True_Or_Not_True_Application:
    def __init__(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        button = InlineKeyboardButton("Да", callback_data="yes_All_True_Or_Not_True_Application")
        keyboard_markup.add(button)
        button = InlineKeyboardButton("Нет", callback_data="no_All_True_Or_Not_True_Application")
        keyboard_markup.add(button)
        self.markup = keyboard_markup