from ...utils.Constants import *

class CaliforniaStateTaxCredits:
    """California state tax credits calculator."""
    
    def __init__(self, tax_year: int, filing_status: str, state_data: dict):
        """
        Initialize California tax credits calculator.
        
        Args:
            tax_year: The tax year
            filing_status: The filing status
            state_data: Dictionary containing California-specific tax data
        """
        self.tax_year = tax_year
        self.filing_status = filing_status
        self.state_data = state_data
        
    def calculate_total_credits(self, taxable_incomes: list[float]) -> list[float]:
        """
        Calculate total California tax credits for each income scenario.
        
        Args:
            taxable_incomes: List of taxable income amounts
            income_taxes: List of calculated income tax amounts
            
        Returns:
            List of total credit amounts for each scenario
        """
        total_credits = []
        
        for taxable_income in taxable_incomes:
            credits = 0.0
            
            # California Earned Income Tax Credit (CalEITC)
            credits += self._calculate_cal_eitc(taxable_income)
            
            # Dependent exemption credits
            credits += self._calculate_dependent_exemption_credits()
            
            # Other California-specific credits
            credits += self._calculate_other_credits(taxable_income)
            
            total_credits.append(credits)
            
        return total_credits
    
    def _calculate_cal_eitc(self, taxable_income: float) -> float:
        """Calculate California Earned Income Tax Credit."""
        # CalEITC income limits and credit amounts
        if self.tax_year == 2024:
            if self.filing_status in [SINGLE, MARRIED_FILING_SEPARATELY, HEAD_OF_HOUSEHOLD]:
                if taxable_income <= 7000:
                    return min(255, taxable_income * 0.085)
                elif taxable_income <= 25220:
                    return max(0, 255 - (taxable_income - 7000) * 0.0596)
            elif self.filing_status == MARRIED_FILING_JOINTLY:
                if taxable_income <= 7000:
                    return min(255, taxable_income * 0.085)
                elif taxable_income <= 31220:
                    return max(0, 255 - (taxable_income - 7000) * 0.0596)
        elif self.tax_year == 2023:
            if self.filing_status in [SINGLE, MARRIED_FILING_SEPARATELY, HEAD_OF_HOUSEHOLD]:
                if taxable_income <= 7000:
                    return min(255, taxable_income * 0.085)
                elif taxable_income <= 25220:
                    return max(0, 255 - (taxable_income - 7000) * 0.0596)
            elif self.filing_status == MARRIED_FILING_JOINTLY:
                if taxable_income <= 7000:
                    return min(255, taxable_income * 0.085)
                elif taxable_income <= 31220:
                    return max(0, 255 - (taxable_income - 7000) * 0.0596)
        elif self.tax_year == 2022:
            if self.filing_status in [SINGLE, MARRIED_FILING_SEPARATELY, HEAD_OF_HOUSEHOLD]:
                if taxable_income <= 7000:
                    return min(255, taxable_income * 0.085)
                elif taxable_income <= 25220:
                    return max(0, 255 - (taxable_income - 7000) * 0.0596)
            elif self.filing_status == MARRIED_FILING_JOINTLY:
                if taxable_income <= 7000:
                    return min(255, taxable_income * 0.085)
                elif taxable_income <= 31220:
                    return max(0, 255 - (taxable_income - 7000) * 0.0596)
        
        return 0.0
    
    def _calculate_dependent_exemption_credits(self) -> float:
        """Calculate dependent exemption credits."""
        dependents = self.state_data.get('dependents', 0)
        
        # California dependent exemption
        if self.tax_year == 2024:
            return dependents * 154
        elif self.tax_year == 2023:
            return dependents * 151
        elif self.tax_year == 2022:
            return dependents * 148
            
        return 0.0
    
    def _calculate_other_credits(self, taxable_income: float) -> float:
        """Calculate other California-specific credits."""
        credits = 0.0
        
        # Young Child Tax Credit (if applicable)
        young_children = self.state_data.get('young_children_under_6', 0)
        if self.tax_year >= 2022 and young_children > 0:
            # Income limits for Young Child Tax Credit
            income_limit = 75000 if self.filing_status != MARRIED_FILING_JOINTLY else 150000
            if taxable_income <= income_limit:
                credits += young_children * 1000
        
        # Additional credits can be added here based on state_data
        # Examples: Senior exemption, blind exemption, etc.
        
        return credits 