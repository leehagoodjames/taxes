# Local Imports
from ..base.ProgressiveTax import ProgressiveTax
from ..base.ProgressiveTaxBracket import ProgressiveTaxBracket

# Note: Medicare and the additional medicare tax are modeled as a progressive tax. This should be mathamaticallly equivalent

# 2024 Medicare Employee Rate
# Source: https://www.irs.gov/pub/irs-pdf/p926.pdf
# https://www.irs.gov/taxtopics/tc751

brackets = {
    2025: ProgressiveTax(
        ProgressiveTaxBracket(
        tax_rates = [0.0145, 0.0235],
            income_thresholds = [200000])
        ),
    2024: ProgressiveTax(
        ProgressiveTaxBracket(
        tax_rates = [0.0145, 0.0235],
            income_thresholds = [200000])
        ),
    2023: ProgressiveTax(
        ProgressiveTaxBracket(
            tax_rates = [0.0145, 0.0235],
            income_thresholds = [200000])
        ),
    2022: ProgressiveTax(
        ProgressiveTaxBracket(
            tax_rates = [0.0145, 0.0235],
            income_thresholds = [200000])
        )
}
