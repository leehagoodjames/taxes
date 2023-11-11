# tax_input_validator.py
from ..utils.Constants import *


class InputValidator:
    @staticmethod
    def validate_tax_year(tax_year):
        if tax_year not in SUPPORTED_TAX_YEARS:
            raise ValueError(f"tax_year must be in SUPPORTED_TAX_YEARS: {SUPPORTED_TAX_YEARS}, got: {tax_year}")

    @staticmethod
    def validate_filing_status(filing_status):
        if filing_status not in SUPPORTED_FILING_STATUSES:
            raise ValueError(f"filing_status must be in SUPPORTED_FILING_STATUSES: {SUPPORTED_FILING_STATUSES}, got: {filing_status}")

    @staticmethod
    def validate_state(state):
        if state not in SUPPORTED_STATES:
            raise ValueError(f"state must be in SUPPORTED_STATES: {SUPPORTED_STATES}, got: {state}")
