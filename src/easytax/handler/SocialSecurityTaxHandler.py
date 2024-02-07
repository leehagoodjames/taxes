
# Local Imports
from ..brackets import SocialSecurityIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler


# Each handler can have its own AGI / MAGI
class SocialSecurityIndividualIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int,  federalIncomeHandlers: list[FederalIncomeHandler]):
        """Create a SocialSecurityIndividualIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        federalIncomeHandlers: list[FederalIncomeHandler] - List of FederalIncomeHandler objects
        """

        InputValidator.validate_tax_year(tax_year)
        
        self.tax_year = tax_year
        # Social Security taxes are only on salaries and wages.
        self.taxable_incomes = [f.salaries_and_wages for f in federalIncomeHandlers]
        self.tax_name = "Social Security"

        if self.tax_year == 2023: 
            self.income_tax_brackets = SocialSecurityIncomeTaxBrackets.individual_2023_tax  
        elif self.tax_year == 2022:
            self.income_tax_brackets = SocialSecurityIncomeTaxBrackets.individual_2022_tax
        else:
            raise ValueError(f"Unsupported year {self.tax_year}")
        
        return
    