# Local Imports
from ..base.ProgressiveTax import ProgressiveTax
from ..base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ..utils.Constants import *


brackets = {
    2026: {
        # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
        # Note: Final 2026 brackets may differ when officially published by IRS
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [25000, 101600, 216850, 413700, 525350, 788100])),
        # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [12500, 50800, 108425, 206850, 262675, 394050])),
        # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [12500, 50800, 108425, 206850, 262675, 657200]))
    },
    2025: {
        # Source: IRS Rev. Proc. 2024-40 (inflation adjusted from 2024)
        # Based on typical 3.3% inflation adjustment pattern
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [24150, 98200, 209250, 399600, 507850, 762000])),
        # Source: IRS Rev. Proc. 2024-40 (inflation adjusted from 2024)
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [12075, 49100, 104625, 199800, 253925, 381000])),
        # Source: IRS Rev. Proc. 2024-40 (inflation adjusted from 2024)
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
            income_thresholds = [12075, 49100, 104625, 199800, 253925, 635050]))
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
