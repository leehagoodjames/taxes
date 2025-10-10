# Standard Library Imports
import unittest

# Local Imports
from src.easytax.brackets.FederalIncomeTaxBrackets import *


class TestFederalincomeTaxBracket(unittest.TestCase):

    def test_married_filing_jointly_2023_tax(self):
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 12615)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(500 * 1000), 118789)

    def test_married_filing_separately_2023_tax(self):
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 17400)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(500 * 1000), 149957)
        
    def test_married_filing_jointly_2022_tax(self):
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 13234)

    def test_married_filing_separately_2022_tax(self):
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 17835.5)

    def test_married_filing_jointly_2025_tax(self):
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(100), 10)
        # Basic calculation test for 2025 brackets
        tax_100k = brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000)
        self.assertGreater(tax_100k, 0)  # Should have some tax liability
        self.assertLess(tax_100k, 100000)  # Should be less than income

    def test_married_filing_separately_2025_tax(self):
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 10)
        # Basic calculation test for 2025 brackets
        tax_100k = brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000)
        self.assertGreater(tax_100k, 0)  # Should have some tax liability
        self.assertLess(tax_100k, 100000)  # Should be less than income

    def test_single_2025_tax(self):
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(100), 10)
        # Basic calculation test for 2025 brackets
        tax_100k = brackets[2025][SINGLE].calculate_taxes(100 * 1000)
        self.assertGreater(tax_100k, 0)  # Should have some tax liability
        self.assertLess(tax_100k, 100000)  # Should be less than income


if __name__ == '__main__':
    unittest.main()
