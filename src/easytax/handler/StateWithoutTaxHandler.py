# Local Imports
from . import RegionalTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler
from ..base import FlatTax
from ..base import FlatTaxBracket


# Each handler can have its own AGI / MAGI
class StateWithoutTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, federal_income_handlers: list[FederalIncomeHandler], state: str):
        """Create a StatesWithoutTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filing Jointly, Single, etc)
        federal_income_handlers: list[FederalIncomeHandler] - List of FederalIncomeHandler objects
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        InputValidator.validate_region_does_not_have_any_tax(state)

        self.tax_year = tax_year
        self.filing_status = filing_status
        self.region = state
        self.taxable_incomes = [0 for _ in federal_income_handlers]
        self.long_term_capital_gains = [0 for _ in federal_income_handlers]
        self.income_tax_brackets =  FlatTax.FlatTax(FlatTaxBracket.FlatTaxBracket(0.0)) # Zero Income Tax
        self.long_term_capital_gains_tax_brackets = FlatTax.FlatTax(FlatTaxBracket.FlatTaxBracket(0.0)) # Zero Capital Gains Tax
        return
    