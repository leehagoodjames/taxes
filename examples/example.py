# Third Party Imports
from taxes.brackets import FederalIncomeTaxBrackets
from taxes.brackets import GeorgiaStateIncomeTaxBrackets
from taxes.brackets import SocialSecurityIncomeTaxBrackets
from taxes.brackets import MedicareIncomeTaxBrackets

# Load in tax brackets for your year and filing-status.
federal_taxes = FederalIncomeTaxBrackets.married_filing_jointly_2022_tax
georgia_taxes = GeorgiaStateIncomeTaxBrackets.married_filing_jointly_2022_tax
social_security_taxes = SocialSecurityIncomeTaxBrackets.social_security_employee_2022_tax
medicare_taxes = MedicareIncomeTaxBrackets.medicare_employee_2022_tax

# Compute the taxes.
agi = 100000
federal_tax = federal_taxes.calculate_taxes(agi)
state_tax = georgia_taxes.calculate_taxes(agi)
social_security_tax = social_security_taxes.calculate_taxes(agi)
medicare_tax = medicare_taxes.calculate_taxes(agi)

# Show the result.
print(f'adjusted gross income: ${agi:,.0f}')
print(f'federal tax: ${federal_tax:,.0f}')
print(f'state tax: ${state_tax:,.0f}')
print(f'social security tax: ${social_security_tax:,.0f}')
print(f'medicare tax: ${medicare_tax:,.0f}')
