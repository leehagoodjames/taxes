
# Local Imports
from .FederalTaxHandler import FederalTaxHandler
from .GeorgiaTaxHandler import GeorgiaTaxHandler
from .SocialSecurityTaxHandler import SocialSecurityIndividualIncomeTaxHandler
from .MedicareTaxHandler import MedicareIndividualIncomeTaxHandler
from ..utils.Logger import logger
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler

class TaxHandler:

    def __init__(self, tax_year: int, filing_status: str, state: str, incomes: list[dict], state_data = None, deductions = None):
        """Create a TaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filling Jointly, Single, etc)
        state: str - The state that you will be filing. TODO: Support more than 1 state
        incomes: list[dict] - List of dicts of income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        state_data: dict - information relevant to the selected state 
        deductions: dict - information relevant to Deductions
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        InputValidator.validate_state(state)

        self.federalIncomeHandlers = [FederalIncomeHandler.from_dict(d | {'tax_year': tax_year, 'filing_status': filing_status}) for d in incomes]
        
        # if filing_status == "Married_Filling_Jointly":
        #     # Don't require all inputs to be the same length, fold them into one
        #     FederalIncomeHandler.from_dict(income_data)
        # elif filing_status == "Married_Filling_separately":
        #     if len() != 2:
        #         raise ValueError(f"")
        # # TODO: Other statuses

        self.tax_year = tax_year
        self.filing_status = filing_status
        self.state = state
        # self.incomes = incomes
        # self.retirement_incomes = retirement_incomes
        # self.long_term_capital_gains = long_term_capital_gains

        if self.state == "Georgia":
            self.stateTaxHandler = GeorgiaTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federalIncomeHandlers=self.federalIncomeHandlers,
            # incomes=incomes,
            # incomes=[i + r for i,r in zip(incomes, retirement_incomes)], # this is wrong, they aren't guranteed to be the same length 
            # long_term_capital_gains=long_term_capital_gains,
            state_data = state_data,
        )
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}, and state {self.state}")
        
        self.federalHander = FederalTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            # incomes=incomes,
            federalIncomeHandlers=self.federalIncomeHandlers,
            # incomes=[i + r for i,r in zip(incomes, retirement_incomes)], # this is wrong, they aren't guranteed to be the same length 
            # long_term_capital_gains=long_term_capital_gains,
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
            