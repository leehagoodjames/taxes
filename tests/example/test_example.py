# Standard Library Imports
import unittest
import json

# Third Party Imports
from src.easytax.handler import TaxHandler


class TestExample(unittest.TestCase):

    def test_example_success(self):
        # This test should simply not throw errors

        # Load in tax brackets for your year and filing-status.
        taxHandler = TaxHandler.TaxHandler(
            tax_year = 2022,
            filing_status = "Married_Filing_Jointly",
            state = "Georgia",
            incomes_adjustments_and_deductions = [
                {
                    # Income
                    'salaries_and_wages': 200000,
                    'taxable_pensions': 0, # 401k distributions,
                    'long_term_capital_gains': 100000,

                    # Adjustments
                    'other_adjustments': 2000,

                    # Deductions
                    'use_standard_deduction': False,
                    'taxes_paid': 10000,
                    'interest_paid': 15000,
                    'charitable_contributions':20000,
                }
            ],
            state_data={
                'exemptions': 2
            },
        )

        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()
        print(json.dumps(taxHandler.summary_json(), indent=4))


if __name__ == '__main__':
    unittest.main()
