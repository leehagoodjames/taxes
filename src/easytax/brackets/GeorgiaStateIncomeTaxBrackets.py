# Local Imports
from ..base import ProgressiveTax
from ..base import ProgressiveTaxBracket


# 2023 Married Filing Jointly
# Source: https://dor.georgia.gov/tax-tables-georgia-tax-rate-schedule
married_filing_jointly_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
        income_thresholds = [1000, 3000, 5000, 7000, 10000])
    )

# 2023 Married Filing Separately
# Source: https://dor.georgia.gov/tax-tables-georgia-tax-rate-schedule
married_filing_separately_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
        income_thresholds = [500, 1500, 2500, 3500, 5000])
    )

# 2022 Married Filing Jointly
# Source: https://www.incometaxpro.net/tax-rates/georgia.htm
married_filing_jointly_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
        income_thresholds = [1000, 3000, 5000, 7000, 10000])
    )

# 2022 Married Filing Separately
# Source: https://www.incometaxpro.net/tax-rates/georgia.htm
married_filing_separately_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
        income_thresholds = [500, 1500, 2500, 3500, 5000])
    )
