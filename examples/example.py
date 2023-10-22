# Third Party Imports
from easytax.brackets import FederalIncomeTaxBrackets
from easytax.brackets import GeorgiaStateIncomeTaxBrackets
from easytax.brackets import GeorgiaStateLongTermCapitalGainsTaxBrackets
from easytax.brackets import SocialSecurityIncomeTaxBrackets
from easytax.brackets import MedicareIncomeTaxBrackets
from easytax.utils.Logger import logger

# Load in tax brackets for your year and filing-status.
federal_taxes = FederalIncomeTaxBrackets.married_filing_jointly_2022_tax
georgia_taxes = GeorgiaStateIncomeTaxBrackets.married_filing_jointly_2022_tax
georgia_capital_gains_taxes = GeorgiaStateLongTermCapitalGainsTaxBrackets.married_filing_jointly_2022_tax
social_security_taxes = SocialSecurityIncomeTaxBrackets.social_security_employee_2022_tax
medicare_taxes = MedicareIncomeTaxBrackets.medicare_employee_2022_tax

# Compute the taxes.
agi = 100000 # Includes short term capital gains
long_term_capital_gains = 10000
federal_tax = federal_taxes.calculate_taxes(agi)
state_tax = georgia_taxes.calculate_taxes(agi) + georgia_capital_gains_taxes.calculate_taxes(long_term_capital_gains)
social_security_tax = social_security_taxes.calculate_taxes(agi)
medicare_tax = medicare_taxes.calculate_taxes(agi)

# Show the result.
logger.info(f'adjusted gross income: ${agi:,.0f}')
logger.info(f'long term capital gains: ${long_term_capital_gains:,.0f}')
logger.info(f'federal tax: ${federal_tax:,.0f}')
logger.info(f'state tax: ${state_tax:,.0f}')
logger.info(f'social security tax: ${social_security_tax:,.0f}')
logger.info(f'medicare tax: ${medicare_tax:,.0f}')
