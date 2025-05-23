# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler.states import CaliforniaTaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *
from src.easytax.utils.InputValidator import InputValidator

def handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filing_status=SUPPORTED_FILING_STATUS, 
        federal_income_handlers=SUPPORTED_FEDERAL_INCOME_HANDLERS,
        state_data=SUPPORTED_STATE_DATA):
    return CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federal_income_handlers=federal_income_handlers,
            state_data=state_data,
        )

class TestCaliforniaTaxHandler(unittest.TestCase):

    def test_init_success(self):
        taxHandler = handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.taxable_incomes, 
                         [SUPPORTED_SALARY_AND_WAGES_1 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_1 +
                         SUPPORTED_SALARY_AND_WAGES_2 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_2 - taxHandler.standard_deduction])
        self.assertEqual(taxHandler.long_term_capital_gains[0], 0)

    def test_init_failure_unsupported_tax_year(self):
        unsupported_tax_year = 2020
        with self.assertRaises(ValueError) as cm:
            handler_builder(tax_year=unsupported_tax_year)
        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {InputValidator.alphabetize_set(SUPPORTED_TAX_YEARS)}, got: {unsupported_tax_year}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_calculate_taxes(self):
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        self.assertIsNotNone(taxHandler.income_tax_owed)
        self.assertEqual(taxHandler.long_term_capital_gains_tax_owed[0], 0)

    def test_mental_health_services_tax(self):
        # Test the additional 1% tax on income over $1 million
        high_income_handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=SUPPORTED_TAX_YEAR,
            filing_status=SUPPORTED_FILING_STATUS,
            federal_income_handlers=[
            FederalIncomeHandler(
                filing_status=SUPPORTED_FILING_STATUS,
                tax_year=SUPPORTED_TAX_YEAR,
                salaries_and_wages=2000000, # $2 million
                long_term_capital_gains=0,
                taxable_pensions=0,
                use_standard_deduction=False, # Simplifies examples by making deductions zero
                ),
            ],
            state_data=SUPPORTED_STATE_DATA
        )
        high_income_handler.calculate_taxes()
        self.assertGreater(high_income_handler.income_tax_owed[0], 0)
        # Check if the additional 1% tax is applied
        self.assertGreaterEqual(high_income_handler.income_tax_owed[0], (2000000 - 1000000) * 0.01)

    def test_display_tax_summary_success(self):
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        # This should not raise an exception
        taxHandler.display_tax_summary()

    def test_display_tax_summary_failure(self):
        taxHandler = handler_builder()
        with self.assertRaises(AttributeError) as cm:
            taxHandler.display_tax_summary()
        expected_message = "'CaliforniaTaxHandler' object has no attribute 'income_tax_owed'. Ensure you call 'calculate_taxes' before attempting to call this method."
        self.assertEqual(str(cm.exception), expected_message)

if __name__ == '__main__':
    unittest.main()
