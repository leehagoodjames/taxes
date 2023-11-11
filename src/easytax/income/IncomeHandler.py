from ..utils.Constants import *

class IncomeCalculator:
    def __init__(self, filing_status: str, dependents: int, 
                 salaries_and_wages: float = 0, 
                 interest_income: float = 0, 
                 tax_exempt_interest: float = 0, 
                 dividend_income: float = 0, 
                 qualified_dividend_income: float = 0, 
                 taxable_state_local_refunds: float = 0, 
                 alimony_received: float = 0, 
                 business_income_loss: float = 0, 
                 capital_gain_loss: float = 0, 
                 other_gains_losses: float = 0, 
                 taxable_ira_distributions: float = 0, 
                 taxable_pensions: float = 0, 
                 rent_royalty_income: float = 0, 
                 partnership_scorp_income: float = 0, 
                 estate_trust_income: float = 0, 
                 farm_income_loss: float = 0, 
                 unemployment_compensation: float = 0, 
                 taxable_social_security: float = 0, 
                 other_income: float = 0):
        

        self.filing_status = filing_status
        self.dependents = dependents
        self.salaries_and_wages = salaries_and_wages
        self.interest_income = interest_income
        self.tax_exempt_interest = tax_exempt_interest
        self.dividend_income = dividend_income
        self.qualified_dividend_income = qualified_dividend_income
        self.taxable_state_local_refunds = taxable_state_local_refunds
        self.alimony_received = alimony_received
        self.business_income_loss = business_income_loss
        self.capital_gain_loss = capital_gain_loss
        self.other_gains_losses = other_gains_losses
        self.taxable_ira_distributions = taxable_ira_distributions
        self.taxable_pensions = taxable_pensions
        self.rent_royalty_income = rent_royalty_income
        self.partnership_scorp_income = partnership_scorp_income
        self.estate_trust_income = estate_trust_income
        self.farm_income_loss = farm_income_loss
        self.unemployment_compensation = unemployment_compensation
        self.taxable_social_security = taxable_social_security
        self.other_income = other_income
        self.incomes = [
            self.salaries_and_wages, 
            self.interest_income, 
            self.tax_exempt_interest, 
            self.dividend_income, 
            self.qualified_dividend_income, 
            self.taxable_state_local_refunds, 
            self.alimony_received, 
            self.business_income_loss, 
            self.capital_gain_loss, 
            self.other_gains_losses, 
            self.taxable_ira_distributions, 
            self.taxable_pensions, 
            self.rent_royalty_income, 
            self.partnership_scorp_income, 
            self.estate_trust_income, 
            self.farm_income_loss, 
            self.unemployment_compensation, 
            self.taxable_social_security, 
            self.other_income
        ]
        for i in self.incomes:
            if type(i) is not int or type(i) is not float:
                raise TypeError(f"Unsupported income type {type(i)} for income {i}")
        if filing_status not in SUPPORTED_FILING_STATUSES:
            raise ValueError(f"filing_status must be in SUPPORTED_FILING_STATUSES: {SUPPORTED_FILING_STATUSES}, got: {filing_status}")
        

        # TODO:
        self.total_income = sum(self.incomes)

    def compute_total_income(self):
        return sum([
            self.salaries_and_wages, 
            self.interest_income, 
            self.tax_exempt_interest, 
            self.dividend_income, 
            self.qualified_dividend_income, 
            self.taxable_state_local_refunds, 
            self.alimony_received, 
            self.business_income_loss, 
            self.capital_gain_loss, 
            self.other_gains_losses, 
            self.taxable_ira_distributions, 
            self.taxable_pensions, 
            self.rent_royalty_income, 
            self.partnership_scorp_income, 
            self.estate_trust_income, 
            self.farm_income_loss, 
            self.unemployment_compensation, 
            self.taxable_social_security, 
            self.other_income
        ])

# Example usage
tax_calculator = IncomeCalculator(filing_status="single", dependents=0)
total_income = tax_calculator.compute_total_income()
print(f"Total Income: {total_income}")
