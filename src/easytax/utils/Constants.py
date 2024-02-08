SUPPORTED_TAX_YEARS = {2022, 2023}
SUPPORTED_FILING_STATUSES = {"Married_Filing_Jointly", "Married_Filing_Separately"}
SUPPORTED_STATES = {
    "Alaska",
    "Florida",
    "Georgia",
    "New Hampshire",
    "Nevada",
    "South Dakota",
    "Tennessee",
    "Texas",
    # "Washington", Excluding Washington because they have a 7% capital gains tax
    "Wyoming",
    }

# Set of states with 0 income tax and 0 capital gains tax for SUPPORTED_TAX_YEARS &  SUPPORTED_FILING_STATUSES
STATES_WITHOUT_INCOME_TAX = {
    "Alaska",
    "Florida",
    "New Hampshire",
    "Nevada",
    "South Dakota",
    "Tennessee",
    "Texas",
    # "Washington", Excluding Washington because they have a 7% capital gains tax
    "Wyoming",
}
