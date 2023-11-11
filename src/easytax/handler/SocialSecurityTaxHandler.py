
# Local Imports
from ..brackets import SocialSecurityIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase
from ..utils.InputValidator import InputValidator


# Each handler can have its own AGI / MAGI
class SocialSecurityIndividualIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int, incomes: list[float]):
        """Create a SocialSecurityIndividualIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        """

        InputValidator.validate_tax_year(tax_year)
        
        self.tax_year = tax_year
        self.incomes = incomes
        self.tax_name = "Social Security"

        if self.tax_year == 2023: 
            self.income_tax_brackets = SocialSecurityIncomeTaxBrackets.individual_2023_tax  
        elif self.tax_year == 2022:
            self.income_tax_brackets = SocialSecurityIncomeTaxBrackets.individual_2022_tax
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        
        return
    