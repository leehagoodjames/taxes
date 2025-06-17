"""
Tests for the External Tax Verifier framework.

This module tests the external source verification system to ensure it works correctly
and can serve as a reliable source of truth for tax calculations.
"""

import unittest
import tempfile
import shutil
from pathlib import Path

from .external_tax_verifier import (
    ExternalTaxVerifier, 
    IRSPublicationSource, 
    CacheManager
)
from .test_helpers import ExternalSourceTestCase


class TestIRSPublicationSource(unittest.TestCase):
    """Test the IRS Publication Source implementation."""
    
    def setUp(self):
        self.source = IRSPublicationSource()
    
    def test_is_available(self):
        """Test that IRS publication source is always available."""
        self.assertTrue(self.source.is_available())
    
    def test_get_source_name(self):
        """Test that source name is returned correctly."""
        self.assertEqual(self.source.get_source_name(), "IRS Publications")
    
    def test_federal_income_tax_calculation(self):
        """Test federal income tax calculation with known values."""
        # Test case: $250,000 income, MFJ, 2023, no deductions (use standard)
        # Should be in 22% bracket
        result = self.source.calculate_federal_income_tax(
            income=250000,
            filing_status="Married Filing Jointly",
            tax_year=2023,
            deductions=0  # Will use standard deduction
        )
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
        # With standard deduction, should be reasonable amount
        self.assertLess(result, 100000)  # Sanity check
    
    def test_federal_income_tax_unsupported_year(self):
        """Test that unsupported tax year returns None."""
        result = self.source.calculate_federal_income_tax(
            income=100000,
            filing_status="Married Filing Jointly",
            tax_year=2020,  # Unsupported
            deductions=0
        )
        
        self.assertIsNone(result)
    
    def test_state_income_tax_georgia(self):
        """Test Georgia state income tax calculation."""
        result = self.source.calculate_state_income_tax(
            income=100000,
            state="Georgia",
            filing_status="Married Filing Jointly",
            tax_year=2023,
            deductions=0
        )
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
    
    def test_state_income_tax_unsupported_state(self):
        """Test that unsupported state returns None."""
        result = self.source.calculate_state_income_tax(
            income=100000,
            state="California",  # Not implemented yet
            filing_status="Married Filing Jointly",
            tax_year=2023,
            deductions=0
        )
        
        self.assertIsNone(result)
    
    def test_long_term_capital_gains_tax(self):
        """Test long-term capital gains tax calculation."""
        # Test 15% bracket
        result = self.source.calculate_long_term_capital_gains_tax(
            gains=50000,
            income=100000,  # Total income puts us in 15% LTCG bracket
            filing_status="Married Filing Jointly",
            tax_year=2023
        )
        
        self.assertIsNotNone(result)
        self.assertEqual(result, 7500.0)  # 50,000 * 0.15
    
    def test_payroll_taxes(self):
        """Test payroll tax calculations."""
        result = self.source.calculate_payroll_taxes(
            wages=100000,
            tax_year=2023
        )
        
        self.assertIsNotNone(result)
        self.assertIn('social_security', result)
        self.assertIn('medicare', result)
        
        # Check calculated values
        expected_ss = 100000 * 0.062  # 6.2%
        expected_medicare = 100000 * 0.0145  # 1.45%
        
        self.assertEqual(result['social_security'], expected_ss)
        self.assertEqual(result['medicare'], expected_medicare)
    
    def test_payroll_taxes_ss_cap(self):
        """Test that Social Security tax is capped at wage base."""
        high_wages = 200000  # Above 2023 SS wage base of $160,200
        result = self.source.calculate_payroll_taxes(
            wages=high_wages,
            tax_year=2023
        )
        
        # SS should be capped at wage base
        expected_ss = 160200 * 0.062
        expected_medicare = high_wages * 0.0145  # No cap on Medicare
        
        self.assertEqual(result['social_security'], expected_ss)
        self.assertEqual(result['medicare'], expected_medicare)


class TestCacheManager(unittest.TestCase):
    """Test the caching functionality."""
    
    def setUp(self):
        # Create temporary directory for cache
        self.temp_dir = tempfile.mkdtemp()
        self.cache = CacheManager(cache_dir=self.temp_dir)
    
    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.temp_dir)
    
    def test_cache_set_and_get(self):
        """Test basic cache set and get functionality."""
        # Set a value
        self.cache.set('test_calc', 1234.56, income=100000, year=2023)
        
        # Get the value back
        result = self.cache.get('test_calc', income=100000, year=2023)
        
        self.assertEqual(result, 1234.56)
    
    def test_cache_miss(self):
        """Test cache miss returns None."""
        result = self.cache.get('nonexistent', income=100000, year=2023)
        self.assertIsNone(result)
    
    def test_cache_key_consistency(self):
        """Test that cache keys are generated consistently."""
        # Set value with params in one order
        self.cache.set('test', 100, a=1, b=2, c=3)
        
        # Get value with params in different order - should still work
        result = self.cache.get('test', c=3, a=1, b=2)
        
        self.assertEqual(result, 100)


class TestExternalTaxVerifier(unittest.TestCase):
    """Test the main ExternalTaxVerifier class."""
    
    def setUp(self):
        # Create verifier with temporary cache
        self.temp_dir = tempfile.mkdtemp()
        self.verifier = ExternalTaxVerifier()
        self.verifier.cache = CacheManager(cache_dir=self.temp_dir)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_verify_federal_income_tax_success(self):
        """Test successful federal income tax verification."""
        # Use known calculation that should match IRS source
        result = self.verifier.verify_federal_income_tax(
            expected=34800,  # This should be close to the IRS calculation
            income=250000,
            filing_status="Married Filing Jointly",
            tax_year=2023,
            deductions=27700,  # Standard deduction
            tolerance=100  # Allow $100 tolerance for this test
        )
        
        self.assertTrue(result['verified'])
        self.assertIsNotNone(result['calculated'])
        self.assertEqual(result['expected'], 34800)
        self.assertIn('source', result)
    
    def test_verify_federal_income_tax_no_sources(self):
        """Test verification when no sources are available."""
        # Create verifier with no sources
        empty_verifier = ExternalTaxVerifier(sources=[])
        
        result = empty_verifier.verify_federal_income_tax(
            expected=1000,
            income=50000,
            filing_status="Single",
            tax_year=2023
        )
        
        self.assertFalse(result['verified'])
        self.assertIsNone(result['calculated'])
        self.assertIn('error', result)
    
    def test_verify_payroll_taxes(self):
        """Test payroll tax verification."""
        wages = 100000
        expected_ss = wages * 0.062
        expected_medicare = wages * 0.0145
        
        result = self.verifier.verify_payroll_taxes(
            expected_ss=expected_ss,
            expected_medicare=expected_medicare,
            wages=wages,
            tax_year=2023,
            tolerance=0.01
        )
        
        self.assertTrue(result['verified'])
        self.assertTrue(result['within_tolerance'])
        self.assertEqual(result['calculated_social_security'], expected_ss)
        self.assertEqual(result['calculated_medicare'], expected_medicare)


class TestExternalSourceTestCase(ExternalSourceTestCase):
    """Test the ExternalSourceTestCase helper class."""
    
    def test_inheritance(self):
        """Test that this class properly inherits from ExternalSourceTestCase."""
        self.assertIsInstance(self, unittest.TestCase)
        self.assertTrue(hasattr(self, 'verifier'))
        self.assertTrue(hasattr(self, 'verification_tolerance'))
    
    def test_payroll_tax_verification_helper(self):
        """Test the payroll tax verification helper method."""
        # Test with known good values
        wages = 50000
        expected_ss = wages * 0.062
        expected_medicare = wages * 0.0145
        
        # This should not raise an assertion error
        self.assertPayrollTaxesVerified(
            expected_ss=expected_ss,
            expected_medicare=expected_medicare,
            wages=wages,
            tax_year=2023
        )


if __name__ == '__main__':
    unittest.main()