from abc import ABC, abstractmethod


class Tax(ABC):

    @abstractmethod
    def calculate_taxes(self, taxable_income):
        """Calculates the taxes for a given taxable income.

        Keyword arguments:
        taxable_income -- The taxable income
        """
        pass
