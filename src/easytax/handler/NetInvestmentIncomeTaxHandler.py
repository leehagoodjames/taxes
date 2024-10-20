# Local Imports
from ..brackets import NetInvestmentIncomeTaxBrackets
from .IndividualIncomeTaxHandlerBase import IndividualIncomeTaxHandlerBase
from ..utils.InputValidator import InputValidator
from ..income.FederalIncomeHandler import FederalIncomeHandler
from ..utils.Constants import *


# Each handler can have its own AGI / MAGI
class NetInvestmentIncomeTaxHandler(IndividualIncomeTaxHandlerBase):
    def __init__(self, tax_year: int, filing_status: str, federal_income_handlers: list[FederalIncomeHandler]):
        """Create a NetInvestmentIncomeTaxHandler object.

        Keyword arguments:
        tax_year: int - The year for tax filling. 
        filing_status: str - The type of filling (Married Filing Jointly, Single, etc)
        federal_income_handlers: list[NetInvestmentIncomeHandler] - List of NetInvestmentIncomeHandler objects
        """

        """
        individual taxpayers are liable for a 3.8 percent Net Investment Income Tax on the 
        lesser of their net investment income, or the amount by which their modified 
        adjusted gross income exceeds the statutory threshold amount based on their filing status
        """
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)

        self.tax_year = tax_year
        self.filing_status = filing_status
        # self.total_incomes = [f.total_income for f in federal_income_handlers]
        # self.taxable_incomes = [f.taxable_income for f in federal_income_handlers]
        self.taxable_incomes = [f.niit_income for f in federal_income_handlers]
        # self.long_term_capital_gains = [f.long_term_capital_gains for f in federal_income_handlers]
        self.tax_name = "NetInvestmentIncome"

        # self.threshold_amount = self._get_tax_brackets(tax_year, filing_status)

        # # If the taxpayer is married filing jointly, head of household, or single, their incomes are combined
        # if self.filing_status in {MARRIED_FILING_JOINTLY, HEAD_OF_HOUSEHOLD, SINGLE}:
        #     self.taxable_incomes = [sum(self.taxable_incomes)]
        #     self.niit_income = [sum(self.niit_income)]

        # if self.taxable_incomes[0] > self.threshold_amount:
        #     # Subtract the threshold amount from the taxable income
        #     self.taxable_incomes[0] = self.taxable_incomes[0] - self.threshold_amount

        #     # Choose the lesser of the taxable income or NIIT
        #     self.taxable_incomes[0] = min(self.taxable_incomes[0], self.threshold_amount)
        # else:
        #     self.taxable_incomes[0] = 0

        self.income_tax_brackets = self._get_tax_brackets(tax_year, filing_status)
        
    @staticmethod
    def _get_tax_brackets(tax_year: int, filing_status: str):
        if tax_year not in NetInvestmentIncomeTaxBrackets.brackets:
            raise ValueError(f"Unsupported tax year: {tax_year}")
        
        if filing_status not in NetInvestmentIncomeTaxBrackets.brackets[tax_year]:
            raise ValueError(f"Unsupported filing status: {filing_status} for tax year {tax_year}")

        
        return NetInvestmentIncomeTaxBrackets.brackets[tax_year][filing_status]

