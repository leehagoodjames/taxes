# Local Imports
from ..base.FlatTax import FlatTax
from ..base.FlatTaxBracket import FlatTaxBracket
from ..utils.Constants import *


# https://www.irs.gov/individuals/net-investment-income-tax#:~:text=In%20general%2C%20net%20investment%20income,and%20most%20self%2Demployment%20income.
# Update as needed when the tax brackets are updated
brackets = {year: {
    status: FlatTax(FlatTaxBracket(0.038))
    for status in [MARRIED_FILING_JOINTLY, MARRIED_FILING_SEPARATELY, SINGLE]
} for year in [2026, 2025, 2024, 2023, 2022]}

# https://www.irs.gov/individuals/net-investment-income-tax#:~:text=In%20general%2C%20net%20investment%20income,and%20most%20self%2Demployment%20income.
# NIIT thresholds have remained the same for years 2022-2026
threshold_amounts = {year: {
    MARRIED_FILING_JOINTLY: 250000,
    MARRIED_FILING_SEPARATELY: 125000,
    SINGLE: 200000,
    HEAD_OF_HOUSEHOLD: 200000,
} for year in [2026, 2025, 2024, 2023, 2022]}


