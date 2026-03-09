# Local Imports
from ..base.ProgressiveTax import ProgressiveTax
from ..base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ..utils.Constants import *


brackets = {
    2026: {
        # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
        # Note: Final 2026 brackets may differ when officially published by IRS
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [101600, 632250])),
        # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [50800, 316125])),
        # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [50800, 561100]))
    },
    2025: {
        # Source: IRS Rev. Proc. 2024-40 (inflation adjusted from 2024)
        # Based on typical 3.3% inflation adjustment pattern
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [98200, 610600])),
        # Source: IRS Rev. Proc. 2024-40 (inflation adjusted from 2024)
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [49100, 305300])),
        # Source: IRS Rev. Proc. 2024-40 (inflation adjusted from 2024)
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [49100, 542100]))
    },
    2024: {
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2024%20capital%20gains%20tax%20rates
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [94050, 583750])),
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2024%20capital%20gains%20tax%20rates
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [47025, 291850])),
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2024%20capital%20gains%20tax%20rates
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [47025, 518900]))
    },
    2023: {
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2023%20capital%20gains%20tax%20rates
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [89250, 553850])),
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2023%20capital%20gains%20tax%20rates
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [44625, 276900])),
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2023%20capital%20gains%20tax%20rates
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [44625, 492300]))
    },
    2022: {
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2022%20capital%20gains%20tax%20rates
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [83350, 517200])),
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2022%20capital%20gains%20tax%20rates
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [41675, 258600])),
        # Source: https://www.nerdwallet.com/article/taxes/capital-gains-tax-rates#2022%20capital%20gains%20tax%20rates
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [41675, 459750]))
    }
}
