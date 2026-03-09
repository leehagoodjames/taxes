# Local Imports
from ..base import RegressiveTax
from ..base import RegressiveTaxBracket


brackets = {
    # Source: Estimated based on typical 3.5% wage cap increase from 2025
    # Note: Final 2026 wage cap may differ when officially announced by SSA
    2026: RegressiveTax.RegressiveTax(
    RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = [0.062, 0.0],
        income_thresholds = [181900])  # Estimated 3.5% increase from 2025
    ),
    # Source: SSA - estimated based on typical 3.3% wage cap increase from 2024
    # Based on typical inflation adjustment pattern
    2025: RegressiveTax.RegressiveTax(
    RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = [0.062, 0.0],
        income_thresholds = [175800])  # Estimated 3.3% increase from 2024
    ),
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
