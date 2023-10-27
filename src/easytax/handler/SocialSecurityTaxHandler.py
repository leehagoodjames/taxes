
# Local Imports
from easytax.brackets import SocialSecurityIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase


SUPPORTED_TAX_YEARS = {2022, 2023}

# Each handler can have its own AGI / MAGI
class SocialSecurityIndividualIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int, incomes: list[float]):
        """Create a SocialSecurityIndividualIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        """
        
        if tax_year not in SUPPORTED_TAX_YEARS:
            raise ValueError(f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {tax_year}")
        
        self.tax_year = tax_year
        self.incomes = incomes
        self.tax_name = "Social Security"

        if self.tax_year == 2023: 
            self.income_tax_brackets = SocialSecurityIncomeTaxBrackets.individual_2023_tax  
        elif self.tax_year == 2022:
            self.income_tax_brackets = SocialSecurityIncomeTaxBrackets.individual_2022_tax
        else:
            raise ValueError(f"Unsupported combination of status: {self.filling_status}, year {self.tax_year}")
        
        return
    