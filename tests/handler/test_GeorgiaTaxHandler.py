# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import GeorgiaTaxHandler
from src.easytax.handler.TaxHandler import SUPPORTED_TAX_YEARS
from src.easytax.handler.TaxHandler import SUPPORTED_FILLING_STATUSES

SUPPORTED_TAX_YEAR = 2023
SUPPORTED_FILLING_STATUS = "Married_Filling_Jointly"
SUPPORTED_INCOMES = [150000, 100000]
SUPPORTED_LONG_TERM_CAPITAL_GAINS = [60000, 40000]

# Creates a TaxHandler that defaults to supported values
def handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filling_status=SUPPORTED_FILLING_STATUS, 
        incomes=SUPPORTED_INCOMES,
        long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS):
    return GeorgiaTaxHandler.GeorgiaTaxHandler(
            tax_year=tax_year, 
            filling_status=filling_status, 
            incomes=incomes, 
            long_term_capital_gains=long_term_capital_gains,
        )


class TestGeorgiaTaxHandler(unittest.TestCase):

    def test_init_success(self):
        taxHandler = handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filling_status, SUPPORTED_FILLING_STATUS)
        self.assertEqual(taxHandler.incomes, [210000, 140000]) # Georgia considers LTCG income.
        self.assertEqual(taxHandler.long_term_capital_gains, [0, 0])

    def test_init_failure_unsupported_tax_year(self):
        tax_year = 2020 # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(tax_year=tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {tax_year}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_filling_status(self):
        filling_status = "Unsupported" # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(filling_status=filling_status)

        expected_message = f"filling_status must be in SUPPORTED_FILLING_STATUSES: {SUPPORTED_FILLING_STATUSES}, got: {filling_status}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_calculate_taxes_married_filling_jointly(self):
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.income_tax_owed, [19890])
        self.assertEqual(taxHandler.long_term_capital_gains_tax_owed, [0]) # Georgia considers LTCG income.


    def test_display_tax_summary_success(self):

        # This test should simply not throw errors
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()
        
        
    def test_display_tax_summary_failure(self):

        taxHandler = handler_builder()

        with self.assertRaises(AttributeError) as cm:
            taxHandler.display_tax_summary()

        expected_message = "'GeorgiaTaxHandler' object has no attribute 'income_tax_owed'. Ensure you call 'calculate_taxes' before attempting to call this method."
        self.assertEqual(str(cm.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
