
# Local Imports
from ..brackets import GeorgiaStateIncomeTaxBrackets
from ..brackets import GeorgiaStateLongTermCapitalGainsTaxBrackets
from . import RegionalTaxHandlerBase
from ..utils.InputValidator import InputValidator


# Each handler can have its own AGI / MAGI
class GeorgiaTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, incomes: list[float], long_term_capital_gains: list[float], state_data: dict):
        """Create a GeorgiaTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filling Jointly, Single, etc)
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
        state_data: dict - Inputs relevant to Georiga
            state_data.exemptions: int - defined by the state of Georgia on line 6c.
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        if len(incomes) != len(long_term_capital_gains):
            raise ValueError(f"'incomes' must have the same length as 'long_term_capital_gains'. got lengths of {len(incomes)} and {len(long_term_capital_gains)} respectively")
        if state_data is None:
            raise ValueError(f"invalid value for 'state_data': {state_data}")
        if state_data.get('exemptions') is None:
            raise ValueError(f"state_data specified invalid value for 'exemptions': {state_data.get('exemptions')}")
        if type(state_data.get('exemptions')) is not int:
            raise TypeError(f"state_data specified invalid type for 'exemptions': {type(state_data.get('exemptions'))}")
        
        self.tax_year = tax_year
        self.filing_status = filing_status
        self.region = "Georgia"

        # The state of Georgia treats long term capital gains as income
        self.incomes = [i + ltcg for i,ltcg in zip(incomes, long_term_capital_gains)]
        self.long_term_capital_gains = [0] * len(long_term_capital_gains)

        if self.tax_year == 2023: 
            # TODO: Fix this deduction logic
            self.deduction = 3700 * state_data.get('exemptions')
            deduction_per_income = self.deduction / len(self.incomes)
            self.incomes = [i - deduction_per_income for i in self.incomes]

            if self.filing_status == "Married_Filling_Jointly":
                self.income_tax_brackets = GeorgiaStateIncomeTaxBrackets.married_filing_jointly_2023_tax
                self.long_term_capital_gains_tax_brackets = GeorgiaStateIncomeTaxBrackets.married_filing_jointly_2023_tax # Doesn't need to be used, LTCG are zero
            elif self.filing_status == "Married_Filling_separately":
                self.income_tax_brackets = GeorgiaStateIncomeTaxBrackets.married_filing_separately_2023_tax
                self.long_term_capital_gains_tax_brackets = GeorgiaStateLongTermCapitalGainsTaxBrackets.married_filing_separately_2023_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")  
        elif self.tax_year == 2022:
            # TODO: Fix this deduction logic
            self.deduction = 3700 * state_data.get('exemptions')
            deduction_per_income = self.deduction / len(self.incomes)
            self.incomes = [i - deduction_per_income for i in self.incomes]

            if self.filing_status == "Married_Filling_Jointly":
                self.income_tax_brackets = GeorgiaStateIncomeTaxBrackets.married_filing_jointly_2022_tax
                self.long_term_capital_gains_tax_brackets = GeorgiaStateLongTermCapitalGainsTaxBrackets.married_filing_jointly_2022_tax
            elif self.filing_status == "Married_Filling_separately":
                self.income_tax_brackets = GeorgiaStateIncomeTaxBrackets.married_filing_separately_2022_tax
                self.long_term_capital_gains_tax_brackets = GeorgiaStateLongTermCapitalGainsTaxBrackets.married_filing_separately_2022_tax 
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        
        return
    