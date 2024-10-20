# Local Imports
from ..base import RegressiveTax
from ..base import RegressiveTaxBracket


brackets = {
    # Source: https://www.ssa.gov/news/press/factsheets/colafacts2024.pdf
    2024: RegressiveTax.RegressiveTax(
    RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = [0.062, 0.0],
        income_thresholds = [168600])
    ),
    # Source: https://www.ssa.gov/oact/cola/cbb.html#:~:text=The%20OASDI%20tax%20rate%20for,for%20employees%20and%20employers%2C%20each.
    2023: RegressiveTax.RegressiveTax(
    RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = [0.062, 0.0],
        income_thresholds = [160200])
    ),
    # Source: https://www.ssa.gov/oact/cola/cbb.html#:~:text=The%20OASDI%20tax%20rate%20for,for%20employees%20and%20employers%2C%20each.
    2022: RegressiveTax.RegressiveTax(
    RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = [0.062, 0.0],
        income_thresholds = [147000])
    )
}
