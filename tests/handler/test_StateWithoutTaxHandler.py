# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import StateWithoutTaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *
from src.easytax.utils.InputValidator import InputValidator


# Creates a TaxHandler that defaults to supported values
def handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filing_status=SUPPORTED_FILING_STATUS, 
        federal_income_handlers=SUPPORTED_FEDERAL_INCOME_HANDLERS,
        state=SUPPORTED_STATE_WITHOUT_INCOME_TAX):
    return StateWithoutTaxHandler.StateWithoutTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federal_income_handlers=federal_income_handlers,
            state=state,
        )


class TestStateWithoutTaxHandler(unittest.TestCase):

    def test_init_success(self):
        taxHandler = handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.taxable_incomes, [0])
        self.assertEqual(taxHandler.long_term_capital_gains, [0])


    def test_init_failure_unsupported_tax_year(self):
        unsupported_tax_year = 2020

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(tax_year=unsupported_tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {InputValidator.alphabetize_set(SUPPORTED_TAX_YEARS)}, got: {unsupported_tax_year}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_filing_status(self):
        unsupported_filing_status = "Unsupported"

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(filing_status=unsupported_filing_status)

        expected_message = f"filing_status must be in SUPPORTED_FILING_STATUSES: {InputValidator.alphabetize_set(SUPPORTED_FILING_STATUSES)}, got: {unsupported_filing_status}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_state(self):
        unsupported_state = "Georgia" # Must contain 'exemptions'

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(state=unsupported_state)

        expected_message = f"state must be in STATES_WITHOUT_INCOME_TAX: {InputValidator.alphabetize_set(STATES_WITHOUT_INCOME_TAX)}, got: {unsupported_state}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_state_empty(self):
        unsupported_state = "" # Must be non-empty

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(state=unsupported_state)

        expected_message = f"state must be in STATES_WITHOUT_INCOME_TAX: {InputValidator.alphabetize_set(STATES_WITHOUT_INCOME_TAX)}, got: {unsupported_state}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_state_none(self):
        unsupported_state = None

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(state=unsupported_state)

        expected_message = f"state must be in STATES_WITHOUT_INCOME_TAX: {InputValidator.alphabetize_set(STATES_WITHOUT_INCOME_TAX)}, got: {unsupported_state}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_calculate_taxes_married_filling_jointly(self):
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.income_tax_owed, [0])
        self.assertEqual(taxHandler.long_term_capital_gains_tax_owed, [0])


    def test_display_tax_summary_success(self):

        # This test should simply not throw errors
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()
        
        
    def test_display_tax_summary_failure(self):

        taxHandler = handler_builder()

        with self.assertRaises(AttributeError) as cm:
            taxHandler.display_tax_summary()

        expected_message = "'StateWithoutTaxHandler' object has no attribute 'income_tax_owed'. Ensure you call 'calculate_taxes' before attempting to call this method."
        self.assertEqual(str(cm.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
