"""
External Sources module for tax calculation verification.

This module provides tools for verifying tax calculations against external sources of truth.
"""

from .external_tax_verifier import ExternalTaxVerifier, ExternalTaxSource, default_verifier

__all__ = ['ExternalTaxVerifier', 'ExternalTaxSource', 'default_verifier']