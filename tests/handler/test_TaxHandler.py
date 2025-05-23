# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import TaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *
from src.easytax.utils.InputValidator import InputValidator


# Creates a TaxHandler that defaults to supported values
def tax_handler_builder(
        tax_year: int =SUPPORTED_TAX_YEAR, 
        filing_status: str =SUPPORTED_FILING_STATUS, 
        state: str =SUPPORTED_STATE, 
        incomes: list[dict]=SUPPORTED_INCOMES,
        state_data: dict=SUPPORTED_STATE_DATA,
        ):
    return TaxHandler.TaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            state=state, 
            incomes_adjustments_and_deductions=incomes,
            state_data=state_data,
        )


class TestTaxHandler(unittest.TestCase):
   

    def test_init_success(self):
        self.maxDiff = None
        taxHandler = tax_handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.state, SUPPORTED_STATE)
        self.assertEqual(taxHandler.federal_income_handlers, SUPPORTED_FEDERAL_INCOME_HANDLERS)


    def test_init_failure_unsupported_tax_year(self):
        tax_year = 2020 # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(tax_year=tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {InputValidator.alphabetize_set(SUPPORTED_TAX_YEARS)}, got: {tax_year}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_filing_status(self):
        filing_status = "Unsupported" # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(filing_status=filing_status)

        expected_message = f"filing_status must be in SUPPORTED_FILING_STATUSES: {InputValidator.alphabetize_set(SUPPORTED_FILING_STATUSES)}, got: {filing_status}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_state(self):
        state = "Unsupported" # Unsupported state

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(state=state)

        expected_message = f"state must be in SUPPORTED_STATES: {InputValidator.alphabetize_set(SUPPORTED_STATES)}, got: {state}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_calculate_taxes_married_filling_jointly(self):
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.federal_tax_owed, [46800]) # 34,800
        self.assertEqual(taxHandler.federal_long_term_capital_gains_tax_owed, [15000]) # All at 15% bracket
        self.assertEqual(taxHandler.state_tax_owed, [19890]) # ?
        self.assertEqual(taxHandler.state_long_term_capital_gains_tax_owed, [0]) # ?
        self.assertEqual(taxHandler.social_security_tax_owed, [9300, 6200]) # ?
        self.assertEqual(taxHandler.medicare_tax_owed, [2175, 1450]) # ?


    def test_calculate_taxes_married_filling_separately(self):
        taxHandler = tax_handler_builder(filing_status=MARRIED_FILING_SEPARATELY)
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.federal_tax_owed, [29400.0, 17400.0])
        self.assertEqual(taxHandler.federal_long_term_capital_gains_tax_owed, [9000, 6000]) # All at 15% bracket
        self.assertEqual(taxHandler.state_tax_owed, [11957.5, 7932.5])
        self.assertEqual(taxHandler.state_long_term_capital_gains_tax_owed, [0, 0])
        self.assertEqual(taxHandler.social_security_tax_owed, [9300, 6200])
        self.assertEqual(taxHandler.medicare_tax_owed, [2175, 1450])


    def test_display_tax_summary_success(self):

        # This test should simply not throw errors
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()


if __name__ == '__main__':
    unittest.main()
