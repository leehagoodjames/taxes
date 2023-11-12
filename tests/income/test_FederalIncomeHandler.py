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



if __name__ == '__main__':
    unittest.main()
