#!/usr/bin/env python3
"""
Example: Using the External Source Test Framework

This example demonstrates how to use the External Source Test Framework
to validate tax calculations against official examples and generate
comprehensive test suites.

Run this example with: python3 examples/external_source_validation_example.py
"""

import sys
import os
import tempfile
import shutil

# Add src to path so we can import easytax modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tests.utils.ExternalSourceTestFramework import (
    ExternalSourceValidator,
    OfficialExampleGenerator,
    TestDataManager
)


def main():
    """Main example function demonstrating the external source framework."""
    print("=" * 60)
    print("External Source Test Framework Example")
    print("=" * 60)
    
    # Create temporary directory for this example
    temp_dir = tempfile.mkdtemp(prefix='easytax_validation_')
    print(f"Using temporary directory: {temp_dir}")
    
    try:
        # Initialize framework components
        validator = ExternalSourceValidator(temp_dir)
        generator = OfficialExampleGenerator(validator)
        data_manager = TestDataManager(temp_dir)
        
        print("\n1. Creating sample data files...")
        data_manager.create_sample_data_files()
        print("   ✓ Sample data files created")
        
        # Demonstrate IRS example validation
        print("\n2. Validating IRS Publication Examples...")
        print("-" * 40)
        
        irs_examples = generator.create_irs_publication_examples()
        print(f"Generated {len(irs_examples)} IRS examples")
        
        for i, example in enumerate(irs_examples, 1):
            print(f"\nExample {i}: {example['name']}")
            print(f"Source: {example['source']}")
            print(f"Scenario: {example['filing_status']}, {example['tax_year']}")
            
            is_valid, results = validator.validate_scenario(example)
            
            if 'error' in results:
                print(f"   ❌ Error: {results['error']}")
            else:
                print(f"   Status: {'✓ PASS' if is_valid else '⚠ NEEDS REVIEW'}")
                
                if 'actual' in results:
                    actual = results['actual']
                    print(f"   Federal Tax: {actual.get('federal_tax_owed', 'N/A')}")
                    print(f"   State Tax: {actual.get('state_tax_owed', 'N/A')}")
                    print(f"   Total Tax: {actual.get('total_tax_owed', 'N/A')}")
                
                if not is_valid and 'expected' in results:
                    expected = results['expected']
                    print(f"   Expected Federal: {expected.get('federal_tax_owed', 'N/A')}")
                    print(f"   Expected State: {expected.get('state_tax_owed', 'N/A')}")
        
        # Demonstrate state example validation
        print("\n3. Validating State Examples...")
        print("-" * 40)
        
        for state in ['Georgia', 'California']:
            print(f"\n{state} Examples:")
            state_examples = generator.create_state_examples(state)
            
            if not state_examples:
                print(f"   No examples available for {state}")
                continue
            
            for example in state_examples:
                print(f"   Testing: {example['name']}")
                is_valid, results = validator.validate_scenario(example)
                
                if 'error' in results:
                    print(f"      ❌ Error: {results['error']}")
                else:
                    print(f"      Status: {'✓ PASS' if is_valid else '⚠ NEEDS REVIEW'}")
                    if 'actual' in results:
                        actual = results['actual']
                        print(f"      State Tax: {actual.get('state_tax_owed', 'N/A')}")
        
        # Demonstrate bracket boundary validation
        print("\n4. Validating Tax Bracket Boundaries...")
        print("-" * 40)
        
        bracket_scenarios = validator.generate_bracket_validation_scenarios(2024)
        print(f"Generated {len(bracket_scenarios)} bracket validation scenarios")
        
        # Test a few bracket scenarios
        for scenario in bracket_scenarios[:5]:
            print(f"\nTesting: {scenario['name']}")
            
            is_valid, results = validator.validate_scenario(scenario)
            
            if 'error' in results:
                print(f"   ❌ Error: {results['error']}")
            else:
                print(f"   Status: Executed {'successfully' if 'actual' in results else 'with issues'}")
                if 'actual' in results:
                    actual = results['actual']
                    print(f"   Federal Tax: {actual.get('federal_tax_owed', [0])[0]}")
        
        # Demonstrate cross-validation
        print("\n5. Cross-Validation Example...")
        print("-" * 40)
        
        test_scenario = {
            'tax_year': 2024,
            'filing_status': 'Single',
            'state': 'Georgia',
            'incomes_adjustments_and_deductions': [{
                'salaries_and_wages': 75000,
                'long_term_capital_gains': 25000,
                'use_standard_deduction': True
            }]
        }
        
        print("Cross-validating scenario:")
        print(f"   Filing Status: {test_scenario['filing_status']}")
        print(f"   Salary: ${test_scenario['incomes_adjustments_and_deductions'][0]['salaries_and_wages']:,}")
        print(f"   LTCG: ${test_scenario['incomes_adjustments_and_deductions'][0]['long_term_capital_gains']:,}")
        
        cross_results = validator.cross_validate_calculations(test_scenario)
        
        if cross_results.get('cross_validation_passed'):
            primary = cross_results['primary']
            print(f"   ✓ Cross-validation passed")
            print(f"   Federal Tax: {primary['federal_tax']}")
            print(f"   State Tax: {primary['state_tax']}")
            print(f"   Total Tax: ${primary['total_tax']:,.2f}")
        else:
            print(f"   ❌ Cross-validation failed: {cross_results.get('error', 'Unknown error')}")
        
        # Demonstrate data file management
        print("\n6. Data File Management...")
        print("-" * 40)
        
        # Load saved examples
        saved_irs_examples = data_manager.load_scenarios('irs_examples/publication_17_examples.json')
        print(f"Loaded {len(saved_irs_examples)} saved IRS examples")
        
        # Create and save custom scenarios
        custom_scenarios = [
            {
                'name': 'Custom_High_Income_Example',
                'source': 'Custom example for demonstration',
                'tax_year': 2024,
                'filing_status': 'Married_Filing_Jointly',
                'state': 'Georgia',
                'incomes_adjustments_and_deductions': [{
                    'salaries_and_wages': 300000,
                    'long_term_capital_gains': 150000,
                    'use_standard_deduction': True
                }],
                'validation_type': 'custom_example'
            }
        ]
        
        data_manager.save_scenarios(custom_scenarios, 'custom_examples.json')
        loaded_custom = data_manager.load_scenarios('custom_examples.json')
        print(f"Saved and loaded {len(loaded_custom)} custom scenarios")
        
        # Validate custom scenario
        for scenario in loaded_custom:
            print(f"\nValidating custom scenario: {scenario['name']}")
            is_valid, results = validator.validate_scenario(scenario)
            
            if 'actual' in results:
                actual = results['actual']
                print(f"   Federal Tax: {actual.get('federal_tax_owed', 'N/A')}")
                print(f"   State Tax: {actual.get('state_tax_owed', 'N/A')}")
                print(f"   Total Tax: {actual.get('total_tax_owed', 'N/A')}")
        
        print("\n7. Framework Usage Summary...")
        print("-" * 40)
        print("The External Source Test Framework provides:")
        print("   ✓ Validation against official IRS and state examples")
        print("   ✓ Automated bracket boundary testing")
        print("   ✓ Cross-validation between calculation methods")
        print("   ✓ Data file management for test scenarios")
        print("   ✓ Zero-dependency implementation")
        print("   ✓ Extensible architecture for custom validations")
        
        print(f"\nFramework successfully demonstrated using temporary directory:")
        print(f"   {temp_dir}")
        
    except Exception as e:
        print(f"\n❌ Error during example execution: {e}")
        raise
    
    finally:
        # Clean up temporary directory
        try:
            shutil.rmtree(temp_dir)
            print(f"\n✓ Cleaned up temporary directory")
        except Exception as e:
            print(f"\n⚠ Could not clean up temporary directory: {e}")
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == '__main__':
    main()