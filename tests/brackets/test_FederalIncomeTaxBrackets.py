# Standard Library Imports
import unittest

# Local Imports
from src.easytax.brackets.FederalIncomeTaxBrackets import *


class TestFederalincomeTaxBracket(unittest.TestCase):

    def test_married_filing_jointly_2026_tax(self):
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 11530.76)
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(500 * 1000), 112801.1)

    def test_married_filing_separately_2026_tax(self):
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 16765.32)
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(500 * 1000), 145929.07)

    def test_single_2026_tax(self):
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(0), 0)
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(100), 10)
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(100 * 1000), 16765.32)
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(500 * 1000), 143665.43)

    def test_married_filing_jointly_2025_tax(self):
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 11827.0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(500 * 1000), 114128.0)

    def test_married_filing_separately_2025_tax(self):
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 10)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 16913.5)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(500 * 1000), 147032.25)

    def test_single_2025_tax(self):
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(100), 10)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(100 * 1000), 16913.5)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(500 * 1000), 144548.25)

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


if __name__ == '__main__':
    unittest.main()
