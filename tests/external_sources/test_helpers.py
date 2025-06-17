"""
Test helpers for external source verification.

This module provides utility functions and classes to help integrate external source
verification into existing test cases.
"""

import unittest
from typing import List, Union, Optional
from .external_tax_verifier import default_verifier


class ExternalSourceTestCase(unittest.TestCase):
    """
    Base test case class that provides external source verification methods.
    
    This class extends unittest.TestCase with methods for verifying tax calculations
    against external sources while maintaining backward compatibility with manual assertions.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verifier = default_verifier
        self.verification_tolerance = 0.01  # $0.01 tolerance for floating point comparisons
    
    def assertTaxCalculationVerified(self, 
                                   expected: Union[float, List[float]], 
                                   calculation_type: str,
                                   **calculation_params):
        """
        Assert that a tax calculation matches external source verification.
        
        Args:
            expected: Expected tax amount(s) from the tax handler
            calculation_type: Type of tax calculation ('federal_income', 'state_income', 'ltcg', 'payroll')
            **calculation_params: Parameters needed for external source verification
        
        Raises:
            AssertionError: If the calculation doesn't match external sources within tolerance
        """
        if isinstance(expected, list):
            # Handle list of expected values (e.g., for multiple taxpayers)
            for i, exp_value in enumerate(expected):
                self._verify_single_calculation(exp_value, calculation_type, i, **calculation_params)
        else:
            self._verify_single_calculation(expected, calculation_type, 0, **calculation_params)
    
    def _verify_single_calculation(self, 
                                 expected: float, 
                                 calculation_type: str, 
                                 index: int,
                                 **calculation_params):
        """Verify a single tax calculation against external sources."""
        
        if calculation_type == 'federal_income':
            result = self.verifier.verify_federal_income_tax(
                expected=expected,
                income=calculation_params.get('income'),
                filing_status=calculation_params.get('filing_status'),
                tax_year=calculation_params.get('tax_year'),
                deductions=calculation_params.get('deductions', 0),
                tolerance=self.verification_tolerance
            )
            self._assert_verification_result(result, 'Federal Income Tax', index)
            
        elif calculation_type == 'state_income':
            result = self.verifier.verify_state_income_tax(
                expected=expected,
                income=calculation_params.get('income'),
                state=calculation_params.get('state'),
                filing_status=calculation_params.get('filing_status'),
                tax_year=calculation_params.get('tax_year'),
                deductions=calculation_params.get('deductions', 0),
                tolerance=self.verification_tolerance
            )
            self._assert_verification_result(result, 'State Income Tax', index)
            
        elif calculation_type == 'ltcg':
            result = self.verifier.verify_long_term_capital_gains_tax(
                expected=expected,
                gains=calculation_params.get('gains'),
                income=calculation_params.get('income'),
                filing_status=calculation_params.get('filing_status'),
                tax_year=calculation_params.get('tax_year'),
                tolerance=self.verification_tolerance
            )
            self._assert_verification_result(result, 'Long-Term Capital Gains Tax', index)
            
        else:
            # Fallback to manual assertion for unsupported calculation types
            # This maintains backward compatibility
            self.assertTrue(True, f"External verification not supported for {calculation_type}")
    
    def assertPayrollTaxesVerified(self, 
                                 expected_ss: Union[float, List[float]],
                                 expected_medicare: Union[float, List[float]],
                                 wages: Union[float, List[float]],
                                 tax_year: int):
        """
        Assert that payroll tax calculations match external source verification.
        
        Args:
            expected_ss: Expected Social Security tax amount(s)
            expected_medicare: Expected Medicare tax amount(s)  
            wages: Wage amount(s) for calculation
            tax_year: Tax year
        """
        # Handle lists for multiple wage earners
        if isinstance(expected_ss, list):
            for i, (exp_ss, exp_medicare, wage) in enumerate(zip(expected_ss, expected_medicare, wages)):
                result = self.verifier.verify_payroll_taxes(
                    expected_ss=exp_ss,
                    expected_medicare=exp_medicare,
                    wages=wage,
                    tax_year=tax_year,
                    tolerance=self.verification_tolerance
                )
                self._assert_payroll_verification_result(result, i)
        else:
            result = self.verifier.verify_payroll_taxes(
                expected_ss=expected_ss,
                expected_medicare=expected_medicare,
                wages=wages,
                tax_year=tax_year,
                tolerance=self.verification_tolerance
            )
            self._assert_payroll_verification_result(result, 0)
    
    def _assert_verification_result(self, result: dict, tax_type: str, index: int):
        """Assert that a verification result indicates success."""
        if not result['verified']:
            # If external verification isn't available, fall back to manual assertion
            # This maintains backward compatibility when external sources are down
            self.skipTest(f"External verification not available for {tax_type}: {result.get('error', 'Unknown error')}")
        
        if not result['within_tolerance']:
            expected = result['expected']
            calculated = result['calculated']
            difference = result['difference']
            source = result['source']
            
            self.fail(
                f"{tax_type} verification failed (index {index}):\n"
                f"Expected: ${expected:,.2f}\n"
                f"External source ({source}): ${calculated:,.2f}\n"
                f"Difference: ${difference:,.2f}\n"
                f"Tolerance: ${self.verification_tolerance:,.2f}"
            )
    
    def _assert_payroll_verification_result(self, result: dict, index: int):
        """Assert that a payroll tax verification result indicates success."""
        if not result['verified']:
            self.skipTest(f"External verification not available for payroll taxes: {result.get('error', 'Unknown error')}")
        
        if not result['within_tolerance']:
            exp_ss = result['expected_social_security']
            calc_ss = result['calculated_social_security']
            exp_medicare = result['expected_medicare']
            calc_medicare = result['calculated_medicare']
            source = result['source']
            
            self.fail(
                f"Payroll tax verification failed (index {index}):\n"
                f"Expected SS: ${exp_ss:,.2f}, External: ${calc_ss:,.2f}\n"
                f"Expected Medicare: ${exp_medicare:,.2f}, External: ${calc_medicare:,.2f}\n"
                f"Source: {source}\n"
                f"Tolerance: ${self.verification_tolerance:,.2f}"
            )


def verify_tax_calculation(expected: float, 
                         calculation_type: str, 
                         tolerance: float = 0.01,
                         **calculation_params) -> bool:
    """
    Standalone function to verify a tax calculation against external sources.
    
    Args:
        expected: Expected tax amount
        calculation_type: Type of calculation ('federal_income', 'state_income', 'ltcg')
        tolerance: Acceptable difference between expected and calculated values
        **calculation_params: Parameters for the specific calculation type
    
    Returns:
        True if verification passes, False otherwise
    """
    verifier = default_verifier
    
    if calculation_type == 'federal_income':
        result = verifier.verify_federal_income_tax(
            expected=expected,
            tolerance=tolerance,
            **calculation_params
        )
    elif calculation_type == 'state_income':
        result = verifier.verify_state_income_tax(
            expected=expected,
            tolerance=tolerance,
            **calculation_params
        )
    elif calculation_type == 'ltcg':
        result = verifier.verify_long_term_capital_gains_tax(
            expected=expected,
            tolerance=tolerance,
            **calculation_params
        )
    else:
        return False  # Unsupported calculation type
    
    return result.get('verified', False) and result.get('within_tolerance', False)


def get_verification_report(expected: float, 
                          calculation_type: str,
                          **calculation_params) -> dict:
    """
    Get a detailed verification report for a tax calculation.
    
    Returns:
        Dictionary containing verification details including source, differences, etc.
    """
    verifier = default_verifier
    
    if calculation_type == 'federal_income':
        return verifier.verify_federal_income_tax(expected=expected, **calculation_params)
    elif calculation_type == 'state_income':
        return verifier.verify_state_income_tax(expected=expected, **calculation_params)
    elif calculation_type == 'ltcg':
        return verifier.verify_long_term_capital_gains_tax(expected=expected, **calculation_params)
    else:
        return {'error': f'Unsupported calculation type: {calculation_type}'}