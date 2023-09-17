from aiogram.dispatcher.filters.state import State, StatesGroup


class FormI765(StatesGroup):

    ReasonForApplyingChoice = State()
    # Part1_Checkbox_0 = State()
    # Part1_Checkbox_1 = State()
    # Part1_Checkbox_2 = State()

    Line1a_FamilyName_0 = State()
    Line1b_GivenName_0 = State()
    Line1c_MiddleName_0 = State()

    Used_Other_Names = State()

    Line2a_FamilyName_0 = State()
    Line2b_GivenName_0 = State()
    Line2c_MiddleName_0 = State()

    Used_Other_Names_1 = State()

    Line3a_FamilyName_1 = State()
    Line3b_GivenName_1 = State()
    Line3c_MiddleName_1 = State()

    Used_Other_Names_2 = State()

    Line3a_FamilyName_0 = State()
    Line3b_GivenName_0 = State()
    Line3c_MiddleName_0 = State()

    Line4a_InCareofName_0 = State()
    Line4b_StreetNumberName_0 = State()

    AptSteFlr_Choice_Mailing = State()
    # Pt2Line5_Unit_2 = State()
    # Pt2Line5_Unit_0 = State()
    # Pt2Line5_Unit_1 = State()

    Pt2Line5_AptSteFlrNumber_0 = State()

    Pt2Line5_CityOrTown_0 = State()
    Pt2Line5_State_0 = State()
    Pt2Line5_ZipCode_0 = State()

    MailingAddressChoice = State()
    # Part2Line5_Checkbox_0 = State()
    # Part2Line5_Checkbox_1 = State()

    Pt2Line7_StreetNumberName_0 = State()

    AptSteFlr_Choice_Physical = State()
    # Pt2Line7_Unit_2 = State()
    # Pt2Line7_Unit_0 = State()
    # Pt2Line7_Unit_1 = State()

    Pt2Line7_AptSteFlrNumber_0 = State()
    Pt2Line7_CityOrTown_0 = State()
    Pt2Line7_State_0 = State()
    Pt2Line7_ZipCode_0 = State()

    Line7_AlienNumber_0 = State()
    Line8_ElisAccountNumber_0 = State()

    GenderChoice = State()
    # Line9_Checkbox_0 = State()
    # Line9_Checkbox_1 = State()

    MaritalStatusChoice = State()
    # Line10_Checkbox_0 = State()
    # Line10_Checkbox_1 = State()
    # Line10_Checkbox_2 = State()
    # Line10_Checkbox_3 = State()

    AppliedEarlierChoice = State()
    # Line19_Checkbox_0 = State()
    # Line19_Checkbox_1 = State()

    SSACardWasIssuedChoice = State()
    # Line12a_Checkbox_0 = State()
    # Line12a_Checkbox_1 = State()

    Line12b_SSN_0 = State()
    WantSSACardToBeIssuedChoice = State()
    # Line13_Checkbox_0 = State()
    # Line13_Checkbox_1 = State()

    WantToShareInformationWithSSAChoice = State()
    # Line14_Checkbox_No_0 = State()
    # Line14_Checkbox_Yes_0 = State()

    Line15a_FamilyName_0 = State()
    Line15b_GivenName_0 = State()
    Line16a_FamilyName_0 = State()
    Line16b_GivenName_0 = State()
    Line17a_CountryOfBirth_0 = State()
    Line17b_CountryOfBirth_0 = State()

    Line18a_CityTownOfBirth_0 = State()
    Line18b_CityTownOfBirth_0 = State()
    Line18c_CountryOfBirth_0 = State()
    Line19_DOB_0 = State()
    Line20a_I94Number_0 = State()
    Line20b_Passport_0 = State()
    Line20c_TravelDoc_0 = State()
    Line20d_CountryOfIssuance_0 = State()
    Line20e_ExpDate_0 = State()
    Line21_DateOfLastEntry_0 = State()
    Place_OfLastEntry_0 = State()
    Line23_StatusLastEntry_0 = State()
    Line24_CurrentStatus_0 = State()
    Line26_SEVISnumber_0 = State()
    EligibilityCategory = State()
    # area_1_section_1 = State()
    # area_1_section_2 = State()
    # area_1_section_3 = State()
    Line27a_Degree_0 = State()
    Line27b_Everify_0 = State()
    Line27c_EverifyIDNumber_0 = State()
    Line28_ReceiptNumber_0 = State()

    EligibilityCategoryArrestedChoice = State()
    # PtLine29_YesNo_0 = State()
    # PtLine29_YesNo_1 = State()

    Line18a_Receipt_0_Line30a_ReceiptNumber_0 = State()

    EligibilityCategoryArrestedChoice_1 = State()
    # PtLine30b_YesNo_0 = State()
    # PtLine30b_YesNo_1 = State()

    ApplicantStatementChoice = State()
    # Pt3Line1Checkbox_1 = State()
    #
    # Pt3Line1Checkbox_0 = State()
    Pt3Line1b_Language_0 = State()

    Part3_Checkbox_0 = State()
    Pt3Line2_RepresentativeName_0 = State()

    Pt3Line3_DaytimePhoneNumber1_0 = State()
    Pt3Line4_MobileNumber1_0 = State()
    Pt3Line5_Email_0 = State()

    Pt4Line6_Checkbox_0 = State()

    Pt3Line7a_Signature_0 = State()
    Pt3Line7b_DateofSignature_0 = State()
    Pt4Line1a_InterpreterFamilyName_0 = State()
    Pt4Line1b_InterpreterGivenName_0 = State()
    Pt4Line2_InterpreterBusinessorOrg_0 = State()
    Pt5Line3a_StreetNumberName_0 = State()

    Pt5Line3b_Unit_1 = State()
    Pt5Line3b_Unit_2 = State()
    Pt5Line3b_Unit_0 = State()

    Pt5Line3b_AptSteFlrNumber_0 = State()
    Pt5Line3c_CityOrTown_0 = State()
    Pt5Line3d_State_0 = State()
    Pt5Line3e_ZipCode_0 = State()

    Pt5Line3f_Province_0 = State()
    Pt5Line3g_PostalCode_0 = State()
    Pt5Line3h_Country_0 = State()
    Pt4Line4_InterpreterDaytimeTelephone_0 = State()
    Pt4Line5_MobileNumber_0 = State()
    Pt4Line6_Email_0 = State()
    Part4_NameofLanguage_0 = State()
    Pt4Line6a_Signature_0 = State()
    Pt4Line6b_DateofSignature_0 = State()

    Part5Line7_Checkbox_0 = State()
    Part5Line7_Checkbox_1 = State()
    Part5Line7b_Checkbox_0 = State()
    Part5Line7b_Checkbox_1 = State()

    Pt5Line1a_PreparerFamilyName_0 = State()
    Pt5Line1b_PreparerGivenName_0 = State()
    Pt5Line2_BusinessName_0 = State()
    Pt6Line3a_StreetNumberName_0 = State()

    Pt6Line3b_Unit_1 = State()
    Pt6Line3b_Unit_0 = State()
    Pt6Line3b_Unit_2 = State()

    Pt6Line3b_AptSteFlrNumber_0 = State()
    Pt6Line3c_CityOrTown_0 = State()
    Pt6Line3d_State_0 = State()
    Pt6Line3e_ZipCode_0 = State()
    Pt6Line3f_Province_0 = State()
    Pt6Line3g_PostalCode_0 = State()
    Pt6Line3h_Country_0 = State()
    Pt5Line4_DaytimePhoneNumber1_0 = State()
    Pt5Line5_PreparerFaxNumber_0 = State()
    Pt5Line6_Email_0 = State()

    Pt5Line8a_Signature_0 = State()
    Pt5Line8b_DateofSignature_0 = State()

    _7_Line1a_FamilyName_0 = State()
    _7_Line1b_GivenName_0 = State()
    _7_Line1c_MiddleName_0 = State()
    _7_Line7_AlienNumber_0 = State()
    Pt6Line3a_PageNumber_0 = State()
    Pt6Line3b_PartNumber_0 = State()
    Pt6Line3c_ItemNumber_0 = State()
    Pt6Line4d_AdditionalInfo_1 = State()
    Pt6Line4a_PageNumber_0 = State()
    Pt6Line4b_PartNumber_0 = State()
    Pt6Line4c_ItemNumber_0 = State()
    Pt6Line4d_AdditionalInfo_0 = State()

    Pt6Line5a_PageNumber_0 = State()
    Pt6Line5b_PartNumber_0 = State()
    Pt6Line5c_ItemNumber_0 = State()
    Pt6Line5d_AdditionalInfo_0 = State()
    Pt6Line6a_PageNumber_0 = State()
    Pt6Line6b_PartNumber_0 = State()
    Pt6Line6c_ItemNumber_0 = State()
    Pt6Line6d_AdditionalInfo_0 = State()
    Pt6Line7a_PageNumber_0 = State()
    Pt6Line7b_PartNumber_0 = State()
    Pt6Line7c_ItemNumber_0 = State()
    Pt6Line7d_AdditionalInfo_0 = State()
