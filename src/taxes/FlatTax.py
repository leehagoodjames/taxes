# Local Imports
from taxes import FlatTaxBracket

class FlatTax:

    def __init__(self, flat_tax_bracket: FlatTaxBracket):
        """Create a FlatTax object.

        Keyword arguments:
        flat_tax_bracket -- The FlatTaxBracket
        """
        self.rate = flat_tax_bracket.rate
        return

    def calculate_taxes(self, adjusted_gross_income):
        """Calculates the taxes for a given Adjusted Gross Income.

        Keyword arguments:
        adjusted_gross_income -- The Adjusted Gross Income
        """
        if adjusted_gross_income <= 0:
            return 0

        return adjusted_gross_income * self.rate
