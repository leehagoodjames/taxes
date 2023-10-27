
# Local Imports
from easytax.utils.Logger import logger


# Each handler can have its own AGI / MAGI
class ForceRequiredAttributeDefinitionMeta(type):
    def __call__(cls, *args, **kwargs):
        class_object = type.__call__(cls, *args, **kwargs)
        class_object.check_required_attributes()
        return class_object
    

class RegionalTaxHandlerBase(metaclass=ForceRequiredAttributeDefinitionMeta):

    """
    Base Object for a RegionalTaxHandler, such as a State or Federal Taxes.
    
    Keyword arguments:
    filling_status: str - The type of filling (Married Filling Jointly, Single, etc)
    region: str - The region that you will be filing. TODO: Support case when indivudal splits time across regions.
    incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
    long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
    """

    incomes = None
    long_term_capital_gains = None
    filling_status = None
    income_tax_brackets = None
    long_term_capital_gains_tax_brackets = None
    region = None

    def check_required_attributes(self):
        if self.incomes is None:
            raise TypeError(f"Subclass must define class attribute 'incomes'")
        if self.long_term_capital_gains is None:
            raise TypeError(f"Subclass must define class attribute 'long_term_capital_gains'")
        if self.filling_status is None:
            raise TypeError(f"Subclass must define class attribute 'filling_status'")
        if self.income_tax_brackets is None:
            raise TypeError(f"Subclass must define class attribute 'income_tax_brackets'")
        if self.long_term_capital_gains_tax_brackets is None:
            raise TypeError(f"Subclass must define class attribute 'long_term_capital_gains_tax_brackets'")
        if self.region is None:
            raise TypeError(f"Subclass must define class attribute 'region'")


    def calculate_taxes(self):

        if self.filling_status == "Married_Filling_Jointly":
            self.income_tax_owed = [self.income_tax_brackets.calculate_taxes(sum(self.incomes))]
            self.long_term_capital_gains_tax_owed = [self.long_term_capital_gains_tax_brackets.calculate_taxes(sum(self.long_term_capital_gains))]
        
        elif self.filling_status == "Married_Filling_separately":
            self.income_tax_owed = [self.income_tax_brackets.calculate_taxes(i) for i in self.incomes]
            self.long_term_capital_gains_tax_owed = [self.long_term_capital_gains_tax_brackets.calculate_taxes(i) for i in self.incomes]
        else:
            raise Exception(f"Unexpected filling_status {self.filling_status}")
        return
    

    def display_tax_summary(self):

        try:
            logger.info(f'{self.region} Income Tax owed: {", ".join([f"${i:,.0f}" for i in self.income_tax_owed])}')
            logger.info(f'{self.region} LTCG tax owed: {", ".join([f"${i:,.0f}" for i in self.long_term_capital_gains_tax_owed])}')
        except AttributeError as e:
            raise AttributeError(f"{e}. Ensure you call 'calculate_taxes' before attempting to call this method.")
        return
            