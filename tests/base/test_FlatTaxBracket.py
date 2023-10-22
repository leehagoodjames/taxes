# Standard Library Imports
import unittest

# Local Imports
from src.easytax.base import FlatTaxBracket


class TestFlatTaxBracket(unittest.TestCase):

    def test_init_success(self):
        # 50%
        tax_rate = 0.5
        brackets = FlatTaxBracket.FlatTaxBracket(tax_rate = tax_rate)

        self.assertTrue(brackets.rate == tax_rate)

    def test_init_failure_negative_rate(self):
        tax_rate = -0.1 # negative rate

        with self.assertRaises(ValueError) as cm:
            brackets = FlatTaxBracket.FlatTaxBracket(tax_rate = tax_rate)

        expected_message = f"tax_rate cannot be negative, recieved: {tax_rate}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_list_of_rates(self):
        tax_rates = [0.75, 0.5] # one extra rate

        with self.assertRaises(TypeError) as cm:
            brackets = FlatTaxBracket.FlatTaxBracket(tax_rate = tax_rates)


if __name__ == '__main__':
    unittest.main()
