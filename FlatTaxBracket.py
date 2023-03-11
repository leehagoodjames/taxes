class FlatTaxBracket:


    def __init__(self, tax_rate: float):
        """Create a FlatTaxBracket object.

        Keyword arguments:
        tax_rate -- The flat tax rate
        """
        if tax_rate < 0:
            raise ValueError(f"tax_rate cannot be negative, recieved: {tax_rate}")

        self.rate = tax_rate
        return
