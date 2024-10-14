# Local Imports
from ..utils.InputValidator import InputValidator
from ..deductions import FederalStandardDeductions
from ..utils.Constants import *


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
                # Income Adjustments
                moving_expenses: float = 0,
                deductible_self_employment_tax: float = 0,
                sep_simple_qualified_plans_deductions: float = 0,
                self_employment_health_insurance: float = 0,
                penalty_early_withdrawal_savings: float = 0,
                alimony_paid: float = 0,
                ira_deductions: float = 0,
                student_loan_interest: float = 0,
                other_adjustments: float = 0,
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

        # Income Adjustments
        self.moving_expenses = moving_expenses
        self.deductible_self_employment_tax = deductible_self_employment_tax
        self.sep_simple_qualified_plans_deductions = sep_simple_qualified_plans_deductions
        self.self_employment_health_insurance = self_employment_health_insurance
        self.penalty_early_withdrawal_savings = penalty_early_withdrawal_savings
        self.alimony_paid = alimony_paid
        self.ira_deductions = ira_deductions
        self.student_loan_interest = student_loan_interest
        self.other_adjustments = other_adjustments

        # Deductions
        self.medical_expenses = medical_expenses
        self.taxes_paid = taxes_paid
        self.interest_paid = interest_paid
        self.charitable_contributions = charitable_contributions
        self.casualty_losses = casualty_losses
        self.miscellaneous_expenses = miscellaneous_expenses

        # Set standard Deduction
        if self.tax_year == 2024:
            if self.filing_status == MARRIED_FILING_JOINTLY:
                self.standard_deduction = FederalStandardDeductions.married_filing_jointly_2024_deduction
            elif self.filing_status == MARRIED_FILING_SEPARATELY:
                self.standard_deduction = FederalStandardDeductions.married_filing_separately_2024_deduction
            elif self.filing_status == SINGLE:
                self.standard_deduction = FederalStandardDeductions.single_filer_2024_deduction
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        elif self.tax_year == 2023: 
            if self.filing_status == MARRIED_FILING_JOINTLY:
                self.standard_deduction = FederalStandardDeductions.married_filing_jointly_2023_deduction
            elif self.filing_status == MARRIED_FILING_SEPARATELY:
                self.standard_deduction = FederalStandardDeductions.married_filing_separately_2023_deduction
            elif self.filing_status == SINGLE:
                self.standard_deduction = FederalStandardDeductions.single_filer_2023_deduction
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")  
        elif self.tax_year == 2022:
            if self.filing_status == MARRIED_FILING_JOINTLY:
                self.standard_deduction = FederalStandardDeductions.married_filing_jointly_2022_deduction
            elif self.filing_status == MARRIED_FILING_SEPARATELY:
                self.standard_deduction = FederalStandardDeductions.married_filing_separately_2022_deduction
            elif self.filing_status == SINGLE:
                self.standard_deduction = FederalStandardDeductions.single_filer_2022_deduction
            else:
                raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")
        else:
            raise ValueError(f"Unsupported combination of status: {self.filing_status}, year {self.tax_year}")

        # QBID
        self.qbid = qbid

        # Notably omit long_term_capital_gains
        self.income_sources = [
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
        for i in self.income_sources:
            if type(i) not in (int, float):
                raise TypeError(f"Unsupported income type {type(i)} for income {i}")
        self.total_income = sum(self.income_sources)

        # Calculate Total Income, Adjustments, and AGI
        self.adjustment_sources = [
            self.moving_expenses, 
            self.deductible_self_employment_tax, 
            self.sep_simple_qualified_plans_deductions, 
            self.self_employment_health_insurance, 
            self.penalty_early_withdrawal_savings, 
            self.alimony_paid, 
            self.ira_deductions, 
            self.student_loan_interest, 
            self.other_adjustments
        ]
        for i in self.adjustment_sources:
            if type(i) not in (int, float):
                raise TypeError(f"Unsupported income type {type(i)} for adjustment {i}")
            
        self.total_adjustments = sum(self.adjustment_sources)
        self.adjusted_gross_income = self.total_income - self.total_adjustments

        # Deduction fields
        self.deduction_sources = [
            self.medical_expenses, 
            self.taxes_paid, 
            self.interest_paid, 
            self.charitable_contributions, 
            self.casualty_losses, 
            self.miscellaneous_expenses, 
        ]
        for i in self.deduction_sources:
            if type(i) not in (int, float):
                raise TypeError(f"Unsupported deduction type {type(i)} for deduction {i}")
        
        # TODO: Perform any other value validation on incomes. Some may be negative, but those that must be positive should be checked.
        self.allowable_itemized_deductions = sum(self.deduction_sources)

        # handle the fact that not all pre-tax contributions are tax-deductible, such as IRA contributions if you are, or are not, covered by a retirement plan at work and make above a certain amount
        # https://www.irs.gov/retirement-plans/2023-ira-deduction-limits-effect-of-modified-agi-on-deduction-if-you-are-covered-by-a-retirement-plan-at-work
        # https://www.irs.gov/retirement-plans/2023-ira-deduction-limits-effect-of-modified-agi-on-deduction-if-you-are-not-covered-by-a-retirement-plan-at-work
        if self.use_standard_deduction:
            self.deduction_taken = self.standard_deduction
        else:
            self.deduction_taken = self.allowable_itemized_deductions

        # Taxable Income Before Qualified Business Income Deduction 
        self.taxable_income_before_qbid = self.adjusted_gross_income - self.deduction_taken

        self.taxable_income = max(self.taxable_income_before_qbid - self.qbid, 0)
        if self.taxable_income < 0:
            raise ValueError(f"Taxable Income cannot be less than zero. Got {self.taxable_income}")
        
        # NIIT
        niit_incomes = [
            self.capital_gain_or_loss,
            self.long_term_capital_gains, 
            self.interest_income,
            self.rent_royalty_income,
            business_income_or_loss
        ]
        self.niit_income = sum(niit_incomes)
    
    def __eq__(self, other):
        if not isinstance(other, FederalIncomeHandler):
            return NotImplemented

        return (
            self.filing_status == other.filing_status and
            self.tax_year == other.tax_year and
            self.dependents == other.dependents and
            self.use_standard_deduction == other.use_standard_deduction and
            # Income
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
            # LTCG
            self.long_term_capital_gains == other.long_term_capital_gains and
            # Adjustments
            self.moving_expenses == other.moving_expenses and
            self.deductible_self_employment_tax == other.deductible_self_employment_tax and
            self.sep_simple_qualified_plans_deductions == other.sep_simple_qualified_plans_deductions and
            self.self_employment_health_insurance == other.self_employment_health_insurance and
            self.penalty_early_withdrawal_savings == other.penalty_early_withdrawal_savings and
            self.alimony_paid == other.alimony_paid and
            self.ira_deductions == other.ira_deductions and
            self.student_loan_interest == other.student_loan_interest and
            self.other_adjustments == other.other_adjustments and
            # Deductions
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
            # Income
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
            # LTCG
            f"Long Term Capital Gains: {self.long_term_capital_gains}\n"
            # Adjustments
            f"Moving Expenses: {self.moving_expenses}\n",
            f"Deductible Self-Employment Tax: {self.deductible_self_employment_tax}\n",
            f"SEP/SIMPLE/Qualified Plans Deductions: {self.sep_simple_qualified_plans_deductions}\n",
            f"Self-Employment Health Insurance: {self.self_employment_health_insurance}\n",
            f"Penalty on Early Withdrawal of Savings: {self.penalty_early_withdrawal_savings}\n",
            f"Alimony Paid: {self.alimony_paid}\n",
            f"IRA Deductions: {self.ira_deductions}\n",
            f"Student Loan Interest: {self.student_loan_interest}\n",
            f"Other Adjustments: {self.other_adjustments}\n"
            # Deductions
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
            # Income
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
            # LTCG
            "long_term_capital_gains": 0,
            # Adjustments
            "moving_expenses": 0,
            "deductible_self_employment_tax": 0,
            "sep_simple_qualified_plans_deductions": 0,
            "self_employment_health_insurance": 0,
            "penalty_early_withdrawal_savings": 0,
            "alimony_paid": 0,
            "ira_deductions": 0,
            "student_loan_interest": 0,
            "other_adjustments": 0,
            # Deductions
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