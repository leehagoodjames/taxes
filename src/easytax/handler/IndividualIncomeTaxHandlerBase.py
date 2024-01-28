
# Local Imports
from ..utils.Logger import logger


# Each handler can have its own AGI / MAGI
class ForceRequiredAttributeDefinitionMeta(type):
    def __call__(cls, *args, **kwargs):
        class_object = type.__call__(cls, *args, **kwargs)
        class_object.check_required_attributes()
        return class_object
    

class IndividualIncomeTaxHandlerBase(metaclass=ForceRequiredAttributeDefinitionMeta):

    """
    Base object for an IndividualIncomeTax Handler, for taxes applied at the individual level, like Social Security and Medicare.

    Keyword arguments:
    tax_year: int - The year for tax filling. 
    incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
    """

    taxable_incomes = None
    income_tax_brackets = None
    tax_name = None

    def check_required_attributes(self):
        if self.taxable_incomes is None:
            raise TypeError(f"Subclass must define class attribute 'incomes'")
        if self.income_tax_brackets is None:
            raise TypeError(f"Subclass must define class attribute 'income_tax_brackets'")
        if self.tax_name is None:
                    raise TypeError(f"Subclass must define class attribute 'tax_name'")


    def calculate_taxes(self):
        self.income_tax_owed = [self.income_tax_brackets.calculate_taxes(i) for i in self.taxable_incomes]
        return
    

    def display_tax_summary(self):

        try:            
            logger.info(f'{self.tax_name} Tax Summary')
            logger.info(f'{self.tax_name} Modified Adjusted Gross Incomes: {", ".join([f"${i:,.0f}" for i in self.taxable_incomes])}')
            logger.info(f'{self.tax_name} Income Tax owed: {", ".join([f"${i:,.0f}" for i in self.income_tax_owed])}\n')
        except AttributeError as e:
            raise AttributeError(f"{e}. Ensure you call 'calculate_taxes' before attempting to call this method.")
        return


    def summary_json(self):

        try:
            return {
                    'taxable_incomes': self.taxable_incomes,
                    'income_tax_owed': self.income_tax_owed,
                }
        except AttributeError as e:
            raise AttributeError(f"{e}. Ensure you call 'calculate_taxes' before attempting to call this method.")
