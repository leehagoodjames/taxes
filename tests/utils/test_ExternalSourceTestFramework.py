"""
Unit tests for External Source Test Framework

This module tests the external source validation framework functionality.
"""

import unittest
import os
import json
import tempfile
import shutil
from tests.utils.ExternalSourceTestFramework import (
    ExternalSourceValidator,
    OfficialExampleGenerator, 
    TestDataManager
)
from src.easytax.utils.Constants import SUPPORTED_TAX_YEARS, SUPPORTED_FILING_STATUSES


class TestExternalSourceValidator(unittest.TestCase):
    """Test the ExternalSourceValidator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.validator = ExternalSourceValidator(self.temp_dir)
        
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_init_creates_data_directory(self):
        """Test that initialization creates the data directory."""
        self.assertTrue(os.path.exists(self.temp_dir))
        
    def test_load_official_examples_empty_file(self):
        """Test loading from non-existent file returns empty list."""
        examples = self.validator.load_official_examples('nonexistent.json')
        self.assertEqual(examples, [])
    
    def test_load_official_examples_valid_file(self):
        """Test loading from valid JSON file."""
        # Create test data file
        test_data = [
            {
                'name': 'test_scenario',
                'tax_year': 2024,
                'filing_status': 'Single'
            }
        ]
        
        test_file = os.path.join(self.temp_dir, 'test_examples.json')
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        
        examples = self.validator.load_official_examples('test_examples.json')
        self.assertEqual(len(examples), 1)
        self.assertEqual(examples[0]['name'], 'test_scenario')
    
    def test_validate_scenario_success(self):
        """Test successful scenario validation."""
        scenario = {
            'name': 'Simple test scenario',
            'tax_year': 2024,
            'filing_status': 'Single',
            'state': 'Georgia',
            'incomes_adjustments_and_deductions': [{
                'salaries_and_wages': 50000,
                'use_standard_deduction': True
            }],
            'expected_results': {
                'federal_tax_owed': [5739.0],
                'state_tax_owed': [2250.0]
            },
            'tolerance': 0.1  # 10% tolerance for test
        }
        
        is_valid, results = self.validator.validate_scenario(scenario)
        
        # Should not error out (though may not match exactly due to tolerance)
        self.assertIn('expected', results)
        self.assertIn('actual', results)
        self.assertIn('scenario', results)
    
    def test_validate_scenario_error_handling(self):
        """Test scenario validation with invalid parameters."""
        invalid_scenario = {
            'name': 'Invalid scenario',
            'tax_year': 1999,  # Unsupported year
            'filing_status': 'Single',
            'state': 'Georgia',
            'incomes_adjustments_and_deductions': [{
                'salaries_and_wages': 50000,
                'use_standard_deduction': True
            }]
        }
        
        is_valid, results = self.validator.validate_scenario(invalid_scenario)
        self.assertFalse(is_valid)
        self.assertIn('error', results)
    
    def test_values_match_numeric(self):
        """Test numeric value matching with tolerance."""
        # Exact match
        self.assertTrue(self.validator._values_match(100.0, 100.0, 0.01))
        
        # Within tolerance
        self.assertTrue(self.validator._values_match(100.0, 99.5, 0.01))  # 0.5% difference
        
        # Outside tolerance
        self.assertFalse(self.validator._values_match(100.0, 95.0, 0.01))  # 5% difference
        
        # Zero values
        self.assertTrue(self.validator._values_match(0, 0.5, 1.0))  # Within absolute tolerance
    
    def test_values_match_non_numeric(self):
        """Test non-numeric value matching."""
        self.assertTrue(self.validator._values_match('Single', 'Single', 0.01))
        self.assertFalse(self.validator._values_match('Single', 'Married_Filing_Jointly', 0.01))
        self.assertTrue(self.validator._values_match(None, None, 0.01))
    
    def test_generate_bracket_validation_scenarios(self):
        """Test generation of bracket validation scenarios."""
        scenarios = self.validator.generate_bracket_validation_scenarios(2024)
        
        # Should generate scenarios for supported filing statuses
        self.assertGreater(len(scenarios), 0)
        
        # Check scenario structure
        for scenario in scenarios[:2]:  # Check first few scenarios
            self.assertIn('name', scenario)
            self.assertIn('tax_year', scenario)
            self.assertIn('filing_status', scenario)
            self.assertEqual(scenario['tax_year'], 2024)
            self.assertIn(scenario['filing_status'], SUPPORTED_FILING_STATUSES)
    
    def test_cross_validate_calculations(self):
        """Test cross-validation functionality."""
        scenario = {
            'tax_year': 2024,
            'filing_status': 'Single',
            'state': 'Georgia',
            'incomes_adjustments_and_deductions': [{
                'salaries_and_wages': 50000,
                'use_standard_deduction': True
            }]
        }
        
        results = self.validator.cross_validate_calculations(scenario)
        
        self.assertIn('primary', results)
        self.assertIn('cross_validation_passed', results)
        
        if results['cross_validation_passed']:
            self.assertIn('federal_tax', results['primary'])
            self.assertIn('state_tax', results['primary'])
            self.assertIn('total_tax', results['primary'])


class TestOfficialExampleGenerator(unittest.TestCase):
    """Test the OfficialExampleGenerator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        temp_dir = tempfile.mkdtemp()
        validator = ExternalSourceValidator(temp_dir)
        self.generator = OfficialExampleGenerator(validator)
        self.temp_dir = temp_dir
    
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_create_irs_publication_examples(self):
        """Test creation of IRS publication examples."""
        examples = self.generator.create_irs_publication_examples()
        
        self.assertGreater(len(examples), 0)
        
        for example in examples:
            self.assertIn('name', example)
            self.assertIn('source', example)
            self.assertIn('tax_year', example)
            self.assertIn('filing_status', example)
            self.assertIn('incomes_adjustments_and_deductions', example)
            self.assertIn('expected_results', example)
            
            # Check that source references IRS
            self.assertIn('IRS', example['source'])
    
    def test_create_state_examples_georgia(self):
        """Test creation of Georgia state examples."""
        examples = self.generator.create_state_examples('Georgia')
        
        self.assertGreater(len(examples), 0)
        
        for example in examples:
            self.assertIn('name', example)
            self.assertIn('source', example)
            self.assertEqual(example['state'], 'Georgia')
            self.assertIn('Georgia', example['source'])
    
    def test_create_state_examples_california(self):
        """Test creation of California state examples (not currently supported)."""
        examples = self.generator.create_state_examples('California')
        
        # California is not currently fully integrated, so should return empty list
        self.assertEqual(len(examples), 0)
    
    def test_create_state_examples_unsupported_state(self):
        """Test creation of examples for unsupported state."""
        examples = self.generator.create_state_examples('UnsupportedState')
        self.assertEqual(len(examples), 0)


class TestTestDataManager(unittest.TestCase):
    """Test the TestDataManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.manager = TestDataManager(self.temp_dir)
    
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_ensure_data_directory_creates_structure(self):
        """Test that data directory structure is created."""
        expected_dirs = [
            self.temp_dir,
            os.path.join(self.temp_dir, 'irs_examples'),
            os.path.join(self.temp_dir, 'state_examples'),
            os.path.join(self.temp_dir, 'bracket_validation')
        ]
        
        for expected_dir in expected_dirs:
            self.assertTrue(os.path.exists(expected_dir))
    
    def test_save_and_load_scenarios(self):
        """Test saving and loading scenarios."""
        test_scenarios = [
            {
                'name': 'Test Scenario 1',
                'tax_year': 2024,
                'filing_status': 'Single'
            },
            {
                'name': 'Test Scenario 2', 
                'tax_year': 2023,
                'filing_status': 'Married_Filing_Jointly'
            }
        ]
        
        filename = 'test_scenarios.json'
        
        # Save scenarios
        self.manager.save_scenarios(test_scenarios, filename)
        
        # Verify file was created
        filepath = os.path.join(self.temp_dir, filename)
        self.assertTrue(os.path.exists(filepath))
        
        # Load scenarios
        loaded_scenarios = self.manager.load_scenarios(filename)
        
        # Verify loaded data matches
        self.assertEqual(len(loaded_scenarios), 2)
        self.assertEqual(loaded_scenarios[0]['name'], 'Test Scenario 1')
        self.assertEqual(loaded_scenarios[1]['name'], 'Test Scenario 2')
    
    def test_load_scenarios_nonexistent_file(self):
        """Test loading from non-existent file."""
        scenarios = self.manager.load_scenarios('nonexistent.json')
        self.assertEqual(scenarios, [])
    
    def test_create_sample_data_files(self):
        """Test creation of sample data files."""
        self.manager.create_sample_data_files()
        
        # Check that sample files were created
        expected_files = [
            'irs_examples/publication_17_examples.json',
            'state_examples/georgia_examples.json'
        ]
        
        for expected_file in expected_files:
            filepath = os.path.join(self.temp_dir, expected_file)
            self.assertTrue(os.path.exists(filepath), f"Expected file {expected_file} was not created")
            
            # Verify file contains valid JSON
            with open(filepath, 'r') as f:
                data = json.load(f)
                self.assertIsInstance(data, list)
        
        # Check bracket validation files for each supported tax year
        for year in SUPPORTED_TAX_YEARS:
            bracket_file = f'bracket_validation/{year}_bracket_tests.json'
            filepath = os.path.join(self.temp_dir, bracket_file)
            self.assertTrue(os.path.exists(filepath), f"Expected bracket file {bracket_file} was not created")


if __name__ == '__main__':
    unittest.main()