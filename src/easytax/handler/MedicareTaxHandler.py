
# Local Imports
from ..brackets import MedicareIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.PayrollTaxIncomeHandler import PayrollTaxIncomeHandler


# Each handler can have its own AGI / MAGI
class MedicareIndividualIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int,  federal_income_handlers: list[PayrollTaxIncomeHandler]):
        """Create a MedicareIndividualIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        federal_income_handlers: list[PayrollTaxIncomeHandler] - List of PayrollTaxIncomeHandler objects
        """
        
        InputValidator.validate_tax_year(tax_year)
        
        self.tax_year = tax_year
        # Medicare taxes are only on salaries and wages.
        self.taxable_incomes = [f.salaries_and_wages for f in federal_income_handlers]
        self.tax_name = "Medicare"
        self.income_tax_brackets = self._get_tax_brackets(tax_year)
        
        return
    
    @staticmethod
    def _get_tax_brackets(tax_year: int):
        if tax_year not in MedicareIncomeTaxBrackets.brackets:
            raise ValueError(f"Unsupported tax year: {tax_year}")
        
        return MedicareIncomeTaxBrackets.brackets[tax_year]
    