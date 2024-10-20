
# Local Imports
from ..brackets import FederalIncomeTaxBrackets
from ..brackets import FederalLongTermCapitalGainsTaxBrackets
from . import RegionalTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler
from ..utils.Constants import *


# Each handler can have its own AGI / MAGI
class FederalTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, federal_income_handlers: list[FederalIncomeHandler]):
        """Create a FederalTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filing Jointly, Single, etc)
        federal_income_handlers: list[FederalIncomeHandler] - List of FederalIncomeHandler objects
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)

        self.tax_year = tax_year
        self.filing_status = filing_status
        self.total_incomes = [f.total_income for f in federal_income_handlers]
        self.taxable_incomes = [f.taxable_income for f in federal_income_handlers]
        self.long_term_capital_gains = [f.long_term_capital_gains for f in federal_income_handlers]
        self.region = "Federal"

        self.income_tax_brackets = self._get_tax_brackets(tax_year, filing_status, FederalIncomeTaxBrackets.brackets)
        self.long_term_capital_gains_tax_brackets = self._get_tax_brackets(tax_year, filing_status, FederalLongTermCapitalGainsTaxBrackets.brackets)
        
        return