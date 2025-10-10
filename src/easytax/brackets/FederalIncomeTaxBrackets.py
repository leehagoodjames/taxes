# Local Imports
from ..base.ProgressiveTax import ProgressiveTax
from ..base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ..utils.Constants import *


brackets = {
    2025: {
        # Source: IRS inflation adjustments for 2025 (estimated based on historical patterns)
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [23800, 96700, 206200, 394050, 500050, 750200])),
        # Source: IRS inflation adjustments for 2025 (estimated based on historical patterns)
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11900, 48350, 103100, 197025, 250025, 375100])),
        # Source: IRS inflation adjustments for 2025 (estimated based on historical patterns)
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11900, 48350, 103100, 197025, 250025, 625500]))
    },
    2024: {
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20jointly
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [23200, 94300, 201050, 383900, 487450, 731200])),
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20separately
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11600, 47150, 100525, 191950, 243725, 365600])),
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20single%20filers
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11600, 47150, 100525, 191950, 243725, 609350]))
    },
    2023: {
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20jointly
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [22000, 89450, 190750, 364200, 462500, 693750])),
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20separately
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11000, 44725, 95375, 182100, 231250, 346875])),
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20single%20filers
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11000, 44725, 95375, 182100, 231250, 578125]))
    },
    2022: {
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20jointly
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [20550, 83550, 178150, 340100, 431900, 647850])),
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20married,%20filing%20separately
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [10275, 41775, 89075, 170050, 215950, 323925])),
        # Source: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets#2023%20tax%20brackets:%20single%20filers
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [10275, 41775, 89075, 170050, 215950, 539900]))
    },
}
