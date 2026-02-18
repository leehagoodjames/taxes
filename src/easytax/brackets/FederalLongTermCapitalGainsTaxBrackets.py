# Local Imports
from ..base.ProgressiveTax import ProgressiveTax
from ..base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ..utils.Constants import *


brackets = {
    2026: {
        # Source: Projected based on 3% inflation adjustment from 2025 brackets
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [99473, 617459])),
        # Source: Projected based on 3% inflation adjustment from 2025 brackets
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [49736, 308729])),
        # Source: Projected based on 3% inflation adjustment from 2025 brackets
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [49736, 549237]))
    },
    2025: {
        # Source: https://www.irs.gov/newsroom/irs-announces-2025-tax-year-inflation-adjustments
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [96700, 600050])),
        # Source: https://www.irs.gov/newsroom/irs-announces-2025-tax-year-inflation-adjustments
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [48350, 300025])),
        # Source: https://www.irs.gov/newsroom/irs-announces-2025-tax-year-inflation-adjustments
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0, 0.15, 0.2],
            income_thresholds = [48350, 533400]))
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
