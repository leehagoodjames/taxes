# Standard Library Imports
import unittest

# Local Imports
from src.easytax.brackets.FederalLongTermCapitalGainsTaxBrackets import *


class TestFederalincomeTaxBracket(unittest.TestCase):

    def test_2025_ltcg_correctness(self):
        """Verify 2025 LTCG brackets per NerdWallet/IRS."""
        # Single: 0% to $48,350, 15% to $533,400, 20% above
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(48350), 0)
        # $50,000: 15% on $1,650 = $247.50
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(50000), 247.5)
        # MFJ: 0% to $96,700, 15% to $600,050
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(96700), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(100000), 495)

    def test_married_filing_jointly_2023_tax(self):
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(100), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 1612.5)
        self.assertEqual(brackets[2023][MARRIED_FILING_JOINTLY].calculate_taxes(1000 * 1000), 158920)

    def test_married_filing_separately_2023_tax(self):
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 0)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 8306.25)
        self.assertEqual(brackets[2023][MARRIED_FILING_SEPARATELY].calculate_taxes(1000 * 1000), 179461.25)

    def test_married_filing_jointly_2022_tax(self):
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(100), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 2497.5)
        self.assertEqual(brackets[2022][MARRIED_FILING_JOINTLY].calculate_taxes(1000 * 1000), 161637.5)

    def test_married_filing_separately_2022_tax(self):
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 0)
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 8748.75)
        self.assertEqual(brackets[2022][MARRIED_FILING_SEPARATELY].calculate_taxes(1000 * 1000), 180818.75)

if __name__ == '__main__':
    unittest.main()
