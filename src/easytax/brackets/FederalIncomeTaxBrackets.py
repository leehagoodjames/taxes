# Local Imports
from ..base.ProgressiveTax import ProgressiveTax
from ..base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ..utils.Constants import *


brackets = {
    2026: {
        # Source: Projected based on 3% inflation adjustment from 2025 brackets
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [24597, 99773, 212551, 405983, 515674, 773636])),
        # Source: Projected based on 3% inflation adjustment from 2025 brackets
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [12299, 49887, 106275, 202991, 257837, 386818])),
        # Source: Projected based on 3% inflation adjustment from 2025 brackets
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [12299, 49887, 106275, 202991, 257837, 644629]))
    },
    2025: {
        # Source: https://www.irs.gov/newsroom/irs-announces-2025-tax-year-inflation-adjustments
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [23900, 96950, 206550, 394600, 501050, 751600])),
        # Source: https://www.irs.gov/newsroom/irs-announces-2025-tax-year-inflation-adjustments
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11950, 48475, 103275, 197300, 250525, 375800])),
        # Source: https://www.irs.gov/newsroom/irs-announces-2025-tax-year-inflation-adjustments
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [11950, 48475, 103275, 197300, 250525, 626350]))
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
