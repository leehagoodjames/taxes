# Local Imports
from ..base import ProgressiveTax
from ..base import ProgressiveTaxBracket


# 2023 Married Filing Jointly
# Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2023%20capital%20gains%20tax%20rates
married_filing_jointly_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0, 0.15, 0.2],
        income_thresholds = [89250, 553850])
    )

# 2023 Married Filing Seperatlely
# Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2023%20capital%20gains%20tax%20rates
married_filing_separately_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0, 0.15, 0.2],
        income_thresholds = [44625, 276900])
    )

# 2022 Married Filing Jointly
# Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2022%20capital%20gains%20tax%20rates
married_filing_jointly_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0, 0.15, 0.2],
        income_thresholds = [83350, 517200])
    )

# 2022 Married Filing Seperatlely
# Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2022%20capital%20gains%20tax%20rates
married_filing_separately_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0, 0.15, 0.2],
        income_thresholds = [41675, 258600])
    )