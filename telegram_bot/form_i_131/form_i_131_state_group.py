from aiogram.dispatcher.filters.state import State, StatesGroup


class FormI131(StatesGroup):
    Page1_1a_FamilyName_0 = State()
    Page1_1b_GivenName_0 = State()
    Page1_1c_MiddleName_0 = State()
    Page1_2a_InCareofName_0 = State()

    Page1_2b_StreetNumberName_0 = State()

    Page1_TypeOfBuildingChoice = State()
    # Page1_2c_Unit_0 = State()
    # Page1_2c_Unit_1 = State()
    # Page1_2c_Unit_2 = State()

    Page1_2c_AptSteFlrNumber_0 = State()

    Page1_2d_CityOrTown_0 = State()
    Page1_2e_State_0 = State()
    Page1_2f_ZipCode_0 = State()

    Page1_2g_PostalCode_0 = State()
    Page1_2h_Province_0 = State()
    Page1_2i_Country_0 = State()

    Page1_3_AlienNumber_0 = State()

    Page1_4_CountryOfBirth_0 = State()
    Page1_5_CountryOfCitizenship_0 = State()
    Page1_6_ClassofAdmission_0 = State()

    Page1_ChooseGenderChoice = State()
    # Page1_7_Female_0 = State()
    # Page1_7_Male_0 = State()

    Page1_8_DateOfBirth_0 = State()

    Page1_9_SSN_0 = State()

    Page2_ApplicationTypeChoice = State()
    # Page2_1a_checkbox_0 = State()
    # Page2_1b_checkbox_0 = State()
    # Page2_1c_checkbox_0 = State()
    # Page2_1d_checkbox_0 = State()
    # Page2_1e_checkbox_0 = State()
    # Page2_1f_checkbox_0 = State()

    Page2_2a_FamilyName_0 = State()
    Page2_2b_GivenName_0 = State()
    Page2_2c_MiddleName_0 = State()

    Page2_2d_DateOfBirth_0 = State()
    Page2_2e_CountryOfBirth_0 = State()
    Page2_2f_CountryOfCitizenship_0 = State()

    Page2_2g_DaytimePhoneNumber1_0 = State()
    Page2_2g_DaytimePhoneNumber2_0 = State()

    Page2_2h_InCareofName_0 = State()
    Page2_2i_StreetNumberName_0 = State()

    Page2_TypeOfBuildingChoice = State()
    # Page2_2j_Unit_0 = State()
    # Page2_2j_Unit_1 = State()
    # Page2_2j_Unit_2 = State()

    Page2_2j_AptSteFlrNumber_0 = State()

    Page2_2k_CityOrTown_0 = State()

    Page2_2l_State_0 = State()
    Page2_2m_ZipCode_0 = State()

    Page2_2n_PostalCode_0 = State()
    Page2_2o_Province_0 = State()

    Page2_2p_Country_0 = State()

    Page2_1_DateIntendedDeparture_0 = State()
    Page2_2_ExpectedLengthTrip_0 = State()

    PeopleIncludedInApplicationAreInExclusionChoice = State()
    # Page2_3a_Yes_0 = State()
    # Page2_3a_No_0 = State()

    Page2_3b_NameDHSOffice_0 = State()

    Page2_HadBeenPermitedReentryChoice = State()
    # Page2_4a_Yes_0 = State()
    # Page2_4a_No_0 = State()

    Page2_4b_DateIssued_0 = State()

    Page2_4c_Disposition_0 = State()

    Page3_WhereToSendTravelDocumentChoice = State()

    # Page3_5_USAddress_0 = State()
    # Page3_6_USEmbassy_0 = State()

    Page3_6a_CityOrTown_0 = State()
    Page3_6b_Country_0 = State()

    # Page3_7_DHSOffice_0 = State()
    Page3_7a_CityOrTown_0 = State()
    Page3_7b_Country_0 = State()

    Page3_NoticeAddressChoice = State()
    # Page3_8_AddressPart2_0 = State()
    # Page3_9_AddressBelow_0 = State()

    Page3_10a_InCareofName_0 = State()
    Page3_10b_StreetNumberName_0 = State()

    Page3_TypeOfBuildingChoice = State()
    # Page3_10c_Unit_0 = State()
    # Page3_10c_Unit_1 = State()
    # Page3_10c_Unit_2 = State()

    Page3_10c_AptSteFlrNumber_0 = State()

    Page3_10d_CityOrTown_0 = State()
    Page3_10e_State_0 = State()
    Page3_10f_ZipCode_0 = State()

    Page3_10g_PostalCode_0 = State()

    Page3_10h_Province_0 = State()

    Page3_10i_Country_0 = State()

    Page3_10j_DaytimePhoneNumber1_0 = State()
    Page3_10j_DaytimePhoneNumber2_0 = State()

    Page3_1a_Purpose_0 = State()
    Page3_1b_ListCountries_0 = State()

    Page3_1a_Lessthan6_0 = State()
    Page3_1b_6months_0 = State()
    Page3_1c_1to2_0 = State()
    Page3_1d_2to3_0 = State()
    Page3_1e_3to4_0 = State()
    Page3_1f_morethan_0 = State()

    Page3_2_Yes_0 = State()
    Page3_2_No_0 = State()

    Page4_1_CountryRefugee_0 = State()
    Page4_2_No1_0 = State()
    Page4_2_Yes1_0 = State()

    Page4_3a_Yes1_0 = State()
    Page4_3a_No1_0 = State()

    Page4_3b_No_0 = State()
    Page4_3b_Yes_0 = State()

    Page4_3c_Yes_0 = State()
    Page4_3c_No_0 = State()

    Page4_4a_No_1 = State()
    Page4_4a_Yes_1 = State()

    Page4_4b_Yes_0 = State()
    Page4_4b_No_0 = State()

    Page4_4c_No_0 = State()
    Page4_4c_Yes_0 = State()

    Page4_1_OneTrip_0 = State()
    Page4_1_MoreThanOne_0 = State()

    Page4_2a_CityOrTown_0 = State()
    Page4_2b_Country_0 = State()

    Page4_3_AddressPart2_0 = State()
    Page4_4_AddressBelow_0 = State()

    Page4_4a_InCareofName_0 = State()
    Page4_4b_StreetNumberName_0 = State()

    Page4_4c_Unit_0 = State()
    Page4_4c_Unit_1 = State()
    Page4_4c_Unit_2 = State()

    Page4_4c_AptSteFlrNumber_0 = State()
    Page4_4d_CityOrTown_0 = State()

    Page4_4e_State_0 = State()
    Page4_4f_ZipCode_0 = State()

    Page4_4g_PostalCode_0 = State()
    Page4_4h_Province_0 = State()
    Page4_4i_Country_0 = State()

    Page4_4j_DaytimePhoneNumber1_0 = State()
    Page4_4j_DaytimePhoneNumber2_0 = State()
    Page4_4j_DaytimePhoneNumber3_0 = State()

    Page4_1_OAW_0 = State()
    Page4_1_OAW_1 = State()

    Page5_1a_SignatureofApplicant_0 = State()
    Page5_1b_DateOfSignature_0 = State()

    Page5__2_DaytimePhoneNumber1_0 = State()
    Page5__2_DaytimePhoneNumber2_0 = State()
    Page5__2_DaytimePhoneNumber3_0 = State()

    Page5_1a_PreparerFamilyName_0 = State()
    Page5_1b_PreparerGivenName_0 = State()
    Page5_2_BusinessName_0 = State()

    Page5_3a_StreetNumberName_0 = State()

    Page5_3b_Unit_0 = State()
    Page5_3b_Unit_1 = State()
    Page5_3b_Unit_2 = State()

    Page5_3b_AptSteFlrNumber_0 = State()

    Page5_3c_CityOrTown_0 = State()
    Page5_3d_State_0 = State()
    Page5_3e_ZipCode_0 = State()

    Page5_3f_PostalCode_0 = State()
    Page5_3g_Province_0 = State()
    Page5_3h_Country_0 = State()

    Page5_4_DaytimePhoneNumber1_0 = State()
    Page5_4_DaytimePhoneNumber2_0 = State()
    Page5_4_DaytimePhoneNumber3_0 = State()

    Page5_4_Extension_0 = State()
    Page5_5_Email_0 = State()
    Page5_6a_SignatureofPreparer_0 = State()

    Page5_6b_DateOfSignature_0 = State()
