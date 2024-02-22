# Standard Library Imports
import unittest

# Local Imports
from src.easytax.utils.Constants import *
from src.easytax.income.PayrollTaxIncomeHandler import PayrollTaxIncomeHandler
from tests.utils.TestContants import *



class TestPayrollTaxIncomeHandler(unittest.TestCase):
   

    def test_init_success(self):
        payrollTaxIncomeHandler = PayrollTaxIncomeHandler(
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1
        )
        self.assertEqual(payrollTaxIncomeHandler.salaries_and_wages, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(payrollTaxIncomeHandler.income_sources, [SUPPORTED_SALARY_AND_WAGES_1])
        self.assertEqual(payrollTaxIncomeHandler.total_income, SUPPORTED_SALARY_AND_WAGES_1)
        self.assertEqual(payrollTaxIncomeHandler.taxable_income, SUPPORTED_SALARY_AND_WAGES_1)


    def test_zero_income(self):
        payrollTaxIncomeHandler = PayrollTaxIncomeHandler(
            salaries_and_wages=0
        )
        self.assertEqual(payrollTaxIncomeHandler.salaries_and_wages, 0)
        self.assertEqual(payrollTaxIncomeHandler.income_sources, [0])
        self.assertEqual(payrollTaxIncomeHandler.total_income, 0)
        self.assertEqual(payrollTaxIncomeHandler.taxable_income, 0)


    def test_negative_income(self):
        payrollTaxIncomeHandler = PayrollTaxIncomeHandler(
            salaries_and_wages=-100
        )
        self.assertEqual(payrollTaxIncomeHandler.salaries_and_wages, -100)
        self.assertEqual(payrollTaxIncomeHandler.income_sources, [-100])
        self.assertEqual(payrollTaxIncomeHandler.total_income, -100)
        self.assertEqual(payrollTaxIncomeHandler.taxable_income, 0) # Taxable income cannot be zero


    def test_equal(self):
        payrollTaxIncomeHandler1 = PayrollTaxIncomeHandler(
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1
        )
        payrollTaxIncomeHandler2 = PayrollTaxIncomeHandler(
            salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1
        )
        self.assertEqual(payrollTaxIncomeHandler1, payrollTaxIncomeHandler2)


    def test_from_dict(self):
        # Instantiate using the __init__ method with unique values for each field
        payrollTaxIncomeHandler1 = PayrollTaxIncomeHandler(
            salaries_and_wages=100000, # $100K
        )

        # Create a dictionary with the same values
        data = {
            "salaries_and_wages": 100000, # $100K
        }
        payrollTaxIncomeHandler2 = PayrollTaxIncomeHandler.from_dict(data)
        self.assertEqual(payrollTaxIncomeHandler1, payrollTaxIncomeHandler2)



if __name__ == '__main__':
    unittest.main()
