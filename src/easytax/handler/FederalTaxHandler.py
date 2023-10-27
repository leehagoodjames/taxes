
# Local Imports
from ..brackets import FederalIncomeTaxBrackets
from ..brackets import FederalLongTermCapitalGainsTaxBrackets
from . import RegionalTaxHandlerBase


SUPPORTED_TAX_YEARS = {2022, 2023}
SUPPORTED_FILLING_STATUSES = {"Married_Filling_Jointly", "Married_Filling_separately"}

# Each handler can have its own AGI / MAGI
class FederalTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filling_status: str, incomes: list[float], long_term_capital_gains: list[float]):
        """Create a FederalTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filling_status: str - The type of filling (Married Filling Jointly, Single, etc)
        incomes: list[float] - List of the total income for each person in a household. If one person has muliplte W2s, the income on each W2 should be summed together to a single integer for that person's income.
        long_term_capital_gains: list[float] - The total long term capital gains for each person in the household.
        """
        
        if tax_year not in SUPPORTED_TAX_YEARS:
            raise ValueError(f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {tax_year}")
        if filling_status not in SUPPORTED_FILLING_STATUSES:
            raise ValueError(f"filling_status must be in SUPPORTED_FILLING_STATUSES: {SUPPORTED_FILLING_STATUSES}, got: {filling_status}")
        if len(incomes) != len(long_term_capital_gains):
            raise ValueError(f"'incomes' must have the same length as 'long_term_capital_gains'. got lengths of {len(incomes)} and {len(long_term_capital_gains)} respectively")
        
        self.tax_year = tax_year
        self.filling_status = filling_status
        self.incomes = incomes
        self.long_term_capital_gains = long_term_capital_gains
        self.region = "Federal"

        if self.tax_year == 2023: 
            if self.filling_status == "Married_Filling_Jointly":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_jointly_2023_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_jointly_2023_tax
            elif self.filling_status == "Married_Filling_separately":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_separately_2023_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_separately_2023_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filling_status}, year {self.tax_year}")  
        elif self.tax_year == 2022:
            if self.filling_status == "Married_Filling_Jointly":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_jointly_2022_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_jointly_2022_tax
            elif self.filling_status == "Married_Filling_separately":
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_separately_2022_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_separately_2022_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filling_status}, year {self.tax_year}")
        else:
            raise ValueError(f"Unsupported combination of status: {self.filling_status}, year {self.tax_year}")
        
        return