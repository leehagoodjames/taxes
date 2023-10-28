# Standard Library Imports
import unittest

# Third Party Imports
from src.easytax.handler import TaxHandler


class TestExample(unittest.TestCase):

    def test_example_success(self):
        # This test should simply not throw errors

        # Load in tax brackets for your year and filing-status.
        taxHandler = TaxHandler.TaxHandler(
            tax_year = 2022, 
            filling_status = "Married_Filling_Jointly", 
            state = "Georgia", 
            incomes = [200000], 
            retirement_incomes=[0],
            long_term_capital_gains = [100000],
        )

        taxHandler.calculate_taxes()
        taxHandler.display_tax_summary()


if __name__ == '__main__':
    unittest.main()
