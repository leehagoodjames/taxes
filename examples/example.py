# Third Party Imports
from easytax.handler import TaxHandler

# Load in tax brackets for your year and filing-status.
taxHandler = TaxHandler.TaxHandler(
    tax_year = 2022, 
    filling_status = "Married_Filling_Jointly", 
    state = "Georgia", 
    incomes = [247472 + 85 + 41 + 6767 + 272 - (44076 + 3000) ], 
    retirement_incomes=[0],
    long_term_capital_gains = [0],
)

taxHandler.calculate_taxes()
taxHandler.display_tax_summary()
