from src.easytax.income.FederalIncomeHandler import FederalIncomeHandler

SUPPORTED_TAX_YEAR = 2023
SUPPORTED_FILING_STATUS = "Married_Filing_Jointly"
SUPPORTED_STATE = "Georgia"
SUPPORTED_STATE_DATA = {'exemptions': 0 }
SUPPORTED_SALARY_AND_WAGES_1 = 150000
SUPPORTED_SALARY_AND_WAGES_2 = 100000
SUPPORTED_TAXABLE_PENSIONS_1 = 0
SUPPORTED_TAXABLE_PENSIONS_2 = 0
SUPPORTED_LONG_TERM_CAPITAL_GAINS_1 = 60000
SUPPORTED_LONG_TERM_CAPITAL_GAINS_2 = 40000
SUPPORTED_INCOMES = [
    {
        "salaries_and_wages": SUPPORTED_SALARY_AND_WAGES_1,
        "taxable_pensions": SUPPORTED_TAXABLE_PENSIONS_1, # 401k distributions,
        "long_term_capital_gains": SUPPORTED_LONG_TERM_CAPITAL_GAINS_1,
        "use_standard_deduction": False, # Simplifies examples by making deductions zero
    },
    {
        "salaries_and_wages": SUPPORTED_SALARY_AND_WAGES_2,
        "taxable_pensions": SUPPORTED_TAXABLE_PENSIONS_2, # 401k distributions,
        "long_term_capital_gains": SUPPORTED_LONG_TERM_CAPITAL_GAINS_2,
        "use_standard_deduction": False, # Simplifies examples by making deductions zero
    }
]
SUPPORTED_FEDERAL_INCOME_HANDLERS = [
    FederalIncomeHandler(
        filing_status=SUPPORTED_FILING_STATUS,
        tax_year=SUPPORTED_TAX_YEAR,
        salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_1, 
        long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS_1,
        taxable_pensions=SUPPORTED_TAXABLE_PENSIONS_1,
        use_standard_deduction=False, # Simplifies examples by making deductions zero
        ),
    FederalIncomeHandler(
        filing_status=SUPPORTED_FILING_STATUS,
        tax_year=SUPPORTED_TAX_YEAR,
        salaries_and_wages=SUPPORTED_SALARY_AND_WAGES_2, 
        long_term_capital_gains=SUPPORTED_LONG_TERM_CAPITAL_GAINS_2,
        taxable_pensions=SUPPORTED_TAXABLE_PENSIONS_2,
        use_standard_deduction=False, # Simplifies examples by making deductions zero
        ),
]


SUPPORTED_TAXES_PAID = 10000
SUPPORTED_CHARITABLE_CONTRIBUTIONS = 15000

# Georgia
SUPPORTED_STATE_DATA = {'exemptions': 0}
