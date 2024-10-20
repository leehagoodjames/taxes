
# Local Imports
from ..brackets import SocialSecurityIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.PayrollTaxIncomeHandler import PayrollTaxIncomeHandler


# Each handler can have its own AGI / MAGI
class SocialSecurityIndividualIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int,  federal_income_handlers: list[PayrollTaxIncomeHandler]):
        """Create a SocialSecurityIndividualIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        federal_income_handlers: list[PayrollTaxIncomeHandler] - List of PayrollTaxIncomeHandler objects
        """

        InputValidator.validate_tax_year(tax_year)
        
        self.tax_year = tax_year
        # Social Security taxes are only on salaries and wages.
        self.taxable_incomes = [f.salaries_and_wages for f in federal_income_handlers]
        self.tax_name = "Social Security"
        self.income_tax_brackets = self._get_tax_brackets(tax_year, SocialSecurityIncomeTaxBrackets.brackets)
        
        return
    