# Standard Library Imports
import unittest

# Local Imports
from src.easytax.base import RegressiveTax
from src.easytax.base import RegressiveTaxBracket


class TestRegressiveTax(unittest.TestCase):

    # 10% for first $10, 25% for $10-$50, and 50% for > $50
    tax_rates = [0.5, 0.25, 0.0]
    income_thresholds = [10, 50]

    brackets = RegressiveTaxBracket.RegressiveTaxBracket(
        tax_rates = tax_rates,
        income_thresholds = income_thresholds)

    pt = RegressiveTax.RegressiveTax(brackets)

    def test_negative_income(self):
        self.assertTrue(self.pt.calculate_taxes(-5) == 0)

    def test_lowest_bracket(self):
        # 50% of 5 -> 2.5
        self.assertTrue(self.pt.calculate_taxes(5) == 2.5)

    def test_second_highest_bracket(self):
        # (10*0.5) + (20*0.25) -> 5 + 5 -> 10
        self.assertTrue(self.pt.calculate_taxes(30) == 10)

    def test_highest_bracket(self):
        # (10*0.5) + (40*0.25) + (50*0)-> 5 + 10 -> 15
        self.assertTrue(self.pt.calculate_taxes(100) == 15)

if __name__ == '__main__':
    unittest.main()
