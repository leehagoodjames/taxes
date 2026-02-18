# Local Imports
from ...base.ProgressiveTax import ProgressiveTax
from ...base.ProgressiveTaxBracket import ProgressiveTaxBracket
from ...utils.Constants import *


# The Mental Health Services Act (MHSA) was passed by the California Legislature in 2013. It is not included in the tax brackets below.
# It adds an additional 1% mental health services tax for taxable income over $1 million.
# # https://www.dhcs.ca.gov/services/MH/Pages/MH_Prop63.aspx#:~:text=The%20MHSA%20was%20passed%20by,the%20public%20behavioral%20health%20system.


brackets = {
    2026: {
        # Source: Projected based on 3% inflation adjustment from 2025 brackets
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [22078, 52345, 82578, 114576, 144913, 739669, 887450, 1479019]
        )),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [11039, 26172, 41289, 57288, 72456, 369834, 443725, 739509]
        )),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [11039, 26172, 41289, 57288, 72456, 369834, 443725, 739509]
        ))
    },
    2025: {
        # Source: Projected based on 3% inflation adjustment from 2024 brackets
        MARRIED_FILING_JOINTLY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [21449, 50849, 80256, 111327, 140761, 718224, 863060, 1436438]
        )),
        MARRIED_FILING_SEPARATELY: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10724, 25424, 40128, 55663, 70381, 359412, 431530, 719219]
        )),
        SINGLE: ProgressiveTax(ProgressiveTaxBracket(
            tax_rates = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
            income_thresholds = [10724, 25424, 40128, 55663, 70381, 359412, 431530, 719219]
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



