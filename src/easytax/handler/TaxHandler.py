
# Local Imports
from ..utils.Constants import *
from ..utils.Logger import logger
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler
from ..income.PayrollTaxIncomeHandler import PayrollTaxIncomeHandler
from .FederalTaxHandler import FederalTaxHandler
from .GeorgiaTaxHandler import GeorgiaTaxHandler
from .SocialSecurityTaxHandler import SocialSecurityIndividualIncomeTaxHandler
from .MedicareTaxHandler import MedicareIndividualIncomeTaxHandler
from .StateWithoutTaxHandler import StateWithoutTaxHandler


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

        self.tax_year = tax_year
        self.filing_status = filing_status
        self.state = state

        # Used for federal taxes and state 
        self.make_federal_income_handlers(incomes_adjustments_and_deductions)

        # Used for social security taxes and medicare taxes
        self.make_payroll_income_handlers(incomes_adjustments_and_deductions)

        if self.state == "Georgia":
            self.stateTaxHandler = GeorgiaTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federal_income_handlers=self.federal_income_handlers,
            state_data = state_data,
        )
        elif self.state in STATES_WITHOUT_INCOME_TAX:
            self.stateTaxHandler = StateWithoutTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federal_income_handlers=self.federal_income_handlers,
            state = self.state,
        )
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}, and state {self.state}")
        
        self.federalHander = FederalTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federal_income_handlers=self.federal_income_handlers,
        )
        self.socialSecurityTaxHandler = SocialSecurityIndividualIncomeTaxHandler(
            tax_year=tax_year, 
            federal_income_handlers=self.payroll_income_handlers,
        )
        self.medicareTaxHandler = MedicareIndividualIncomeTaxHandler(
            tax_year=tax_year, 
            federal_income_handlers=self.payroll_income_handlers,
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
                # 'niit': niit_summary,
                'total_tax_owed': total_tax_owed
            }
        except AttributeError as e:
            raise AttributeError(f"{e} Ensure you call 'calculate_taxes' on relevant Handlers")
        
    
    # Makes federal income handlers. Handles the case when two incomes are provided for MARRIED_FILING_JOINTLY and combines them
    def make_federal_income_handlers(self, incomes_adjustments_and_deductions: list[dict]): 
        if self.filing_status == MARRIED_FILING_JOINTLY and len(incomes_adjustments_and_deductions) == 2:
            # There are two earners and they need their incomes combined into a single entity
            combined = {}
            for k,v in incomes_adjustments_and_deductions[0].items():
                # Check the fields that should not be summed and should be equivalent
                if k == 'dependents':
                    if v != incomes_adjustments_and_deductions[1][k]:
                        raise ValueError(f"Cannot have differing number of dependents when filing status is {MARRIED_FILING_JOINTLY}. Recieved {v} and {incomes_adjustments_and_deductions[1][k]}.")
                    combined[k] = v
                elif k == 'use_standard_deduction':
                    if v != incomes_adjustments_and_deductions[1][k]:
                        raise ValueError(f"Cannot have itemized and non-itemized deductions when {MARRIED_FILING_JOINTLY}. For 'use_standard_deduction', recieved {v} and {incomes_adjustments_and_deductions[1][k]}.")
                    combined[k] = v
                else:
                    # Sum the fields if they are a field that should be summed
                    combined[k] = v + incomes_adjustments_and_deductions[1][k]
            self.federal_income_handlers = [FederalIncomeHandler.from_dict(combined | {'tax_year': self.tax_year, 'filing_status': self.filing_status})]

        else: 
            self.federal_income_handlers = [FederalIncomeHandler.from_dict(i | {'tax_year': self.tax_year, 'filing_status': self.filing_status}) for i in incomes_adjustments_and_deductions]

   # Makes payroll income handlers. 
    def make_payroll_income_handlers(self, incomes_adjustments_and_deductions: list[dict]): 
        self.payroll_income_handlers = [PayrollTaxIncomeHandler.from_dict({'salaries_and_wages': i['salaries_and_wages']}) for i in incomes_adjustments_and_deductions]
