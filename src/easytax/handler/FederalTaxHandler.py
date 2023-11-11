
# Local Imports
from ..brackets import FederalIncomeTaxBrackets
from ..brackets import FederalLongTermCapitalGainsTaxBrackets
from . import RegionalTaxHandlerBase
from ..utils.Constants import *
from ..utils.InputValidator import InputValidator


# Each handler can have its own AGI / MAGI
class FederalTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, incomes: list[float], long_term_capital_gains: list[float]):
        """Create a FederalTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filling Jointly, Single, etc)
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        
        if len(incomes) != len(long_term_capital_gains):
            raise ValueError(f"'incomes' must have the same length as 'long_term_capital_gains'. got lengths of {len(incomes)} and {len(long_term_capital_gains)} respectively")
        
        self.tax_year = tax_year
        self.filing_status = filing_status
        self.incomes = incomes
        self.long_term_capital_gains = long_term_capital_gains
        self.region = "Federal"

        if self.tax_year == 2023: 
            if self.filing_status == "Married_Filling_Jointly":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_jointly_2023_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_jointly_2023_tax
            elif self.filing_status == "Married_Filling_separately":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_separately_2023_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_separately_2023_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")  
        elif self.tax_year == 2022:
            if self.filing_status == "Married_Filling_Jointly":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_jointly_2022_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_jointly_2022_tax
            elif self.filing_status == "Married_Filling_separately":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_separately_2022_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_separately_2022_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        
        return