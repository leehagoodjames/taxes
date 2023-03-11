class ProgressiveTaxBracket:


    def __init__(self, tax_rates: list[float], income_thresholds: list[float]):
        """Create a ProgressiveTaxBracket object.

        Keyword arguments:
        tax_rates -- ASC ordered list of tax rates
        income_thresholds -- ASC ordered list of income bracket-thresholds
        """
        if len(tax_rates) != len(income_thresholds) + 1:
            raise ValueError(f"Recieved {len(tax_rates)} but expected {len(income_thresholds) + 1} tax_rates for the following income_thresholds {income_thresholds}")

        if sorted(income_thresholds) != income_thresholds:
            raise ValueError(f"Income thresholds must be monotonically increasing to be progressive. Recieved: {income_thresholds}.")

        if sorted(tax_rates) != tax_rates:
            raise ValueError(f"Tax rates must be monotonically increasing to be progressive. Recieved: {tax_rates}.")

        if income_thresholds[0] < 0 :
            raise ValueError(f"income_thresholds cannot be negative, recieved: {income_thresholds[0]}")

        if tax_rates[0] < 0 :
            raise ValueError(f"tax_rates cannot be negative, recieved: {tax_rates[0]}")

        self.rates = tax_rates
        self.thresholds = income_thresholds
        return
