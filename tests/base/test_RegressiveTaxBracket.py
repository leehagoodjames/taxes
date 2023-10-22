# Standard Library Imports
import unittest

# Local Imports
from src.easytax.base import RegressiveTax
from src.easytax.base import RegressiveTaxBracket


class TestRegressiveTaxBracket(unittest.TestCase):

    def test_init_success(self):
        # 50% for first $10, 25% for $10-$50, and 10% for > $50
        tax_rates = [0.5, 0.25, 0.1]
        income_thresholds = [10, 50]
        brackets = RegressiveTaxBracket.RegressiveTaxBracket(
            tax_rates = tax_rates,
            income_thresholds = income_thresholds)

        self.assertTrue(brackets.rates == tax_rates)
        self.assertTrue(brackets.thresholds == income_thresholds)

    def test_init_failure_negative_rate(self):
        tax_rates = [0.5, 0.25, -0.1] # negative rate
        income_thresholds = [10, 50]

        with self.assertRaises(ValueError) as cm:
            brackets = RegressiveTaxBracket.RegressiveTaxBracket(
                tax_rates = tax_rates,
                income_thresholds = income_thresholds)

        expected_message = f"tax_rates cannot be negative, recieved: {tax_rates[-1]}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_negative_threshold(self):
        tax_rates = [0.5, 0.25, 0.1]
        income_thresholds = [-10, 50] # negative threshold

        with self.assertRaises(ValueError) as cm:
            brackets = RegressiveTaxBracket.RegressiveTaxBracket(
                tax_rates = tax_rates,
                income_thresholds = income_thresholds)

        expected_message = f"income_thresholds cannot be negative, recieved: {income_thresholds[0]}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_too_many_rates(self):
        tax_rates = [0.75, 0.5, 0.25, 0.1] # one extra rate
        income_thresholds = [10, 50]

        with self.assertRaises(ValueError) as cm:
            brackets = RegressiveTaxBracket.RegressiveTaxBracket(
                tax_rates = tax_rates,
                income_thresholds = income_thresholds)

        expected_message = f"Recieved {len(tax_rates)} but expected {len(income_thresholds) + 1} tax_rates for the following income_thresholds {income_thresholds}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_too_many_thresholds(self):
        tax_rates = [0.5, 0.25, 0.1]
        income_thresholds = [10, 50, 75] # one extra threshold

        with self.assertRaises(ValueError) as cm:
            brackets = RegressiveTaxBracket.RegressiveTaxBracket(
                tax_rates = tax_rates,
                income_thresholds = income_thresholds)

        expected_message = f"Recieved {len(tax_rates)} but expected {len(income_thresholds) + 1} tax_rates for the following income_thresholds {income_thresholds}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_unordered_rates(self):
        tax_rates = [0.1, 0.5, 0.25] # incorrect order
        income_thresholds = [10, 50]

        with self.assertRaises(ValueError) as cm:
            brackets = RegressiveTaxBracket.RegressiveTaxBracket(
                tax_rates = tax_rates,
                income_thresholds = income_thresholds)

        expected_message = f"Tax rates must be monotonically descreasing to be regressive. Recieved: {tax_rates}."
        self.assertEqual(str(cm.exception), expected_message)

    def test_init_failure_unordered_thresholds(self):
        tax_rates = [0.5, 0.25, 0.1]
        income_thresholds = [50, 10] # incorrect order

        with self.assertRaises(ValueError) as cm:
            brackets = RegressiveTaxBracket.RegressiveTaxBracket(
                tax_rates = tax_rates,
                income_thresholds = income_thresholds)

        expected_message = f"Income thresholds must be monotonically increasing to be regressive. Recieved: {income_thresholds}."
        self.assertEqual(str(cm.exception), expected_message)

if __name__ == '__main__':
    unittest.main()
