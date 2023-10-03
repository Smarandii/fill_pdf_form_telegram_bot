from aiogram.dispatcher.filters.state import State, StatesGroup


class FormI485(StatesGroup):
    S_0_Pt1Line10_AlienNumber_0 = State()

    S_0_Pt1Line1a_FamilyName_0 = State()
    S_0_Pt1Line1b_GivenName_0 = State()
    S_0_Pt1Line1c_MiddleName_0 = State()

    UsedOtherNamesChoice_1 = State()

    S_0_Pt1Line2a_FamilyName_0 = State()
    S_0_Pt1Line2b_GivenName_0 = State()
    S_0_Pt1Line2c_MiddleName_0 = State()

    UsedOtherNamesChoice_2 = State()

    S_0_Pt1Line3a_FamilyName_0 = State()
    S_0_Pt1Line3b_GivenName_0 = State()
    S_0_Pt1Line3c_MiddleName_0 = State()

    UsedOtherNamesChoice_3 = State()

    S_0_Pt1Line4a_FamilyName_0 = State()
    S_0_Pt1Line4b_GivenName_0 = State()
    S_0_Pt1Line4c_MiddleName_0 = State()

    S_0_Pt1Line5_DateofBirth_0 = State()

    GenderChoice_1 = State()
    # S_0_Pt1Line6_Gender_0 = State()
    # S_0_Pt1Line6_Gender_1 = State()

    S_0_Pt1Line6_CityOrTown_0 = State()

    S_1_Pt1Line8_CountryofBirth_0 = State()
    S_1_Pt1Line9_CountryofCitizenship_0 = State()

    # S_1_Pt1Line10_AlienNumber_1 = State()

    S_1_Pt1Line10_AlienNumber_2 = State()
    S_1_Pt1Line11_USCISELISAcctNumber_0 = State()
    S_1_Pt1Line12_InCareofName_0 = State()

    S_1_Pt1Line12_StreetNumberName_0 = State()

    TypeOfBuildingChoice_1 = State()

    # S_1_Pt1Line12_Unit_0 = State()
    # S_1_Pt1Line12_Unit_1 = State()
    # S_1_Pt1Line12_Unit_2 = State()

    S_1_Pt1Line12_AptSteFlrNumber_0 = State()

    S_1_Pt1Line12_CityOrTown_0 = State()
    S_1_Pt1Line12_State_0 = State()
    S_1_Pt1Line12_ZipCode_0 = State()

    AlternateMailingAddressChoice = State()

    S_1_Pt1Line13_InCareofName_0 = State()
    S_1_Pt1Line13_StreetNumberName_0 = State()

    TypeOfBuildingChoice_2 = State()

    # S_1_Pt1Line13_Unit_0 = State()
    # S_1_Pt1Line13_Unit_1 = State()
    # S_1_Pt1Line13_Unit_2 = State()

    S_1_Pt1Line13_AptSteFlrNumber_0 = State()

    S_1_Pt1Line13_CityOrTown_0 = State()
    S_1_Pt1Line13_State_0 = State()
    S_1_Pt1Line13_ZipCode_0 = State()

    SSA_Choice = State()

    # S_1_Pt1Line14_YN_0 = State()
    # S_1_Pt1Line14_YN_1 = State()

    S_1_Pt1Line15_SSN_0 = State()

    IssueSSCChoice = State()
    # S_1_Pt1Line16_YN_0 = State()
    # S_1_Pt1Line16_YN_1 = State()

    SSACouldUseInformationChoice = State()
    # S_1_Pt1Line17_YN_0 = State()
    # S_1_Pt1Line17_YN_1 = State()

    S_1_Pt1Line18_PassportNum_0 = State()
    S_1_Pt2Line19_TravelDoc_0 = State()
    S_1_Pt1Line20_ExpDate_0 = State()
    S_1_Pt1Line21_Passport_0 = State()
    S_1_Pt1Line22_VisaNum_0 = State()
    S_1_Pt1Line23a_CityTown_0 = State()
    S_1_Pt1Line23b_State_0 = State()
    S_1_Pt1Line24_Date_0 = State()

    # S_2_Pt1Line10_AlienNumber_3 = State()

    S_2_Pt1Line25a_CB_0 = State()
    S_2_Pt1Line25a_AdmissionEntry_0 = State()

    S_2_Pt1Line25b_CB_0 = State()
    S_2_Pt1Line25b_ParoleEntrance_0 = State()

    S_2_Pt1Line25c_CB_0 = State()

    S_2_Pt1Line25d_CB_0 = State()
    S_2_Pt2Line25d_other_0 = State()

    I94WasIssuedChoice = State()

    S_2_P2Line26a_I94_0 = State()
    S_2_Pt1Line26b_Date_0 = State()

    S_2_Pt1Line26c_Status_0 = State()

    S_2_Pt1Line27_Status_0 = State()

    S_2_Pt1Line28a_FamilyName_0 = State()
    S_2_Pt1Line28b_GivenName_0 = State()
    S_2_Pt1Line28c_MiddleName_0 = State()

    ApplicationByFamilyCategory = State()
    TypeOfFamilyCategoryApplication = State()

    # S_2_Pt2Line1_CB_0 = State()
    # S_2_Pt2Line1_CB_1 = State()
    # S_2_Pt2Line1_CB_2 = State()
    # S_2_Pt2Line1_CB_3 = State()
    # S_2_Pt2Line1_CB_4 = State()

    ApplicationByEmploymentBasedCategory = State()
    TypeOfEmploymentBasedCategoryApplication = State()

    # S_2_Pt2Line1_CB_5 = State()
    # S_2_Pt2Line1_CB_6 = State()

    ApplicationBySpecialImmigrantCategory = State()
    TypeOfSpecialImmigrantCategoryApplication = State()

    # S_2_Pt2Line1_CB_7 = State()
    # S_2_Pt2Line1_CB_8 = State()
    # S_2_Pt2Line1_CB_9 = State()
    # S_2_Pt2Line1_CB_10 = State()
    # S_2_Pt2Line1_CB_11 = State()

    ApplicationByAsyleeOrRefugeeCategory = State()
    TypeOfAsyleeOrRefugeeCategoryApplication = State()

    # S_2_Pt2Line1_CB_12 = State()
    # S_2_Pt2Line1_CB_13 = State()

    ApplicationByHumanTraffickingVictimCategory = State()
    TypeOfHumanTraffickingVictimCategoryApplication = State()

    # S_2_Pt2Line1_CB_14 = State()
    # S_2_Pt2Line1_CB_15 = State()

    ApplicationBySpecialProgramsCategory = State()
    TypeOfSpecialProgramsCategoryApplication = State()

    # S_3_Pt2Line1_CB_16 = State()
    # S_3_Pt2Line1_CB_17 = State()
    # S_3_Pt2Line1_CB_18 = State()
    # S_3_Pt2Line1_CB_19 = State()
    # S_3_Pt2Line1_CB_20 = State()
    # S_3_Pt2Line1_CB_21 = State()
    # S_3_Pt2Line1_CB_22 = State()

    ApplicationByAdditionalOptionsCategory = State()
    TypeOfAdditionalOptionsCategoryApplication = State()

    # S_3_Pt2Line1_CB_23 = State()
    # S_3_Pt2Line1_CB_24 = State()
    # S_3_Pt2Line1_CB_25 = State()
    # S_3_Pt2Line1_CB_26 = State()

    S_3_Pt2Line1g_OtherEligibility_0 = State()

    ImmigrationAndNationalityActChoice = State()

    # S_3_Pt2Line2_CB_0 = State()
    # S_3_Pt2Line2_CB_1 = State()

    PrincipalApplicatnChoice = State()

    S_3_Pt2Line3_Receipt_0 = State()

    S_3_Pt2Line4_Date_0 = State()

    DerivativeApplicatnChoice = State()

    S_3_Pt2Line5a_FamilyName_0 = State()
    S_3_Pt2Line5b_GivenName_0 = State()
    S_3_Pt2Line5c_MiddleName_0 = State()

    S_3_Pt1Line8_AlienNumber_0 = State()
    S_3_Pt2Line7_Date_0 = State()
    S_3_Pt2Line8_ReceiptNumber_0 = State()
    S_3_Pt2Line9_Date_0 = State()

    AppliedForImmigrantVisaChoice = State()
    # S_3_Pt3Line1_YN_0 = State()
    # S_3_Pt3Line1_YN_1 = State()

    S_3_Pt3Line2a_City_0 = State()
    S_3_Pt3Line2b_Country_0 = State()
    S_3_Pt3Line3_Decision_0 = State()
    S_3_Pt3Line4_Date_0 = State()

    S_4_Pt3Line5_StreetNumberName_0 = State()

    TypeOfBuildingChoice_3 = State()

    # S_4_Pt3Line5_Unit_0 = State()
    # S_4_Pt3Line5_Unit_1 = State()
    # S_4_Pt3Line5_Unit_2 = State()

    S_4_Pt3Line5_AptSteFlrNumber_0 = State()
    S_4_Pt3Line5_CityOrTown_0 = State()
    S_4_Pt3Line5_State_0 = State()
    S_4_Pt3Line5_ZipCode_0 = State()
    S_4_Pt3Line5_Province_0 = State()
    S_4_Pt3Line5_PostalCode_0 = State()

    S_4_Pt3Line5_Country_0 = State()
    S_4_Pt3Line6a_Date_0 = State()
    S_4_Pt3Line6b_Date_0 = State()

    S_4_Pt3Line7_StreetNumberName_0 = State()

    TypeOfBuildingChoice_4 = State()

    # S_4_Pt3Line7_Unit_0 = State()
    # S_4_Pt3Line7_Unit_1 = State()
    # S_4_Pt3Line7_Unit_2 = State()

    S_4_Pt3Line7_AptSteFlrNumber_0 = State()
    S_4_Pt3Line7_CityOrTown_0 = State()

    S_4_Pt3Line7_State_0 = State()
    S_4_Pt3Line7_ZipCode_0 = State()

    S_4_Pt3Line7_Province_0 = State()
    S_4_Pt3Line7_PostalCode_0 = State()

    S_4_Pt3Line7_Country_0 = State()
    S_4_Pt3Line8a_DateFrom_0 = State()
    S_4_Pt3Line8b_DateTo_0 = State()

    AddressWasProvidedAboveChoice = State()

    TypeOfBuildingChoice_5 = State()

    # S_4_Pt3Line9_Unit_0 = State()
    # S_4_Pt3Line9_Unit_1 = State()
    # S_4_Pt3Line9_Unit_2 = State()

    S_4_Pt3Line9_AptSteFlrNumber_0 = State()

    S_4_Pt3Line9_CityOrTown_0 = State()
    S_4_Pt3Line9_State_0 = State()
    S_4_Pt3Line9_ZipCode_0 = State()
    S_4_Pt3Line9_Province_0 = State()
    S_4_Pt3Line9_PostalCode_0 = State()
    S_4_Pt3Line9_Country_0 = State()
    S_4_Pt3Line10a_DateFrom_0 = State()
    S_4_Pt3Line10a_DateTo_0 = State()

    S_4_Pt3Line11_EmployerName_0 = State()
    S_4_Pt3Line12_StreetNumberName_0 = State()

    TypeOfBuildingChoice_6 = State()

    # S_4_Pt3Line12_Unit_0 = State()
    # S_4_Pt3Line12_Unit_1 = State()
    # S_4_Pt3Line12_Unit_2 = State()

    S_4_Pt3Line12_AptSteFlrNumber_0 = State()
    S_4_Pt3Line12_CityOrTown_0 = State()
    S_4_Pt3Line12_State_0 = State()
    S_4_Pt3Line12_ZipCode_0 = State()
    S_4_Pt3Line12_Province_0 = State()
    S_4_Pt3Line12_PostalCode_0 = State()

    S_4_Pt3Line12_Country_0 = State()
    S_4_Pt3Line13_EmployerName_0 = State()

    S_5_Pt3Line14a_DateFrom_0 = State()
    S_5_Pt3Line14b_DateTo_0 = State()

    S_5_Pt3Line4a_EmployerName_0 = State()

    S_5_Pt3Line16_StreetNumberName_0 = State()

    TypeOfBuildingChoice_7 = State()

    # S_5_Pt3Line16_Unit_0 = State()
    # S_5_Pt3Line16_Unit_1 = State()
    # S_5_Pt3Line16_Unit_2 = State()

    S_5_Pt3Line16_AptSteFlrNumber_0 = State()

    S_5_Pt3Line16_CityOrTown_0 = State()
    S_5_Pt3Line16_State_0 = State()
    S_5_Pt3Line16_ZipCode_0 = State()

    S_5_Pt3Line16_Province_0 = State()
    S_5_Pt3Line16_PostalCode_0 = State()

    S_5_Pt3Line16_Country_0 = State()

    S_5_Pt3Line17_EmployerName_0 = State()
    S_5_Pt3Line18a_DateFrom_0 = State()
    S_5_Pt3Line18a_DateTo_0 = State()

    S_5_Pt3Line19_EmployerName_0 = State()

    S_5_Pt3Line20_StreetNumberName_0 = State()

    TypeOfBuildingChoice_8 = State()

    # S_5_Pt3Line20_Unit_0 = State()
    # S_5_Pt3Line20_Unit_1 = State()
    # S_5_Pt3Line20_Unit_2 = State()

    S_5_Pt3Line20_AptSteFlrNumber_0 = State()

    S_5_Pt3Line20_CityOrTown_0 = State()
    S_5_Pt3Line20_State_0 = State()
    S_5_Pt3Line20_ZipCode_0 = State()
    S_5_Pt3Line20_Province_0 = State()
    S_5_Pt3Line20_PostalCode_0 = State()

    S_5_Pt3Line20_Country_0 = State()
    S_5_Pt3Line20_EmployerName_0 = State()
    S_5_Pt3Line22a_DateFrom_0 = State()
    S_5_Pt3Line22a_DateTo_0 = State()

    # Parent 1
    S_5_Pt4Line1a_FamilyName_0 = State()
    S_5_Pt4Line1b_GivenName_0 = State()
    S_5_Pt4Line1c_MiddleName_0 = State()

    ParentHasDifferentNameChoice = State()

    S_5_Pt4Line2a_FamilyName_0 = State()
    S_5_Pt4Line2b_GivenName_0 = State()
    S_5_Pt4Line2c_MiddleName_0 = State()

    S_5_Pt4Line3_DateofBirth_0 = State()

    Parent1_Gender_Choice = State()
    # S_5_Pt4Line4_Gender_0 = State()
    # S_5_Pt4Line4_Gender_1 = State()

    S_5_Pt4Line5_CityTown_0 = State()
    S_5_Pt4Line6_Country_0 = State()

    S_6_Pt4Line7_CityTown_0 = State()
    S_6_Pt4Line8_Country_0 = State()

    # Parent 2
    S_6_Pt4Line9a_FamilyName_0 = State()
    S_6_Pt4Line9b_GivenName_0 = State()
    S_6_Pt4Line9c_MiddleName_0 = State()

    ParentHasDifferentNameChoice_2 = State()

    S_6_Pt4Line10a_FamilyName_0 = State()
    S_6_Pt4Line10b_GivenName_0 = State()
    S_6_Pt4Line10c_MiddleName_0 = State()

    S_6_Pt4Line11_DateofBirth_0 = State()

    Parent2_Gender_Choice = State()
    # S_6_Pt4Line12_Gender_0 = State()
    # S_6_Pt4Line12_Gender_1 = State()

    S_6_Pt4Line13_CityTown_0 = State()
    S_6_Pt4Line14_Country_0 = State()

    S_6_Pt4Line15_CityTown_0 = State()
    S_6_Pt4Line16_Country_0 = State()

    MaritalStatusChoice = State()

    # S_6_Pt5Line1_MaritalStatus_0 = State()
    # S_6_Pt5Line1_MaritalStatus_1 = State()
    # S_6_Pt5Line1_MaritalStatus_2 = State()
    # S_6_Pt5Line1_MaritalStatus_3 = State()
    # S_6_Pt5Line1_MaritalStatus_4 = State()
    # S_6_Pt5Line1_MaritalStatus_5 = State()

    IsYourSpouceInArmyChoice = State()
    # S_6_Pt5Line2_YNNA_0 = State()
    # S_6_Pt5Line2_YNNA_1 = State()
    # S_6_Pt5Line2_YNNA_2 = State()

    S_6_Pt5Line3_TimesMarried_0 = State()
    S_6_Pt5Line4a_FamilyName_0 = State()
    S_6_Pt5Line4b_GivenName_0 = State()
    S_6_Pt5Line4c_MiddleName_0 = State()

    S_6_Pt5Line5_AlienNumber_0 = State()

    S_6_Pt5Line6_DateofBirth_0 = State()

    S_6_Pt5Line7_Date_0 = State()
    S_6_Pt5Line8a_CityTown_0 = State()
    S_6_Pt5Line8b_State_0 = State()
    S_6_Pt5Line8c_Country_0 = State()

    S_6_Pt5Line9a_CityTown_0 = State()
    S_6_Pt5Line9b_State_0 = State()
    S_6_Pt5Line9c_Country_0 = State()

    SpouceApplyingTooChoice = State()
    # S_6_Pt5Line10_YN_0 = State()
    # S_6_Pt5Line10_YN_1 = State()

    BeenMarriedBeforeChoice = State()

    S_7_Pt511a_FamilyName_0 = State()
    S_7_Pt5Line11b_GivenName_0 = State()
    S_7_Pt5Line11c_MiddleName_0 = State()
    S_7_Pt5Line12_DateofBirth_0 = State()
    S_7_Pt5Line13_Date_0 = State()

    S_7_Pt5Line14a_CityTown_0 = State()
    S_7_Pt5Line14b_State_0 = State()
    S_7_Pt5Line14c_Country_0 = State()

    S_7_Pt5Line15_Date_0 = State()
    S_7_Pt5Line16a_CityTown_0 = State()
    S_7_Pt5Line16b_State_0 = State()
    S_7_Pt5Line16c_Country_0 = State()

    HaveKidsChoice = State()
    S_7_Pt6Line1_TotalChildren_0 = State()
    S_7_Pt6Line2a_FamilyName_0 = State()
    S_7_Pt6Line2b_GivenName_0 = State()
    S_7_Pt6Line2c_MiddleName_0 = State()

    S_7_Pt6Line3_AlienNumber_0 = State()

    S_7_Pt6Line4_DateofBirth_0 = State()
    S_7_Pt6Line6_Country_0 = State()

    Child1ApplyingTooChoice = State()
    # S_7_Pt6Line6_YesNo_0 = State()
    # S_7_Pt6Line6_YesNo_1 = State()

    S_7_Pt6Line7a_FamilyName_0 = State()
    S_7_Pt6Line7b_GivenName_0 = State()
    S_7_Pt6Line7c_MiddleName_0 = State()

    S_7_Pt6Line8_AlienNumber_0 = State()

    S_7_Pt6Line9_DateofBirth_0 = State()
    S_7_Pt6Line10_Country_0 = State()

    Child1ApplyingTooChoice_2 = State()
    # S_7_Pt6Line11_YesNo_0 = State()
    # S_7_Pt6Line11_YesNo_1 = State()

    S_8_Pt6Line12a_FamilyName_0 = State()
    S_8_Pt6Line12b_GivenName_0 = State()
    S_8_Pt6Line12c_MiddleName_0 = State()

    S_8_Pt6Line13_AlienNumber_0 = State()

    S_8_Pt6Line14_DateofBirth_0 = State()
    S_8_Pt6Line15_Country_0 = State()

    Child1ApplyingTooChoice_3 = State()
    # S_8_Pt6Line16_YesNo_0 = State()
    # S_8_Pt6Line16_YesNo_1 = State()

    EthicityChoice = State()
    # S_8_Pt7Line1_Ethnicity_0 = State()
    # S_8_Pt7Line1_Ethnicity_1 = State()

    RaceChoice = State()
    # S_8_Pt7Line2_Race_0 = State()
    # S_8_Pt7Line2_Race_1 = State()
    # S_8_Pt7Line2_Race_2 = State()
    # S_8_Pt7Line2_Race_3 = State()
    # S_8_Pt7Line2_Race_4 = State()

    S_8_Pt7Line3_HeightFeetAndInches = State()

    WeightField = State()
    # S_8_Pt7Line4_Weight1_0 = State()
    # S_8_Pt7Line4_Weight2_0 = State()
    # S_8_Pt7Line4_Weight3_0 = State()

    EyeColorChoice = State()
    # S_8_Pt7Line5_Eyecolor_0 = State()
    # S_8_Pt7Line5_Eyecolor_1 = State()
    # S_8_Pt7Line5_Eyecolor_2 = State()
    # S_8_Pt7Line5_Eyecolor_3 = State()
    # S_8_Pt7Line5_Eyecolor_4 = State()
    # S_8_Pt7Line5_Eyecolor_5 = State()
    # S_8_Pt7Line5_Eyecolor_6 = State()
    # S_8_Pt7Line5_Eyecolor_7 = State()
    # S_8_Pt7Line5_Eyecolor_8 = State()

    HairColorChoice = State()
    # S_8_Pt7Line6_Haircolor_0 = State()
    # S_8_Pt7Line6_Haircolor_1 = State()
    # S_8_Pt7Line6_Haircolor_2 = State()
    # S_8_Pt7Line6_Haircolor_3 = State()
    # S_8_Pt7Line6_Haircolor_4 = State()
    # S_8_Pt7Line6_Haircolor_5 = State()
    # S_8_Pt7Line6_Haircolor_6 = State()
    # S_8_Pt7Line6_Haircolor_7 = State()
    # S_8_Pt7Line6_Haircolor_8 = State()

    WasOrIsMemberOfAnyOrganization = State()
    # S_8_Pt8Line1_YesNo_0 = State()
    # S_8_Pt8Line1_YesNo_1 = State()

    S_8_Pt8Line2_OrgName_0 = State()
    S_8_Pt8Line3a_CityTown_0 = State()
    S_8_Pt8Line3b_State_0 = State()
    S_8_Pt8Line3c_Country_0 = State()
    S_8_Pt8Line4_Group_0 = State()
    S_8_Pt8Line5a_DateFrom_0 = State()
    S_8_Pt8Line5b_DateTo_0 = State()

    S_8_Pt8Line6_OrgName_0 = State()
    S_8_Pt8Line8a_CityTown_0 = State()
    S_8_Pt8Line7b_State_0 = State()
    S_8_Pt8Line7c_Country_0 = State()
    S_8_Pt8Line8_Group_0 = State()

    S_9_Pt8Line9a_DateFrom_0 = State()
    S_9_Pt8Line9b_DateTo_0 = State()

    S_9_Pt8Line10_OrgName_0 = State()
    S_9_Pt8Line11a_CityTown_0 = State()
    S_9_Pt8Line11b_State_0 = State()
    S_9_Pt8Line11c_Country_0 = State()
    S_9_Pt8Line12_Group_0 = State()

    S_9_Pt8Line13a_DateFrom_0 = State()
    S_9_Pt8Line13b_DateTo_0 = State()

    WasEverRefusedToEnterUSAChoice = State()
    # S_9_Pt8Line14_YesNo_0 = State()
    # S_9_Pt8Line14_YesNo_1 = State()

    HaveEverBeenDeniedVisaToTheUSA = State()
    # S_9_Pt8Line15_YesNo_0 = State()
    # S_9_Pt8Line15_YesNo_1 = State()

    HaveEverWorkedWithoutAuthorization = State()
    # S_9_Pt8Line16_YesNo_0 = State()
    # S_9_Pt8Line16_YesNo_1 = State()

    HaveEverViolatedConditionsOfNonimmigrantStatus = State()
    # S_9_Pt8Line17_YesNo_0 = State()
    # S_9_Pt8Line17_YesNo_1 = State()

    HaveEverBeenInRemoval = State()
    # S_9_Pt8Line18_YesNo_0 = State()
    # S_9_Pt8Line18_YesNo_1 = State()

    HaveEverBeenIssuedAFinalOrder = State()
    # S_9_Pt8Line19_YesNo_0 = State()
    # S_9_Pt8Line19_YesNo_1 = State()

    HaveEverHadPriorFinalOrder = State()
    # S_9_Pt8Line20_YesNo_0 = State()
    # S_9_Pt8Line20_YesNo_1 = State()

    HaveEverHeldLawfulPermanentResidentStatus = State()
    # S_9_Pt8Line21_YesNo_0 = State()
    # S_9_Pt8Line21_YesNo_1 = State()

    HaveEverFailedToDepart = State()
    # S_9_Pt8Line22_YesNo_0 = State()
    # S_9_Pt8Line22_YesNo_1 = State()

    HaveEverAppliedForProtection = State()
    # S_9_Pt8Line23_YesNo_0 = State()
    # S_9_Pt8Line23_YesNo_1 = State()

    HaveEverBeenAJNonImmigrantExchange = State()
    # S_9_Pt8Line24a_YesNo_0 = State()
    # S_9_Pt8Line24a_YesNo_1 = State()

    HaveEverCompliedWithForeignResidenceRequirement = State()
    # S_9_Pt8Line24b_YesNo_0 = State()
    # S_9_Pt8Line24b_YesNo_1 = State()

    HaveBeenGrantedAWaiver = State()
    # S_9_Pt8Line24c_YesNo_0 = State()
    # S_9_Pt8Line24c_YesNo_1 = State()

    HaveEverBeenArrested = State()
    # S_9_Pt8Line25_YesNo_0 = State()
    # S_9_Pt8Line25_YesNo_1 = State()

    HaveEverCommitedACrime = State()
    # S_9_Pt8Line26_YesNo_0 = State()
    # S_9_Pt8Line26_YesNo_1 = State()

    HaveEverPledGuilty = State()
    # S_10_Pt8Line27_YesNo_0 = State()
    # S_10_Pt8Line27_YesNo_1 = State()

    HaveEverBeenOrderedPunishedByAJudge = State()
    # S_10_Pt8Line28_YesNo_0 = State()
    # S_10_Pt8Line28_YesNo_1 = State()

    HaveEverBeenDefendantOrTheAccused = State()
    # S_10_Pt8Line29_YesNo_0 = State()
    # S_10_Pt8Line29_YesNo_1 = State()

    HaveEverViolatedAnyControlledSubstanceLaw = State()
    # S_10_Pt8Line30_YesNo_0 = State()
    # S_10_Pt8Line30_YesNo_1 = State()

    HaveEverBeenConvictedOfTwoOrMoreOffenses = State()
    # S_10_Pt8Line31_YesNo_0 = State()
    # S_10_Pt8Line31_YesNo_1 = State()

    HaveEverIllicitlyTraffickedOrBenefitedFromNarcotics = State()
    # S_10_Pt8Line32_YesNo_0 = State()
    # S_10_Pt8Line32_YesNo_1 = State()

    HaveEverAssistedInTraffickingSubstances = State()
    # S_10_Pt8Line33_YesNo_0 = State()
    # S_10_Pt8Line33_YesNo_1 = State()

    YourFamilyIllicitlyTrafickedSubstances = State()
    # S_10_Pt8Line34_YesNo_0 = State()
    # S_10_Pt8Line34_YesNo_1 = State()

    HaveEverEngagedInProstitution = State()
    # S_10_Pt8Line35_YesNo_0 = State()
    # S_10_Pt8Line35_YesNo_1 = State()

    HaveEverProcuredProstitutes = State()
    # S_10_Pt8Line36_YesNo_0 = State()
    # S_10_Pt8Line36_YesNo_1 = State()

    HaveEverReceivedMoneyFromProstitution = State()
    # S_10_Pt8Line37_YesNo_0 = State()
    # S_10_Pt8Line37_YesNo_1 = State()

    IllegalGambling = State()
    # S_10_Pt8Line38_YesNo_0 = State()
    # S_10_Pt8Line38_YesNo_1 = State()

    HaveEverExercisedImmunityForCriminalOffense = State()
    # S_10_Pt8Line39_YesNo_0 = State()
    # S_10_Pt8Line39_YesNo_1 = State()

    HaveEverServingForeignGovernment = State()
    # S_10_Pt8Line40_YesNo_0 = State()
    # S_10_Pt8Line40_YesNo_1 = State()

    HaveEverInductedByForce = State()
    # S_10_Pt8Line41_YesNo_0 = State()
    # S_10_Pt8Line41_YesNo_1 = State()

    HaveEverTraffickedPersonInvoluntary = State()
    # S_10_Pt8Line42_YesNo_0 = State()
    # S_10_Pt8Line42_YesNo_1 = State()

    HaveEverKnowinglyAidedTraffickingPersonInvoluntary = State()
    # S_10_Pt8Line43_YesNo_0 = State()
    # S_10_Pt8Line43_YesNo_1 = State()

    FamilyEngagedInTraffickingPersonInvoluntary = State()
    # S_10_Pt8Line44_YesNo_0 = State()
    # S_10_Pt8Line44_YesNo_1 = State()

    HaveEverEngagedInMoneyLaundering = State()
    # S_10_Pt8Line45_YesNo_0 = State()
    # S_10_Pt8Line45_YesNo_1 = State()

    IntendToEngageInEspionage = State()
    # S_11_Pt8Line46a_YesNo_0 = State()
    # S_11_Pt8Line46a_YesNo_1 = State()

    IntendToEngageInProhibitedExport = State()
    # S_11_Pt8Line46b_YesNo_0 = State()
    # S_11_Pt8Line46b_YesNo_1 = State()

    IntendToOwerthrowUSGovernment = State()
    # S_11_Pt8Line46c_YesNo_0 = State()
    # S_11_Pt8Line46c_YesNo_1 = State()

    IntendToEndangerWelfare = State()
    # S_11_Pt8Line46d_YesNo_0 = State()
    # S_11_Pt8Line46d_YesNo_1 = State()

    IntendToEngageInAnyUnlawfulActivity = State()
    # S_11_Pt8Line46e_YesNo_0 = State()
    # S_11_Pt8Line46e_YesNo_1 = State()

    IntendToAdverseForeignPolicy = State()
    # S_11_Pt8Line47_YesNo_0 = State()
    # S_11_Pt8Line47_YesNo_1 = State()

    HaveEverCommitedACrime_2 = State()
    # S_11_Pt8Line48a_YesNo_0 = State()
    # S_11_Pt8Line48a_YesNo_1 = State()

    HaveEverBeenInOrganizationThatCommitedACrime = State()
    # S_11_Pt8Line48b_YesNo_0 = State()
    # S_11_Pt8Line48b_YesNo_1 = State()

    HaveEverDoneServiceToOrganizationThatCommitedACrime = State()
    # S_11_Pt8Line48c_YesNo_0 = State()
    # S_11_Pt8Line48c_YesNo_1 = State()

    HaveEverProvidedToOrganizationThatCommitedACrime = State()
    # S_11_Pt8Line48d_YesNo_0 = State()
    # S_11_Pt8Line48d_YesNo_1 = State()

    HaveEverProvidedToOrganizationThatCommitedACrime_2 = State()
    # S_11_Pt8Line48e_YesNo_0 = State()
    # S_11_Pt8Line48e_YesNo_1 = State()

    HaveEverReceivedMilitaryTraining = State()
    # S_11_Pt8Line49_YesNo_0 = State()
    # S_11_Pt8Line49_YesNo_1 = State()

    IntendToEngageInCommitingACrime = State()
    # S_11_Pt8Line50_YesNo_0 = State()
    # S_11_Pt8Line50_YesNo_1 = State()

    SpouceOfCriminalChoice = State()
    # S_11_Pt8Line51a_YesNo_0 = State()
    # S_11_Pt8Line51a_YesNo_1 = State()

    SpouceOfCriminalChoice_2 = State()
    # S_11_Pt8Line51b_YesNo_0 = State()
    # S_11_Pt8Line51b_YesNo_1 = State()

    SpouceOfCriminalChoice_3 = State()
    # S_11_Pt8Line51c_YesNo_0 = State()
    # S_11_Pt8Line51c_YesNo_1 = State()

    SpouceOfCriminalChoice_4 = State()
    # S_11_Pt8Line51d_YesNo_0 = State()
    # S_11_Pt8Line51d_YesNo_1 = State()

    SpouceOfCriminalChoice_5 = State()
    # S_11_Pt8Line51e_YesNo_0 = State()
    # S_11_Pt8Line51e_YesNo_1 = State()

    SpouceOfCriminalChoice_6 = State()
    # S_11_Pt8Line51f_YesNo_0 = State()
    # S_11_Pt8Line51f_YesNo_1 = State()

    HaveEverTradedWeaponOfHarm = State()
    # S_11_Pt8Line52_YesNo_0 = State()
    # S_11_Pt8Line52_YesNo_1 = State()

    HaveEverWorkedInPrison = State()
    # S_12_Pt8Line53_YesNo_0 = State()
    # S_12_Pt8Line53_YesNo_1 = State()

    HaveEverUsedWeaponAgainstPeople = State()
    # S_12_Pt8Line54_YesNo_0 = State()
    # S_12_Pt8Line54_YesNo_1 = State()

    HaveEverServedInMilitary = State()
    # S_12_Pt8Line55_YesNo_0 = State()
    # S_12_Pt8Line55_YesNo_1 = State()

    HaveEverBeenInCommunistParty = State()
    # S_12_Pt8Line56_YesNo_0 = State()
    # S_12_Pt8Line56_YesNo_1 = State()

    ParticipatedInWW2AsNazi = State()
    # S_12_Pt8Line57_YesNo_0 = State()
    # S_12_Pt8Line57_YesNo_1 = State()

    HaveEverOrderedActsGenocide = State()
    # S_12_Pt8Line58a_YesNo_0 = State()
    # S_12_Pt8Line58a_YesNo_1 = State()

    HaveEverKilledAnyBody = State()
    # S_12_Pt8Line58b_YesNo_0 = State()
    # S_12_Pt8Line58b_YesNo_1 = State()

    HaveEverIntentionalyInjuredAnyBody = State()
    # S_12_Pt8Line58c_YesNo_0 = State()
    # S_12_Pt8Line58c_YesNo_1 = State()

    HaveEverHadSexWithoutConsentOfPartner = State()
    # S_12_Pt8Line58d_YesNo_0 = State()
    # S_12_Pt8Line58d_YesNo_1 = State()

    HaveEverTriedToStopReligiousPerson = State()
    # S_12_Pt8Line58e_YesNo_0 = State()
    # S_12_Pt8Line58e_YesNo_1 = State()

    HaveEverRecrutedTeensAsMercenaries = State()
    # S_12_Pt8Line59_YesNo_0 = State()
    # S_12_Pt8Line59_YesNo_1 = State()

    HaveEverUsedTeensAsServantsInCombat = State()
    # S_12_Pt8Line60_YesNo_0 = State()
    # S_12_Pt8Line60_YesNo_1 = State()

    AreYouSubjectToThePublicHargeGround = State()
    # S_12_Pt8Line61_YesNo_0 = State()
    # S_12_Pt8Line61_YesNo_1 = State()

    S_12_Pt8Line62_FamilyStatus_0 = State()

    IndicateAnnualHouseHoldIncome = State()
    # S_12_Pt8Line63_CB_0 = State()
    # S_12_Pt8Line63_CB_1 = State()
    # S_12_Pt8Line63_CB_2 = State()
    # S_12_Pt8Line63_CB_3 = State()
    # S_12_Pt8Line63_CB_4 = State()

    IndentifyTotalValueOfYourAssets = State()
    # S_12_Pt8Line64_CB_0 = State()
    # S_12_Pt8Line64_CB_1 = State()
    # S_12_Pt8Line64_CB_2 = State()
    # S_12_Pt8Line64_CB_3 = State()
    # S_12_Pt8Line64_CB_4 = State()

    IndentifyTotalValueOfYourLiabilities = State()
    # S_13_Pt8Line65_CB_0 = State()
    # S_13_Pt8Line65_CB_1 = State()
    # S_13_Pt8Line65_CB_2 = State()
    # S_13_Pt8Line65_CB_3 = State()
    # S_13_Pt8Line65_CB_4 = State()

    IndicateEducationLevel = State()
    # S_13_Pt8Line66_CB_0 = State()
    # S_13_Pt8Line66_CB_1 = State()
    # S_13_Pt8Line66_CB_2 = State()
    # S_13_Pt8Line66_CB_3 = State()
    # S_13_Pt8Line66_CB_4 = State()
    # S_13_Pt8Line66_CB_5 = State()
    # S_13_Pt8Line66_CB_6 = State()
    # S_13_Pt8Line66_CB_7 = State()
    # S_13_Pt8Line66_CB_8 = State()

    S_13_Pt8Line67_Row1_0 = State()
    # S_13_Pt8Line67_Row2_0 = State()
    # S_13_Pt8Line67_Row3_0 = State()
    # S_13_Pt8Line67_Row4_0 = State()
    # S_13_Pt8Line67_Row5_0 = State()
    # S_13_Pt8Line67_Row6_0 = State()
    # S_13_Pt8Line67_Row7_0 = State()
    # S_13_Pt8Line67_Row8_0 = State()

    HaveEverRecievedSupplementalSecurityIncome = State()
    # S_13_Pt8Line68a_YesNo_0 = State()
    # S_13_Pt8Line68a_YesNo_1 = State()

    HaveEverRecievedLongTermInstitutionalization = State()
    # S_13_Pt8Line68b_YesNo_0 = State()
    # S_13_Pt8Line68b_YesNo_1 = State()

    # Benefit 1
    S_13_Pt8Line68c_Column1Row1_0 = State()
    S_13_Pt8Line68c_Column2Row1_0 = State()
    S_13_Pt8Line68c_Column3Row1_0 = State()
    S_13_Pt8Line68c_Column4Row1_0 = State()

    # Benefit 2
    S_13_Pt8Line68c_Column1Row2_0 = State()
    S_13_Pt8Line68c_Column2Row2_0 = State()
    S_13_Pt8Line68c_Column3Row2_0 = State()
    S_13_Pt8Line68c_Column4Row2_0 = State()

    # Benefit 3
    S_13_Pt8Line68c_Column1Row3_0 = State()
    S_13_Pt8Line68c_Column2Row3_0 = State()
    S_13_Pt8Line68c_Column3Row3_0 = State()
    S_13_Pt8Line68c_Column4Row3_0 = State()

    # Benefit 4
    S_13_Pt8Line68c_Column1Row4_0 = State()
    S_13_Pt8Line68c_Column2Row4_0 = State()
    S_13_Pt8Line68c_Column3Row4_0 = State()
    S_13_Pt8Line68c_Column4Row4_0 = State()

    # Institutionalization 1
    S_13_Pt8Line68d_Column1Row1_0 = State()
    S_13_Pt8Line68d_Column2Row1_0 = State()
    S_13_Pt8Line68d_Column3Row1_0 = State()
    S_13_Pt8Line68d_Column4Row1_0 = State()

    # Institutionalization 2
    S_13_Pt8Line68d_Column1Row2_0 = State()
    S_13_Pt8Line68d_Column2Row2_0 = State()
    S_13_Pt8Line68d_Column3Row2_0 = State()
    S_13_Pt8Line68d_Column4Row2_0 = State()

    # Institutionalization 3
    S_13_Pt8Line68d_Column1Row3_0 = State()
    S_13_Pt8Line68d_Column2Row3_0 = State()
    S_13_Pt8Line68d_Column3Row3_0 = State()
    S_13_Pt8Line68d_Column4Row3_0 = State()

    # Institutionalization 4
    S_13_Pt8Line68d_Column1Row4_0 = State()
    S_13_Pt8Line68d_Column2Row4_0 = State()
    S_13_Pt8Line68d_Column3Row4_0 = State()
    S_13_Pt8Line68d_Column4Row4_0 = State()

    HaveEverFailedToAttendRemovalProceeding = State()
    # S_14_Pt8Line69a_YesNo_0 = State()
    # S_14_Pt8Line69a_YesNo_1 = State()

    YouHadReasonableCause = State()
    # S_14_Pt8Line69b_YesNo_0 = State()
    # S_14_Pt8Line69b_YesNo_1 = State()

    HaveEverSubmitedFraudilentDocumentation = State()
    # S_14_Pt8Line70_YesNo_0 = State()
    # S_14_Pt8Line70_YesNo_1 = State()

    HaveEverLiedToObtainVisa = State()
    # S_14_Pt8Line71_YesNo_0 = State()
    # S_14_Pt8Line71_YesNo_1 = State()

    HaveEverFalselyClaimedToBeUSCitizen = State()
    # S_14_Pt8Line72_YesNo_0 = State()
    # S_14_Pt8Line72_YesNo_1 = State()

    HaveEverBeenStowaway = State()
    # S_14_Pt8Line73_YesNo_0 = State()
    # S_14_Pt8Line73_YesNo_1 = State()

    HaveEverKnowinglyAidedForeignNationalToEnterUS = State()
    # S_14_Pt8Line74_YesNo_0 = State()
    # S_14_Pt8Line74_YesNo_1 = State()

    AreUnderFinalOrderOfCivilPenalty = State()
    # S_14_Pt8Line75_YesNo_0 = State()
    # S_14_Pt8Line75_YesNo_1 = State()

    HaveEverBeenDeportedFromUS = State()
    # S_14_Pt8Line76_YesNo_0 = State()
    # S_14_Pt8Line76_YesNo_1 = State()

    HaveEverEnteredUSWithoutParole = State()
    # S_14_Pt8Line77_YesNo_0 = State()
    # S_14_Pt8Line77_YesNo_1 = State()

    BeenUnlawfullyPresentInUS_1 = State()
    # S_14_Pt8Line78a_YesNo_0 = State()
    # S_14_Pt8Line78a_YesNo_1 = State()

    BeenUnlawfullyPresentInUS_2 = State()
    # S_14_Pt8Line78b_YesNo_0 = State()
    # S_14_Pt8Line78b_YesNo_1 = State()

    HaveEverReenteredUSWithoutParole_1 = State()
    # S_14_Pt8Line79a_YesNo_0 = State()
    # S_14_Pt8Line79a_YesNo_1 = State()

    HaveEverReenteredUSWithoutParole_2 = State()
    # S_14_Pt8Line79b_YesNo_0 = State()
    # S_14_Pt8Line79b_YesNo_1 = State()

    PlanToPracticePolygamyInUs = State()
    # S_14_Pt8Line80_YesNo_0 = State()
    # S_14_Pt8Line80_YesNo_1 = State()

    AcompanyingAnotherForeignNational = State()
    # S_14_Pt8Line81_YesNo_0 = State()
    # S_14_Pt8Line81_YesNo_1 = State()

    HaveEverAssistedInDetainingCustody = State()
    # S_14_Pt8Line82_YesNo_0 = State()
    # S_14_Pt8Line82_YesNo_1 = State()

    HaveEverVotedInViolationOfConstitutionalRegulation = State()
    # S_14_Pt8Line83_YesNo_0 = State()
    # S_14_Pt8Line83_YesNo_1 = State()

    HaveEverRenouncedUSCitizenshipToAvoidTaxes = State()
    # S_14_Pt8Line84_YesNo_0 = State()
    # S_14_Pt8Line84_YesNo_1 = State()

    HaveEverAppliedForExemption = State()
    # S_14_Pt8Line85a_YesNo_0 = State()
    # S_14_Pt8Line85a_YesNo_1 = State()

    BeenRelievedFromTraining = State()
    # S_15_Pt8Line85b_YesNo_0 = State()
    # S_15_Pt8Line85b_YesNo_1 = State()

    BeenConvictedOfDesertionFromUSForces = State()
    # S_15_Pt8Line85c_YesNo_0 = State()
    # S_15_Pt8Line85c_YesNo_1 = State()

    HaveEverRemainedOutsideUSToAvoidTrainingService = State()
    # S_15_Pt8Line86a_YesNo_0 = State()
    # S_15_Pt8Line86a_YesNo_1 = State()

    S_15_Pt8Line86b_Nationality_0 = State()

    AreYouRequestingAccomidationBecauseOfDisabilities = State()
    # S_15_Pt9Line1_YesNo_0 = State()
    # S_15_Pt9Line1_YesNo_1 = State()

    S_15_Pt9Line2a_Deaf_0 = State()
    S_15_Pt9Line2a_Accommodation_0 = State()

    S_15_Pt9Line2b_Blind_0 = State()
    S_15_Pt9Line2b_Accommodation_0 = State()

    S_15_Pt9Line2c_Other_0 = State()
    S_15_Pt9Line2c_Accommodation_0 = State()

    ApplicantStatementChoice = State()

    S_15_Pt10Line1b_Language_0 = State()

    S_15_Pt10Line2_PreparerCB_0 = State()
    S_15_Pt10Line2_Preparer_0 = State()

    S_15_Pt10Line3_DaytimePhone_0 = State()
    S_15_Pt10Line4_MobilePhone_0 = State()
    S_15_Pt10Line5_Email_0 = State()

    S_16_Pt5Line6a_Signature_0 = State()
    S_16_Pt10Line6b_Date_0 = State()

    # Interpreter
    S_15_Pt10Line1_English_1 = State()


    S_16_Pt1Line10_AlienNumber_1 = State()
    S_16_Pt11Line1a_FamilyName_0 = State()
    S_16_Pt11Line1b_GivenName_0 = State()
    S_16_Pt11Line2_OrgName_0 = State()

    S_16_Pt11Line3_StreetNumberName_0 = State()
    S_16_Pt11Line3_AptSteFlrNumber_0 = State()

    S_16_Pt11Line3_Unit_0 = State()
    S_16_Pt11Line3_Unit_1 = State()
    S_16_Pt11Line3_Unit_2 = State()

    S_16_Pt11Line3_CityOrTown_0 = State()
    S_16_Pt11Line3_State_0 = State()
    S_16_Pt11Line3_ZipCode_0 = State()
    S_16_Pt11Line3_Province_0 = State()

    S_16_Pt11Line3_PostalCode_0 = State()

    S_16_Pt11Line3_Country_0 = State()

    S_16_Pt11Line4_DayPhone_0 = State()
    S_16_Pt11Line5_MobilePhone_0 = State()
    S_16_Pt11Line6_Email_0 = State()

    S_17_Pt1Line10_AlienNumber_1 = State()

    S_17_Part11_NameofLanguage_0 = State()

    S_17_Pt5Line6a_Signature_1 = State()

    S_17_Pt11Line7b_DateofSignature_0 = State()
    S_17_Pt12Line1a_PreparerFamilyName_0 = State()

    S_17_Pt12Line1b_PreparerGivenName_0 = State()
    S_17_Pt12Line2_BusinessName_0 = State()

    S_17_Pt12Line3_StreetNumberName_0 = State()
    S_17_Pt12Line3_AptSteFlrNumber_0 = State()

    S_17_Pt12Line3_Unit_0 = State()
    S_17_Pt12Line3_Unit_1 = State()
    S_17_Pt12Line3_Unit_2 = State()

    S_17_Pt12Line3_CityOrTown_0 = State()

    S_17_Pt12Line3_State_0 = State()
    S_17_Pt12Line3_ZipCode_0 = State()
    S_17_Pt12Line3_Province_0 = State()
    S_17_Pt12Line3_PostalCode_0 = State()

    S_17_Pt12Line3_Country_0 = State()
    S_17_Pt12Line4_DaytimePhoneNumber1_0 = State()
    S_17_Pt12Line5_MobileNumber_0 = State()
    S_17_Pt12Line6_Email_0 = State()
    S_17_Part12Line7_Checkbox_0 = State()
    S_17_Part12Line7_Checkbox_1 = State()
    S_17_Part12Line7b_Extend_0 = State()
    S_17_Part12Line7b_NotExtend_0 = State()

    S_18_Pt1Line10_AlienNumber_1 = State()

    S_18_Pt12Line8a_Signature_0 = State()
    S_18_Pt12Line8b_DateofSignature_0 = State()
