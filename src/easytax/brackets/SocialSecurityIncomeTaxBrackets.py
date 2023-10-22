# Local Imports
from easytax.base import RegressiveTax
from easytax.base import RegressiveTaxBracket


# 2022 Social Security
# Source: https://www.ssa.gov/oact/cola/cbb.html#:~:text=The%20OASDI%20tax%20rate%20for,for%20employees%20and%20employers%2C%20each.
social_security_employee_2022_tax = RegressiveTax.RegressiveTax(
    RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = [0.062, 0.0],
        income_thresholds = [147000])
    )

# 2023 Social Security
# Source: https://www.ssa.gov/oact/cola/cbb.html#:~:text=The%20OASDI%20tax%20rate%20for,for%20employees%20and%20employers%2C%20each.
social_security_employee_2023_tax = RegressiveTax.RegressiveTax(
    RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = [0.062, 0.0],
        income_thresholds = [160200])
    )
