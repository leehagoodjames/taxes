
# Local Imports
from .FederalTaxHandler import FederalTaxHandler
from .GeorgiaTaxHandler import GeorgiaTaxHandler
from .SocialSecurityTaxHandler import SocialSecurityIndividualIncomeTaxHandler
from .MedicareTaxHandler import MedicareIndividualIncomeTaxHandler
from ..utils.Logger import logger
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler

class TaxHandler:

    def __init__(self, tax_year: int, filing_status: str, state: str, incomes_adjustments_and_deductions: list[dict], state_data = None):
        """Create a TaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filing Jointly, Single, etc)
        state: str - The state that you will be filing. TODO: Support more than 1 state
        incomes_adjustments_and_deductions: list[dict] - List of dicts of income for each person in a household.
         If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        state_data: dict - information relevant to the selected state 
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        InputValidator.validate_state(state)

        self.federalIncomeHandlers = [FederalIncomeHandler.from_dict(i | {'tax_year': tax_year, 'filing_status': filing_status}) for i in incomes_adjustments_and_deductions]

        self.tax_year = tax_year
        self.filing_status = filing_status
        self.state = state

        if self.state == "Georgia":
            self.stateTaxHandler = GeorgiaTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federalIncomeHandlers=self.federalIncomeHandlers,
            state_data = state_data,
        )
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}, and state {self.state}")
        
        self.federalHander = FederalTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federalIncomeHandlers=self.federalIncomeHandlers,
        )
        self.socialSecurityTaxHandler = SocialSecurityIndividualIncomeTaxHandler(
            tax_year=tax_year, 
            federalIncomeHandlers=self.federalIncomeHandlers,
        )
        self.medicareTaxHandler = MedicareIndividualIncomeTaxHandler(
            tax_year=tax_year, 
            federalIncomeHandlers=self.federalIncomeHandlers,
        )
        self.calculate_taxes()
        self.compute_total_tax()

        return
    

    def calculate_taxes(self):

        self.federalHander.calculate_taxes()
        self.stateTaxHandler.calculate_taxes()
        self.socialSecurityTaxHandler.calculate_taxes()
        self.medicareTaxHandler.calculate_taxes()

        self.federal_tax_owed = self.federalHander.income_tax_owed
        self.federal_long_term_capital_gains_tax_owed = self.federalHander.long_term_capital_gains_tax_owed
        self.state_tax_owed = self.stateTaxHandler.income_tax_owed
        self.state_long_term_capital_gains_tax_owed = self.stateTaxHandler.long_term_capital_gains_tax_owed
        self.social_security_tax_owed = self.socialSecurityTaxHandler.income_tax_owed
        self.medicare_tax_owed = self.medicareTaxHandler.income_tax_owed
        return
    

    def compute_total_tax(self):
        self.total_tax = sum(self.federal_tax_owed + \
            self.federal_long_term_capital_gains_tax_owed + \
            self.state_tax_owed + \
            self.state_long_term_capital_gains_tax_owed + \
            self.social_security_tax_owed + \
            self.medicare_tax_owed)
        return
    

    def display_tax_summary(self):

        try:
            self.federalHander.display_tax_summary()
            self.socialSecurityTaxHandler.display_tax_summary()
            self.medicareTaxHandler.display_tax_summary()
            self.stateTaxHandler.display_tax_summary()
            logger.info(f'Total Tax Owed: ${self.total_tax:,.0f}')
        except AttributeError as e:
            raise AttributeError(f"{e} Ensure you call 'calculate_taxes' on relevant Handlers")
        return


    def summary_json(self):
        
        try:
            federal_summary = self.federalHander.summary_json()
            social_security_summary = self.socialSecurityTaxHandler.summary_json()
            medicare_summary = self.medicareTaxHandler.summary_json()
            state_summary = self.stateTaxHandler.summary_json()
            total_tax_owed = self.total_tax
            return {
                'federal': federal_summary,
                'social_security': social_security_summary,
                'medicare': medicare_summary,
                'state': state_summary,
                'total_tax_owed': total_tax_owed
            }
        except AttributeError as e:
            raise AttributeError(f"{e} Ensure you call 'calculate_taxes' on relevant Handlers")
