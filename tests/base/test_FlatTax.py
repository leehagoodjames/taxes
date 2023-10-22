# Standard Library Imports
import unittest

# Local Imports
from src.easytax.base import FlatTax
from src.easytax.base import FlatTaxBracket


class TestFlatTax(unittest.TestCase):

    # 50%
    tax_rate = 0.5

    brackets = FlatTaxBracket.FlatTaxBracket(tax_rate = tax_rate)

    pt = FlatTax.FlatTax(brackets)

    def test_negative_income(self):
        self.assertTrue(self.pt.calculate_taxes(-5) == 0)

    def test_flat_bracket(self):
        # 50% of 5 -> 2.5
        self.assertTrue(self.pt.calculate_taxes(5) == 2.5)

if __name__ == '__main__':
    unittest.main()
