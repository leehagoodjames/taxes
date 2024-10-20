# Local Imports
from ...base.ProgressiveTax import ProgressiveTax
from ...base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ...base.FlatTax import FlatTax
from ...base.FlatTaxBracket import FlatTaxBracket
from ...utils.Constants import *


brackets = {
    2024: {
        # Source: https://gov.georgia.gov/press-releases/2024-04-18/gov-kemp-signs-historic-tax-cut-package-law
        MARRIED_FILING_JOINTLY: FlatTax(FlatTaxBracket(tax_rate = 0.0539)),
        MARRIED_FILING_SEPARATELY: FlatTax(FlatTaxBracket(tax_rate = 0.0539)),
        SINGLE: FlatTax(FlatTaxBracket(tax_rate = 0.0539))
    },
    # Note - in 2024 Georiga transitioned to a flat tax rate
    2023: {
        # https://dor.georgia.gov/tax-tables-georgia-tax-rate-schedule
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
            income_thresholds = [1000, 3000, 5000, 7000, 10000])),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
            income_thresholds = [500, 1500, 2500, 3500, 5000])),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
            income_thresholds = [750, 2250, 3750, 5250, 7000]))
    },
    2022: {
        # https://www.incometaxpro.net/tax-rates/georgia.htm
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
            income_thresholds = [1000, 3000, 5000, 7000, 10000])),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
            income_thresholds = [500, 1500, 2500, 3500, 5000])),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
            income_thresholds = [750, 2250, 3750, 5250, 7000]))
    }
}
