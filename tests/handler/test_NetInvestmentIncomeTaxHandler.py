# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import NetInvestmentIncomeTaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *
from src.easytax.utils.InputValidator import InputValidator


# Creates a TaxHandler that defaults to supported values
def handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filing_status=SUPPORTED_FILING_STATUS, 
        federal_income_handlers=SUPPORTED_FEDERAL_INCOME_HANDLERS,
        ):
    return NetInvestmentIncomeTaxHandler.NetInvestmentIncomeTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federal_income_handlers=federal_income_handlers,
        )


class TestNetInvestmentIncomeTaxHandler(unittest.TestCase):

    def test_init_success(self):
        
        taxHandler = handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.taxable_incomes, [0]) # The income should be zero because MAGI < threshold

    def test_init_success_with_niit(self):

        federal_income_handlers = [
            FederalIncomeHandler(
                filing_status=SUPPORTED_FILING_STATUS,
                tax_year=SUPPORTED_TAX_YEAR,
                salaries_and_wages=10000 + SUPPORTED_SALARY_AND_WAGES_1 + SUPPORTED_SALARY_AND_WAGES_2, 
                long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS_1 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_2,
                taxable_pensions=SUPPORTED_TAXABLE_PENSIONS_1 + SUPPORTED_TAXABLE_PENSIONS_2,
                use_standard_deduction=False, # Simplifies examples by making deductions zero
            ),
        ]
        taxHandler = handler_builder(federal_income_handlers=federal_income_handlers)
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.taxable_incomes, [10000]) # The lesser of the sum of the NIIT incomes or the taxable income minus the NIIT threshold

    def test_init_failure_unsupported_tax_year(self):
        tax_year = 2020 # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(tax_year=tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {InputValidator.alphabetize_set(SUPPORTED_TAX_YEARS)}, got: {tax_year}"
        self.assertEqual(str(cm.exception), expected_message)


    def test_init_failure_unsupported_filing_status(self):
        filing_status = "Unsupported" # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = handler_builder(filing_status=filing_status)

        expected_message = f"filing_status must be in SUPPORTED_FILING_STATUSES: {InputValidator.alphabetize_set(SUPPORTED_FILING_STATUSES)}, got: {filing_status}"
        self.assertEqual(str(cm.exception), expected_message)



    def test_calculate_taxes_married_filling_jointly(self):

        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.income_tax_owed, [0]) # Test case without NIIT, MAGI < threshold


    def test_calculate_taxes_married_filling_jointly(self):

        federal_income_handlers = [
            FederalIncomeHandler(
                filing_status=SUPPORTED_FILING_STATUS,
                tax_year=SUPPORTED_TAX_YEAR,
                salaries_and_wages=10000 + SUPPORTED_SALARY_AND_WAGES_1 + SUPPORTED_SALARY_AND_WAGES_2, 
                long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS_1 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_2,
                taxable_pensions=SUPPORTED_TAXABLE_PENSIONS_1 + SUPPORTED_TAXABLE_PENSIONS_2,
                use_standard_deduction=False, # Simplifies examples by making deductions zero
            ),
        ]
        taxHandler = handler_builder(federal_income_handlers=federal_income_handlers)
        taxHandler.calculate_taxes()
        
        self.assertEqual(taxHandler.income_tax_owed, [380])


    def test_display_tax_summary_success(self):

        # This test should simply not throw errors
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()
        
        
    def test_display_tax_summary_failure(self):

        taxHandler = handler_builder()

        with self.assertRaises(AttributeError) as cm:
            taxHandler.display_tax_summary()

        expected_message = "'NetInvestmentIncomeTaxHandler' object has no attribute 'income_tax_owed'. Ensure you call 'calculate_taxes' before attempting to call this method."
        self.assertEqual(str(cm.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
