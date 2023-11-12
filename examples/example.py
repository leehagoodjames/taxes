# Third Party Imports
from easytax.handler import TaxHandler

# Load in tax brackets for your year and filing-status.
taxHandler = TaxHandler.TaxHandler(
    tax_year = 2022,
    filing_status = "Married_Filling_Jointly",
    state = "Georgia",
    incomes = [
        {
            "salaries_and_wages": 200000,
            "taxable_pensions": 0, # 401k distributions,
            "long_term_capital_gains": 100000,
        }
    ],
    deductions={
        'use_standard_deduction': False,
        'taxes_paid': 10000,
        'interest_paid': 15000,
        'charitable_contributions':20000,
    },
    state_data={
        'exemptions': 2
    },
    )

taxHandler.calculate_taxes()
taxHandler.display_tax_summary()
