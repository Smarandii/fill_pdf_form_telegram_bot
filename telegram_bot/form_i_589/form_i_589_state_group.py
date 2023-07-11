from aiogram.dispatcher.filters.state import State, StatesGroup


class Form_I_589(StatesGroup):
    A_I_CheckBox31_0 = State()  # Check this box if you also want to apply for withholding of removal under the Convention Against Torture.
    A_I_PtAILine1_ANumber_0 = State()  # 1 Alien Registration Number(s) (A-Number) (if any)
    A_I_TextField1_0 = State()  # 2 U.S. Social Security Number (if any)
    A_I_TextField1_8 = State()  # 3 USCIS Online Account Number (if any)
    A_I_PtAILine4_LastName_0 = State()  # 4  # Complete Last Name
    A_I_PtAILine5_FirstName_0 = State()  # 5  # First Name
    A_I_PtAILine6_MiddleName_0 = State()  # 6  # Middle Name
    A_I_TextField1_1 = State()  # 7  # What other names have you used (include maiden name and aliases)?

    A_I_PtAILine8_StreetNumandName_0 = State()  # 8 Street Number and Name
    A_I_PtAILine8_AptNumber_0 = State()  # 9 Apt. Number
    A_I_TextField1_2 = State()  # 10 City
    A_I_PtAILine8_State_0 = State()  # 11 State
    A_I_PtAILine8_Zipcode_0 = State()  # 12 Zip Code
    A_I_PtAILine8_AreaCode_0 = State()  # 13 Telephone Area Code
    A_I_PtAILine8_TelephoneNumber_0 = State()  # 14  # Telephone Number

    A_I_PtAILine9_InCareOf_0 = State()  # 15  # In Care Of (if applicable)
    A_I_PtAILine9_AreaCode_0 = State()  # 16  # Telephone Area Code
    A_I_PtAILine9_TelephoneNumber_0 = State()  # 17  # Telephone Number
    A_I_PtAILine9_StreetNumandName_0 = State()  # 18 Street Number and Name
    A_I_PtAILine9_AptNumber_0 = State()  # 19 Apt. Number
    A_I_PtAILine9_City_0 = State()  # 20 City
    A_I_PtAILine9_State_0 = State()  # 21 State
    A_I_PtAILine9_ZipCode_0 = State()  # 22 Zip Code

    A_I_ChooseGender = State()
    # A_I_PartALine9Gender_0 = State()  # Gender Male
    # A_I_PartALine9Gender_1 = State()  # Gender Female

    A_I_ChooseMaritalStatus = State()
    # A_I_Marital_0 = State()  # Marital Status Single
    # A_I_Marital_1 = State()  # Marital Status Married
    # A_I_Marital_2 = State()  # Marital Status Divorced
    # A_I_Marital_3 = State()  # Marital Status Widowed

    A_I_DateTimeField1_0 = State()  # 23 Date of Birth (mm/dd/yyyy)
    A_I_TextField1_4 = State()  # 24  # City and Country of Birth
    A_I_TextField1_3 = State()  # 25  # Present Nationality (Citizenship)
    A_I_TextField1_5 = State()  # 26  # Nationality at Birth
    A_I_TextField1_6 = State()  # 27  # Race Ethnic or Tribal Group
    A_I_TextField1_7 = State()  # 28 Religion

    A_I_ChooseImmigrationCourtProceedingsStatus = State()
    # A_I_CheckBox3_0 = State()  # I have never been in Immigration Court proceedings.
    # A_I_CheckBox3_1 = State()  # I am now in Immigration Court proceedings.
    # A_I_CheckBox3_2 = State()  # I am not now in Immigration Court proceedings but I have been in the past.

    A_I_DateTimeField6_0 = State()  # 29 When did you last leave your country? (mm/dd/yyyy)
    A_I_TextField3_0 = State()  # 30 What is your current I-94  # Number if any?

    A_I_DateTimeField2_0 = State()  # 31 Date
    A_I_TextField4_0 = State()  # 32 Place
    A_I_TextField4_1 = State()  # 33 Status
    A_I_DateTimeField2_1 = State()  # 34 Date Status Expires

    A_I_DateTimeField3_0 = State()  # 35  # Date
    A_I_TextField4_2 = State()  # 36  # Place
    A_I_TextField4_3 = State()  # 37  # Status

    A_I_DateTimeField4_0 = State()  # 38  # Date
    A_I_TextField4_4 = State()  # 39 Place
    A_I_TextField4_5 = State()  # 40 Status

    A_I_TextField5_0 = State()  # 41 What country issued your last passport or travel document?
    A_I_TextField5_1 = State()  # 42 Passport Number
    A_I_TextField5_2 = State()  # 43 Travel Document Number
    A_I_DateTimeField2_2 = State()  # 44  # Expiration Date (mm/dd/yyyy)

    A_I_TextField7_0 = State()  # 45  # What is your native language (include dialect if applicable)?

    A_I_EngFluencyChoice = State()
    # A_I_CheckBox4_1 = State()  # Are you fluent in English? Yes
    # A_I_CheckBox4_0 = State()  # Are you fluent in English? No

    A_I_TextField7_1 = State()  # 46  # What other languages do you speak fluently?

    # A_I_TextField8_0 = State()  # 47  # For EOIR use only_
    # A_I_DateTimeField2_6 = State()  # 48 Interview Date
    # A_I_TextField9_0 = State()  # 49 Asylum Officer ID No_
    # A_I_DateTimeField2_3 = State()  # 50 Approval Date
    # A_I_DateTimeField2_4 = State()  # 51 Denial Date
    # A_I_DateTimeField2_5 = State()  # 52 Referral Date

    # Spouse
    A_II_NotMarried_0_PtAIILine1_ANumber_0 = State()  # 53 Alien Registration Number of your spouse (A-Number) (if any)
    A_II_NotMarried_0_TextField10_1 = State()  # 54  # Passport/ID Card Number (if any)
    A_II_NotMarried_0_DateTimeField7_0 = State()  # 55  # Date of Birth (mm/dd/yyyy)
    A_II_NotMarried_0_TextField10_2 = State()  # 56  # U_S_ Social Security Number (if any)
    A_II_NotMarried_0_PtAIILine5_LastName_0 = State()  # 57  # Complete Last Name
    A_II_NotMarried_0_PtAIILine6_FirstName_0 = State()  # 58 First Name
    A_II_NotMarried_0_PtAIILine7_MiddleName_0 = State()  # 59 Middle Name
    A_II_NotMarried_0_TextField10_3 = State()  # 60 Other names used (include maiden name and aliases)
    A_II_NotMarried_0_DateTimeField8_0 = State()  # 61 Date of Marriage (mm/dd/yyyy)
    A_II_NotMarried_0_TextField10_4 = State()  # 62 Place of Marriage
    A_II_NotMarried_0_TextField10_5 = State()  # 63 City and Country of Birth
    A_II_NotMarried_0_TextField10_0 = State()  # 64  # Nationality (Citizenship)
    A_II_NotMarried_0_TextField10_6 = State()  # 65  # Race Ethnic or Tribal Group

    A_II_ChooseGenderSpouse = State()
    # A_II_NotMarried_0_CheckBox14_Gender_0 = State()  # Gender Male
    # A_II_NotMarried_0_CheckBox14_Gender_1 = State()  # Gender Female

    A_II_IsInUSChoiceSpouse = State()
    # A_II_NotMarried_0_PtAIILine15_CheckBox15_1 = State()  # Is this person in the U_S_? Yes (Complete Blocks 16  # to 24_)
    # A_II_NotMarried_0_PtAIILine15_CheckBox15_0 = State()  # Is this person in the U_S_? No (Specify location) = State()

    A_II_NotMarried_0_PtAIILine15_Specify_0 = State()  # 66  # Specify location
    A_II_NotMarried_0_PtAIILine16_PlaceofLastEntry_0 = State()  # 67  # Place of last entry into the U_S_
    A_II_NotMarried_0_PtAIILine17_DateofLastEntry_0 = State()  # 68 Date of last entry into the U_S_ (mm/dd/yyyy)
    A_II_NotMarried_0_PtAIILine18_I94Number_0 = State()  # 69 I-94  # Number (if any)
    A_II_NotMarried_0_PtAIILine19_StatusofLastAdmission_0 = State()  # 70 Status when last admitted (Visa type if any)
    A_II_NotMarried_0_PtAIILine20_SpouseCurrentStatus_0 = State()  # 71 What is your spouse s current status?
    A_II_NotMarried_0_PtAIILine21_ExpDateofAuthorizedStay_0 = State()  # 72 What is the expiration date of his/her authorized stay if any? (mm/dd/yyyy)

    A_II_IsImmigrationCourtProceedingsSpouse = State()
    # A_II_NotMarried_0_PtAIILine22_Yes_0 = State()  # Is your spouse in Immigration Court proceedings? Yes
    # A_II_NotMarried_0_PtAIILine22_No_0 = State()  # Is your spouse in Immigration Court proceedings? No

    A_II_NotMarried_0_PtAIILine23_PreviousArrivalDate_0 = State()  # 73 If previously in the U_S_ date of previous arrival (mm/dd/yyyy)

    A_II_IsSpouseIncludedInApplication = State()
    # A_II_NotMarried_0_PtAIILine24_Yes_0 = State()  # If in the U_S_ is your spouse to be included in this application? (Check the appropriate box_) Yes
    # A_II_NotMarried_0_PtAIILine24_No_0 = State()  # If in the U_S_ is your spouse to be included in this application? (Check the appropriate box_) No

    # Children
    A_II_HaveChildrenChoice = State()
    # A_II_ChildrenCheckbox_1 = State()  # I do not have any children_ (Skip to Part A_III_ Information about your background_)
    # A_II_ChildrenCheckbox_0 = State()  # I have children_
    A_II_TotalChild_0 = State()  # 74  # Total number of children

    # Child 1
    A_II_ChildAlien1_0 = State()  # 75  # Alien Registration Number (A-Number) (if any)
    A_II_ChildPassport1_0 = State()  # 76  # Passport/ID Card Number (if any
    A_II_ChildMarital1_0 = State()  # 77  # Marital Status (Married Single Divorced Widowed)
    A_II_ChildSSN1_0 = State()  # 78 U_S_ Social Security Number (if any
    A_II_ChildLast1_0 = State()  # 80 Complete Last Name
    A_II_ChildFirst1_0 = State()  # 81 First Name
    A_II_ChildMiddle1_0 = State()  # 82 Middle Name
    A_II_ChildDOB1_0 = State()  # 83 Date of Birth (mm/dd/yyyy)
    A_II_ChildCity1_0 = State()  # 84  # City and Country of Birth
    A_II_ChildNat1_0 = State()  # 85  # Nationality (Citizenship)
    A_II_ChildRace1_0 = State()  # 86  # Race Ethnic or Tribal Group

    A_II_ChooseGenderChild1 = State()
    # A_II_CheckBox16_0 = State()  # Gender Male
    # A_II_CheckBox16_1 = State()  # Gender Female

    A_II_ChooseLocationChild1 = State()
    # A_II_CheckBox17_0 = State()  # Yes (Complete Blocks 14  # to 21_)
    # A_II_CheckBox17_1 = State()  # No (Specify location) = State()  # {PtAIILine13_Specify_0}

    A_II_PtAIILine13_Specify_0 = State()  # 87  # (Specify location)
    A_II_PtAIILine14_PlaceofLastEntry_0 = State()  # 88 Place of last entry into the U_S_
    A_II_PtAIILine15_ExpirationDate_0 = State()  # 89 Date of last entry into the U_S_ (mm/dd/yyyy)
    A_II_PtAIILine16_I94Number_0 = State()  # 90 I-94  # Number (If any)
    A_II_PtAIILine17_StatusofLastAdmission_0 = State()  # 91 Status when last admitted (Visa type if any
    A_II_PtAIILine18_CurrentStatusofChild_0 = State()  # 92 What is your child s current status?
    A_II_PtAIILine19_ExpDateofAuthorizedStay_0 = State()  # 93 What is the expiration date of his/her authorized stay if any? (mm/dd/yyyy)

    A_II_IsImmigrationCourtProceedingsChild1 = State()
    # A_II_PtAIILine20_Yes_0 = State()  # Is your child in Immigration Court proceedings? Yes
    # A_II_PtAIILine20_No_0 = State()  # Is your child in Immigration Court proceedings? No

    A_II_IsIncludedInApplicationChild1 = State()
    # A_II_PtAIILine21_Yes_0 = State()  # If in the U_S_ is this child to be included in this application? Yes
    # A_II_PtAIILine21_No_0 = State()  # If in the U_S_ is this child to be included in this application? No

    A_II_IsFillChild2 = State()

    # Child 2
    A_II_ChildAlien2_0 = State()  # 94  # Alien Registration Number (A-Number) (if any)
    A_II_ChildPassport2_0 = State()  # 95  # Passport/ID Card Number (if any)
    A_II_ChildMarital2_0 = State()  # 96  # Marital Status (Married Single Divorced Widowed)
    A_II_ChildSSN2_0 = State()  # 97  # U_S_ Social Security Number (if any)
    A_II_ChildLast2_0 = State()  # 98 Complete Last Name
    A_II_ChildFirst2_0 = State()  # 99 First Name
    A_II_ChildMiddle2_0 = State()  # 100 Middle Name
    A_II_ChildDOB2_0 = State()  # 101 Date of Birth (mm/dd/yyyy)
    A_II_ChildCity2_0 = State()  # 102 City and Country of Birth
    A_II_ChildNat2_0 = State()  # 103 Nationality (Citizenship)
    A_II_ChildRace2_0 = State()  # 104  # Race Ethnic or Tribal Group

    A_II_ChooseGenderChild2 = State()
    # A_II_CheckBox26_Gender_0 = State()  # Gender Male
    # A_II_CheckBox26_Gender_1 = State()  # Gender Female

    A_II_ChooseLocationChild2 = State()
    # A_II_CheckBox27_0 = State()  # Is this child in the U_S_ ? Yes (Complete Blocks 14  # to 21_)
    # A_II_CheckBox27_1 = State()  # Is this child in the U_S_ ? No (Specify location) = State()  # {_3_PtAIILine13_Specify2_0}

    A_II_PtAIILine13_Specify2_0 = State()  # 105  # Specify location
    A_II_PtAIILine14_PlaceofLastEntry2_0 = State()  # 106  # Place of last entry into the U_S_
    A_II_PtAIILine15_DateofLastEntry2_0 = State()  # 107  # Date of last entry into the U_S_ (mm/dd/yyyy)
    A_II_PtAIILine16_I94Number2_0 = State()  # 108 I-94  # Number (If any)
    A_II_PtAIILine17_StatusofLastAdmission2_0 = State()  # 109 Status when last admitted (Visa type if any)
    A_II_PtAIILine18_ChildCurrentStatus2_0 = State()  # 110 What is your child s current status?
    A_II_PtAIILine19_ExpDateofAuthorizedStay2_0 = State()  # 111 What is the expiration date of his/her authorized stay if any? (mm/dd/yyyy)

    A_II_IsImmigrationCourtProceedingsChild2 = State()
    # A_II_PtAIILine20_Yes2_0 = State()  # Is your child in Immigration Court proceedings? Yes
    # A_II_PtAIILine20_No2_0 = State()  # Is your child in Immigration Court proceedings? No

    A_II_IsIncludedInApplicationChild2 = State()
    # A_II_PtAIILine21_Yes2_0 = State()  # If in the U_S_ is this child to be included in this application? Yes
    # A_II_PtAIILine21_No2_0 = State()  # If in the U_S_ is this child to be included in this application? No

    A_II_IsFillChild3 = State()

    # Child 3
    A_II_ChildAlien3_0 = State()  # 112 Alien Registration Number (A-Number) (if any)
    A_II_ChildPassport3_0 = State()  # 113 Passport/ID Card Number (if any)
    A_II_ChildMarital3_0 = State()  # 114  # Marital Status (Married Single Divorced Widowed)
    A_II_ChildSSN3_0 = State()  # 115  # U_S_ Social Security Number (if any)
    A_II_ChildLast3_0 = State()  # 116  # Complete Last Name
    A_II_ChildFirst3_0 = State()  # 117  # First Name
    A_II_ChildMiddle3_0 = State()  # 118 Middle Name
    A_II_ChildDOB3_0 = State()  # 119 Date of Birth (mm/dd/yyyy)
    A_II_ChildCity3_0 = State()  # 120 City and Country of Birth
    A_II_ChildNat3_0 = State()  # 121 Nationality (Citizenship)
    A_II_ChildRace3_0 = State()  # 122 Race Ethnic or Tribal Group

    A_II_ChooseGenderChild3 = State()
    # A_II_CheckBox36_Gender_0 = State()  # Gender Male
    # A_II_CheckBox36_Gender_1 = State()  # Gender Female

    A_II_ChooseLocationChild3 = State()
    # A_II_CheckBox37_0 = State()  # Is this child in the U_S_ ? Yes (Complete Blocks 14  # to 21_)
    # A_II_CheckBox37_1 = State()  # Is this child in the U_S_ ? No (Specify location) = State()  # {_3_PtAIILine13_Specify3_0}

    A_II_PtAIILine13_Specify3_0 = State()  # 123 Specify location
    A_II_PtAIILine14_PlaceofLastEntry3_0 = State()  # 124  # Place of last entry into the U_S_
    A_II_PtAIILine15_DateofLastEntry3_0 = State()  # 125  # Date of last entry into the U_S_ (mm/dd/yyyy)
    A_II_PtAIILine16_I94Number3_0 = State()  # 126  # I-94  # Number (If any)
    A_II_PtAIILine17_StatusofLastAdmission3_0 = State()  # 127  # Status when last admitted (Visa type if any)
    A_II_PtAIILine18_ChildCurrentStatus3_0 = State()  # 128 What is your child s current status?
    A_II_PtAIILine19_ExpDateofAuthorizedStay3_0 = State()  # 129 What is the expiration date of his/her authorized stay if any? (mm/dd/yyyy)

    A_II_IsImmigrationCourtProceedingsChild3 = State()
    # A_II_PtAIILine20_Yes3_0 = State()  # Is your child in Immigration Court proceedings? yes
    # A_II_PtAIILine20_No3_0 = State()  # Is your child in Immigration Court proceedings? no

    A_II_IsIncludedInApplicationChild3 = State()
    # A_II_PtAIILine21_Yes3_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) Yes
    # A_II_PtAIILine21_No3_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) No

    A_II_IsFillChild4 = State()

    # Child 4
    A_II_ChildAlien4_0 = State()  # 130 Alien Registration Number (A-Number) (if any)
    A_II_ChildPassport4_0 = State()  # 131 Passport/ID Card Number (if any
    A_II_ChildMarital4_0 = State()  # 132 Marital Status (Married Single Divorced Widowed)
    A_II_ChildSSN4_0 = State()  # 133 U_S_ Social Security Number (if any)
    A_II_ChildLast4_0 = State()  # 134  # Complete Last Name
    A_II_ChildFirst4_0 = State()  # 135  # First Name
    A_II_ChildMiddle4_0 = State()  # 136  # Middle Name
    A_II_ChildDOB4_0 = State()  # 137  # Date of Birth (mm/dd/yyyy)
    A_II_ChildCity4_0 = State()  # 138 City and Country of Birth
    A_II_ChildNat4_0 = State()  # 139 Nationality (Citizenship)
    A_II_ChildRace4_0 = State()  # 140 Race Ethnic or Tribal Group

    A_II_ChooseGenderChild4 = State()
    # A_II_CheckBox46_Gender_0 = State()  # Gender Male
    # A_II_CheckBox46_Gender_1 = State()  # Gender Female

    A_II_ChooseLocationChild4 = State()
    # A_II_CheckBox47_0 = State()  # Is this child in the U_S_ ? Yes (Complete Blocks 14  # to 21_)
    # A_II_CheckBox47_1 = State()  # Is this child in the U_S_ ? No (Specify location) = State()  # {_3_PtAIILine13_Specify4_0}

    A_II_PtAIILine13_Specify4_0 = State()  # 141 Specify location
    A_II_PtAIILine14_PlaceofLastEntry4_0 = State()  # 142 Place of last entry into the U_S_
    A_II_PtAIILine15_DateofLastEntry4_0 = State()  # 143 Date of last entry into the U_S_ (mm/dd/yyyy)
    A_II_PtAIILine16_I94Number4_0 = State()  # 144  # I-94  # Number (If any)
    A_II_PtAIILine17_StatusofLastAdmission4_0 = State()  # 145  # Status when last admitted (Visa type if any)
    A_II_PtAIILine18_ChildCurrentStatus4_0 = State()  # 146  # What is your child s current status?
    A_II_PtAIILine19_ExpDateofAuthorizedStay4_0 = State()  # 147  # What is the expiration date of his/her authorized stay if any? (mm/dd/yyyy)

    A_II_IsImmigrationCourtProceedingsChild4 = State()
    # A_II_PtAIILine20_Yes4_0 = State()  # Is your child in Immigration Court proceedings? Yes
    # A_II_PtAIILine20_No4_0 = State()  # Is your child in Immigration Court proceedings? No

    A_II_IsIncludedInApplicationChild4 = State()
    # A_II_PtAIILine21_Yes4_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) Yes
    # A_II_PtAIILine21_No4_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) No

    Supplement_A_IsFillChild5 = State()

    # Child 5
    Supplement_A_TextField12_6 = State()  # 288 A-Number
    Supplement_A_TextField12_7 = State()  # 289 Passport/ID Card Number
    Supplement_A_TextField12_8 = State()  # 290 Marital Status
    Supplement_A_TextField12_9 = State()  # 291 U_S_ Social Security Number
    Supplement_A_TextField12_0 = State()  # 292 Complete Last Name
    Supplement_A_TextField12_2 = State()  # 293 First Name
    Supplement_A_TextField12_3 = State()  # 294  # Middle Name
    Supplement_A_DateTimeField14_0 = State()  # 295  # Date of Birth (mm/dd/yyyy)
    Supplement_A_TextField12_1 = State()  # 296  # City and Country of Birth
    Supplement_A_TextField12_4 = State()  # 297  # Nationality (Citizenship)
    Supplement_A_TextField12_5 = State()  # 298 Race Ethnic or Tribal Group

    Supplement_A_ChooseGenderChild5 = State()
    # Supplement_A_CheckBox12_Gender_0 = State()  # Gender Male
    # Supplement_A_CheckBox12_Gender_1 = State()  # Gender Female

    Supplement_A_ChooseLocationChild5 = State()
    # Supplement_A_CheckBox57_0 = State()  # Is this child in the U_S_ ? Yes
    # Supplement_A_CheckBox57_1 = State()  # Is this child in the U_S_ ? No specify location = State()  # {Supplement_A_SuppLALine13_Specify_0}

    Supplement_A_SuppLALine13_Specify_0 = State()  # 299 Specify location
    Supplement_A_ChildEntry5_0 = State()  # 300 Place of last entry into the U_S_
    Supplement_A_ChildExp5_0 = State()  # 301 Date of last entry into the U_S
    Supplement_A_ChildINum5_0 = State()  # 302 I-94  # Number
    Supplement_A_ChildStatus5_0 = State()  # 303 Status when last admitted
    Supplement_A_ChildCurrent5_0 = State()  # 304  # What is your child s current status?
    Supplement_A_ChildExpAuth5_0 = State()  # 305  # What is the expiration date of his/her authorized stay

    Supplement_A_IsImmigrationCourtProceedingsChild5 = State()
    # Supplement_A_SuppA_CheckBox20_0 = State()  # Is your child in Immigration Court proceedings? Yes
    # Supplement_A_SuppA_CheckBox20_1 = State()  # Is your child in Immigration Court proceedings? No

    Supplement_A_IsIncludedInApplicationChild5 = State()
    # Supplement_A_SuppA_CheckBox21_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) yes
    # Supplement_A_SuppA_CheckBox21_1 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) no

    Supplement_A_IsFillChild6 = State()

    # Child 6
    Supplement_A_TextField12_16 = State()  # 306  # A-Number (If available)
    Supplement_A_TextField12_17 = State()  # 307  # Passport/ID Card Number
    Supplement_A_TextField12_18 = State()  # 308 Marital Status
    Supplement_A_TextField12_19 = State()  # 309 U_S_ Social Security Number
    Supplement_A_TextField12_10 = State()  # 310 Complete Last Name
    Supplement_A_TextField12_12 = State()  # 311 First Name
    Supplement_A_TextField12_13 = State()  # 312 Middle Name
    Supplement_A_DateTimeField14_1 = State()  # 313 Date of Birth
    Supplement_A_TextField12_11 = State()  # 314  # City and Country of Birth
    Supplement_A_TextField12_14 = State()  # 315  # Nationality
    Supplement_A_TextField12_15 = State()  # 316  # Race Ethnic or Tribal Group

    Supplement_A_ChooseGenderChild6 = State()
    # Supplement_A_SuppAL12_CheckBox_0 = State()  # Gender Male
    # Supplement_A_SuppAL12_CheckBox_1 = State()  # Gender Female

    Supplement_A_ChooseLocationChild6 = State()
    # Supplement_A_SuppAL13_CheckBox_0 = State()  # Is this child in the U_S_ ? Yes
    # Supplement_A_SuppAL13_CheckBox_1 = State()  # Is this child in the U_S_ ? No

    Supplement_A_SuppLALine13_Specify2_0 = State()  # 317  # Specify location
    Supplement_A_ChildEntry6_0 = State()  # 318 Place of last entry into the U_S_
    Supplement_A_ChildExp6_0 = State()  # 319 Date of last entry into the U_S_
    Supplement_A_ChildINum6_0 = State()  # 320 I-94  # Number
    Supplement_A_ChildStatus6_0 = State()  # 321 Status when last admitted (Visa type if any)
    Supplement_A_ChildCurrent6_0 = State()  # 322 What is your child s current status?
    Supplement_A_ChildExpAuth6_0 = State()  # 323 What is the expiration date of his/her authorized stay if any? (mm/dd/yyyy)

    Supplement_A_IsImmigrationCourtProceedingsChild6 = State()
    # Supplement_A_SuppALine20_CheckBox2_0 = State()  # Is your child in Immigration Court proceedings? Yes
    # Supplement_A_SuppALine20_CheckBox2_1 = State()  # Is your child in Immigration Court proceedings? No

    Supplement_A_IsIncludedInApplicationChild6 = State()
    # Supplement_A_SuppALine21_CheckBox_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) Yes
    # Supplement_A_SuppALine21_CheckBox_1 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) No

    # A III
    # Address Where Don't Fear Persecution
    A_III_TextField13_0 = State()  # 148 Number and Street (Provide if available)
    A_III_TextField13_2 = State()  # 149 City/Town
    A_III_TextField13_4 = State()  # 150 Department Province or State
    A_III_TextField13_6 = State()  # 151 Country
    A_III_DateTimeField21_0 = State()  # 152 Dates From (Mo/Yr)
    A_III_DateTimeField20_0 = State()  # 153 To (Mo/Yr)

    # Address Where Fear Persecution
    A_III_TextField13_1 = State()  # 154  # Number and Street (Provide if available)
    A_III_TextField13_3 = State()  # 155  # City/Town
    A_III_TextField13_5 = State()  # 156  # Department Province or State
    A_III_TextField13_7 = State()  # 157  # Country
    A_III_DateTimeField22_0 = State()  # 158 Dates From (Mo/Yr)
    A_III_DateTimeField23_0 = State()  # 159 To (Mo/Yr)

    # Present Address
    A_III_TextField13_8 = State()  # 160 Number and Street
    A_III_TextField13_10 = State()  # 161 City/Town
    A_III_TextField13_12 = State()  # 162 Department Province or State
    A_III_TextField13_14 = State()  # 163 Country
    A_III_DateTimeField24_0 = State()  # 164  # Dates From (Mo/Yr)
    A_III_DateTimeField26_0 = State()  # 165  # Dates To (Mo/Yr)

    # First Residence Address
    A_III_TextField13_9 = State()  # 166  # Number and Street
    A_III_TextField13_11 = State()  # 167  # City/Town
    A_III_TextField13_13 = State()  # 168 Department Province or State
    A_III_TextField13_15 = State()  # 169 Country
    A_III_DateTimeField25_0 = State()  # 170 Dates From (Mo/Yr)
    A_III_DateTimeField27_0 = State()  # 171 Dates To (Mo/Yr)

    # Second Residence Address
    A_III_TextField13_16 = State()  # 172 Number and Street
    A_III_TextField13_17 = State()  # 173 City/Town
    A_III_TextField13_18 = State()  # 174  # Department Province or State
    A_III_TextField13_19 = State()  # 175  # Country
    A_III_DateTimeField28_0 = State()  # 176  # Dates From (Mo/Yr)
    A_III_DateTimeField29_0 = State()  # 177  # Dates To (Mo/Yr)

    # Third Residence Address
    A_III_TextField13_20 = State()  # 178 Number and Street
    A_III_TextField13_21 = State()  # 179 City/Town
    A_III_TextField13_22 = State()  # 180 Department Province or State
    A_III_TextField13_23 = State()  # 181 Country
    A_III_DateTimeField30_0 = State()  # 182 Dates From (Mo/Yr)
    A_III_DateTimeField31_0 = State()  # 183 Dates To (Mo/Yr)

    # Fourth Residence Address
    A_III_TextField13_24 = State()  # 184  # Number and Street
    A_III_TextField13_25 = State()  # 185  # City/Town
    A_III_TextField13_26 = State()  # 186  # Department Province or State
    A_III_TextField13_27 = State()  # 187  # Country
    A_III_DateTimeField32_0 = State()  # 188 Dates From (Mo/Yr)
    A_III_DateTimeField33_0 = State()  # 189 Dates To (Mo/Yr)

    # First School
    A_III_TextField13_28 = State()  # 190 Name of School
    A_III_TextField13_30 = State()  # 191 Type of School
    A_III_TextField13_32 = State()  # 192 Location (Address)
    A_III_DateTimeField41_0 = State()  # 193 Attended From (Mo/Yr)
    A_III_DateTimeField40_0 = State()  # 194  # Attended To (Mo/Yr)

    # Second School
    A_III_TextField13_29 = State()  # 195  # Name of School
    A_III_TextField13_31 = State()  # 196  # Type of School
    A_III_TextField13_33 = State()  # 197  # Location (Address)
    A_III_DateTimeField38_0 = State()  # 198 Attended From (Mo/Yr)
    A_III_DateTimeField39_0 = State()  # 199 Attended To (Mo/Yr)

    # Third School
    A_III_TextField13_34 = State()  # 200 Name of School
    A_III_TextField13_35 = State()  # 201 Type of School
    A_III_TextField13_36 = State()  # 202 Location (Address)
    A_III_DateTimeField37_0 = State()  # 203 Attended From (Mo/Yr)
    A_III_DateTimeField36_0 = State()  # 204  # Attended To (Mo/Yr)

    # Fourth School
    A_III_TextField13_37 = State()  # 205  # Name of School
    A_III_TextField13_38 = State()  # 206  # Type of School
    A_III_TextField13_39 = State()  # 207  # Location (Address)
    A_III_DateTimeField34_0 = State()  # 208 Attended From (Mo/Yr)
    A_III_DateTimeField35_0 = State()  # 209 Attended To (Mo/Yr)

    # First Employer
    A_III_TextField13_40 = State()  # 210 Name and Address of Employer
    A_III_TextField13_42 = State()  # 211 Your Occupation
    A_III_DateTimeField42_0 = State()  # 212 Dates From (Mo/Yr)
    A_III_DateTimeField44_0 = State()  # 213 Dates To (Mo/Yr)

    # Second Employer
    A_III_TextField13_41 = State()  # 214  # Name and Address of Employer
    A_III_TextField13_43 = State()  # 215  # Your Occupation
    A_III_DateTimeField43_0 = State()  # 216  # Dates From (Mo/Yr)
    A_III_DateTimeField45_0 = State()  # 217  # Dates To (Mo/Yr)

    # Third Employer
    A_III_TextField13_44 = State()  # 218 Name and Address of Employer
    A_III_TextField13_45 = State()  # 219 Your Occupation
    A_III_DateTimeField46_0 = State()  # 220 Dates From (Mo/Yr)
    A_III_DateTimeField47_0 = State()  # 221 Dates To (Mo/Yr)

    # Mother
    A_III_TextField13_46 = State()  # 222 Full Name
    A_III_TextField13_49 = State()  # 223 City/Town and Country of Birth
    A_III_CheckBoxAIII5_m_0 = State()  # Mother Deceased
    A_III_TextField35_0 = State()  # 224  # Current Location

    # Father
    A_III_TextField13_47 = State()  # 225  # Full Name
    A_III_TextField13_50 = State()  # 226  # City/Town and Country of Birth
    A_III_CheckBoxAIII5_f_0 = State()  # Father Deceased
    A_III_TextField35_1 = State()  # 228 Current Location

    # Sibling 1
    A_III_TextField13_48 = State()  # 229 Full Name
    A_III_TextField13_51 = State()  # 230 City/Town and Country of Birth
    A_III_CheckBoxAIII5_s1_0 = State()  # 1 Sibling Deceased
    A_III_TextField35_2 = State()  # 232 Current Location

    # Sibling 2
    A_III_TextField13_52 = State()  # 233 Full Name
    A_III_TextField13_53 = State()  # 234  # City/Town and Country of Birth
    A_III_CheckBoxAIII5_s2_0 = State()  # 2 Sibling Deceased
    A_III_TextField35_3 = State()  # 236  # Current Location

    # Sibling 3
    A_III_TextField13_54 = State()  # 237  # Full Name
    A_III_TextField13_55 = State()  # 238 City/Town and Country of Birth
    A_III_CheckBoxAIII5_s3_0 = State()  # 3 Sibling Deceased
    A_III_TextField35_4 = State()  # 239 Current Location

    # Sibling 4
    A_III_TextField13_56 = State()  # 240 Full Name
    A_III_TextField13_57 = State()  # 241 City/Town and Country of Birth
    A_III_CheckBoxAIII5_s4_0 = State()  # 4  # Sibling Deceased
    A_III_TextField35_5 = State()  # 242 Current Location

    B_Asylum_Reason_Choice = State()
    # B_CheckBoxrace_0 = State()  # I am seeking asylum or withholding of removal based on Race
    # B_CheckBoxreligion_0 = State()  # I am seeking asylum or withholding of removal based on Religion
    # B_CheckBoxnationality_0 = State()  # I am seeking asylum or withholding of removal based on Nationality
    # B_CheckBoxpolitics_0 = State()  # I am seeking asylum or withholding of removal based on Political opinion
    # B_CheckBoxsocial_0 = State()  # I am seeking asylum or withholding of removal based on Membership in a particular social group
    # B_CheckBoxtorture_0 = State()  # I am seeking asylum or withholding of removal based on Torture Convention

    B_Family_Experienced_Harm_Choice = State()
    # B_ckboxyn1a_1 = State()  # Have you your family or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone? No
    # B_ckboxyn1a_0 = State()  # Have you your family or close friends or colleagues ever experienced harm or mistreatment or threats in the past by anyone? Yes
    B_TextField14_0 = State()  # 243 If \Yes\ explain in detail = State()

    B_You_Fear_Harm_Or_Mistreatment_Choice = State()
    # B_ckboxyn1b_1 = State()  # Do you fear harm or mistreatment if you return to your home country? No
    # B_ckboxyn1b_0 = State()  # Do you fear harm or mistreatment if you return to your home country? Yes
    B_TextField15_0 = State()  # 244  # If \Yes\ explain in detail = State()

    B_You_Or_Family_Accused_Charged_Arrested_Detained_Choice = State()
    # B_ckboxyn2_1 = State()  # Have you or your family members ever been accused charged arrested detained interrogated convicted and sentenced or imprisoned in any country other than the United States (including for an immigration law violation)? No
    # B_ckboxyn2_0 = State()  # Have you or your family members ever been accused charged arrested detained interrogated convicted and sentenced or imprisoned in any country other than the United States (including for an immigration law violation)? Yes
    B_PBL2_TextField_0 = State()  # 245  # If \Yes\ explain the circumstances and reasons for the action_

    B_Been_Associated_With_Any_Organizations_Choice = State()
    # B_ckboxyn3a_1 = State()  # Have you or your family members ever belonged to or been associated with any organizations or groups in your home country such as but not limited to a political party student group labor union religious organization military or paramilitary group civil patrol guerrilla organization ethnic group human rights group or the press or media? No
    # B_ckboxyn3a_0 = State()  # Have you or your family members ever belonged to or been associated with any organizations or groups in your home country such as but not limited to a political party student group labor union religious organization military or paramilitary group civil patrol guerrilla organization ethnic group human rights group or the press or media? Yes
    B_PBL3A_TextField_0 = State()  # 246  # If \Yes\ describe for each person the level of participation any leadership or other positions held and the length of time you or your family members were involved in each organization or activity_

    B_Continue_To_Participate_In_Organizations_Choice = State()
    # B_ckboxyn3b_1 = State()  # Do you or your family members continue to participate in any way in these organizations or groups? No
    # B_ckboxyn3b_0 = State()  # Do you or your family members continue to participate in any way in these organizations or groups? Yes
    B_PBL3B_TextField_0 = State()  # 247  # If \Yes\ describe for each person your or your family members  current level of participation any leadership or other positions currently held and the length of time you or your family members have been involved in each organization or group_

    B_Afraid_Of_Being_Subjected_To_Torture_Choice = State()
    # B_ckboxyn4_1 = State()  # Are you afraid of being subjected to torture in your home country or any other country to which you may be returned? No
    # B_ckboxyn4_0 = State()  # Are you afraid of being subjected to torture in your home country or any other country to which you may be returned? Yes
    B_PB4_TextField_0 = State()  # 248 If \Yes\ explain why you are afraid and describe the nature of torture you fear by whom and why it would be inflicted_

    C_Family_Applied_For_USRefugee_Status_Choice = State()
    # C_ckboxync1_0 = State()  # Have you your spouse your child(ren) your parents or your siblings ever applied to the U_S_ Government for refugee status asylum or withholding of removal? Yes
    # C_ckboxync1_1 = State()  # Have you your spouse your child(ren) your parents or your siblings ever applied to the U_S_ Government for refugee status asylum or withholding of removal? No
    C_PCL1_TextField_0 = State()  # 249 If \Yes\ explain the decision and what happened

    C_Family_Travel_Or_Reside_In_Other_Countries_Before_US_Choice = State()
    # C_ckboxync2a_0 = State()  # After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States? Yes
    # C_ckboxync2a_1 = State()  # After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States? No

    C_Family_Recieved_Any_Lawful_Status_Choice = State()
    # C_ckboxync2b_0 = State()  # After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States? Yes
    # C_ckboxync2b_1 = State()  # After leaving the country from which you are claiming asylum did you or your spouse or child(ren) who are now in the United States travel through or reside in any other country before entering the United States? No
    C_PCL2B_TextField_0 = State()  # 250 If \Yes\

    C_You_Or_Family_Caused_Harm_Or_Suffering_Choice = State()
    # C_ckboxync3_0 = State()  # Have you your spouse or your child(ren) ever ordered incited assisted or otherwise participated in causing harm or suffering to any person because of his or her race religion nationality membership in a particular social group or belief in a particular political opinion? Yes
    # C_ckboxync3_1 = State()  # Have you your spouse or your child(ren) ever ordered incited assisted or otherwise participated in causing harm or suffering to any person because of his or her race religion nationality membership in a particular social group or belief in a particular political opinion? No
    C_PCL3_TextField_0 = State()  # 251 If \Yes\

    C_Returned_To_Bad_Country_Choice = State()
    # C_PCckboxyn4_0 = State()  # After you left the country where you were harmed or fear harm did you return to that country? Yes
    # C_PCckboxyn4_1 = State()  # After you left the country where you were harmed or fear harm did you return to that country? No
    C_PCL4_TextField_0 = State()  # 252 If \Yes\ describe in detail the circumstances of your visit(s)

    C_Last_Arrival_To_US_More_Than_1_Year_Choice = State()
    # C_ckboxync5_0 = State()  # Are you filing this application more than 1 year after your last arrival in the United States? Yes
    # C_ckboxync5_1 = State()  # Are you filing this application more than 1 year after your last arrival in the United States? No
    C_PCL5_TextField_0 = State()  # 253 If \Yes\ explain why you did not file within the first year after you arrived

    C_You_Or_Family_Did_Crime_Choice = State()
    # C_ckboxync6_0 = State()  # Have you or any member of your family included in the application ever committed any crime and/or been arrested charged convicted or sentenced for any crimes in the United States (including for an immigration law violation)? Yes
    # C_ckboxync6_1 = State()  # Have you or any member of your family included in the application ever committed any crime and/or been arrested charged convicted or sentenced for any crimes in the United States (including for an immigration law violation)? No
    C_PCL6_TextField_0 = State()  # 254  # If \Yes\ for each instance specify in your response = State()  # what occurred and the circumstances

    D_TextField20_0 = State()  # 255  # Print your complete name_
    D_TextField20_1 = State()  # 256  # Write your name in your native alphabet

    D_Family_Helped_Complete_Application = State()
    # D_PtD_ckboxynd1_0 = State()  # Did your spouse parent or child(ren) assist you in completing this application? Yes (If \Yes\ list the name and relationship_)
    # D_PtD_ckboxynd1_1 = State()  # Did your spouse parent or child(ren) assist you in completing this application? No

    D_PtD_ChildName1_0 = State()  # 257  # Name
    D_PtD_RelationshipOfChild1_0 = State()  # 258 Relationship
    D_PtD_ChildName2_0 = State()  # 259 Name
    D_PtD_RelationshipOfChild2_0 = State()  # 260 Relationship

    D_Not_Family_Helped_Complete_Application = State()
    # D_ckboxynd2_0 = State()  # Did someone other than your spouse parent or child(ren) prepare this application? Yes (If \Yes\complete Part E_)
    # D_ckboxynd2_1 = State()  # Did someone other than your spouse parent or child(ren) prepare this application? No

    D_Provided_With_List_Of_Persons_Who_May_Assist_Choice = State()
    # D_ckboxynd3_0 = State()  # Asylum applicants may be represented by counsel_ Have you been provided with a list of persons who may be available to assist you at little or no cost with your asylum claim? Yes
    # D_ckboxynd3_1 = State()  # Asylum applicants may be represented by counsel_ Have you been provided with a list of persons who may be available to assist you at little or no cost with your asylum claim? No

    D_TextField22_0 = State()  # 261 Signature
    D_DateTimeField48_0 = State()  # 262 Date of Signature

    E_PtE_PreparerSignature_0 = State()  # 263 Signature of Preparer
    E_PtE_PreparerName_0 = State()  # 264  # Print Complete Name of Preparer
    E_TextField25_1 = State()  # 265  # Daytime Telephone Number
    E_TextField25_0 = State()  # 266  # Daytime Telephone Number
    E_PtE_StreetNumAndName_0 = State()  # 267  # Address of Preparer = State()  # Street Number and Name
    E_PtE_AptNumber_0 = State()  # 268 Apt_ Number
    E_PtE_City_0 = State()  # 269 City
    E_PtE_State_0 = State()  # 270 State
    E_PtE_ZipCode_0 = State()  # 271 Zip Code
    E_Form_G_28_Attached_Choice = State()
    # E_CheckBox1_0 = State()  # Select this box if Form G-28 is attached_
    E_AttorneyStateBarNumber_0 = State()  # 272 Attorney State Bar Number
    E_USCISOnlineAcctNumber_0 = State()  # 273

    F_All_True_Or_Not_True_Application = State()
    # F_CheckBox32_0 = State()  # All True
    # F_CheckBox32_1 = State()  # Not All True
    F_TextField26_0 = State()  # 274 Correction Number
    F_TextField26_1 = State()  # 275 Correction Number
    F_TextField27_2 = State()  # 276  # Signature of applicant
    F_DateTimeField49_0 = State()  # 277  # Date (mm/dd/yyyy)
    F_TextField27_1 = State()  # 278 Write Your Name in Your Native Alphabet
    # F_TextField27_0 = State()  # Signature of Asylum Officer

    G_All_True_Or_Not_True_Application = State()
    # G_PG_CheckBox_0 = State()  # All True
    # G_PG_CheckBox_1 = State()  # Not All True
    G_TextField26_2 = State()  # 279 Correction Number
    G_TextField26_3 = State()  # 280 Correction Number

    G_TextField27_5 = State()  # 281 Signature of Applicant
    G_DateTimeField50_0 = State()  # 282 Date (mm/dd/yyyy)
    G_TextField27_4 = State()  # 283 Write Your Name in Your Native Alphabet
    # G_TextField27_3 = State()  # Signature of Immigration Judge

    Supplement_A_PtAILine1_ANumber_1 = State()  # 284  # A-Number (If available)
    Supplement_A_DateTimeField57_0 = State()  # 285  # Date
    Supplement_A_ApplicantName_0 = State()  # 286  # Applicant s Name
    Supplement_A_TextField28_0 = State()  # 287  # Applicant s Signature

    # Supplement_A_IsFillChild5 = State()
    # # Child 5
    # Supplement_A_TextField12_6 = State()  # 288 A-Number
    # Supplement_A_TextField12_7 = State()  # 289 Passport/ID Card Number
    # Supplement_A_TextField12_8 = State()  # 290 Marital Status
    # Supplement_A_TextField12_9 = State()  # 291 U_S_ Social Security Number
    # Supplement_A_TextField12_0 = State()  # 292 Complete Last Name
    # Supplement_A_TextField12_2 = State()  # 293 First Name
    # Supplement_A_TextField12_3 = State()  # 294  # Middle Name
    # Supplement_A_DateTimeField14_0 = State()  # 295  # Date of Birth (mm/dd/yyyy)
    # Supplement_A_TextField12_1 = State()  # 296  # City and Country of Birth
    # Supplement_A_TextField12_4 = State()  # 297  # Nationality (Citizenship)
    # Supplement_A_TextField12_5 = State()  # 298 Race Ethnic or Tribal Group
    #
    # Supplement_A_ChooseGenderChild5 = State()
    # # Supplement_A_CheckBox12_Gender_0 = State()  # Gender Male
    # # Supplement_A_CheckBox12_Gender_1 = State()  # Gender Female
    #
    # Supplement_A_ChooseLocationChild5 = State()
    # # Supplement_A_CheckBox57_0 = State()  # Is this child in the U_S_ ? Yes
    # # Supplement_A_CheckBox57_1 = State()  # Is this child in the U_S_ ? No specify location = State()  # {Supplement_A_SuppLALine13_Specify_0}
    #
    # Supplement_A_SuppLALine13_Specify_0 = State()  # 299 Specify location
    # Supplement_A_ChildEntry5_0 = State()  # 300 Place of last entry into the U_S_
    # Supplement_A_ChildExp5_0 = State()  # 301 Date of last entry into the U_S
    # Supplement_A_ChildINum5_0 = State()  # 302 I-94  # Number
    # Supplement_A_ChildStatus5_0 = State()  # 303 Status when last admitted
    # Supplement_A_ChildCurrent5_0 = State()  # 304  # What is your child s current status?
    # Supplement_A_ChildExpAuth5_0 = State()  # 305  # What is the expiration date of his/her authorized stay
    #
    # Supplement_A_IsImmigrationCourtProceedingsChild5 = State()
    # # Supplement_A_SuppA_CheckBox20_0 = State()  # Is your child in Immigration Court proceedings? Yes
    # # Supplement_A_SuppA_CheckBox20_1 = State()  # Is your child in Immigration Court proceedings? No
    #
    # Supplement_A_IsIncludedInApplicationChild5 = State()
    # # Supplement_A_SuppA_CheckBox21_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) yes
    # # Supplement_A_SuppA_CheckBox21_1 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) no
    #
    # # Child 6
    # Supplement_A_TextField12_16 = State()  # 306  # A-Number (If available)
    # Supplement_A_TextField12_17 = State()  # 307  # Passport/ID Card Number
    # Supplement_A_TextField12_18 = State()  # 308 Marital Status
    # Supplement_A_TextField12_19 = State()  # 309 U_S_ Social Security Number
    # Supplement_A_TextField12_10 = State()  # 310 Complete Last Name
    # Supplement_A_TextField12_12 = State()  # 311 First Name
    # Supplement_A_TextField12_13 = State()  # 312 Middle Name
    # Supplement_A_DateTimeField14_1 = State()  # 313 Date of Birth
    # Supplement_A_TextField12_11 = State()  # 314  # City and Country of Birth
    # Supplement_A_TextField12_14 = State()  # 315  # Nationality
    # Supplement_A_TextField12_15 = State()  # 316  # Race Ethnic or Tribal Group
    #
    # Supplement_A_ChooseGenderChild6 = State()
    # # Supplement_A_SuppAL12_CheckBox_0 = State()  # Gender Male
    # # Supplement_A_SuppAL12_CheckBox_1 = State()  # Gender Female
    #
    # Supplement_A_ChooseLocationChild6 = State()
    # # Supplement_A_SuppAL13_CheckBox_0 = State()  # Is this child in the U_S_ ? Yes
    # # Supplement_A_SuppAL13_CheckBox_1 = State()  # Is this child in the U_S_ ? No
    #
    # Supplement_A_SuppLALine13_Specify2_0 = State()  # 317  # Specify location
    # Supplement_A_ChildEntry6_0 = State()  # 318 Place of last entry into the U_S_
    # Supplement_A_ChildExp6_0 = State()  # 319 Date of last entry into the U_S_
    # Supplement_A_ChildINum6_0 = State()  # 320 I-94  # Number
    # Supplement_A_ChildStatus6_0 = State()  # 321 Status when last admitted (Visa type if any)
    # Supplement_A_ChildCurrent6_0 = State()  # 322 What is your child s current status?
    # Supplement_A_ChildExpAuth6_0 = State()  # 323 What is the expiration date of his/her authorized stay if any? (mm/dd/yyyy)
    #
    # Supplement_A_IsImmigrationCourtProceedingsChild6 = State()
    # Supplement_A_SuppALine20_CheckBox2_0 = State()  # Is your child in Immigration Court proceedings? Yes
    # Supplement_A_SuppALine20_CheckBox2_1 = State()  # Is your child in Immigration Court proceedings? No
    #
    # Supplement_A_IsIncludedInApplicationChild6 = State()
    # Supplement_A_SuppALine21_CheckBox_0 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) Yes
    # Supplement_A_SuppALine21_CheckBox_1 = State()  # If in the U_S_ is this child to be included in this application? (Check the appropriate box_) No

    Supplement_B_PtAILine1_ANumber_2 = State()  # 324  # A-Number (if available)
    Supplement_B_DateTimeField58_0 = State()  # 325  # Date
    Supplement_B_SupBApplicantName_0 = State()  # 326  # Applicant s Name
    Supplement_B_TextField30_0 = State()  # 327  # Applicant s Signature

    Supplement_B_Fill_Choice = State()

    Supplement_B_TextField31_0 = State()  # 328  # Part
    Supplement_B_TextField31_1 = State()  # 329  # Question
    Supplement_B_TextField32_0 = State()  # 330
