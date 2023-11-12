# Local Imports
from ..utils.InputValidator import InputValidator
from ..deductions import FederalStandardDeductions


class FederalIncomeHandler:
    def __init__(self,
                filing_status: str,
                tax_year: int,
                dependents: int = 0,
                use_standard_deduction: bool = True,
                # Income
                salaries_and_wages: float = 0, 
                interest_income: float = 0, 
                tax_exempt_interest: float = 0, 
                dividend_income: float = 0, 
                qualified_dividend_income: float = 0, 
                taxable_state_local_refunds: float = 0, 
                alimony_received: float = 0, 
                business_income_or_loss: float = 0, 
                capital_gain_or_loss: float = 0, 
                other_gains_or_losses: float = 0, 
                taxable_ira_distributions: float = 0, 
                taxable_pensions: float = 0, 
                rent_royalty_income: float = 0, 
                partnership_or_s_corp_income: float = 0, 
                estate_trust_income: float = 0, 
                farm_income_or_loss: float = 0, 
                unemployment_compensation: float = 0, 
                taxable_social_security: float = 0, 
                other_income: float = 0,
                # LTCG
                long_term_capital_gains: float = 0,
                # Deductions
                medical_expenses: float = 0,
                taxes_paid: float = 0,
                interest_paid: float = 0,
                charitable_contributions: float = 0,
                casualty_losses: float = 0,
                miscellaneous_expenses: float = 0,
                qbid: float = 0,
                ):
        
        InputValidator.validate_tax_year(tax_year)
        InputValidator.validate_filing_status(filing_status)
        self.filing_status = filing_status
        self.tax_year = tax_year
        self.dependents = dependents
        self.use_standard_deduction = use_standard_deduction

        # Income fields
        self.salaries_and_wages = salaries_and_wages
        self.interest_income = interest_income
        self.tax_exempt_interest = tax_exempt_interest
        self.dividend_income = dividend_income
        self.qualified_dividend_income = qualified_dividend_income
        self.taxable_state_local_refunds = taxable_state_local_refunds
        self.alimony_received = alimony_received
        self.business_income_or_loss = business_income_or_loss
        self.capital_gain_or_loss = capital_gain_or_loss
        self.other_gains_or_losses = other_gains_or_losses
        self.taxable_ira_distributions = taxable_ira_distributions
        self.taxable_pensions = taxable_pensions
        self.rent_royalty_income = rent_royalty_income
        self.partnership_or_s_corp_income = partnership_or_s_corp_income
        self.estate_trust_income = estate_trust_income
        self.farm_income_or_loss = farm_income_or_loss
        self.unemployment_compensation = unemployment_compensation
        self.taxable_social_security = taxable_social_security
        self.other_income = other_income

        # LTCG
        self.long_term_capital_gains = long_term_capital_gains

        # Deductions
        self.medical_expenses = medical_expenses
        self.taxes_paid = taxes_paid
        self.interest_paid = interest_paid
        self.charitable_contributions = charitable_contributions
        self.casualty_losses = casualty_losses
        self.miscellaneous_expenses = miscellaneous_expenses

        # Set standard Deduction
        if self.tax_year == 2023: 
            if self.filing_status == "Married_Filling_Jointly":
                self.standard_deduction = FederalStandardDeductions.married_filing_jointly_2023_deduction
            elif self.filing_status == "Married_Filling_separately":
                self.standard_deduction = FederalStandardDeductions.married_filing_separately_2023_deduction
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")  
        elif self.tax_year == 2022:
            if self.filing_status == "Married_Filling_Jointly":
                self.standard_deduction = FederalStandardDeductions.married_filing_jointly_2022_deduction
            elif self.filing_status == "Married_Filling_separately":
                self.standard_deduction = FederalStandardDeductions.married_filing_separately_2022_deduction
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")

        # QBID
        self.qbid = qbid

        # Notably omit long_term_capital_gains
        self.incomes_towards_agi = [
            self.salaries_and_wages, 
            self.interest_income, 
            self.tax_exempt_interest, 
            self.dividend_income, 
            self.qualified_dividend_income, 
            self.taxable_state_local_refunds, 
            self.alimony_received, 
            self.business_income_or_loss, 
            self.capital_gain_or_loss, 
            self.other_gains_or_losses, 
            self.taxable_ira_distributions, 
            self.taxable_pensions, 
            self.rent_royalty_income, 
            self.partnership_or_s_corp_income, 
            self.estate_trust_income, 
            self.farm_income_or_loss, 
            self.unemployment_compensation, 
            self.taxable_social_security, 
            self.other_income
        ]
        for i in self.incomes_towards_agi:
            if type(i) is not int and type(i) is not float:
                raise TypeError(f"Unsupported income type {type(i)} for income {i}")

        # Deduction fields
        self.deduction_fields = [
            self.medical_expenses, 
            self.taxes_paid, 
            self.interest_paid, 
            self.charitable_contributions, 
            self.casualty_losses, 
            self.miscellaneous_expenses, 
        ]
        for i in self.deduction_fields:
            if type(i) is not int and type(i) is not float:
                raise TypeError(f"Unsupported deduction type {type(i)} for deduction {i}")
        
        # TODO: Perform any other value validation on incomes. Some may be negative, but those that must be positive should be checked.
        self.total_income = sum(self.incomes_towards_agi)
        self.allowable_itemized_deductions = sum(self.deduction_fields)

        if self.use_standard_deduction:
            self.deduction_taken = self.standard_deduction

            
        else:
            self.deduction_taken = self.allowable_itemized_deductions

        # Taxable Iincome Before Qualified Business Income Deduction 
        self.taxable_income_before_qbid = self.total_income - self.deduction_taken

        self.taxable_income = self.taxable_income_before_qbid - self.qbid
    
    def __eq__(self, other):
        if not isinstance(other, FederalIncomeHandler):
            return NotImplemented

        return (
            self.filing_status == other.filing_status and
            self.tax_year == other.tax_year and
            self.dependents == other.dependents and
            self.use_standard_deduction == other.use_standard_deduction and
            self.salaries_and_wages == other.salaries_and_wages and
            self.interest_income == other.interest_income and
            self.tax_exempt_interest == other.tax_exempt_interest and
            self.dividend_income == other.dividend_income and
            self.qualified_dividend_income == other.qualified_dividend_income and
            self.taxable_state_local_refunds == other.taxable_state_local_refunds and
            self.alimony_received == other.alimony_received and
            self.business_income_or_loss == other.business_income_or_loss and
            self.capital_gain_or_loss == other.capital_gain_or_loss and
            self.other_gains_or_losses == other.other_gains_or_losses and
            self.taxable_ira_distributions == other.taxable_ira_distributions and
            self.taxable_pensions == other.taxable_pensions and
            self.rent_royalty_income == other.rent_royalty_income and
            self.partnership_or_s_corp_income == other.partnership_or_s_corp_income and
            self.estate_trust_income == other.estate_trust_income and
            self.farm_income_or_loss == other.farm_income_or_loss and
            self.unemployment_compensation == other.unemployment_compensation and
            self.taxable_social_security == other.taxable_social_security and
            self.other_income == other.other_income and
            self.long_term_capital_gains == other.long_term_capital_gains and
            self.medical_expenses == other.medical_expenses and
            self.taxes_paid == other.taxes_paid and
            self.interest_paid == other.interest_paid and
            self.charitable_contributions == other.charitable_contributions and
            self.casualty_losses == other.casualty_losses and
            self.miscellaneous_expenses == other.miscellaneous_expenses and
            self.standard_deduction == other.standard_deduction and
            self.qbid == other.qbid
        )

    def __str__(self):
        return (
            f"Federal Income Handler:\n"
            f"Tax Year: {self.tax_year}\n"
            f"Filing Status: {self.filing_status}\n"
            f"Dependents: {self.dependents}\n"
            f"Use Standard Deduction: {self.use_standard_deduction}\n"
            f"Salaries and Wages: {self.salaries_and_wages}\n"
            f"Interest Income: {self.interest_income}\n"
            f"Tax Exempt Interest: {self.tax_exempt_interest}\n"
            f"Dividend Income: {self.dividend_income}\n"
            f"Qualified Dividend Income: {self.qualified_dividend_income}\n"
            f"Taxable State Local Refunds: {self.taxable_state_local_refunds}\n"
            f"Alimony Received: {self.alimony_received}\n"
            f"Business Income or Loss: {self.business_income_or_loss}\n"
            f"Capital Gain or Loss: {self.capital_gain_or_loss}\n"
            f"Other Gains or Losses: {self.other_gains_or_losses}\n"
            f"Taxable IRA Distributions: {self.taxable_ira_distributions}\n"
            f"Taxable Pensions: {self.taxable_pensions}\n"
            f"Rent Royalty Income: {self.rent_royalty_income}\n"
            f"Partnership or S Corp Income: {self.partnership_or_s_corp_income}\n"
            f"Estate Trust Income: {self.estate_trust_income}\n"
            f"Farm Income or Loss: {self.farm_income_or_loss}\n"
            f"Unemployment Compensation: {self.unemployment_compensation}\n"
            f"Taxable Social Security: {self.taxable_social_security}\n"
            f"Other Income: {self.other_income}\n"
            f"Long Term Capital Gains: {self.long_term_capital_gains}\n"
            f"Medical Expenses: {self.medical_expenses}\n"
            f"Taxes Paid: {self.taxes_paid}\n"
            f"Interest Paid: {self.interest_paid}\n"
            f"Charitable Contributions: {self.charitable_contributions}\n"
            f"Casualty Losses: {self.casualty_losses}\n"
            f"Miscellaneous Expenses: {self.miscellaneous_expenses}\n"
            f"Standard Deduction: {self.standard_deduction}\n"
            f"QBID: {self.qbid}\n"
            f"Total Income: {self.total_income}\n"
            f"Allowable Itemized Deductions: {self.allowable_itemized_deductions}\n"
            f"Taxable Income Before QBID: {self.taxable_income_before_qbid}\n"
            f"Taxable Income: {self.taxable_income}"
        )

    @classmethod
    def from_dict(cls, data: dict):
        # Mandatory fields without default values
        if 'filing_status' not in data or 'tax_year' not in data:
            raise ValueError("filing_status and tax_year are required fields")

        # Set default values to 0 if not provided in data
        default_values = {
            "tax_year": "REPLACE",
            "filing_status": "REPLACE",
            "dependents": 0,
            "use_standard_deduction": True,
            "salaries_and_wages": 0,
            "interest_income": 0,
            "tax_exempt_interest": 0,
            "dividend_income": 0,
            "qualified_dividend_income": 0,
            "taxable_state_local_refunds": 0,
            "alimony_received": 0,
            "business_income_or_loss": 0,
            "capital_gain_or_loss": 0,
            "other_gains_or_losses": 0,
            "taxable_ira_distributions": 0,
            "taxable_pensions": 0,
            "rent_royalty_income": 0,
            "partnership_or_s_corp_income": 0,
            "estate_trust_income": 0,
            "farm_income_or_loss": 0,
            "unemployment_compensation": 0,
            "taxable_social_security": 0,
            "other_income": 0,
            "long_term_capital_gains": 0,
            "medical_expenses": 0,
            "taxes_paid": 0,
            "interest_paid": 0,
            "charitable_contributions": 0,
            "casualty_losses": 0,
            "miscellaneous_expenses": 0,
            "qbid": 0,
        }

        # Update default values with those provided in data
        for key in default_values.keys():
            if key in data:
                default_values[key] = data[key]

        for key in data.keys():
            if key not in default_values.keys():
                raise ValueError(f"Unsupported income for key {key}")

        # Create an instance of the class with the updated values
        return cls(**default_values)