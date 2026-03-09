from ...utils.Constants import *

class CaliforniaStandardDeductions:
    """California standard deduction amounts by tax year and filing status."""
    
    # California standard deduction amounts
    STANDARD_DEDUCTIONS = {
        2026: {
            # Source: Estimated based on 3.5% inflation adjustment from 2025 figures
            SINGLE: 6000,
            MARRIED_FILING_JOINTLY: 12000,
            MARRIED_FILING_SEPARATELY: 6000,
            HEAD_OF_HOUSEHOLD: 12000
        },
        2025: {
            # Source: California FTB - inflation adjusted from 2024
            # Based on typical 3.3% inflation adjustment pattern
            SINGLE: 5800,
            MARRIED_FILING_JOINTLY: 11600,
            MARRIED_FILING_SEPARATELY: 5800,
            HEAD_OF_HOUSEHOLD: 11600
        },
        2024: {
            SINGLE: 5540,
            MARRIED_FILING_JOINTLY: 11080,
            MARRIED_FILING_SEPARATELY: 5540,
            HEAD_OF_HOUSEHOLD: 11080
        },
        2023: {
            SINGLE: 5363,
            MARRIED_FILING_JOINTLY: 10726,
            MARRIED_FILING_SEPARATELY: 5363,
            HEAD_OF_HOUSEHOLD: 10726
        },
        2022: {
            SINGLE: 5202,
            MARRIED_FILING_JOINTLY: 10404,
            MARRIED_FILING_SEPARATELY: 5202,
            HEAD_OF_HOUSEHOLD: 10404
        }
    }
    
    @classmethod
    def get_standard_deduction(cls, tax_year: int, filing_status: str) -> float:
        """
        Get the California standard deduction for the given tax year and filing status.
        
        Args:
            tax_year: The tax year
            filing_status: The filing status (single, married_filing_jointly, etc.)
            
        Returns:
            The standard deduction amount
            
        Raises:
            ValueError: If tax year or filing status is not supported
        """
        if tax_year not in cls.STANDARD_DEDUCTIONS:
            raise ValueError(f"Tax year {tax_year} not supported for California standard deductions")
            
        if filing_status not in cls.STANDARD_DEDUCTIONS[tax_year]:
            raise ValueError(f"Filing status '{filing_status}' not supported for California standard deductions")
            
        return cls.STANDARD_DEDUCTIONS[tax_year][filing_status] 