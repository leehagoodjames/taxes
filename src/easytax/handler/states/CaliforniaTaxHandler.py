# Local Imports
from ...brackets.states import CaliforniaStateIncomeTaxBrackets
from ...brackets.states import CaliforniaStateLongTermCapitalGainsTaxBrackets
from .. import RegionalTaxHandlerBase
from ...utils.InputValidator import InputValidator
from ...income.FederalIncomeHandler import FederalIncomeHandler
from ...deductions.states import CaliforniaStandardDeductions
from ...credits.states import CaliforniaStateTaxCredits
from ...utils.Constants import *

class CaliforniaTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, federal_income_handlers: list[FederalIncomeHandler], state_data: dict | None = None):
        """Create a CaliforniaTaxHandler object."""
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        
        if state_data is None:
            raise ValueError(f"invalid value for 'state_data': {state_data}")
        # Add any California-specific validations here
        
        self.tax_year = tax_year
        self.filing_status = filing_status
        self.region = CALIFORNIA
        self.state_data = state_data

        # The state of California treats long term capital gains as taxable income
        self.taxable_income_before_dependents_and_exmptions = [f.taxable_income + f.long_term_capital_gains for f in federal_income_handlers]
        self.long_term_capital_gains = [0 for _ in federal_income_handlers]

        self.income_tax_brackets = self._get_tax_brackets(tax_year, filing_status, CaliforniaStateIncomeTaxBrackets.brackets)
        self.long_term_capital_gains_tax_brackets = self._get_tax_brackets(tax_year, filing_status, CaliforniaStateLongTermCapitalGainsTaxBrackets.brackets)

        # Handle California deductions
        self.standard_deduction = CaliforniaStandardDeductions.CaliforniaStandardDeductions.get_standard_deduction(tax_year, filing_status)
        self.taxable_incomes = [max(0, income - self.standard_deduction) for income in self.taxable_income_before_dependents_and_exmptions]
        
        # Initialize California tax credits
        self.tax_credits = CaliforniaStateTaxCredits.CaliforniaStateTaxCredits(tax_year, filing_status, state_data)
    

    def calculate_taxes(self):
        # Call the parent class's calculate_taxes method first
        super().calculate_taxes()
        
        # Apply California tax credits
        total_credits = self.tax_credits.calculate_total_credits(self.taxable_incomes)
        self.income_tax_owed = [max(0, tax - credits) for tax, credits in zip(self.income_tax_owed, total_credits)]
        
        # Apply Mental Health Services Act (MHSA) 1% tax on income over $1 million
        self._apply_mental_health_services_tax()
        
        return
    
    def _apply_mental_health_services_tax(self):
        """
        Apply California Mental Health Services Act (MHSA) tax.
        
        The MHSA adds an additional 1% tax on taxable income over $1 million.
        This tax was passed by the California Legislature in 2013.
        
        Reference: https://www.dhcs.ca.gov/services/MH/Pages/MH_Prop63.aspx
        """
        mhsa_threshold = 1000000  # $1 million
        mhsa_rate = 0.01  # 1%
        
        for i, taxable_income in enumerate(self.taxable_incomes):
            if taxable_income > mhsa_threshold:
                mhsa_tax = (taxable_income - mhsa_threshold) * mhsa_rate
                self.income_tax_owed[i] += mhsa_tax
