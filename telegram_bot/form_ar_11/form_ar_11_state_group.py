from aiogram.dispatcher.filters.state import State, StatesGroup


class Form_AR_11(StatesGroup):
    # Information About You
    S1_FamilyName = State()
    S1_GivenName = State()
    S1_MiddleName = State()
    S1_DateOfBirth = State()
    AlienNumber = State()

    # Present Physical Address
    S2B_StreetNumberName = State()
    S2B_CityOrTown = State()
    Page1_TypeOfBuildingChoice = State()
    S2B_AptSteFlrNumber = State()
    S2B_State = State()
    S2B_ZipCode = State()

    # Previous Physical Address
    S2A_StreetNumberName = State()
    S2A_CityOrTown = State()
    Page1_TypeOfBuildingChoice_2 = State()
    S2A_AptSteFlrNumber = State()
    S2A_State = State()
    S2A_ZipCode = State()

    MailingAddressSameAsPhysicalAddress = State()

    # Mailing Address (optional)
    S2C_StreetNumberName = State()
    S2C_CityOrTown = State()
    Page1_TypeOfBuildingChoice_3 = State()
    S2C_AptSteFlrNumber = State()
    S2C_State = State()
    S2C_ZipCode = State()

    S3_SignatureApplicant = State()
    # Date of signature filled automatically