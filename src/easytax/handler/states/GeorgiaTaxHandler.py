
# Local Imports
from ...brackets.states import GeorgiaStateIncomeTaxBrackets
from ...brackets.states import GeorgiaStateLongTermCapitalGainsTaxBrackets
from .. import RegionalTaxHandlerBase
from ...utils.InputValidator import InputValidator
from ...income.FederalIncomeHandler import FederalIncomeHandler
from ...utils.Constants import *


# Each handler can have its own AGI / MAGI
class GeorgiaTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, federal_income_handlers: list[FederalIncomeHandler], state_data: dict | None):
        """Create a GeorgiaTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filing Jointly, Single, etc)
        federal_income_handlers: list[FederalIncomeHandler] - List of FederalIncomeHandler objects
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
        state_data: dict - Inputs relevant to Georiga
            state_data.exemptions: int - defined by the state of Georgia on line 6c.
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        
        self.tax_year = tax_year
        self.filing_status = filing_status
        self.region = GEORGIA

        # The state of Georgia treats long term capital gains as taxable income
        self.taxable_income_before_dependents_and_exmptions = [f.taxable_income + f.long_term_capital_gains for f in federal_income_handlers]
        self.long_term_capital_gains = [0 for _ in federal_income_handlers]

        self.income_tax_brackets = self._get_tax_brackets(tax_year, filing_status, GeorgiaStateIncomeTaxBrackets.brackets)
        self.long_term_capital_gains_tax_brackets = self._get_tax_brackets(tax_year, filing_status, GeorgiaStateLongTermCapitalGainsTaxBrackets.brackets)

        # The Georiga personal exemption deduction of $3,700 per person was removed in 2024. 
        if self.tax_year < 2024:
            if state_data is None:
                self.deduction = 0
            elif state_data.get('exemptions') is None:
                self.deduction = 0
            elif type(state_data.get('exemptions')) is not int:
                raise TypeError(f"state_data specified invalid type for 'exemptions': {type(state_data.get('exemptions'))}")
            else:
                self.deduction = 3700 * state_data.get('exemptions', 0)
        else:
            self.deduction = 0

        deduction_per_income = self.deduction / len(self.taxable_income_before_dependents_and_exmptions)
        self.taxable_incomes = [i - deduction_per_income for i in self.taxable_income_before_dependents_and_exmptions]
        
        return
    