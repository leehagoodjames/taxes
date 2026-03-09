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
# NIIT thresholds are typically adjusted for inflation annually
threshold_amounts = {
    # 2026 thresholds (estimated 3.5% inflation adjustment from 2025)
    2026: {
        MARRIED_FILING_JOINTLY: 267500,
        MARRIED_FILING_SEPARATELY: 133750,
        SINGLE: 214000,
        HEAD_OF_HOUSEHOLD: 214000,
    },
    # 2025 thresholds (estimated 3.3% inflation adjustment from 2024)
    2025: {
        MARRIED_FILING_JOINTLY: 258250,
        MARRIED_FILING_SEPARATELY: 129125,
        SINGLE: 206600,
        HEAD_OF_HOUSEHOLD: 206600,
    },
    # 2024 and earlier thresholds (existing)
    2024: {
        MARRIED_FILING_JOINTLY: 250000,
        MARRIED_FILING_SEPARATELY: 125000,
        SINGLE: 200000,
        HEAD_OF_HOUSEHOLD: 200000,
    },
    2023: {
        MARRIED_FILING_JOINTLY: 250000,
        MARRIED_FILING_SEPARATELY: 125000,
        SINGLE: 200000,
        HEAD_OF_HOUSEHOLD: 200000,
    },
    2022: {
        MARRIED_FILING_JOINTLY: 250000,
        MARRIED_FILING_SEPARATELY: 125000,
        SINGLE: 200000,
        HEAD_OF_HOUSEHOLD: 200000,
    }
}


