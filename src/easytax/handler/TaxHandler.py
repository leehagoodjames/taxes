
# Local Imports
from .FederalTaxHandler import FederalTaxHandler
from .GeorgiaTaxHandler import GeorgiaTaxHandler
from .SocialSecurityTaxHandler import SocialSecurityIndividualIncomeTaxHandler
from .MedicareTaxHandler import MedicareIndividualIncomeTaxHandler
from ..utils.Logger import logger


SUPPORTED_TAX_YEARS = {2022, 2023}
SUPPORTED_FILLING_STATUSES = {"Married_Filling_Jointly", "Married_Filling_separately"}
SUPPORTED_STATES = {"Georgia"}

class TaxHandler:

    def __init__(self, tax_year: int, filling_status: str, state: str, incomes: list[float], retirement_incomes: list[float], long_term_capital_gains: list[float], state_data = None):
        """Create a TaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filling_status: str - The type of filling (Married Filling Jointly, Single, etc)
        state: str - The state that you will be filing. TODO: Support more than 1 state
        incomes: list[float] - List of the Adjust Gross Income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        retirement_incomes: list[float] - List of incomes from qualified retirement accounts, such as Traditional IRA and Tradional 401K distributions
        long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
        state_data: A dictionary of information relevant to the selected state 
        """
        
        if tax_year not in SUPPORTED_TAX_YEARS:
            raise ValueError(f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {tax_year}")
        if filling_status not in SUPPORTED_FILLING_STATUSES:
            raise ValueError(f"filling_status must be in SUPPORTED_FILLING_STATUSES: {SUPPORTED_FILLING_STATUSES}, got: {filling_status}")
        if state not in SUPPORTED_STATES:
            raise ValueError(f"state must be in SUPPORTED_STATES: {SUPPORTED_STATES}, got: {state}")
        
        self.tax_year = tax_year
        self.filling_status = filling_status
        self.state = state
        self.incomes = incomes
        self.retirement_incomes = retirement_incomes
        self.long_term_capital_gains = long_term_capital_gains

        if self.state == "Georgia":
            self.stateTaxHandler = GeorgiaTaxHandler(
            tax_year=tax_year, 
            filling_status=filling_status, 
            incomes=[i + r for i,r in zip(incomes, retirement_incomes)], # this is wrong, they aren't guranteed to be the same length 
            long_term_capital_gains=long_term_capital_gains,
            state_data = state_data,
        )
        else:
            raise ValueError(f"Unsupported combination of status: {self.filling_status}, year {self.tax_year}, and state {self.state}")
        
        self.federalHander = FederalTaxHandler(
            tax_year=tax_year, 
            filling_status=filling_status, 
            incomes=[i + r for i,r in zip(incomes, retirement_incomes)], # this is wrong, they aren't guranteed to be the same length 
            long_term_capital_gains=long_term_capital_gains,
        )
        self.socialSecurityTaxHandler = SocialSecurityIndividualIncomeTaxHandler(
            tax_year=tax_year, 
            incomes=incomes, 
        )
        self.medicareTaxHandler = MedicareIndividualIncomeTaxHandler(
            tax_year=tax_year, 
            incomes=incomes, 
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
            