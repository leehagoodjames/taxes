"""
Integration tests using the External Source Test Framework

This module demonstrates how to use the external source testing framework
to validate tax calculations against official examples and bracket boundaries.
"""

import unittest
import os
import tempfile
import shutil
from tests.utils.ExternalSourceTestFramework import (
    ExternalSourceValidator,
    OfficialExampleGenerator,
    TestDataManager
)
from src.easytax.utils.Constants import SUPPORTED_TAX_YEARS, SUPPORTED_FILING_STATUSES


class TestExternalSourceIntegration(unittest.TestCase):
    """
    Integration tests that validate our tax calculations against external sources.
    
    These tests demonstrate how the framework can be used to validate
    calculations against official examples and generate comprehensive test suites.
    """
    
    def setUp(self):
        """Set up test fixtures with temporary directory."""
        self.temp_dir = tempfile.mkdtemp()
        self.validator = ExternalSourceValidator(self.temp_dir)
        self.generator = OfficialExampleGenerator(self.validator)
        self.data_manager = TestDataManager(self.temp_dir)
    
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_irs_publication_examples_validation(self):
        """Test validation against IRS Publication examples."""
        # Generate IRS examples
        irs_examples = self.generator.create_irs_publication_examples()
        
        validation_results = []
        for example in irs_examples:
            is_valid, results = self.validator.validate_scenario(example)
            validation_results.append({
                'scenario': example['name'],
                'valid': is_valid,
                'results': results
            })
        
        # Log results for analysis
        for result in validation_results:
            print(f"\nIRS Example: {result['scenario']}")
            print(f"Valid: {result['valid']}")
            if not result['valid'] and 'error' not in result['results']:
                print(f"Expected: {result['results'].get('expected', 'N/A')}")
                print(f"Actual: {result['results'].get('actual', 'N/A')}")
        
        # At least some examples should validate successfully
        successful_validations = sum(1 for r in validation_results if r['valid'])
        self.assertGreater(successful_validations, 0, 
                          "At least some IRS examples should validate successfully")
    
    def test_state_examples_validation(self):
        """Test validation against state tax department examples."""
        for state in ['Georgia']:
            with self.subTest(state=state):
                state_examples = self.generator.create_state_examples(state)
                
                if not state_examples:
                    self.skipTest(f"No examples available for {state}")
                
                validation_results = []
                for example in state_examples:
                    is_valid, results = self.validator.validate_scenario(example)
                    validation_results.append({
                        'scenario': example['name'],
                        'valid': is_valid,
                        'results': results
                    })
                
                # Log results
                for result in validation_results:
                    print(f"\n{state} Example: {result['scenario']}")
                    print(f"Valid: {result['valid']}")
                
                # At least some examples should validate
                successful_validations = sum(1 for r in validation_results if r['valid'])
                self.assertGreater(successful_validations, 0,
                                  f"At least some {state} examples should validate successfully")
    
    def test_bracket_boundary_validation(self):
        """Test validation of tax bracket boundaries."""
        # Test bracket boundaries for most recent supported year
        current_year = max(SUPPORTED_TAX_YEARS)
        bracket_scenarios = self.validator.generate_bracket_validation_scenarios(current_year)
        
        self.assertGreater(len(bracket_scenarios), 0, "Should generate bracket validation scenarios")
        
        validation_results = []
        # Test a subset to avoid too many tests
        for scenario in bracket_scenarios[:10]:
            is_valid, results = self.validator.validate_scenario(scenario)
            validation_results.append({
                'scenario': scenario['name'],
                'valid': is_valid,
                'results': results
            })
        
        # All bracket boundary tests should execute without errors
        error_count = sum(1 for r in validation_results if 'error' in r['results'])
        self.assertEqual(error_count, 0, "Bracket boundary tests should not produce errors")
        
        print(f"\nTested {len(validation_results)} bracket boundary scenarios")
        successful = sum(1 for r in validation_results if r['valid'])
        print(f"Successful validations: {successful}/{len(validation_results)}")
    
    def test_cross_validation_functionality(self):
        """Test cross-validation between different calculation methods."""
        # Create simple test scenarios
        test_scenarios = [
            {
                'tax_year': 2024,
                'filing_status': 'Single',
                'state': 'Georgia',
                'incomes_adjustments_and_deductions': [{
                    'salaries_and_wages': 30000,
                    'use_standard_deduction': True
                }]
            },
            {
                'tax_year': 2024,
                'filing_status': 'Married_Filing_Jointly',
                'state': 'Georgia',
                'incomes_adjustments_and_deductions': [{
                    'salaries_and_wages': 80000,
                    'use_standard_deduction': True
                }]
            }
        ]
        
        for scenario in test_scenarios:
            with self.subTest(filing_status=scenario['filing_status']):
                results = self.validator.cross_validate_calculations(scenario)
                
                print(f"\nCross-validation for {scenario['filing_status']}:")
                print(f"Passed: {results.get('cross_validation_passed', False)}")
                
                if results.get('cross_validation_passed'):
                    primary = results['primary']
                    print(f"Federal Tax: {primary['federal_tax']}")
                    print(f"State Tax: {primary['state_tax']}")
                    print(f"Total Tax: {primary['total_tax']}")
                
                # Should not fail with errors
                self.assertNotIn('error', results, f"Cross-validation should not error: {results.get('error', '')}")
    
    def test_data_file_management(self):
        """Test the data file management functionality."""
        # Create sample data files
        self.data_manager.create_sample_data_files()
        
        # Test loading IRS examples
        irs_examples = self.data_manager.load_scenarios('irs_examples/publication_17_examples.json')
        self.assertGreater(len(irs_examples), 0, "Should load IRS examples")
        
        # Validate structure of loaded examples
        for example in irs_examples:
            self.assertIn('name', example)
            self.assertIn('source', example)
            self.assertIn('tax_year', example)
            self.assertIn('filing_status', example)
            self.assertIn('expected_results', example)
        
        # Test loading state examples
        for state in ['georgia', 'california']:
            state_examples = self.data_manager.load_scenarios(f'state_examples/{state}_examples.json')
            if len(state_examples) > 0:  # May be empty for some states
                for example in state_examples:
                    self.assertIn('state', example)
                    self.assertEqual(example['state'].lower(), state.lower())
    
    def test_framework_extensibility(self):
        """Test that the framework can be extended with new validation types."""
        # Example of how to add custom validation scenarios
        custom_scenarios = [
            {
                'name': 'Custom_High_Income_Test',
                'tax_year': 2024,
                'filing_status': 'Single',
                'state': 'Georgia',
                'incomes_adjustments_and_deductions': [{
                    'salaries_and_wages': 500000,
                    'long_term_capital_gains': 200000,
                    'use_standard_deduction': True
                }],
                'validation_type': 'high_income_scenario'
            },
            {
                'name': 'Custom_Multiple_Income_Sources_Test',
                'tax_year': 2024,
                'filing_status': 'Married_Filing_Jointly',
                'state': 'Georgia',
                'incomes_adjustments_and_deductions': [{
                    'salaries_and_wages': 120000,
                    'long_term_capital_gains': 50000,
                    'interest_income': 5000,
                    'dividend_income': 10000,
                    'use_standard_deduction': False,
                    'taxes_paid': 15000,
                    'interest_paid': 12000,
                    'charitable_contributions': 8000
                }],
                'validation_type': 'complex_income_scenario'
            }
        ]
        
        # Save custom scenarios
        self.data_manager.save_scenarios(custom_scenarios, 'custom_validation_scenarios.json')
        
        # Load and validate custom scenarios
        loaded_scenarios = self.data_manager.load_scenarios('custom_validation_scenarios.json')
        self.assertEqual(len(loaded_scenarios), 2)
        
        # Test that custom scenarios can be validated
        for scenario in loaded_scenarios:
            is_valid, results = self.validator.validate_scenario(scenario)
            
            # Should not error out (though validation may not pass due to lack of expected results)
            self.assertIn('actual', results, "Should generate actual results for custom scenarios")
            print(f"\nCustom scenario: {scenario['name']}")
            print(f"Validation completed: {'error' not in results}")
    
    def test_performance_with_multiple_scenarios(self):
        """Test framework performance with multiple validation scenarios."""
        # Generate a larger set of test scenarios
        all_scenarios = []
        
        # Add IRS examples
        all_scenarios.extend(self.generator.create_irs_publication_examples())
        
        # Add state examples
        for state in ['Georgia']:
            all_scenarios.extend(self.generator.create_state_examples(state))
        
        # Add bracket validation for one year
        all_scenarios.extend(self.validator.generate_bracket_validation_scenarios(2024))
        
        print(f"\nTesting framework performance with {len(all_scenarios)} scenarios")
        
        # Run validations
        import time
        start_time = time.time()
        
        results = []
        for scenario in all_scenarios:
            is_valid, result = self.validator.validate_scenario(scenario)
            results.append(is_valid)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"Validated {len(all_scenarios)} scenarios in {duration:.2f} seconds")
        print(f"Average time per scenario: {duration/len(all_scenarios):.4f} seconds")
        
        # Performance should be reasonable (less than 1 second per scenario on average)
        avg_time = duration / len(all_scenarios)
        self.assertLess(avg_time, 1.0, "Framework should validate scenarios efficiently")
        
        # Should have some successful validations
        successful_validations = sum(results)
        print(f"Successful validations: {successful_validations}/{len(all_scenarios)}")


if __name__ == '__main__':
    # Run with verbose output to see validation details
    unittest.main(verbosity=2)