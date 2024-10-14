# All 50 states
ALABAMA = "Alabama"
ALASKA = "Alaska"
ARIZONA = "Arizona"
ARKANSAS = "Arkansas"
CALIFORNIA = "California"
COLORADO = "Colorado"
CONNECTICUT = "Connecticut"
DELAWARE = "Delaware"
FLORIDA = "Florida"
GEORGIA = "Georgia"
HAWAII = "Hawaii"
IDAHO = "Idaho"
ILLINOIS = "Illinois"
INDIANA = "Indiana"
IOWA = "Iowa"
KANSAS = "Kansas"
KENTUCKY = "Kentucky"
LOUISIANA = "Louisiana"
MAINE = "Maine"
MARYLAND = "Maryland"
MASSACHUSETTS = "Massachusetts"
MICHIGAN = "Michigan"
MINNESOTA = "Minnesota"
MISSISSIPPI = "Mississippi"
MISSOURI = "Missouri"
MONTANA = "Montana"
NEBRASKA = "Nebraska"
NEVADA = "Nevada"
NEW_HAMPSHIRE = "New Hampshire"
NEW_JERSEY = "New Jersey"
NEW_MEXICO = "New Mexico"
NEW_YORK = "New York"
NORTH_CAROLINA = "North Carolina"
NORTH_DAKOTA = "North Dakota"
OHIO = "Ohio"
OKLAHOMA = "Oklahoma"
OREGON = "Oregon"
PENNSYLVANIA = "Pennsylvania"
RHODE_ISLAND = "Rhode Island"
SOUTH_CAROLINA = "South Carolina"
SOUTH_DAKOTA = "South Dakota"
TENNESSEE = "Tennessee"
TEXAS = "Texas"
UTAH = "Utah"
VERMONT = "Vermont"
VIRGINIA = "Virginia"
WASHINGTON = "Washington"
WEST_VIRGINIA = "West Virginia"
WISCONSIN = "Wisconsin"
WYOMING = "Wyoming"

SUPPORTED_STATES = {
    ALASKA,
    FLORIDA,
    GEORGIA,
    NEVADA,
    NEW_HAMPSHIRE,
    SOUTH_DAKOTA,
    TENNESSEE,
    TEXAS,
    # WASHINGTON, Excluding Washington because they have a 7% capital gains tax
    WYOMING,
}

# Set of states with 0 income tax and 0 capital gains tax for SUPPORTED_TAX_YEARS &  SUPPORTED_FILING_STATUSES
STATES_WITHOUT_INCOME_TAX = {
    ALASKA,
    FLORIDA,
    NEVADA,
    NEW_HAMPSHIRE,
    SOUTH_DAKOTA,
    TENNESSEE,
    TEXAS,
    # WASHINGTON, Excluding Washington because they have a 7% capital gains tax
    WYOMING,
}

# Tax Years
SUPPORTED_TAX_YEARS = {2022, 2023, 2024}

# Filing Statuses
MARRIED_FILING_JOINTLY = "Married_Filing_Jointly"
MARRIED_FILING_SEPARATELY = "Married_Filing_Separately"
SINGLE = "Single"
SUPPORTED_FILING_STATUSES = {MARRIED_FILING_JOINTLY, MARRIED_FILING_SEPARATELY, SINGLE}