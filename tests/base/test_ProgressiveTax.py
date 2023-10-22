# Standard Library Imports
import unittest

# Local Imports
from src.easytax.base import ProgressiveTax
from src.easytax.base import ProgressiveTaxBracket


class TestProgressiveTax(unittest.TestCase):

    # 10% for first $10, 25% for $10-$50, and 50% for > $50
    tax_rates = [0.1, 0.25, 0.5]
    income_thresholds = [10, 50]

    brackets = ProgressiveTaxBracket.ProgressiveTaxBracket(
        tax_rates = tax_rates,
        income_thresholds = income_thresholds)

    pt = ProgressiveTax.ProgressiveTax(brackets)

    def test_negative_income(self):
        self.assertTrue(self.pt.calculate_taxes(-5) == 0)

    def test_lowest_bracket(self):
        # 10% of 5 -> 0.5
        self.assertTrue(self.pt.calculate_taxes(5) == 0.5)

    def test_second_highest_bracket(self):
        # (10*0.1) + (20*0.25) -> 1 + 5 -> 6
        self.assertTrue(self.pt.calculate_taxes(30) == 6)

    def test_highest_bracket(self):
        # (10*0.1) + (40*0.25) + (50*50)-> 1 + 10 + 25 -> 36
        self.assertTrue(self.pt.calculate_taxes(100) == 36)

if __name__ == '__main__':
    unittest.main()
