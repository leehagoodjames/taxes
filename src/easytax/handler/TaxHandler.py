
# Local Imports
from .FederalTaxHandler import FederalTaxHandler
from .GeorgiaTaxHandler import GeorgiaTaxHandler
from .SocialSecurityTaxHandler import SocialSecurityIndividualIncomeTaxHandler
from .MedicareTaxHandler import MedicareIndividualIncomeTaxHandler
from easytax.utils.Logger import logger


SUPPORTED_TAX_YEARS = {2022, 2023}
SUPPORTED_FILLING_STATUSES = {"Married_Filling_Jointly", "Married_Filling_separately"}
SUPPORTED_STATES = {"Georgia"}

class TaxHandler:

    def __init__(self, tax_year: int, filling_status: str, state: str, incomes: list[float], long_term_capital_gains: list[float]):
        """Create a TaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filling_status: str - The type of filling (Married Filling Jointly, Single, etc)
        state: str - The state that you will be filing. TODO: Support more than 1 state
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
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
        self.long_term_capital_gains = long_term_capital_gains

        if self.state == "Georgia":
            self.stateTaxHandler = GeorgiaTaxHandler(
            tax_year=tax_year, 
            filling_status=filling_status, 
            incomes=incomes, 
            long_term_capital_gains=long_term_capital_gains,
        )
        else:
            raise ValueError(f"Unsupported combination of status: {self.filling_status}, year {self.tax_year}, and state {self.state}")
        
        self.federalHander = FederalTaxHandler(
            tax_year=tax_year, 
            filling_status=filling_status, 
            incomes=incomes, 
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

    def display_tax_summary(self):

        try:
            logger.info(f'Incomes: {", ".join([f"${i:,.0f}" for i in self.incomes])}') # 
            logger.info(f'Long term capital gains: {", ".join([f"${i:,.0f}" for i in self.long_term_capital_gains])}')
            
            logger.info(f'federal tax owed: {", ".join([f"${i:,.0f}" for i in self.federal_tax_owed])}')
            logger.info(f'federal LTCG tax owed: {", ".join([f"${i:,.0f}" for i in self.federal_long_term_capital_gains_tax_owed])}')
            
            logger.info(f'state tax owed: {", ".join([f"${i:,.0f}" for i in self.state_tax_owed])}')
            logger.info(f'state LTCG tax owed: {", ".join([f"${i:,.0f}" for i in self.state_long_term_capital_gains_tax_owed])}')
            
            logger.info(f'social security tax owed: {", ".join([f"${i:,.0f}" for i in self.social_security_tax_owed])}')
            logger.info(f'medicare tax owed: {", ".join([f"${i:,.0f}" for i in self.medicare_tax_owed])}')
        except AttributeError as e:
            raise AttributeError(f"{e}. Ensure you call 'calculate_taxes' before attempting to call this method.")
        return
            