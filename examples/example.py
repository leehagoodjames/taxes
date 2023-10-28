# Third Party Imports
from easytax.handler import TaxHandler

# Load in tax brackets for your year and filing-status.
taxHandler = TaxHandler.TaxHandler(
    tax_year = 2022, 
    filling_status = "Married_Filling_Jointly", 
    state = "Georgia", 
    incomes = [273000 - 40000], 
    long_term_capital_gains = [0],
)

taxHandler.calculate_taxes()
taxHandler.display_tax_summary()
