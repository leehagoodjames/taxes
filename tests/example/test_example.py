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
            tax_year = 2024,
            filing_status = "Married_Filing_Jointly",
            state = "Georgia",
            incomes_adjustments_and_deductions = [
                {
                    # Income
                    'salaries_and_wages': 274605.63 + 21960,
                    # 'taxable_pensions': 0, # 401k distributions,
                    # 'long_term_capital_gains': 100000,
                    'interest_income': 1020,

                    # Adjustments
                    # 'other_adjustments': 2000,

                    # Deductions
                    'use_standard_deduction': False,
                    'taxes_paid': 5000,
                    'interest_paid': 12499.42 + 543.29,
                    'charitable_contributions': 23639,
                    'capital_gain_or_loss': -1542,
                },
                {
                    # Income
                    'salaries_and_wages': 23611 + 14179,
                    # 'taxable_pensions': 0, # 401k distributions,
                    # 'long_term_capital_gains': 100000,
                    'interest_income': 0,

                    # Adjustments
                    # 'other_adjustments': 2000,

                    # Deductions
                    'use_standard_deduction': False,
                    'taxes_paid': 5000,
                    'interest_paid': 0,
                    'charitable_contributions':516 + (626 + 1250 + 81.76),
                    'capital_gain_or_loss': 0,
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
