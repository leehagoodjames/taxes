# Standard Library Imports
import unittest

# Local Imports
from src.easytax.brackets.FederalLongTermCapitalGainsTaxBrackets import *


class TestFederalincomeTaxBracket(unittest.TestCase):

    def test_married_filing_jointly_2026_tax(self):
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(100), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 79.05)
        self.assertAlmostEqual(brackets[2026][MARRIED_FILING_JOINTLY].calculate_taxes(1000 * 1000), 154206.1, places=1)

    def test_married_filing_separately_2026_tax(self):
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 0)
        self.assertAlmostEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 7539.6, places=1)
        self.assertAlmostEqual(brackets[2026][MARRIED_FILING_SEPARATELY].calculate_taxes(1000 * 1000), 177103.15, places=1)

    def test_single_2026_tax(self):
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(0), 0)
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(100), 0)
        self.assertAlmostEqual(brackets[2026][SINGLE].calculate_taxes(100 * 1000), 7539.6, places=1)
        self.assertEqual(brackets[2026][SINGLE].calculate_taxes(1000 * 1000), 165077.75)

    def test_married_filing_jointly_2025_tax(self):
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(100 * 1000), 495.0)
        self.assertEqual(brackets[2025][MARRIED_FILING_JOINTLY].calculate_taxes(1000 * 1000), 155492.5)

    def test_married_filing_separately_2025_tax(self):
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(100), 0)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(100 * 1000), 7747.5)
        self.assertEqual(brackets[2025][MARRIED_FILING_SEPARATELY].calculate_taxes(1000 * 1000), 177746.25)

    def test_single_2025_tax(self):
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(-100), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(0), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(100), 0)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(100 * 1000), 7747.5)
        self.assertEqual(brackets[2025][SINGLE].calculate_taxes(1000 * 1000), 166077.5)

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
