# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import GeorgiaTaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *


# Creates a TaxHandler that defaults to supported values
def handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filing_status=SUPPORTED_FILING_STATUS, 
        federalIncomeHandlers=SUPPORTED_FEDERAL_INCOME_HANDLERS,
        state_data=SUPPORTED_STATE_DATA):
    return GeorgiaTaxHandler.GeorgiaTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federalIncomeHandlers=federalIncomeHandlers,
            state_data=state_data,
        )


class TestGeorgiaTaxHandler(unittest.TestCase):

    def test_init_success(self):
        taxHandler = handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.taxable_incomes, [
            SUPPORTED_SALARY_AND_WAGES_1 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_1, 
            SUPPORTED_SALARY_AND_WAGES_2 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_2]) # Georgia considers LTCG income.
        self.assertEqual(taxHandler.long_term_capital_gains, [0, 0])

    def test_init_failure_unsupported_tax_year(self):
        unsupported_tax_year = 2020

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(tax_year=unsupported_tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {unsupported_tax_year}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_filing_status(self):
        unsupported_filing_status = "Unsupported"

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(filing_status=unsupported_filing_status)

        expected_message = f"filing_status must be in SUPPORTED_FILING_STATUSES: {SUPPORTED_FILING_STATUSES}, got: {unsupported_filing_status}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_unsupported_state_data_none(self):
        unsupported_state_data = None # Must contain 'exemptions'

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(state_data=unsupported_state_data)

        expected_message = f"invalid value for 'state_data': {unsupported_state_data}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_unsupported_state_data_empty(self):
        unsupported_state_data = {} # Must contain 'exemptions'

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(state_data=unsupported_state_data)

        expected_message = f"state_data specified invalid value for 'exemptions': None"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_unsupported_state_data_exemptions_type(self):
        unsupported_state_data = {'exemptions': 1.0} # Must be an integer

        with self.assertRaises(TypeError) as cm:
            _ = handler_builder(state_data=unsupported_state_data)

        expected_message = f"state_data specified invalid type for 'exemptions': {type(unsupported_state_data.get('exemptions'))}"
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
