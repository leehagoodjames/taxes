# Claude Instructions for EasyTax Repository

## Project Overview

**EasyTax** is a lightweight Python library for calculating personal income taxes in the United States. The project focuses specifically on personal income tax calculations for federal and various state jurisdictions, with **no external dependencies**.

- **Package Name**: `easytax`
- **Current Version**: 0.0.20
- **License**: MIT
- **Published**: PyPI
- **Python Version**: >=3.3
- **Installation**: `python3 -m pip install easytax`

## Architecture

### Design Patterns

The project uses a **Strategy Pattern** for tax calculations with three core tax types:

1. **ProgressiveTax** (`base/ProgressiveTax.py`): Graduated tax brackets (federal income, most state income taxes)
2. **FlatTax** (`base/FlatTax.py`): Single-rate taxes (some state taxes, Medicare)
3. **RegressiveTax** (`base/RegressiveTax.py`): Taxes that decrease at higher incomes (Social Security with wage cap)

Each tax type has a corresponding bracket class that stores the rates and thresholds. All inherit from the abstract `Tax` base class (`base/Tax.py`).

### Project Structure

```
src/easytax/
├── base/              # Core tax calculation classes (FlatTax, ProgressiveTax, RegressiveTax)
├── handler/           # Tax handler classes that orchestrate calculations
│   └── states/        # State-specific tax handlers
├── brackets/          # Tax bracket definitions for federal and state taxes
│   └── states/        # State-specific bracket definitions
├── income/            # Income processing utilities (FederalIncomeHandler, PayrollTaxIncomeHandler)
├── deductions/        # Standard deduction definitions
│   └── states/        # State-specific deduction definitions
├── credits/           # Tax credit implementations by jurisdiction
│   └── states/        # State-specific credit implementations
└── utils/             # Shared utilities (constants, validation, logging)

tests/                 # Comprehensive test suite mirroring source structure
examples/              # Usage examples
```

### Key Classes to Understand

**Tax Base Classes** (`base/`):
- `Tax.py` - Abstract base class for all tax calculations
- `ProgressiveTax.py` - For income taxes with increasing rates
- `FlatTax.py` - For flat-rate taxes
- `RegressiveTax.py` - For regressive tax structures

**Tax Handlers** (`handler/`):
- `TaxHandler.py` - Main orchestrator for all tax calculations
  - Creates income handlers for each person in the household
  - Instantiates federal, state, and payroll tax handlers
  - Calculates all taxes and aggregates them
  - Provides display and JSON output methods
- `FederalTaxHandler.py` - Federal income tax processing
- State-specific handlers in `states/` subdirectory

**Tax Brackets** (`brackets/`):
- Federal and state tax bracket definitions
- Long-term capital gains brackets
- Payroll tax brackets (Medicare, Social Security)
- Tax calculations are organized by jurisdiction (federal, state-specific)
- Brackets are defined in separate modules for easy maintenance

## Supported Features

### Tax Years
- 2022, 2023, 2024
- **Constant**: `SUPPORTED_TAX_YEARS` in `src/easytax/utils/Constants.py`

### Filing Statuses
- `Married_Filing_Jointly`
- `Married_Filing_Separately`
- `Single`
- **Constant**: `SUPPORTED_FILING_STATUSES`

### States
- **Full Support**: Georgia, California
- **No Income Tax**: Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Wyoming
- **Constant**: `SUPPORTED_STATES`, `STATES_WITHOUT_INCOME_TAX`

## Development Guidelines

### Core Principles

- **No External Dependencies**: The project has zero external dependencies - keep it that way
- **Focus on Personal Income Tax**: Only personal income tax calculations - no business or corporate tax features
- **Follow Established Patterns**: Maintain the existing organizational structure when adding features
- **Comprehensive Testing**: All changes must be covered by tests and all tests must pass
- **Official Sources**: Tax brackets must come from official IRS/state sources (document in comments)

### Adding a New State

1. **Create State Handler** in `src/easytax/handler/states/`:
   - Extend `RegionalTaxHandlerBase`
   - Define how the state treats income and capital gains
   - Handle state-specific deductions, exemptions, and credits

2. **Create Tax Brackets** in `src/easytax/brackets/states/`:
   - Create `[State]StateIncomeTaxBrackets.py`
   - Create `[State]StateLongTermCapitalGainsTaxBrackets.py`
   - Use `ProgressiveTax`, `FlatTax`, or `RegressiveTax` as appropriate

3. **Add Deductions** (if applicable) in `src/easytax/deductions/states/`:
   - Create `[State]StandardDeductions.py`

4. **Add Credits** (if applicable) in `src/easytax/credits/states/`:
   - Create `[State]StateTaxCredits.py`

5. **Update TaxHandler** in `src/easytax/handler/TaxHandler.py`:
   - Import the new state handler
   - Add state to the if/elif chain in `__init__`

6. **Update Constants** in `src/easytax/utils/Constants.py`:
   - Add state to `SUPPORTED_STATES` set

7. **Write Tests** in `tests/handler/states/`:
   - Create `test_[State]TaxHandler.py`
   - Test various income scenarios and edge cases

### Adding a New Tax Year

1. **Update Federal Brackets**:
   - `src/easytax/brackets/FederalIncomeTaxBrackets.py`
   - `src/easytax/brackets/FederalLongTermCapitalGainsTaxBrackets.py`
   - Add new year dictionary with brackets for all filing statuses

2. **Update State Brackets** for each supported state

3. **Update Standard Deductions**:
   - `src/easytax/deductions/FederalStandardDeductions.py`
   - State-specific deduction files

4. **Update FederalIncomeHandler** in `src/easytax/income/FederalIncomeHandler.py`:
   - Add year-specific logic in the standard deduction section

5. **Update Constants**:
   - Add year to `SUPPORTED_TAX_YEARS`

6. **Write Tests** for the new year

### Code Conventions

- **Import Order**: Standard library → Third party → Local imports
- **Type Hints**: Use type hints for function parameters (e.g., `filing_status: str`, `state_data: dict | None`)
- **Docstrings**: Include docstrings for all classes and public methods
- **Validation**: Use `InputValidator` for all user inputs
- **Error Messages**: Provide clear error messages with context about what was received and what was expected

### Important Implementation Details

1. **Married Filing Jointly with Two Earners**:
   - `TaxHandler.make_federal_income_handlers()` combines two incomes
   - Fields like `dependents` and `use_standard_deduction` must match
   - Other fields are summed

2. **State-Specific Income Treatment**:
   - Georgia: Treats LTCG as ordinary income (no separate LTCG tax)
   - California: Treats LTCG as ordinary income + has tax credits
   - Check how each state handles income before implementing

3. **Georgia Exemptions**:
   - Personal exemption of $3,700 per person was removed in 2024
   - For years < 2024, require `state_data` with `exemptions` field

4. **California Requirements**:
   - Requires `state_data` parameter (cannot be None)
   - Has standard deductions and tax credit system

5. **NIIT (Net Investment Income Tax)**:
   - 3.8% tax on investment income above threshold
   - Calculated in `NetInvestmentIncomeTaxHandler`
   - Threshold varies by filing status

## Testing

### Testing Requirements - CRITICAL

**Always run the full test suite before committing any changes.**

```bash
python3 -m unittest discover tests
```

All tests MUST pass before any code changes are accepted. No exceptions.

### Running Tests

```bash
# Run all tests (required before any commit)
python3 -m unittest discover tests

# Run specific test module
python3 -m unittest tests.handler.test_FederalTaxHandler

# Run specific test class
python3 -m unittest tests.handler.test_FederalTaxHandler.TestFederalTaxHandler
```

### Test Structure

The test suite comprehensively mirrors the source structure:
- `tests/base/`: Test core tax calculation logic
- `tests/brackets/`: Test tax bracket data and calculations
- `tests/handler/`: Test tax handlers (federal, state, payroll)
- `tests/income/`: Test income processing
- `tests/example/`: Integration test using example.py

### Test Requirements Checklist

**Before any commit or PR**:
- ✅ ALL tests must pass
- ✅ Add tests for new features
- ✅ Test edge cases (zero income, negative adjustments, etc.)
- ✅ Test all supported filing statuses for the feature
- ✅ Test all supported years for the feature

## Release Process

1. **Increment Version** in `pyproject.toml`:
   ```toml
   version = "0.0.21"  # Update this
   ```

2. **Build Package**:
   ```bash
   rm -rf dist
   python3 -m build
   ```

3. **Upload to PyPI**:
   ```bash
   python3 -m twine upload --repository pypi dist/*
   ```

## Installation and Usage

### Installation
```bash
python3 -m pip install easytax
```

### Example Usage

Run the included example: `python3 examples/example.py`

Or use in your own code:

```python
from easytax.handler import TaxHandler

handler = TaxHandler.TaxHandler(
    tax_year=2024,
    filing_status='Married_Filing_Jointly',
    state='Georgia',
    incomes_adjustments_and_deductions=[{
        'salaries_and_wages': 200000,
        'long_term_capital_gains': 100000,
        'other_adjustments': 2000,
        'use_standard_deduction': False,
        'taxes_paid': 10000,
        'interest_paid': 15000,
        'charitable_contributions': 20000,
    }]
)

handler.calculate_taxes()
handler.display_tax_summary()
print(handler.summary_json())
```

See `examples/example.py` for a complete working example.

## GitHub Actions Integration

This project uses Claude Code Action for automated PR assistance:
- Trigger by mentioning `@claude` in issues, PRs, or comments
- Action runs tests and creates PRs when requested
- Custom instructions ensure tests pass before proceeding
- See `.github/workflows/claude.yml` for configuration

## Important Files

- **pyproject.toml**: Package configuration and version
- **src/easytax/utils/Constants.py**: All supported years, states, filing statuses
- **src/easytax/handler/TaxHandler.py**: Main entry point
- **src/easytax/income/FederalIncomeHandler.py**: Comprehensive income processing with AGI, deductions, taxable income
- **examples/example.py**: Working example of library usage

## Common Tasks

### Adding Support for a New Income Type

1. Add parameter to `FederalIncomeHandler.__init__()` with default value of 0
2. Add to appropriate income list (`income_sources` or special handling)
3. Update `from_dict()` classmethod with the new field
4. Update `__eq__()` and `__str__()` methods
5. Add tests

### Debugging Tax Calculations

- Use `display_tax_summary()` to see breakdown of all taxes
- Check `FederalIncomeHandler` calculated values: `total_income`, `adjusted_gross_income`, `taxable_income`
- Verify bracket selection in respective bracket files
- Check if state treats LTCG differently

## Key Considerations and Project Scope

### What This Project Is
- **Personal Income Tax Calculator**: Focus on individual/household W2 income and long-term investments
- **Lightweight Library**: Zero external dependencies - keep it that way
- **Educational and Personal Use**: For understanding and estimating personal tax liability
- **Well-Tested**: Comprehensive test coverage for all calculations

### What This Project Is NOT
- **Not Tax Advice**: Always verify calculations with official tax software
- **Not for Business Taxes**: No corporate, partnership, or business entity calculations
- **Not Fully Comprehensive**: Doesn't handle every edge case or complex tax situation
- **Not a Substitute for Professional Help**: Complex tax situations require professional tax advisors

### Important Notes
- **Data Sources**: Tax brackets come from official IRS/state sources (see comments in bracket files)
- **State Complexity**: Each state has unique rules; research thoroughly before implementation
- **Currency**: All values are in USD, represented as floats or ints
- **No External Dependencies**: Do not add external dependencies without discussion

## Questions or Issues?

- GitHub Issues: https://github.com/leehagoodjames/taxes/issues
- Maintainer: Lee James (leehagoodjames@gmail.com)
