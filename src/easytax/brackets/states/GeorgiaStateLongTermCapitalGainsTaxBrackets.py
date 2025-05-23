# Local Imports
from ...brackets.states import GeorgiaStateIncomeTaxBrackets
from ...utils.Constants import *


# Georgia Taxes Long Term Capital games as Income.
# Ref: https://www.fool.com/research/capital-gains-tax-rates/#:~:text=Georgia%20taxes%20capital%20gains%20as%20income%20and%20both%20are%20taxed%20at%20the%20same%20rates.

brackets = {
    2024: {
        MARRIED_FILING_JOINTLY: GeorgiaStateIncomeTaxBrackets.brackets[2024][MARRIED_FILING_JOINTLY],      
        MARRIED_FILING_SEPARATELY: GeorgiaStateIncomeTaxBrackets.brackets[2024][MARRIED_FILING_SEPARATELY],
        SINGLE: GeorgiaStateIncomeTaxBrackets.brackets[2024][SINGLE]
    },
    2023: { 
        MARRIED_FILING_JOINTLY: GeorgiaStateIncomeTaxBrackets.brackets[2023][MARRIED_FILING_JOINTLY],      
        MARRIED_FILING_SEPARATELY: GeorgiaStateIncomeTaxBrackets.brackets[2023][MARRIED_FILING_SEPARATELY],
        SINGLE: GeorgiaStateIncomeTaxBrackets.brackets[2023][SINGLE]
    },  
    2022: {
        MARRIED_FILING_JOINTLY: GeorgiaStateIncomeTaxBrackets.brackets[2022][MARRIED_FILING_JOINTLY],      
        MARRIED_FILING_SEPARATELY: GeorgiaStateIncomeTaxBrackets.brackets[2022][MARRIED_FILING_SEPARATELY],
        SINGLE: GeorgiaStateIncomeTaxBrackets.brackets[2022][SINGLE]
    }
}

        