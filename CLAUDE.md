# Claude Instructions for Taxes Repository

## Project Overview
This repository creates the `easytax` Python module - a lightweight library for calculating personal income taxes. The project has no external dependencies and focuses specifically on personal income tax calculations for federal and various state jurisdictions.

## Project Structure

### Core Components
- **`src/easytax/`** - Main package directory
  - **`base/`** - Core tax calculation classes (FlatTax, ProgressiveTax, RegressiveTax)
  - **`brackets/`** - Tax bracket definitions for federal and state taxes
  - **`credits/`** - Tax credit implementations by jurisdiction
  - **`deductions/`** - Standard deduction definitions
  - **`handler/`** - Tax handler classes that orchestrate calculations
  - **`income/`** - Income processing utilities
  - **`utils/`** - Shared utilities (constants, validation, logging)

### Testing
- **`tests/`** - Comprehensive test suite mirroring the source structure
- All tests must pass with: `python3 -m unittest discover tests`

## Development Workflow

### Testing Requirements
- Always run the full test suite before committing changes
- Use: `python3 -m unittest discover tests`
- All tests must pass before any code changes are accepted

### Code Organization Principles
- Tax calculations are organized by jurisdiction (federal, state-specific)
- Each tax type has its own handler class
- Tax brackets are defined in separate modules for easy maintenance
- Progressive, flat, and regressive tax structures are supported

### Key Classes to Understand
1. **Tax Base Classes** (`base/`):
   - `Tax.py` - Abstract base class for all tax calculations
   - `ProgressiveTax.py` - For income taxes with increasing rates
   - `FlatTax.py` - For flat-rate taxes
   - `RegressiveTax.py` - For regressive tax structures

2. **Tax Handlers** (`handler/`):
   - `TaxHandler.py` - Main orchestrator for tax calculations
   - `FederalTaxHandler.py` - Federal income tax processing
   - State-specific handlers in `states/` subdirectory

3. **Brackets** (`brackets/`):
   - Federal and state tax bracket definitions
   - Long-term capital gains brackets
   - Payroll tax brackets (Medicare, Social Security)

## Installation and Usage
- Install via pip: `python3 -m pip install easytax`
- Run example: `python3 examples/example.py`

## Release Process
1. Update version in `pyproject.toml`
2. Build: `rm -rf dist; python3 -m build`
3. Upload: `python3 -m twine upload --repository pypi dist/*`

## Working with This Codebase
- Focus on personal income tax calculations only
- Maintain the existing organizational structure
- Follow the established patterns for new tax jurisdictions
- Ensure all changes are covered by tests
- No external dependencies should be added without discussion