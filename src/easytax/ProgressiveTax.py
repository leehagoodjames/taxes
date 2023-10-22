# Local Imports
from . import ProgressiveTaxBracket

class ProgressiveTax:


    def __init__(self, progressive_tax_bracket: ProgressiveTaxBracket):
        """Create a ProgressiveTax object.

        Keyword arguments:
        progressive_tax_bracket -- ProgressiveTaxBracket object
        """
        self.brackets = progressive_tax_bracket
        return

    def calculate_taxes(self, adjusted_gross_income):
        """Calculates the taxes for a given Adjusted Gross Income.

        Keyword arguments:
        adjusted_gross_income -- The Adjusted Gross Income
        """

        if adjusted_gross_income <= 0:
            return 0

        taxes = 0
        lower_threshold = 0

        # Extract taxes at all but the highest marginal tax rate
        for threshold, marginal_rate in zip(self.brackets.thresholds, self.brackets.rates[:-1]):
            if adjusted_gross_income > threshold:
                # take the full tax at this bracket
                marginal_income = threshold - lower_threshold
                taxes += marginal_income * marginal_rate
            else:
                # The is the highest tax bracket for this person
                marginal_income = adjusted_gross_income - lower_threshold
                taxes += marginal_income * marginal_rate
                break # exit loop

            # move the lower threshold
            lower_threshold = threshold

        # Extract remaining taxes at highest marginal tax rate
        if adjusted_gross_income > self.brackets.thresholds[-1]:
            marginal_income = adjusted_gross_income - self.brackets.thresholds[-1]
            marginal_rate = self.brackets.rates[-1]
            taxes +=  marginal_income * marginal_rate

        return taxes
