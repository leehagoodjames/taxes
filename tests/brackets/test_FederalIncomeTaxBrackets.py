# Standard Library Imports
import unittest

# Local Imports
from src.easytax.brackets.FederalIncomeTaxBrackets import *


class TestFederalincomeTaxBracket(unittest.TestCase):

    def test_2025_single_tax_correctness(self):
        """Verify 2025 Single brackets per NerdWallet/IRS."""
        # $50,000: 10% on $11,925 + 12% on $36,550 + 22% on $1,525 = $1,192.50 + $4,386 + $335.50 = $5,914
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(11925), 1192.5)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(50000), 5914)

    def test_2025_married_filing_jointly_tax_correctness(self):
        """Verify 2025 MFJ brackets per NerdWallet/IRS."""
        # $250,000: 10% + 12% + 22% + 24% on remainder
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(23850), 2385)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(250000), 45694)

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
