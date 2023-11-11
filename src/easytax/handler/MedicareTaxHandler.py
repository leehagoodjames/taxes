
# Local Imports
from ..brackets import MedicareIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase
from ..utils.InputValidator import InputValidator


# Each handler can have its own AGI / MAGI
class MedicareIndividualIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int, incomes: list[float]):
        """Create a MedicareIndividualIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        """
        
        InputValidator.validate_tax_year(tax_year)
        
        self.tax_year = tax_year
        self.incomes = incomes
        self.tax_name = "Medicare"

        if self.tax_year == 2023: 
            self.income_tax_brackets = MedicareIncomeTaxBrackets.individual_2023_tax  
        elif self.tax_year == 2022:
            self.income_tax_brackets = MedicareIncomeTaxBrackets.individual_2022_tax
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        
        return
    