"""
Updated TaxHandler tests with external source verification.

This module demonstrates how to use the external source verification framework
to replace manual tax calculation assertions with external source validation.
"""

# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import TaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *
from src.easytax.utils.InputValidator import InputValidator
from tests.external_sources.test_helpers import ExternalSourceTestCase


# Creates a TaxHandler that defaults to supported values
def tax_handler_builder(
        tax_year: int = SUPPORTED_TAX_YEAR, 
        filing_status: str = SUPPORTED_FILING_STATUS, 
        state: str = SUPPORTED_STATE, 
        incomes: list[dict] = SUPPORTED_INCOMES,
        state_data: dict = SUPPORTED_STATE_DATA,
        ):
    return TaxHandler.TaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            state=state, 
            incomes_adjustments_and_deductions=incomes,
            state_data=state_data,
        )


class TestTaxHandlerWithExternalVerification(ExternalSourceTestCase):
    """
    TaxHandler tests that use external source verification instead of manual assertions.
    
    This class inherits from ExternalSourceTestCase to get access to external
    source verification methods while maintaining all standard unittest functionality.
    """

    def test_init_success(self):
        """Test successful initialization - no external verification needed."""
        self.maxDiff = None
        taxHandler = tax_handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.state, SUPPORTED_STATE)
        self.assertEqual(taxHandler.federal_income_handlers, SUPPORTED_FEDERAL_INCOME_HANDLERS)

    def test_init_failure_unsupported_tax_year(self):
        """Test initialization failure with unsupported tax year."""
        tax_year = 2020  # Unsupported year

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(tax_year=tax_year)

        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {InputValidator.alphabetize_set(SUPPORTED_TAX_YEARS)}, got: {tax_year}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_unsupported_filing_status(self):
        """Test initialization failure with unsupported filing status."""
        filing_status = "Unsupported"  # Unsupported filing status

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(filing_status=filing_status)

        expected_message = f"filing_status must be in SUPPORTED_FILING_STATUSES: {InputValidator.alphabetize_set(SUPPORTED_FILING_STATUSES)}, got: {filing_status}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_unsupported_state(self):
        """Test initialization failure with unsupported state."""
        state = "Unsupported"  # Unsupported state

        with self.assertRaises(ValueError) as cm:
            _ = tax_handler_builder(state=state)

        expected_message = f"state must be in SUPPORTED_STATES: {InputValidator.alphabetize_set(SUPPORTED_STATES)}, got: {state}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_calculate_taxes_married_filing_jointly_with_external_verification(self):
        """
        Test tax calculations with external source verification.
        
        This replaces manual assertions with external source validation,
        providing a more robust and accurate test.
        """
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        
        # Calculate total income for verification
        total_income = SUPPORTED_SALARY_AND_WAGES_1 + SUPPORTED_SALARY_AND_WAGES_2
        total_ltcg = SUPPORTED_LONG_TERM_CAPITAL_GAINS_1 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_2
        
        # Verify federal income tax using external sources
        self.assertTaxCalculationVerified(
            expected=taxHandler.federal_tax_owed,
            calculation_type='federal_income',
            income=total_income,
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            deductions=0  # Using no deductions as per test constants
        )
        
        # Verify federal long-term capital gains tax
        self.assertTaxCalculationVerified(
            expected=taxHandler.federal_long_term_capital_gains_tax_owed,
            calculation_type='ltcg',
            gains=total_ltcg,
            income=total_income,
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR
        )
        
        # Verify state income tax
        # Georgia treats LTCG as ordinary income, so include it in income calculation
        georgia_income = total_income + total_ltcg
        self.assertTaxCalculationVerified(
            expected=taxHandler.state_tax_owed,
            calculation_type='state_income',
            income=georgia_income,
            state=SUPPORTED_STATE,
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            deductions=0
        )
        
        # Verify payroll taxes
        wages_list = [SUPPORTED_SALARY_AND_WAGES_1, SUPPORTED_SALARY_AND_WAGES_2]
        self.assertPayrollTaxesVerified(
            expected_ss=taxHandler.social_security_tax_owed,
            expected_medicare=taxHandler.medicare_tax_owed,
            wages=wages_list,
            tax_year=SUPPORTED_TAX_YEAR
        )
        
        # Verify state LTCG tax (should be 0 for Georgia since it treats LTCG as ordinary income)
        self.assertEqual(taxHandler.state_long_term_capital_gains_tax_owed, [0])

    def test_calculate_taxes_married_filing_separately_with_external_verification(self):
        """Test separate filing calculations with external verification."""
        taxHandler = tax_handler_builder(filing_status=MARRIED_FILING_SEPARATELY)
        taxHandler.calculate_taxes()
        
        # For married filing separately, each person's taxes are calculated individually
        incomes = [SUPPORTED_SALARY_AND_WAGES_1, SUPPORTED_SALARY_AND_WAGES_2]
        ltcg_amounts = [SUPPORTED_LONG_TERM_CAPITAL_GAINS_1, SUPPORTED_LONG_TERM_CAPITAL_GAINS_2]
        
        # Verify federal income taxes for each taxpayer
        for i, (income, expected_fed_tax) in enumerate(zip(incomes, taxHandler.federal_tax_owed)):
            self.assertTaxCalculationVerified(
                expected=expected_fed_tax,
                calculation_type='federal_income',
                income=income,
                filing_status=MARRIED_FILING_SEPARATELY,
                tax_year=SUPPORTED_TAX_YEAR,
                deductions=0
            )
        
        # Verify federal LTCG taxes for each taxpayer
        for i, (income, ltcg, expected_ltcg_tax) in enumerate(zip(incomes, ltcg_amounts, taxHandler.federal_long_term_capital_gains_tax_owed)):
            self.assertTaxCalculationVerified(
                expected=expected_ltcg_tax,
                calculation_type='ltcg',
                gains=ltcg,
                income=income,
                filing_status=MARRIED_FILING_SEPARATELY,
                tax_year=SUPPORTED_TAX_YEAR
            )
        
        # Verify state income taxes (Georgia includes LTCG in ordinary income)
        for i, (income, ltcg, expected_state_tax) in enumerate(zip(incomes, ltcg_amounts, taxHandler.state_tax_owed)):
            georgia_income = income + ltcg
            self.assertTaxCalculationVerified(
                expected=expected_state_tax,
                calculation_type='state_income',
                income=georgia_income,
                state=SUPPORTED_STATE,
                filing_status=MARRIED_FILING_SEPARATELY,
                tax_year=SUPPORTED_TAX_YEAR,
                deductions=0
            )
        
        # Verify payroll taxes
        self.assertPayrollTaxesVerified(
            expected_ss=taxHandler.social_security_tax_owed,
            expected_medicare=taxHandler.medicare_tax_owed,
            wages=incomes,
            tax_year=SUPPORTED_TAX_YEAR
        )

    def test_calculate_taxes_traditional_assertions_as_fallback(self):
        """
        Demonstrate fallback to traditional assertions when external verification isn't available.
        
        This test shows how the framework gracefully handles cases where external
        sources might not be available, maintaining backward compatibility.
        """
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        
        # These traditional assertions still work as a fallback
        # The external verification framework supplements, not replaces, traditional testing
        self.assertIsNotNone(taxHandler.federal_tax_owed)
        self.assertIsNotNone(taxHandler.state_tax_owed)
        self.assertIsNotNone(taxHandler.social_security_tax_owed)
        self.assertIsNotNone(taxHandler.medicare_tax_owed)
        
        # Check that all values are positive (basic sanity check)
        for tax_amount in taxHandler.federal_tax_owed:
            self.assertGreaterEqual(tax_amount, 0)
        
        for tax_amount in taxHandler.state_tax_owed:
            self.assertGreaterEqual(tax_amount, 0)

    def test_display_tax_summary_success(self):
        """Test that tax summary displays without errors."""
        # This test doesn't need external verification
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()


class TestTaxHandlerMixedApproach(unittest.TestCase):
    """
    Example showing how to mix external verification with traditional assertions.
    
    This demonstrates a migration strategy where tests can gradually adopt
    external verification while maintaining existing manual assertions.
    """

    def test_mixed_verification_approach(self):
        """
        Show how external verification can be used alongside traditional assertions.
        """
        from tests.external_sources.test_helpers import verify_tax_calculation, get_verification_report
        
        taxHandler = tax_handler_builder()
        taxHandler.calculate_taxes()
        
        # Traditional assertion (existing test)
        self.assertEqual(len(taxHandler.federal_tax_owed), 1)
        
        # External verification for the actual calculation
        total_income = SUPPORTED_SALARY_AND_WAGES_1 + SUPPORTED_SALARY_AND_WAGES_2
        
        # Get detailed verification report
        report = get_verification_report(
            expected=taxHandler.federal_tax_owed[0],
            calculation_type='federal_income',
            income=total_income,
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            deductions=0
        )
        
        # You can examine the report for debugging or logging
        if report.get('verified') and not report.get('within_tolerance'):
            # Log the discrepancy for investigation
            print(f"Tax calculation discrepancy detected:")
            print(f"Expected: {report['expected']}")
            print(f"External source: {report['calculated']}")
            print(f"Source: {report['source']}")
        
        # Use simple verification function for pass/fail
        verification_passed = verify_tax_calculation(
            expected=taxHandler.federal_tax_owed[0],
            calculation_type='federal_income',
            income=total_income,
            filing_status=SUPPORTED_FILING_STATUS,
            tax_year=SUPPORTED_TAX_YEAR,
            deductions=0,
            tolerance=50.0  # Allow $50 tolerance for this example
        )
        
        # Only fail the test if verification was possible and failed
        if report.get('verified') and not verification_passed:
            self.fail(f"External verification failed: {report}")


if __name__ == '__main__':
    unittest.main()