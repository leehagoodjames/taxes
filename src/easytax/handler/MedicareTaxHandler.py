
# Local Imports
from ..brackets import MedicareIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler


# Each handler can have its own AGI / MAGI
class MedicareIndividualIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int,  federalIncomeHandlers: list[FederalIncomeHandler]):
        """Create a MedicareIndividualIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        federalIncomeHandlers: list[FederalIncomeHandler] - List of FederalIncomeHandler objects
        """
        
        InputValidator.validate_tax_year(tax_year)
        
        self.tax_year = tax_year
        # Medicare taxes are only on salaries and wages.
        self.taxable_incomes = [f.salaries_and_wages for f in federalIncomeHandlers]
        self.tax_name = "Medicare"

        if self.tax_year == 2023: 
            self.income_tax_brackets = MedicareIncomeTaxBrackets.individual_2023_tax  
        elif self.tax_year == 2022:
            self.income_tax_brackets = MedicareIncomeTaxBrackets.individual_2022_tax
        else:
            raise ValueError(f"Unsupported year {self.tax_year}")
        
        return
    