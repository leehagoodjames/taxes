# Local Imports
from ..base import ProgressiveTax
from ..base import ProgressiveTaxBracket


# 2023 Married Filing Jointly
# Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20jointly
married_filing_jointly_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [22000, 89450, 190750, 364200, 462500, 693750])
    )

# 2023 Married Filing Seperatlely
# Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20separately
married_filing_separately_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [11000, 44725, 95375, 182100, 231250, 346875])
    )


# 2022 Married Filing Jointly
# Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2022%20tax%20brackets
married_filing_jointly_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [20550, 83550, 178150, 340100, 431900, 647850])
    )

# 2022 Married Filing Seperatlely
# Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2022%20tax%20brackets
married_filing_separately_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [10275, 41775, 89075, 170050, 215950, 323925])
    )