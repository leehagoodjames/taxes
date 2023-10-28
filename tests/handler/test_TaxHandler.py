# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import TaxHandler
from src.easytax.handler.TaxHandler import SUPPORTED_TAX_YEARS
from src.easytax.handler.TaxHandler import SUPPORTED_FILLING_STATUSES
from src.easytax.handler.TaxHandler import SUPPORTED_STATES

SUPPORTED_TAX_YEAR = 2023
SUPPORTED_FILLING_STATUS = "Married_Filling_Jointly"
SUPPORTED_STATE = "Georgia"
SUPPORTED_INCOMES = [150000, 100000]
SUPPORTED_LONG_TERM_CAPITAL_GAINS = [60000, 40000]

# Creates a TaxHandler that defaults to supported values
def tax_handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filling_status=SUPPORTED_FILLING_STATUS, 
        state=SUPPORTED_STATE, 
        incomes=SUPPORTED_INCOMES,
        long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS):
    return TaxHandler.TaxHandler(
            tax_year=tax_year, 
            filling_status=filling_status, 
            state=state, 
            incomes=incomes, 
            long_term_capital_gains=long_term_capital_gains,
        )


class TestTaxHandler(unittest.TestCase):

    def test_init_success(self):
        taxHandler = tax_handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filling_status, SUPPORTED_FILLING_STATUS)
        self.assertEqual(taxHandler.state, SUPPORTED_STATE)
        self.assertEqual(taxHandler.incomes, SUPPORTED_INCOMES)
        self.assertEqual(taxHandler.long_term_capital_gains, SUPPORTED_LONG_TERM_CAPITAL_GAINS)

    def test_init_failure_unsupported_tax_year(self):
        tax_year = 2020 # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(tax_year=tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {tax_year}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_filling_status(self):
        filling_status = "Unsupported" # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(filling_status=filling_status)

        expected_message = f"filling_status must be in SUPPORTED_FILLING_STATUSES: {SUPPORTED_FILLING_STATUSES}, got: {filling_status}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_state(self):
        state = "Unsupported" # Unsupported state

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(state=state)

        expected_message = f"state must be in SUPPORTED_STATES: {SUPPORTED_STATES}, got: {state}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_calculate_taxes_married_filling_jointly(self):
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.federal_tax_owed, [46800]) # 34,800
        self.assertEqual(taxHandler.federal_long_term_capital_gains_tax_owed, [1612.5]) # 1,612.5
        self.assertEqual(taxHandler.state_tax_owed, [19890]) # ?
        self.assertEqual(taxHandler.state_long_term_capital_gains_tax_owed, [0]) # ?
        self.assertEqual(taxHandler.social_security_tax_owed, [9300, 6200]) # ?
        self.assertEqual(taxHandler.medicare_tax_owed, [2175, 1450]) # ?


    def test_display_tax_summary_success(self):

        # This test should simply not throw errors
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()


if __name__ == '__main__':
    unittest.main()
