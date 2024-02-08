# Local Imports
from ..utils.Constants import *


class InputValidator:

    # Put in alphabetic order for readability
    @staticmethod
    def alphabetize_set(s: set):
        l = list(s)
        l.sort()
        return l
     
    @staticmethod
    def validate_tax_year(tax_year):
        if tax_year not in SUPPORTED_TAX_YEARS:
            raise ValueError(f"tax_year must be in SUPPORTED_TAX_YEARS: {InputValidator.alphabetize_set(SUPPORTED_TAX_YEARS)}, got: {tax_year}")

    @staticmethod
    def validate_filing_status(filing_status):
        if filing_status not in SUPPORTED_FILING_STATUSES:
            raise ValueError(f"filing_status must be in SUPPORTED_FILING_STATUSES: {InputValidator.alphabetize_set(SUPPORTED_FILING_STATUSES)}, got: {filing_status}")

    @staticmethod
    def validate_state(state):
        if state not in SUPPORTED_STATES:
            raise ValueError(f"state must be in SUPPORTED_STATES: {InputValidator.alphabetize_set(SUPPORTED_STATES)}, got: {state}")
        
    @staticmethod
    def validate_region_does_not_have_any_tax(state):
        if state not in STATES_WITHOUT_INCOME_TAX:
            raise ValueError(f"state must be in STATES_WITHOUT_INCOME_TAX: {InputValidator.alphabetize_set(STATES_WITHOUT_INCOME_TAX)}, got: {state}")
