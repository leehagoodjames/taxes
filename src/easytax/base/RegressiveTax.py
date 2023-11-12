# Local Imports
from . import RegressiveTaxBracket

class RegressiveTax:

    def __init__(self, regressive_tax_bracket: RegressiveTaxBracket):
        """Create a RegressiveTax object.

        Keyword arguments:
        regressive_tax_bracket -- RegressiveTaxBracket object
        """
        self.brackets = regressive_tax_bracket
        return

    def calculate_taxes(self, taxable_income):
        """Calculates the taxes for a given Adjusted Gross Income.

        Keyword arguments:
        adjusted_gross_income -- The Adjusted Gross Income
        """

        if taxable_income <= 0:
            return 0

        taxes = 0
        lower_threshold = 0

        # Extract taxes at all but the highest marginal tax rate
        for threshold, marginal_rate in zip(self.brackets.thresholds, self.brackets.rates[:-1]):
            if taxable_income > threshold:
                # take the full tax at this bracket
                marginal_income = threshold - lower_threshold
                taxes += marginal_income * marginal_rate
            else:
                # The is the highest tax bracket for this person
                marginal_income = taxable_income - lower_threshold
                taxes += marginal_income * marginal_rate
                break # exit loop

            # move the lower threshold
            lower_threshold = threshold

        # Extract remaining taxes at highest marginal tax rate
        if taxable_income > self.brackets.thresholds[-1]:
            marginal_income = taxable_income - self.brackets.thresholds[-1]
            marginal_rate = self.brackets.rates[-1]
            taxes +=  marginal_income * marginal_rate

        return taxes
