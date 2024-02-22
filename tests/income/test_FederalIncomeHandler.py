# Standard Library Imports
import unittest

# Local Imports
from src.easytax.utils.Constants import *
from src.easytax.income.FederalIncomeHandler import FederalIncomeHandler
from tests.utils.TestContants import *


# Creates a FederalIncomeHandler that defaults to supported values
def federal_income_handler_builder(
                filing_status: str = SUPPORTED_FILING_STATUS,
                tax_year: int = SUPPORTED_TAX_YEAR,
                dependents: int = 0,
                use_standard_deduction: bool = True,
                # Income
                salaries_and_wages: float = SUPPORTED_SALARY_AND_WAGES_1, 
                interest_income: float = 0, 
                tax_exempt_interest: float = 0, 
                dividend_income: float = 0, 
                qualified_dividend_income: float = 0, 
                taxable_state_local_refunds: float = 0, 
                alimony_received: float = 0, 
                business_income_or_loss: float = 0, 
                capital_gain_or_loss: float = 0, 
                other_gains_or_losses: float = 0, 
                taxable_ira_distributions: float = 0, 
                taxable_pensions: float = SUPPORTED_TAXABLE_PENSIONS_1, 
                rent_royalty_income: float = 0, 
                partnership_or_s_corp_income: float = 0, 
                estate_trust_income: float = 0, 
                farm_income_or_loss: float = 0, 
                unemployment_compensation: float = 0, 
                taxable_social_security: float = 0, 
                other_income: float = 0,
                # LTCG
                long_term_capital_gains: float = SUPPORTED_LONG_TERM_CAPITAL_GAINS_1,
                # Income Adjustments
                moving_expenses: float = 0,
                deductible_self_employment_tax: float = 0,
                sep_simple_qualified_plans_deductions: float = 0,
                self_employment_health_insurance: float = 0,
                penalty_early_withdrawal_savings: float = 0,
                alimony_paid: float = 0,
                ira_deductions: float = 0,
                student_loan_interest: float = 0,
                other_adjustments: float = 0,
                # Deductions
                medical_expenses: float = 0,
                taxes_paid: float = 0,
                interest_paid: float = 0,
                charitable_contributions: float = 0,
                casualty_losses: float = 0,
                miscellaneous_expenses: float = 0,
                qbid: float = 0,
        ):
    return FederalIncomeHandler(
            filing_status=filing_status,
            tax_year=tax_year,
            dependents=dependents,
            use_standard_deduction=use_standard_deduction,
            salaries_and_wages=salaries_and_wages,
            interest_income=interest_income,
            tax_exempt_interest=tax_exempt_interest,
            dividend_income=dividend_income,
            qualified_dividend_income=qualified_dividend_income,
            taxable_state_local_refunds=taxable_state_local_refunds,
            alimony_received=alimony_received,
            business_income_or_loss=business_income_or_loss,
            capital_gain_or_loss=capital_gain_or_loss,
            other_gains_or_losses=other_gains_or_losses,
            taxable_ira_distributions=taxable_ira_distributions,
            taxable_pensions=taxable_pensions,
            rent_royalty_income=rent_royalty_income,
            partnership_or_s_corp_income=partnership_or_s_corp_income,
            estate_trust_income=estate_trust_income,
            farm_income_or_loss=farm_income_or_loss,
            unemployment_compensation=unemployment_compensation,
            taxable_social_security=taxable_social_security,
            other_income=other_income,
            long_term_capital_gains=long_term_capital_gains,
            moving_expenses=moving_expenses,
            deductible_self_employment_tax=deductible_self_employment_tax,
            sep_simple_qualified_plans_deductions=sep_simple_qualified_plans_deductions,
            self_employment_health_insurance=self_employment_health_insurance,
            penalty_early_withdrawal_savings=penalty_early_withdrawal_savings,
            alimony_paid=alimony_paid,
            ira_deductions=ira_deductions,
            student_loan_interest=student_loan_interest,
            other_adjustments=other_adjustments,
            medical_expenses=medical_expenses,
            taxes_paid=taxes_paid,
            interest_paid=interest_paid,
            charitable_contributions=charitable_contributions,
            casualty_losses=casualty_losses,
            miscellaneous_expenses=miscellaneous_expenses,
            qbid=qbid,
        )


class TestFederalIncomeHandler(unittest.TestCase):
   

    def test_init_success(self):
        federalIncomeHandler = federal_income_handler_builder()

        self.assertEqual(federalIncomeHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(federalIncomeHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(federalIncomeHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(federalIncomeHandler.salaries_and_wages, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(federalIncomeHandler.long_term_capital_gains, SUPPORTED_LONG_TERM_CAPITAL_GAINS_1)
        self.assertEqual(federalIncomeHandler.taxable_pensions, SUPPORTED_TAXABLE_PENSIONS_1)

    def test_standard_deduction(self):
        federalIncomeHandler = federal_income_handler_builder(
            charitable_contributions=SUPPORTED_CHARITABLE_CONTRIBUTIONS,
            use_standard_deduction=True,
        )
        self.assertEqual(federalIncomeHandler.deduction_taken, 27700) # Standard deduction
        self.assertEqual(federalIncomeHandler.total_income, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(federalIncomeHandler.taxable_income, SUPPORTED_SALARY_AND_WAGES_1 - 27700)

        
    def test_itemized_deduction(self):
        federalIncomeHandler = federal_income_handler_builder(
            taxes_paid=SUPPORTED_TAXES_PAID,
            charitable_contributions=SUPPORTED_CHARITABLE_CONTRIBUTIONS,
            use_standard_deduction=False,
        )
        self.assertEqual(federalIncomeHandler.deduction_taken, SUPPORTED_CHARITABLE_CONTRIBUTIONS + SUPPORTED_TAXES_PAID)
        self.assertEqual(federalIncomeHandler.total_income, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(federalIncomeHandler.taxable_income, SUPPORTED_SALARY_AND_WAGES_1 - (SUPPORTED_CHARITABLE_CONTRIBUTIONS + SUPPORTED_TAXES_PAID))


    def test_equal(self):
        federalIncomeHandler1 = federal_income_handler_builder()
        federalIncomeHandler2 = federal_income_handler_builder()

        self.assertEqual(federalIncomeHandler1, federalIncomeHandler2)


    def test_from_dict(self):
        # Instantiate using the __init__ method with unique values for each field
        federalIncomeHandler1 = FederalIncomeHandler(
            filing_status=MARRIED_FILING_JOINTLY,
            tax_year=2022,
            dependents=1,
            use_standard_deduction=True,
            salaries_and_wages=100000, # $100K
            interest_income=100,
            tax_exempt_interest=200,
            dividend_income=300,
            qualified_dividend_income=400,
            taxable_state_local_refunds=500,
            alimony_received=600,
            business_income_or_loss=700,
            capital_gain_or_loss=800,
            other_gains_or_losses=900,
            taxable_ira_distributions=1000,
            taxable_pensions=1100,
            rent_royalty_income=1200,
            partnership_or_s_corp_income=1300,
            estate_trust_income=1400,
            farm_income_or_loss=1500,
            unemployment_compensation=1600,
            taxable_social_security=1700,
            other_income=1800,
            long_term_capital_gains=1900,
            medical_expenses=2100,
            taxes_paid=2200,
            interest_paid=2300,
            charitable_contributions=2400,
            casualty_losses=2500,
            miscellaneous_expenses=2600,
            qbid=2700,
            moving_expenses=2800,
            deductible_self_employment_tax=2900,
            sep_simple_qualified_plans_deductions=3000,
            self_employment_health_insurance=3100,
            penalty_early_withdrawal_savings=3200,
            alimony_paid=3300,
            ira_deductions=3400,
            student_loan_interest=3500,
            other_adjustments=3600
        )

        # Create a dictionary with the same values
        data = {
            "filing_status": MARRIED_FILING_JOINTLY,
            "tax_year": 2022,
            "dependents": 1,
            "use_standard_deduction": True,
            "salaries_and_wages": 100000, # $100K
            "interest_income": 100,
            "tax_exempt_interest": 200,
            "dividend_income": 300,
            "qualified_dividend_income": 400,
            "taxable_state_local_refunds": 500,
            "alimony_received": 600,
            "business_income_or_loss": 700,
            "capital_gain_or_loss": 800,
            "other_gains_or_losses": 900,
            "taxable_ira_distributions": 1000,
            "taxable_pensions": 1100,
            "rent_royalty_income": 1200,
            "partnership_or_s_corp_income": 1300,
            "estate_trust_income": 1400,
            "farm_income_or_loss": 1500,
            "unemployment_compensation": 1600,
            "taxable_social_security": 1700,
            "other_income": 1800,
            "long_term_capital_gains": 1900,
            "medical_expenses": 2100,
            "taxes_paid": 2200,
            "interest_paid": 2300,
            "charitable_contributions": 2400,
            "casualty_losses": 2500,
            "miscellaneous_expenses": 2600,
            "qbid": 2700,
            "moving_expenses": 2800,
            "deductible_self_employment_tax": 2900,
            "sep_simple_qualified_plans_deductions": 3000,
            "self_employment_health_insurance": 3100,
            "penalty_early_withdrawal_savings": 3200,
            "alimony_paid": 3300,
            "ira_deductions": 3400,
            "student_loan_interest": 3500,
            "other_adjustments": 3600
        }
        federalIncomeHandler2 = FederalIncomeHandler.from_dict(data)
        self.assertEqual(federalIncomeHandler1, federalIncomeHandler2)



if __name__ == '__main__':
    unittest.main()
