# External Source Verification Framework

This framework provides a robust system for verifying tax calculations against external sources of truth, replacing manually computed test values with dynamically validated calculations.

## Overview

Instead of using hard-coded expected values in tests like `self.assertEqual(tax_owed, [46800])`, this framework:

1. **Queries external sources** (IRS publications, tax APIs, etc.) to get authoritative calculations
2. **Compares** the library's calculations against these external sources
3. **Validates** that results are within acceptable tolerance
4. **Caches** results to avoid repeated API calls and improve test performance
5. **Falls back gracefully** when external sources are unavailable

## Key Benefits

- **Accuracy**: Tests against authoritative sources instead of manual calculations
- **Reliability**: Reduces human error in test value computation
- **Maintainability**: Easy to add new external sources and tax scenarios
- **Performance**: Caching prevents repeated external API calls
- **Robustness**: Graceful fallback when external sources are down
- **Best Practices**: Rate limiting, error handling, and configurable tolerances

## Architecture

### Core Components

1. **`ExternalTaxSource`** - Abstract base class for tax calculation sources
2. **`IRSPublicationSource`** - Implementation using IRS tax tables and publications
3. **`ExternalTaxVerifier`** - Main orchestrator that manages multiple sources
4. **`CacheManager`** - Handles caching of external source results
5. **`ExternalSourceTestCase`** - Helper class for easy test integration

### Current External Sources

- **IRS Publications**: Uses official IRS tax brackets and rates for 2023
  - Federal income tax (married filing jointly/separately)
  - Long-term capital gains tax
  - Social Security and Medicare payroll taxes
  - Georgia state income tax (limited implementation)

## Usage Examples

### Basic Usage with ExternalSourceTestCase

```python
from tests.external_sources.test_helpers import ExternalSourceTestCase

class TestMyTaxHandler(ExternalSourceTestCase):
    def test_tax_calculation(self):
        # Calculate taxes using your handler
        handler = MyTaxHandler(income=100000, filing_status="Married Filing Jointly")
        handler.calculate_taxes()
        
        # Verify against external sources
        self.assertTaxCalculationVerified(
            expected=handler.federal_tax_owed,
            calculation_type='federal_income',
            income=100000,
            filing_status="Married Filing Jointly",
            tax_year=2023
        )
```

### Standalone Verification

```python
from tests.external_sources.test_helpers import verify_tax_calculation

# Simple verification
is_valid = verify_tax_calculation(
    expected=12345.67,
    calculation_type='federal_income',
    income=100000,
    filing_status="Married Filing Jointly",
    tax_year=2023,
    tolerance=10.0  # $10 tolerance
)

# Detailed verification report
from tests.external_sources.test_helpers import get_verification_report

report = get_verification_report(
    expected=12345.67,
    calculation_type='federal_income',
    income=100000,
    filing_status="Married Filing Jointly",
    tax_year=2023
)

print(f"Verified: {report['verified']}")
print(f"Expected: ${report['expected']:,.2f}")
print(f"External source: ${report['calculated']:,.2f}")
print(f"Source: {report['source']}")
```

### Mixed Approach (Gradual Migration)

```python
class TestTaxHandlerMixed(unittest.TestCase):
    def test_with_mixed_verification(self):
        handler = MyTaxHandler()
        handler.calculate_taxes()
        
        # Keep existing assertions for basic validation
        self.assertIsNotNone(handler.federal_tax_owed)
        self.assertGreater(handler.federal_tax_owed[0], 0)
        
        # Add external verification for accuracy
        from tests.external_sources.test_helpers import verify_tax_calculation
        
        if verify_tax_calculation(
            expected=handler.federal_tax_owed[0],
            calculation_type='federal_income',
            # ... other parameters
        ):
            print("External verification passed")
        else:
            print("External verification failed or unavailable")
```

## Supported Calculation Types

### Federal Income Tax
- **Type**: `'federal_income'`
- **Parameters**: `income`, `filing_status`, `tax_year`, `deductions` (optional)
- **Supported**: 2023, Married Filing Jointly/Separately

### State Income Tax  
- **Type**: `'state_income'`
- **Parameters**: `income`, `state`, `filing_status`, `tax_year`, `deductions` (optional)
- **Supported**: Georgia 2023, Married Filing Jointly/Separately

### Long-Term Capital Gains Tax
- **Type**: `'ltcg'`
- **Parameters**: `gains`, `income`, `filing_status`, `tax_year`
- **Supported**: Federal 2023, Married Filing Jointly/Separately

### Payroll Taxes
- **Method**: `assertPayrollTaxesVerified()`
- **Parameters**: `expected_ss`, `expected_medicare`, `wages`, `tax_year`
- **Supported**: 2023 Social Security and Medicare rates

## Adding New External Sources

To add a new external source (e.g., a tax API):

```python
from tests.external_sources.external_tax_verifier import ExternalTaxSource

class MyTaxAPISource(ExternalTaxSource):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.taxcalculator.com"
    
    def calculate_federal_income_tax(self, income, filing_status, tax_year, deductions=0):
        if not self.is_available():
            return None
        
        # Make API call
        response = requests.post(f"{self.base_url}/federal", {
            'income': income,
            'filing_status': filing_status,
            'tax_year': tax_year,
            'deductions': deductions,
            'api_key': self.api_key
        })
        
        if response.status_code == 200:
            return response.json().get('tax_owed')
        return None
    
    def is_available(self):
        # Check if API is reachable
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_source_name(self):
        return "My Tax API"
    
    # Implement other required methods...

# Add to verifier
from tests.external_sources import default_verifier
default_verifier.add_source(MyTaxAPISource(api_key="your-key"))
```

## Configuration

### Cache Settings
- **Location**: `tests/external_sources/.cache/`
- **Duration**: 24 hours
- **Format**: JSON

### Tolerance Settings
- **Default**: $0.01
- **Configurable**: Per test or verification call
- **Recommended**: $1-10 for income taxes, $0.01 for payroll taxes

### Rate Limiting
External sources should implement their own rate limiting. The framework provides:
- Caching to reduce API calls
- Graceful fallback when sources are unavailable
- Configurable timeouts

## Error Handling

The framework handles various error scenarios:

1. **External source unavailable**: Tests skip with informative message
2. **API errors**: Framework tries next available source
3. **Network timeouts**: Graceful fallback to manual assertions
4. **Invalid responses**: Source returns `None`, framework continues
5. **Cache corruption**: Framework rebuilds cache automatically

## Best Practices

### For Test Authors

1. **Start gradual**: Add external verification to new tests first
2. **Keep fallbacks**: Maintain basic assertions for critical validations
3. **Use appropriate tolerances**: $1-10 for income taxes, $0.01 for payroll
4. **Handle skips gracefully**: Tests that skip due to unavailable sources are still valuable

### For Source Implementers

1. **Implement all abstract methods**: Even if returning `None` for unsupported cases
2. **Handle errors gracefully**: Return `None` instead of raising exceptions
3. **Respect rate limits**: Implement appropriate delays and caching
4. **Validate inputs**: Check for supported tax years, filing statuses, etc.
5. **Document limitations**: Clearly specify what scenarios are supported

## Migration Strategy

For existing test suites:

1. **Phase 1**: Add framework alongside existing tests
2. **Phase 2**: Create new test files with external verification (like `test_TaxHandler_with_external_verification.py`)
3. **Phase 3**: Gradually migrate individual test methods
4. **Phase 4**: Replace manual assertions with external verification where appropriate
5. **Phase 5**: Keep critical manual assertions as safety nets

## Troubleshooting

### Tests Skipping
- **Cause**: External sources unavailable or unsupported scenario
- **Solution**: Normal behavior; tests provide fallback validation

### Cache Issues
- **Clear cache**: Delete `tests/external_sources/.cache/`
- **Disable cache**: Create verifier with custom cache manager

### Tolerance Issues
- **Too strict**: Increase tolerance value
- **Too loose**: Decrease tolerance, check calculation accuracy

### Adding Support for New Tax Years
1. Update external sources with new tax brackets
2. Add test cases for the new year
3. Update documentation

## Future Enhancements

Potential additions to the framework:

1. **More External Sources**:
   - Additional state tax calculations
   - Commercial tax APIs (TaxJar, Avalara)
   - Open source tax calculators

2. **Enhanced Features**:
   - Configuration file support
   - Multiple tolerance levels
   - Performance metrics
   - Automated regression detection

3. **Extended Coverage**:
   - More tax years (2022, 2024+)
   - Additional filing statuses
   - Business tax calculations
   - International tax scenarios

The framework is designed to be extensible and can accommodate these future enhancements while maintaining backward compatibility.