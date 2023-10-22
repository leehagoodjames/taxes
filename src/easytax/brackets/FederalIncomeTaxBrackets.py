# Local Imports
from easytax import ProgressiveTax
from easytax import ProgressiveTaxBracket


# 2022 Married Filing Jointly
# Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
married_filing_jointly_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [20550, 83550, 178150, 340100, 431900, 647850])
    )

# 2022 Married Filing Seperatlely
# Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
married_filing_seperately_2022_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [10275, 41775, 89075, 170050, 215950, 323925])
    )

# 2023 Married Filing Jointly
# Source: https://www.forbes.com/advisor/taxes/taxes-federal-income-tax-bracket/#:~:text=2023%20Tax%20Brackets%20(Taxes%20Due,the%20bracket%20you're%20in.
married_filing_jointly_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [22000, 89450, 190750, 364200, 462500, 693750])
    )

# 2023 Married Filing Seperatlely
# Source: https://www.forbes.com/advisor/taxes/taxes-federal-income-tax-bracket/#:~:text=2023%20Tax%20Brackets%20(Taxes%20Due,the%20bracket%20you're%20in.
married_filing_seperately_2023_tax = ProgressiveTax.ProgressiveTax(
    ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
        income_thresholds = [11000, 44725, 95375, 182100, 231250, 346875])
    )
