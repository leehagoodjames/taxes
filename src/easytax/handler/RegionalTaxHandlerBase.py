
# Local Imports
from ..utils.Logger import logger
from ..utils.Constants import *


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
    filing_status: str - The type of filling (Married Filing Jointly, Single, etc)
    region: str - The region that you will be filing. TODO: Support case when indivudal splits time across regions.
    taxable_incomess: list[float] - List of the taxable incomse for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
    long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
    """

    taxable_incomes = None
    long_term_capital_gains = None
    filing_status = None
    income_tax_brackets = None
    long_term_capital_gains_tax_brackets = None
    region = None

    def check_required_attributes(self):
        if self.taxable_incomes is None:
            raise TypeError(f"Subclass must define class attribute 'taxable_incomes'")
        if self.long_term_capital_gains is None:
            raise TypeError(f"Subclass must define class attribute 'long_term_capital_gains'")
        if self.filing_status is None:
            raise TypeError(f"Subclass must define class attribute 'filing_status'")
        if self.income_tax_brackets is None:
            raise TypeError(f"Subclass must define class attribute 'income_tax_brackets'")
        if self.long_term_capital_gains_tax_brackets is None:
            raise TypeError(f"Subclass must define class attribute 'long_term_capital_gains_tax_brackets'")
        if self.region is None:
            raise TypeError(f"Subclass must define class attribute 'region'")
        if len(self.taxable_incomes) != len(self.long_term_capital_gains):
            raise ValueError(f"Subclass cannot have '{len(self.taxable_incomes)}' taxable_incomes and '{len(self.long_term_capital_gains)}' long_term_capital_gains. Number of people reporting each must be equal")


    def calculate_taxes(self):
        if self.filing_status == MARRIED_FILING_JOINTLY and len(self.taxable_incomes) != 1:
            raise ValueError(f"Unsupported number of incomes for MARRIED_FILING_JOINTLY. Got '{len(self.taxable_incomes)}', expected: '1'")
        elif self.filing_status == MARRIED_FILING_JOINTLY and len(self.long_term_capital_gains) != 1:
            raise ValueError(f"Unsupported number of long_term_capital_gains for MARRIED_FILING_JOINTLY. Got '{len(self.long_term_capital_gains)}', expected: '1'")        
        elif self.filing_status in {MARRIED_FILING_JOINTLY, MARRIED_FILING_SEPARATELY}:
            self.income_tax_owed = []
            self.long_term_capital_gains_tax_owed = []
            for i, ltcg in zip(self.taxable_incomes, self.long_term_capital_gains):
                self.income_tax_owed.append(self.income_tax_brackets.calculate_taxes(i))
                # LTCG's tax brackets include the addition of taxable income plus long term capital gains.
                # Income is only used to offset the tax brackets used for computing LTCG. This is achieved
                # by introducing a "basis".
                ltcg_basis = self.long_term_capital_gains_tax_brackets.calculate_taxes(i)
                ltcg_tax = self.long_term_capital_gains_tax_brackets.calculate_taxes(i + ltcg)
                self.long_term_capital_gains_tax_owed.append(ltcg_tax - ltcg_basis)
        elif self.filing_status == SINGLE:
            self.income_tax_owed = []
            self.long_term_capital_gains_tax_owed = []
            for i, ltcg in zip(self.taxable_incomes, self.long_term_capital_gains):
                self.income_tax_owed.append(self.income_tax_brackets.calculate_taxes(i))
                # LTCG's tax brackets include the addition of taxable income plus long term capital gains.
                # Income is only used to offset the tax brackets used for computing LTCG. This is achieved
                # by introducing a "basis".
                ltcg_basis = self.long_term_capital_gains_tax_brackets.calculate_taxes(i)
                ltcg_tax = self.long_term_capital_gains_tax_brackets.calculate_taxes(i + ltcg)
                self.long_term_capital_gains_tax_owed.append(ltcg_tax - ltcg_basis)
        else:
            raise Exception(f"Unexpected filing_status {self.filing_status}")
        return
    

    def display_tax_summary(self):

        try:
            logger.info(f'{self.region} Tax Summary')
            logger.info(f'{self.region} Taxable Incomes: {", ".join([f"${i:,.0f}" for i in self.taxable_incomes])}')
            logger.info(f'{self.region} Long term capital gains: {", ".join([f"${i:,.0f}" for i in self.long_term_capital_gains])}')
            logger.info(f'{self.region} Income Tax owed: {", ".join([f"${i:,.0f}" for i in self.income_tax_owed])}')
            logger.info(f'{self.region} LTCG tax owed: {", ".join([f"${i:,.0f}" for i in self.long_term_capital_gains_tax_owed])}\n')
        except AttributeError as e:
            raise AttributeError(f"{e}. Ensure you call 'calculate_taxes' before attempting to call this method.")
        return


    def summary_json(self):

        try:
            return {
                    'taxable_incomes': self.taxable_incomes,
                    'long_term_capital_gains': self.long_term_capital_gains,
                    'income_tax_owed': self.income_tax_owed,
                    'long_term_capital_gains_tax_owed': self.long_term_capital_gains_tax_owed
                }
        except AttributeError as e:
            raise AttributeError(f"{e}. Ensure you call 'calculate_taxes' before attempting to call this method.")
