# Standard Library Imports
import unittest

# Local Imports
from src.easytax.utils.Constants import *
from src.easytax.income.FederalIncomeHandler import FederalIncomeHandler
from tests.utils.TestContants import *



class TestFederalIncomeHandler(unittest.TestCase):
   

    def test_init_success(self):
        federalIncomeHandler = FederalIncomeHandler(
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1, 
            long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS_1,
            taxable_pensions=SUPPORTED_TAXABLE_PENSIONS_1,
        )
        self.assertEqual(federalIncomeHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(federalIncomeHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(federalIncomeHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(federalIncomeHandler.salaries_and_wages, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(federalIncomeHandler.long_term_capital_gains, SUPPORTED_LONG_TERM_CAPITAL_GAINS_1)
        self.assertEqual(federalIncomeHandler.taxable_pensions, SUPPORTED_TAXABLE_PENSIONS_1)

    def test_standard_deduction(self):
        federalIncomeHandler = FederalIncomeHandler(
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1, 
            taxes_paid=SUPPORTED_TAXES_PAID,
            charitable_contributions=SUPPORTED_CHARITABLE_CONTRIBUTIONS,
            use_standard_deduction=True,
        )
        self.assertEqual(federalIncomeHandler.deduction_taken, 27700) # Standard deduction
        self.assertEqual(federalIncomeHandler.total_income, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(federalIncomeHandler.taxable_income, SUPPORTED_SALARY_AND_WAGES_1 - 27700)
        
    def test_itemized_deduction(self):
        federalIncomeHandler = FederalIncomeHandler(
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1, 
            taxes_paid=SUPPORTED_TAXES_PAID,
            charitable_contributions=SUPPORTED_CHARITABLE_CONTRIBUTIONS,
            use_standard_deduction=False,
        )
        self.assertEqual(federalIncomeHandler.deduction_taken, SUPPORTED_CHARITABLE_CONTRIBUTIONS + SUPPORTED_TAXES_PAID)
        self.assertEqual(federalIncomeHandler.total_income, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(federalIncomeHandler.taxable_income, SUPPORTED_SALARY_AND_WAGES_1 - (SUPPORTED_CHARITABLE_CONTRIBUTIONS + SUPPORTED_TAXES_PAID))


    def test_equal(self):
        federalIncomeHandler1 = FederalIncomeHandler(
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1, 
            long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS_1,
            taxable_pensions=SUPPORTED_TAXABLE_PENSIONS_1,
        )
        federalIncomeHandler2 = FederalIncomeHandler(
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1, 
            long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS_1,
            taxable_pensions=SUPPORTED_TAXABLE_PENSIONS_1,
        )
        self.assertEqual(federalIncomeHandler1, federalIncomeHandler2)


    def test_from_dict(self):
        # Instantiate using the __init__ method with unique values for each field
        federalIncomeHandler1 = FederalIncomeHandler(
            filing_status="Married_Filing_Jointly",
            tax_year=2022,
            dependents=1,
            use_standard_deduction=True,
            salaries_and_wages=0,
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
            "filing_status": "Married_Filing_Jointly",
            "tax_year": 2022,
            "dependents": 1,
            "use_standard_deduction": True,
            "salaries_and_wages": 0,
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
