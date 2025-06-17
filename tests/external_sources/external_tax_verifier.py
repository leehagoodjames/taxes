"""
External Tax Verifier Framework

This module provides a framework for verifying tax calculations against external sources of truth.
It supports multiple external sources and provides fallback mechanisms when sources are unavailable.
"""

import json
import time
import hashlib
from typing import Dict, List, Optional, Any, Union
from abc import ABC, abstractmethod
from pathlib import Path


class ExternalTaxSource(ABC):
    """Abstract base class for external tax calculation sources."""
    
    @abstractmethod
    def calculate_federal_income_tax(self, 
                                   income: float, 
                                   filing_status: str, 
                                   tax_year: int,
                                   deductions: float = 0) -> Optional[float]:
        """Calculate federal income tax using external source."""
        pass
    
    @abstractmethod
    def calculate_state_income_tax(self, 
                                 income: float, 
                                 state: str, 
                                 filing_status: str, 
                                 tax_year: int,
                                 deductions: float = 0) -> Optional[float]:
        """Calculate state income tax using external source."""
        pass
    
    @abstractmethod
    def calculate_long_term_capital_gains_tax(self, 
                                            gains: float, 
                                            income: float,
                                            filing_status: str, 
                                            tax_year: int) -> Optional[float]:
        """Calculate long-term capital gains tax using external source."""
        pass
    
    @abstractmethod
    def calculate_payroll_taxes(self, 
                              wages: float, 
                              tax_year: int) -> Optional[Dict[str, float]]:
        """Calculate payroll taxes (Social Security, Medicare) using external source."""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if this external source is currently available."""
        pass
    
    @abstractmethod
    def get_source_name(self) -> str:
        """Get a human-readable name for this source."""
        pass


class IRSPublicationSource(ExternalTaxSource):
    """
    Source based on IRS publications and tax tables.
    Uses publicly available IRS data for verification.
    """
    
    def __init__(self):
        self.name = "IRS Publications"
        # In a real implementation, this would load IRS tax tables
        # For now, we'll use known accurate calculations for 2023
        self._load_irs_data()
    
    def _load_irs_data(self):
        """Load IRS tax tables and brackets."""
        # 2023 Federal Income Tax Brackets - Married Filing Jointly
        self.federal_brackets_2023_mfj = [
            (22275, 0.10),   # 10% on income up to $22,275
            (89450, 0.12),   # 12% on income from $22,275 to $89,450
            (190750, 0.22),  # 22% on income from $89,450 to $190,750
            (364200, 0.24),  # 24% on income from $190,750 to $364,200
            (462500, 0.32),  # 32% on income from $364,200 to $462,500
            (693750, 0.35),  # 35% on income from $462,500 to $693,750
            (float('inf'), 0.37)  # 37% on income over $693,750
        ]
        
        # 2023 Standard Deduction - Married Filing Jointly
        self.standard_deduction_2023_mfj = 27700
        
        # 2023 Long-Term Capital Gains Rates - Married Filing Jointly
        self.ltcg_brackets_2023_mfj = [
            (89250, 0.0),    # 0% on gains if total income <= $89,250
            (553850, 0.15),  # 15% on gains if total income $89,250 - $553,850
            (float('inf'), 0.20)  # 20% on gains if total income > $553,850
        ]
        
        # 2023 Social Security and Medicare rates
        self.social_security_rate = 0.062
        self.medicare_rate = 0.0145
        self.social_security_wage_base = 160200
    
    def calculate_federal_income_tax(self, 
                                   income: float, 
                                   filing_status: str, 
                                   tax_year: int,
                                   deductions: float = 0) -> Optional[float]:
        """Calculate federal income tax based on IRS tax brackets."""
        if tax_year != 2023 or filing_status != "Married Filing Jointly":
            return None
        
        # Apply deductions (use standard deduction if deductions is 0)
        if deductions == 0:
            deductions = self.standard_deduction_2023_mfj
        
        taxable_income = max(0, income - deductions)
        
        tax_owed = 0
        previous_bracket = 0
        
        for bracket_limit, rate in self.federal_brackets_2023_mfj:
            if taxable_income <= previous_bracket:
                break
            
            taxable_in_bracket = min(taxable_income, bracket_limit) - previous_bracket
            tax_owed += taxable_in_bracket * rate
            previous_bracket = bracket_limit
        
        return round(tax_owed, 2)
    
    def calculate_state_income_tax(self, 
                                 income: float, 
                                 state: str, 
                                 filing_status: str, 
                                 tax_year: int,
                                 deductions: float = 0) -> Optional[float]:
        """Calculate state income tax - limited implementation for Georgia."""
        if tax_year != 2023 or filing_status != "Married Filing Jointly" or state != "Georgia":
            return None
        
        # Georgia 2023 tax brackets for MFJ
        ga_brackets = [
            (1000, 0.01),
            (3000, 0.02),
            (5000, 0.03),
            (7000, 0.04),
            (10000, 0.05),
            (float('inf'), 0.0575)
        ]
        
        # Georgia standard deduction for MFJ 2023
        ga_standard_deduction = 6000
        
        if deductions == 0:
            deductions = ga_standard_deduction
        
        taxable_income = max(0, income - deductions)
        
        tax_owed = 0
        previous_bracket = 0
        
        for bracket_limit, rate in ga_brackets:
            if taxable_income <= previous_bracket:
                break
            
            taxable_in_bracket = min(taxable_income, bracket_limit) - previous_bracket
            tax_owed += taxable_in_bracket * rate
            previous_bracket = bracket_limit
        
        return round(tax_owed, 2)
    
    def calculate_long_term_capital_gains_tax(self, 
                                            gains: float, 
                                            income: float,
                                            filing_status: str, 
                                            tax_year: int) -> Optional[float]:
        """Calculate long-term capital gains tax based on IRS rates."""
        if tax_year != 2023 or filing_status != "Married Filing Jointly":
            return None
        
        total_income = income + gains
        
        for bracket_limit, rate in self.ltcg_brackets_2023_mfj:
            if total_income <= bracket_limit:
                return round(gains * rate, 2)
        
        return round(gains * 0.20, 2)  # Fallback to highest rate
    
    def calculate_payroll_taxes(self, 
                              wages: float, 
                              tax_year: int) -> Optional[Dict[str, float]]:
        """Calculate payroll taxes based on IRS rates."""
        if tax_year != 2023:
            return None
        
        # Social Security tax (capped at wage base)
        ss_wages = min(wages, self.social_security_wage_base)
        social_security_tax = round(ss_wages * self.social_security_rate, 2)
        
        # Medicare tax (no cap)
        medicare_tax = round(wages * self.medicare_rate, 2)
        
        return {
            'social_security': social_security_tax,
            'medicare': medicare_tax
        }
    
    def is_available(self) -> bool:
        """IRS publication data is always available."""
        return True
    
    def get_source_name(self) -> str:
        return self.name


class CacheManager:
    """Manages caching of external source results to avoid repeated API calls."""
    
    def __init__(self, cache_dir: str = "tests/external_sources/.cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_file = self.cache_dir / "tax_calculations.json"
        self._load_cache()
    
    def _load_cache(self):
        """Load existing cache from disk."""
        try:
            if self.cache_file.exists():
                with open(self.cache_file, 'r') as f:
                    self.cache = json.load(f)
            else:
                self.cache = {}
        except Exception:
            self.cache = {}
    
    def _save_cache(self):
        """Save cache to disk."""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except Exception:
            pass  # Fail silently if we can't save cache
    
    def _generate_key(self, **kwargs) -> str:
        """Generate a cache key from the calculation parameters."""
        # Sort keys for consistent hashing
        sorted_items = sorted(kwargs.items())
        key_string = json.dumps(sorted_items, sort_keys=True)
        return hashlib.md5(key_string.encode()).hexdigest()
    
    def get(self, calculation_type: str, **kwargs) -> Optional[Any]:
        """Get cached result if available and not expired."""
        key = self._generate_key(type=calculation_type, **kwargs)
        
        if key in self.cache:
            cached_item = self.cache[key]
            # Check if cache is still valid (24 hours)
            if time.time() - cached_item.get('timestamp', 0) < 86400:
                return cached_item.get('result')
        
        return None
    
    def set(self, calculation_type: str, result: Any, **kwargs):
        """Cache a calculation result."""
        key = self._generate_key(type=calculation_type, **kwargs)
        self.cache[key] = {
            'result': result,
            'timestamp': time.time()
        }
        self._save_cache()


class ExternalTaxVerifier:
    """
    Main class for verifying tax calculations against external sources.
    
    Supports multiple external sources with fallback mechanisms and caching.
    """
    
    def __init__(self, sources: Optional[List[ExternalTaxSource]] = None):
        self.sources = sources or [IRSPublicationSource()]
        self.cache = CacheManager()
    
    def add_source(self, source: ExternalTaxSource):
        """Add an external tax calculation source."""
        self.sources.append(source)
    
    def verify_federal_income_tax(self, 
                                expected: float,
                                income: float, 
                                filing_status: str, 
                                tax_year: int,
                                deductions: float = 0,
                                tolerance: float = 0.01) -> Dict[str, Any]:
        """
        Verify federal income tax calculation against external sources.
        
        Returns:
            Dict with verification results including matches, differences, and source info
        """
        cache_key_params = {
            'income': income,
            'filing_status': filing_status,
            'tax_year': tax_year,
            'deductions': deductions
        }
        
        # Check cache first
        cached_result = self.cache.get('federal_income_tax', **cache_key_params)
        if cached_result is not None:
            return self._create_verification_result(expected, cached_result, 'cached', tolerance)
        
        # Try each source
        for source in self.sources:
            if not source.is_available():
                continue
            
            try:
                calculated = source.calculate_federal_income_tax(
                    income, filing_status, tax_year, deductions
                )
                
                if calculated is not None:
                    # Cache the result
                    self.cache.set('federal_income_tax', calculated, **cache_key_params)
                    
                    return self._create_verification_result(
                        expected, calculated, source.get_source_name(), tolerance
                    )
            except Exception as e:
                continue  # Try next source
        
        # No sources available
        return {
            'verified': False,
            'expected': expected,
            'calculated': None,
            'difference': None,
            'source': 'none available',
            'within_tolerance': False,
            'error': 'No external sources available for verification'
        }
    
    def verify_state_income_tax(self, 
                              expected: float,
                              income: float, 
                              state: str,
                              filing_status: str, 
                              tax_year: int,
                              deductions: float = 0,
                              tolerance: float = 0.01) -> Dict[str, Any]:
        """Verify state income tax calculation against external sources."""
        cache_key_params = {
            'income': income,
            'state': state,
            'filing_status': filing_status,
            'tax_year': tax_year,
            'deductions': deductions
        }
        
        cached_result = self.cache.get('state_income_tax', **cache_key_params)
        if cached_result is not None:
            return self._create_verification_result(expected, cached_result, 'cached', tolerance)
        
        for source in self.sources:
            if not source.is_available():
                continue
            
            try:
                calculated = source.calculate_state_income_tax(
                    income, state, filing_status, tax_year, deductions
                )
                
                if calculated is not None:
                    self.cache.set('state_income_tax', calculated, **cache_key_params)
                    return self._create_verification_result(
                        expected, calculated, source.get_source_name(), tolerance
                    )
            except Exception:
                continue
        
        return self._create_no_source_result(expected)
    
    def verify_long_term_capital_gains_tax(self, 
                                         expected: float,
                                         gains: float, 
                                         income: float,
                                         filing_status: str, 
                                         tax_year: int,
                                         tolerance: float = 0.01) -> Dict[str, Any]:
        """Verify long-term capital gains tax calculation against external sources."""
        cache_key_params = {
            'gains': gains,
            'income': income,
            'filing_status': filing_status,
            'tax_year': tax_year
        }
        
        cached_result = self.cache.get('ltcg_tax', **cache_key_params)
        if cached_result is not None:
            return self._create_verification_result(expected, cached_result, 'cached', tolerance)
        
        for source in self.sources:
            if not source.is_available():
                continue
            
            try:
                calculated = source.calculate_long_term_capital_gains_tax(
                    gains, income, filing_status, tax_year
                )
                
                if calculated is not None:
                    self.cache.set('ltcg_tax', calculated, **cache_key_params)
                    return self._create_verification_result(
                        expected, calculated, source.get_source_name(), tolerance
                    )
            except Exception:
                continue
        
        return self._create_no_source_result(expected)
    
    def verify_payroll_taxes(self, 
                           expected_ss: float,
                           expected_medicare: float,
                           wages: float, 
                           tax_year: int,
                           tolerance: float = 0.01) -> Dict[str, Any]:
        """Verify payroll tax calculations against external sources."""
        cache_key_params = {
            'wages': wages,
            'tax_year': tax_year
        }
        
        cached_result = self.cache.get('payroll_taxes', **cache_key_params)
        if cached_result is not None:
            return self._create_payroll_verification_result(
                expected_ss, expected_medicare, cached_result, 'cached', tolerance
            )
        
        for source in self.sources:
            if not source.is_available():
                continue
            
            try:
                calculated = source.calculate_payroll_taxes(wages, tax_year)
                
                if calculated is not None:
                    self.cache.set('payroll_taxes', calculated, **cache_key_params)
                    return self._create_payroll_verification_result(
                        expected_ss, expected_medicare, calculated, 
                        source.get_source_name(), tolerance
                    )
            except Exception:
                continue
        
        return {
            'verified': False,
            'expected_social_security': expected_ss,
            'expected_medicare': expected_medicare,
            'calculated_social_security': None,
            'calculated_medicare': None,
            'source': 'none available',
            'within_tolerance': False,
            'error': 'No external sources available for verification'
        }
    
    def _create_verification_result(self, expected: float, calculated: float, 
                                  source: str, tolerance: float) -> Dict[str, Any]:
        """Create a verification result dictionary."""
        difference = abs(expected - calculated) if calculated is not None else None
        within_tolerance = difference is not None and difference <= tolerance
        
        return {
            'verified': True,
            'expected': expected,
            'calculated': calculated,
            'difference': difference,
            'source': source,
            'within_tolerance': within_tolerance,
            'error': None
        }
    
    def _create_payroll_verification_result(self, expected_ss: float, expected_medicare: float,
                                          calculated: Dict[str, float], source: str, 
                                          tolerance: float) -> Dict[str, Any]:
        """Create a payroll tax verification result."""
        calc_ss = calculated.get('social_security', 0)
        calc_medicare = calculated.get('medicare', 0)
        
        ss_diff = abs(expected_ss - calc_ss)
        medicare_diff = abs(expected_medicare - calc_medicare)
        
        within_tolerance = (ss_diff <= tolerance and medicare_diff <= tolerance)
        
        return {
            'verified': True,
            'expected_social_security': expected_ss,
            'expected_medicare': expected_medicare,
            'calculated_social_security': calc_ss,
            'calculated_medicare': calc_medicare,
            'ss_difference': ss_diff,
            'medicare_difference': medicare_diff,
            'source': source,
            'within_tolerance': within_tolerance,
            'error': None
        }
    
    def _create_no_source_result(self, expected: float) -> Dict[str, Any]:
        """Create a result when no external sources are available."""
        return {
            'verified': False,
            'expected': expected,
            'calculated': None,
            'difference': None,
            'source': 'none available',
            'within_tolerance': False,
            'error': 'No external sources available for verification'
        }


# Global instance for easy access in tests
default_verifier = ExternalTaxVerifier()