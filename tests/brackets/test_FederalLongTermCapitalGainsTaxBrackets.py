# Standard Library Imports
import unittest

# Local Imports
from src.easytax.brackets.FederalLongTermCapitalGainsTaxBrackets import *


class TestFederalincomeTaxBracket(unittest.TestCase):

    def test_married_filing_jointly_2023_tax(self):
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(100), 0)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(100 * 1000), 1612.5)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(1000 * 1000), 158920)

    def test_married_filing_separately_2023_tax(self):
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(100), 0)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(100 * 1000), 8306.25)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(1000 * 1000), 179461.25)

    def test_married_filing_jointly_2022_tax(self):
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(100), 0)
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(100 * 1000), 2497.5)
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(1000 * 1000), 161637.5)

    def test_married_filing_separately_2022_tax(self):
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(100), 0)
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(100 * 1000), 8748.75)
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(1000 * 1000), 180818.75)



if __name__ == '__main__':
    unittest.main()
