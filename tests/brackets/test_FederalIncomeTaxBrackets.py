# Standard Library Imports
import unittest

# Local Imports
from src.easytax.brackets.FederalIncomeTaxBrackets import *


class TestFederalincomeTaxBracket(unittest.TestCase):

    def test_married_filing_jointly_2023_tax(self):
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(100), 10)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(100 * 1000), 12615)
        self.assertEqual(married_filing_jointly_2023_tax.calculate_taxes(500 * 1000), 118789)

    def test_married_filing_separately_2023_tax(self):
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(100), 10)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(100 * 1000), 17400)
        self.assertEqual(married_filing_separately_2023_tax.calculate_taxes(500 * 1000), 149957)
        
    def test_married_filing_jointly_2022_tax(self):
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(100), 10)
        self.assertEqual(married_filing_jointly_2022_tax.calculate_taxes(100 * 1000), 13234)

    def test_married_filing_separately_2022_tax(self):
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(-100), 0)
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(0), 0)
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(100), 10)
        self.assertEqual(married_filing_separately_2022_tax.calculate_taxes(100 * 1000), 17835.5)


if __name__ == '__main__':
    unittest.main()
