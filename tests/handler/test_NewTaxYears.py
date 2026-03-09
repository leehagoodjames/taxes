# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler import TaxHandler
from src.easytax.utils.Constants import *
from src.easytax.income.FederalIncomeHandler import FederalIncomeHandler


class TestNewTaxYears2025And2026(unittest.TestCase):
    """Test cases specifically for the new 2025 and 2026 tax years."""
    
    def setUp(self):
        """Set up test data for 2025 and 2026 tax years."""
        # Test income data
        self.test_income_data = [{
            'salaries_and_wages': 100000,
            'long_term_capital_gains': 50000,
            'other_adjustments': 1000,
            'use_standard_deduction': True,
            'taxes_paid': 5000,
            'interest_paid': 3000,
            'charitable_contributions': 2000,
        }]
        
        # Georgia state data (exemptions not needed for 2025/2026)
        self.georgia_state_data = {}
        
        # California state data
        self.california_state_data = {}
    
    def test_2025_federal_tax_calculation(self):
        """Test that 2025 federal tax calculations work correctly."""
        handler = TaxHandler.TaxHandler(
            tax_year=2025,
            filing_status=MARRIED_FILING_JOINTLY,
            state=FLORIDA,  # No state tax to isolate federal testing
            incomes_adjustments_and_deductions=self.test_income_data
        )
        
        handler.calculate_taxes()
        
        # Verify that calculations complete without error
        self.assertIsNotNone(handler.federalHander.income_tax_owed)
        self.assertIsNotNone(handler.federalHander.long_term_capital_gains_tax_owed)
        self.assertEqual(handler.tax_year, 2025)
    
    def test_2026_federal_tax_calculation(self):
        """Test that 2026 federal tax calculations work correctly."""
        handler = TaxHandler.TaxHandler(
            tax_year=2026,
            filing_status=SINGLE,
            state=ALASKA,  # No state tax to isolate federal testing
            incomes_adjustments_and_deductions=self.test_income_data
        )
        
        handler.calculate_taxes()
        
        # Verify that calculations complete without error
        self.assertIsNotNone(handler.federalHander.income_tax_owed)
        self.assertIsNotNone(handler.federalHander.long_term_capital_gains_tax_owed)
        self.assertEqual(handler.tax_year, 2026)
    
    def test_2025_georgia_tax_calculation(self):
        """Test that 2025 Georgia state tax calculations work correctly."""
        handler = TaxHandler.TaxHandler(
            tax_year=2025,
            filing_status=MARRIED_FILING_SEPARATELY,
            state=GEORGIA,
            incomes_adjustments_and_deductions=self.test_income_data,
            state_data=self.georgia_state_data
        )
        
        handler.calculate_taxes()
        
        # Verify that calculations complete without error
        self.assertIsNotNone(handler.stateTaxHandler.income_tax_owed)
        # Georgia treats LTCG as income, so LTCG tax should be 0
        self.assertEqual(handler.stateTaxHandler.long_term_capital_gains_tax_owed, [0.0])
        self.assertEqual(handler.tax_year, 2025)
    
    def test_2026_georgia_tax_calculation(self):
        """Test that 2026 Georgia state tax calculations work correctly.""" 
        handler = TaxHandler.TaxHandler(
            tax_year=2026,
            filing_status=SINGLE,
            state=GEORGIA,
            incomes_adjustments_and_deductions=self.test_income_data,
            state_data=self.georgia_state_data
        )
        
        handler.calculate_taxes()
        
        # Verify that calculations complete without error
        self.assertIsNotNone(handler.stateTaxHandler.income_tax_owed)
        # Georgia treats LTCG as income, so LTCG tax should be 0
        self.assertEqual(handler.stateTaxHandler.long_term_capital_gains_tax_owed, [0.0])
        self.assertEqual(handler.tax_year, 2026)
    
    def test_2025_california_tax_calculation(self):
        """Test that 2025 California state tax calculations work correctly."""
        handler = TaxHandler.TaxHandler(
            tax_year=2025,
            filing_status=MARRIED_FILING_JOINTLY,
            state=CALIFORNIA,
            incomes_adjustments_and_deductions=self.test_income_data,
            state_data=self.california_state_data
        )
        
        handler.calculate_taxes()
        
        # Verify that calculations complete without error
        self.assertIsNotNone(handler.stateTaxHandler.income_tax_owed)
        # California treats LTCG as income, so LTCG tax should be 0
        self.assertEqual(handler.stateTaxHandler.long_term_capital_gains_tax_owed, [0.0])
        self.assertEqual(handler.tax_year, 2025)
    
    def test_2026_california_tax_calculation(self):
        """Test that 2026 California state tax calculations work correctly."""
        handler = TaxHandler.TaxHandler(
            tax_year=2026,
            filing_status=MARRIED_FILING_SEPARATELY,
            state=CALIFORNIA,
            incomes_adjustments_and_deductions=self.test_income_data,
            state_data=self.california_state_data
        )
        
        handler.calculate_taxes()
        
        # Verify that calculations complete without error
        self.assertIsNotNone(handler.stateTaxHandler.income_tax_owed)
        # California treats LTCG as income, so LTCG tax should be 0  
        self.assertEqual(handler.stateTaxHandler.long_term_capital_gains_tax_owed, [0.0])
        self.assertEqual(handler.tax_year, 2026)
    
    def test_2025_federal_standard_deduction(self):
        """Test that 2025 federal standard deductions are applied correctly."""
        # Create federal income handler directly to test standard deduction
        income_handler = FederalIncomeHandler(
            tax_year=2025,
            filing_status=MARRIED_FILING_JOINTLY,
            salaries_and_wages=100000,
            use_standard_deduction=True
        )
        
        # Verify the standard deduction amount
        expected_deduction = 30550  # 2025 MFJ deduction
        self.assertEqual(income_handler.standard_deduction, expected_deduction)
    
    def test_2026_federal_standard_deduction(self):
        """Test that 2026 federal standard deductions are applied correctly."""
        # Create federal income handler directly to test standard deduction  
        income_handler = FederalIncomeHandler(
            tax_year=2026,
            filing_status=SINGLE,
            salaries_and_wages=100000,
            use_standard_deduction=True
        )
        
        # Verify the standard deduction amount
        expected_deduction = 15800  # 2026 Single deduction
        self.assertEqual(income_handler.standard_deduction, expected_deduction)
    
    def test_comprehensive_2025_calculation(self):
        """Test a comprehensive 2025 tax calculation with multiple scenarios."""
        test_scenarios = [
            # Scenario 1: High income MFJ
            {
                'tax_year': 2025,
                'filing_status': MARRIED_FILING_JOINTLY,
                'state': GEORGIA,
                'income': [{
                    'salaries_and_wages': 400000,
                    'long_term_capital_gains': 200000,
                    'use_standard_deduction': True,
                }],
                'state_data': {}
            },
            # Scenario 2: Lower income Single
            {
                'tax_year': 2025,
                'filing_status': SINGLE,
                'state': CALIFORNIA,
                'income': [{
                    'salaries_and_wages': 75000,
                    'long_term_capital_gains': 10000,
                    'use_standard_deduction': True,
                }],
                'state_data': {}
            }
        ]
        
        for scenario in test_scenarios:
            with self.subTest(scenario=scenario):
                handler = TaxHandler.TaxHandler(
                    tax_year=scenario['tax_year'],
                    filing_status=scenario['filing_status'],
                    state=scenario['state'],
                    incomes_adjustments_and_deductions=scenario['income'],
                    state_data=scenario['state_data']
                )
                
                # Should not raise any exceptions
                handler.calculate_taxes()
                
                # Verify basic sanity checks
                self.assertGreaterEqual(handler.total_tax, 0)
                self.assertEqual(handler.tax_year, 2025)
    
    def test_comprehensive_2026_calculation(self):
        """Test a comprehensive 2026 tax calculation with multiple scenarios."""
        test_scenarios = [
            # Scenario 1: High income MFS
            {
                'tax_year': 2026,
                'filing_status': MARRIED_FILING_SEPARATELY,
                'state': CALIFORNIA,
                'income': [{
                    'salaries_and_wages': 300000,
                    'long_term_capital_gains': 150000,
                    'use_standard_deduction': True,
                }],
                'state_data': {}
            },
            # Scenario 2: Lower income Single
            {
                'tax_year': 2026,
                'filing_status': SINGLE,
                'state': GEORGIA,
                'income': [{
                    'salaries_and_wages': 60000,
                    'long_term_capital_gains': 5000,
                    'use_standard_deduction': True,
                }],
                'state_data': {}
            }
        ]
        
        for scenario in test_scenarios:
            with self.subTest(scenario=scenario):
                handler = TaxHandler.TaxHandler(
                    tax_year=scenario['tax_year'],
                    filing_status=scenario['filing_status'],
                    state=scenario['state'],
                    incomes_adjustments_and_deductions=scenario['income'],
                    state_data=scenario['state_data']
                )
                
                # Should not raise any exceptions
                handler.calculate_taxes()
                
                # Verify basic sanity checks
                self.assertGreaterEqual(handler.total_tax, 0)
                self.assertEqual(handler.tax_year, 2026)


if __name__ == '__main__':
    unittest.main()