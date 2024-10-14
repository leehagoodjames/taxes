
# Local Imports
from ..brackets import FederalIncomeTaxBrackets
from ..brackets import FederalLongTermCapitalGainsTaxBrackets
from . import RegionalTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler
from ..utils.Constants import *


# Each handler can have its own AGI / MAGI
class FederalTaxHandler(RegionalTaxHandlerBase.RegionalTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, federal_income_handlers: list[FederalIncomeHandler]):
        """Create a FederalTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filing Jointly, Single, etc)
        federal_income_handlers: list[FederalIncomeHandler] - List of FederalIncomeHandler objects
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)

        self.tax_year = tax_year
        self.filing_status = filing_status
        self.total_incomes = [f.total_income for f in federal_income_handlers]
        self.taxable_incomes = [f.taxable_income for f in federal_income_handlers]
        self.long_term_capital_gains = [f.long_term_capital_gains for f in federal_income_handlers]
        self.region = "Federal"

        if self.tax_year == 2024:
            if self.filing_status == MARRIED_FILING_JOINTLY:
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_jointly_2024_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_jointly_2024_tax
            elif self.filing_status == MARRIED_FILING_SEPARATELY:
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_separately_2024_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_separately_2024_tax
            elif self.filing_status == SINGLE:
                self.income_tax_brackets = FederalIncomeTaxBrackets.single_filer_2024_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.single_filer_2024_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        elif self.tax_year == 2023:
            if self.filing_status == MARRIED_FILING_JOINTLY:
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_jointly_2023_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_jointly_2023_tax
            elif self.filing_status == MARRIED_FILING_SEPARATELY:
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_separately_2023_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_separately_2023_tax
            elif self.filing_status == SINGLE:
                self.income_tax_brackets = FederalIncomeTaxBrackets.single_filer_2023_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.single_filer_2023_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")  
        elif self.tax_year == 2022:
            if self.filing_status == MARRIED_FILING_JOINTLY:
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_jointly_2022_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_jointly_2022_tax
            elif self.filing_status == MARRIED_FILING_SEPARATELY:
                self.income_tax_brackets = FederalIncomeTaxBrackets.married_filing_separately_2022_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.married_filing_separately_2022_tax
            elif self.filing_status == SINGLE:
                self.income_tax_brackets = FederalIncomeTaxBrackets.single_filer_2022_tax
                self.long_term_capital_gains_tax_brackets = FederalLongTermCapitalGainsTaxBrackets.single_filer_2022_tax
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        
        return