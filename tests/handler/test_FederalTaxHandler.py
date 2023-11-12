# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import FederalTaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *


# Creates a TaxHandler that defaults to supported values
def handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filing_status=SUPPORTED_FILING_STATUS, 
        federalIncomeHandlers=SUPPORTED_FEDERAL_INCOME_HANDLERS,
        ):
    return FederalTaxHandler.FederalTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federalIncomeHandlers=federalIncomeHandlers,
        )


class TestFederalTaxHandler(unittest.TestCase):

    def test_init_success(self):
        taxHandler = handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.taxable_incomes, [SUPPORTED_SALARY_AND_WAGES_1, SUPPORTED_SALARY_AND_WAGES_2])
        self.assertEqual(taxHandler.long_term_capital_gains, [SUPPORTED_LONG_TERM_CAPITAL_GAINS_1, SUPPORTED_LONG_TERM_CAPITAL_GAINS_2])

    def test_init_failure_unsupported_tax_year(self):
        tax_year = 2020 # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(tax_year=tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {tax_year}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_filing_status(self):
        filing_status = "Unsupported" # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(filing_status=filing_status)

        expected_message = f"filing_status must be in SUPPORTED_FILING_STATUSES: {SUPPORTED_FILING_STATUSES}, got: {filing_status}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_calculate_taxes_married_filling_jointly(self):
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.income_tax_owed, [46800])
        self.assertEqual(taxHandler.long_term_capital_gains_tax_owed, [1612.5]) 


    def test_display_tax_summary_success(self):

        # This test should simply not throw errors
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()
        
        
    def test_display_tax_summary_failure(self):

        taxHandler = handler_builder()

        with self.assertRaises(AttributeError) as cm:
            taxHandler.display_tax_summary()

        expected_message = "'FederalTaxHandler' object has no attribute 'income_tax_owed'. Ensure you call 'calculate_taxes' before attempting to call this method."
        self.assertEqual(str(cm.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
