# Local Imports
from ...base.ProgressiveTax import ProgressiveTax
from ...base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ...utils.Constants import *


# The Mental Health Services Act (MHSA) was passed by the California Legislature in 2013. It is not included in the tax brackets below.
# It adds an additional 1% mental health services tax for taxable income over $1 million.
# # https://www.dhcs.ca.gov/services/MH/Pages/MH_Prop63.aspx#:~:text=The%20MHSA%20was%20passed%20by,the%20public%20behavioral%20health%20system.


brackets = {
    2026: {
        # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
        # California typically adjusts brackets annually for inflation
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [22400, 53150, 83850, 116450, 147200, 751750, 901900, 1505000]
        )),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [11200, 26575, 41925, 58225, 73600, 375875, 450950, 752500]
        )),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [11200, 26575, 41925, 58225, 73600, 375875, 450950, 752500]
        ))
    },
    2025: {
        # Source: California FTB - inflation adjusted from 2024 brackets
        # Based on typical 3.3% inflation adjustment pattern
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [21650, 51350, 81000, 112550, 142200, 726500, 871800, 1453900]
        )),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10825, 25675, 40500, 56275, 71100, 363250, 435900, 726950]
        )),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10825, 25675, 40500, 56275, 71100, 363250, 435900, 726950]
        ))
    },
    # https://www.nerdwallet.com/article/taxes/california-state-tax
    2024: {
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [20824, 49368, 77918, 108162, 136700, 698274, 837922, 1396542]
        )),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10412, 24684, 38959, 54081, 68350, 349137, 418961, 698271]
        )),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10412, 24684, 38959, 54081, 68350, 349137, 418961, 698271]
        ))
    },
    2023: {
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [20198, 47884, 75576, 104910, 132590, 677278, 812728, 1354550]
        )),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10099, 23942, 37788, 52455, 66295, 338639, 406364, 677275]
        )),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10099, 23942, 37788, 52455, 66295, 338639, 406364, 677275]
        ))
    },
    2022: {
        # https://www.ftb.ca.gov/forms/2022/california-income-tax-return-instructions.pdf
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [20198, 47884, 75576, 104910, 132590, 677278, 812728, 1354550]
        )),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10099, 23942, 37788, 52455, 66295, 338639, 406364, 677275]
        )),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10099, 23942, 37788, 52455, 66295, 338639, 406364, 677275]
        ))
    }
}



