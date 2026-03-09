# External Source Test Data

This directory contains test data files for validating tax calculations against external sources of truth.

## Directory Structure

- `irs_examples/` - Test scenarios based on official IRS publications and examples
- `state_examples/` - Test scenarios based on state tax department examples  
- `bracket_validation/` - Test scenarios for validating tax bracket boundary calculations
- `custom/` - Custom test scenarios for specific validation needs

## Data File Format

Test scenario files are in JSON format with the following structure:

```json
[
  {
    "name": "Scenario Name",
    "source": "Official Source Reference",
    "tax_year": 2024,
    "filing_status": "Single",
    "state": "Georgia",
    "incomes_adjustments_and_deductions": [
      {
        "salaries_and_wages": 50000,
        "long_term_capital_gains": 10000,
        "use_standard_deduction": true
      }
    ],
    "state_data": {
      "exemptions": 2
    },
    "expected_results": {
      "federal_tax_owed": [5739.0],
      "state_tax_owed": [2250.0],
      "total_tax_owed": 8000.0
    },
    "tolerance": 0.05,
    "notes": "Based on IRS Publication 17 Example 3"
  }
]
```

## Field Descriptions

- `name`: Unique identifier for the test scenario
- `source`: Reference to the official source (IRS publication, state tax guide, etc.)
- `tax_year`: Tax year (must be in SUPPORTED_TAX_YEARS)
- `filing_status`: Filing status (must be in SUPPORTED_FILING_STATUSES)  
- `state`: State for tax calculation (must be in SUPPORTED_STATES)
- `incomes_adjustments_and_deductions`: Array of income/deduction objects matching the TaxHandler format
- `state_data`: Optional state-specific data (required for some states like California and Georgia for certain years)
- `expected_results`: Expected calculation results from official sources
- `tolerance`: Allowed percentage tolerance for numeric comparisons (default: 0.01 = 1%)
- `notes`: Optional notes about the source or scenario

## Usage

The External Source Test Framework automatically loads and validates scenarios from these data files:

```python
from tests.utils.ExternalSourceTestFramework import ExternalSourceValidator

validator = ExternalSourceValidator('tests/data')
irs_examples = validator.load_official_examples('irs_examples/publication_17_examples.json')

for example in irs_examples:
    is_valid, results = validator.validate_scenario(example)
    print(f"{example['name']}: {'PASS' if is_valid else 'FAIL'}")
```

## Adding New Test Data

1. **IRS Examples**: Add scenarios from IRS publications to `irs_examples/`
2. **State Examples**: Add state-specific scenarios to `state_examples/[state_name]_examples.json`
3. **Bracket Tests**: Add bracket boundary tests to `bracket_validation/[year]_bracket_tests.json`
4. **Custom Tests**: Add specialized test scenarios to `custom/` directory

## Data Sources

Test data should be based on official sources:

- **Federal**: IRS Publications (17, 15, 550), IRS examples and worksheets
- **Georgia**: Georgia Department of Revenue publications and examples
- **California**: California Franchise Tax Board publications and examples
- **Payroll Taxes**: Social Security Administration and Medicare publications

## Validation Process

The framework validates scenarios by:

1. Running the tax calculation using our implementation
2. Comparing results to expected values within specified tolerance
3. Cross-validating using alternative calculation methods where possible
4. Reporting discrepancies for manual review

## Maintenance

- Update data files when tax laws change
- Add new scenarios for edge cases discovered during testing
- Verify expected results against official sources annually
- Remove outdated scenarios for unsupported tax years