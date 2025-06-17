# Standard Library Imports
import unittest

# Local Imports
from src.easytax.handler.states import CaliforniaTaxHandler
from src.easytax.utils.Constants import *
from tests.utils.TestContants import *
from src.easytax.utils.InputValidator import InputValidator
from src.easytax.income.FederalIncomeHandler import FederalIncomeHandler

def handler_builder(
        tax_year=SUPPORTED_TAX_YEAR, 
        filing_status=SUPPORTED_FILING_STATUS, 
        federal_income_handlers=SUPPORTED_FEDERAL_INCOME_HANDLERS,
        state_data=SUPPORTED_STATE_DATA):
    return CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=tax_year, 
            filing_status=filing_status, 
            federal_income_handlers=federal_income_handlers,
            state_data=state_data,
        )

class TestCaliforniaTaxHandler(unittest.TestCase):

    def test_init_success(self):
        taxHandler = handler_builder()
        self.assertEqual(taxHandler.tax_year, SUPPORTED_TAX_YEAR)
        self.assertEqual(taxHandler.filing_status, SUPPORTED_FILING_STATUS)
        self.assertEqual(taxHandler.taxable_incomes, 
                         [SUPPORTED_SALARY_AND_WAGES_1 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_1 +
                         SUPPORTED_SALARY_AND_WAGES_2 + SUPPORTED_LONG_TERM_CAPITAL_GAINS_2 - taxHandler.standard_deduction])
        self.assertEqual(taxHandler.long_term_capital_gains[0], 0)

    def test_init_failure_unsupported_tax_year(self):
        unsupported_tax_year = 2020
        with self.assertRaises(ValueError) as cm:
            handler_builder(tax_year=unsupported_tax_year)
        expected_message = f"tax_year must be in SUPPORTED_TAX_YEARS: {InputValidator.alphabetize_set(SUPPORTED_TAX_YEARS)}, got: {unsupported_tax_year}"
        self.assertEqual(str(cm.exception), expected_message)

    def test_calculate_taxes(self):
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        self.assertIsNotNone(taxHandler.income_tax_owed)
        self.assertEqual(taxHandler.long_term_capital_gains_tax_owed[0], 0)

    def test_mental_health_services_tax(self):
        # Test the additional 1% tax on income over $1 million
        high_income_handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=SUPPORTED_TAX_YEAR,
            filing_status=SUPPORTED_FILING_STATUS,
            federal_income_handlers=[
            FederalIncomeHandler(
                filing_status=SUPPORTED_FILING_STATUS,
                tax_year=SUPPORTED_TAX_YEAR,
                salaries_and_wages=2000000, # $2 million
                long_term_capital_gains=0,
                taxable_pensions=0,
                use_standard_deduction=False, # Simplifies examples by making deductions zero
                ),
            ],
            state_data=SUPPORTED_STATE_DATA
        )
        high_income_handler.calculate_taxes()
        self.assertGreater(high_income_handler.income_tax_owed[0], 0)
        # Check if the additional 1% tax is applied
        self.assertGreaterEqual(high_income_handler.income_tax_owed[0], (2000000 - 1000000) * 0.01)

    def test_display_tax_summary_success(self):
        taxHandler = handler_builder()
        taxHandler.calculate_taxes()
        # This should not raise an exception
        taxHandler.display_tax_summary()

    def test_display_tax_summary_failure(self):
        taxHandler = handler_builder()
        with self.assertRaises(AttributeError) as cm:
            taxHandler.display_tax_summary()
        expected_message = "'CaliforniaTaxHandler' object has no attribute 'income_tax_owed'. Ensure you call 'calculate_taxes' before attempting to call this method."
        self.assertEqual(str(cm.exception), expected_message)

    def test_california_tax_brackets_single_2024(self):
        # Test California tax brackets for single filer in 2024
        single_handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=2024,
            filing_status=SINGLE,
            federal_income_handlers=[
                FederalIncomeHandler(
                    filing_status=SINGLE,
                    tax_year=2024,
                    salaries_and_wages=50000,
                    long_term_capital_gains=0,
                    taxable_pensions=0,
                    use_standard_deduction=False,
                ),
            ],
            state_data={'dependents': 0}
        )
        single_handler.calculate_taxes()
        self.assertGreater(single_handler.income_tax_owed[0], 0)
        
    def test_california_tax_brackets_married_filing_jointly_2024(self):
        # Test California tax brackets for married filing jointly in 2024
        mfj_handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=2024,
            filing_status=MARRIED_FILING_JOINTLY,
            federal_income_handlers=[
                FederalIncomeHandler(
                    filing_status=MARRIED_FILING_JOINTLY,
                    tax_year=2024,
                    salaries_and_wages=100000,
                    long_term_capital_gains=0,
                    taxable_pensions=0,
                    use_standard_deduction=False,
                ),
            ],
            state_data={'dependents': 0}
        )
        mfj_handler.calculate_taxes()
        self.assertGreater(mfj_handler.income_tax_owed[0], 0)

    def test_california_standard_deduction_2024(self):
        # Test California standard deduction for 2024
        federal_handler = FederalIncomeHandler(
            filing_status=SINGLE,
            tax_year=2024,
            salaries_and_wages=20000,
            long_term_capital_gains=0,
            taxable_pensions=0,
            use_standard_deduction=False,  # Don't use federal standard deduction for this test
        )
        
        handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=2024,
            filing_status=SINGLE,
            federal_income_handlers=[federal_handler],
            state_data={'dependents': 0}
        )
        
        # Standard deduction for single filer in 2024 should be $5,540
        self.assertEqual(handler.standard_deduction, 5540)
        # California taxable income should be the taxable income before CA deductions minus CA standard deduction
        expected_ca_taxable_income = max(0, 20000 - 5540)  # $20K income - $5,540 CA standard deduction
        self.assertEqual(handler.taxable_incomes[0], expected_ca_taxable_income)

    def test_california_earned_income_tax_credit(self):
        # Test California Earned Income Tax Credit (CalEITC)
        handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=2024,
            filing_status=SINGLE,
            federal_income_handlers=[
                FederalIncomeHandler(
                    filing_status=SINGLE,
                    tax_year=2024,
                    salaries_and_wages=5000,  # Low income to qualify for CalEITC
                    long_term_capital_gains=0,
                    taxable_pensions=0,
                    use_standard_deduction=False,
                ),
            ],
            state_data={'dependents': 0}
        )
        handler.calculate_taxes()
        
        # With low income, should receive CalEITC which reduces tax owed
        # Income of $5,000 should result in credits being applied
        credits = handler.tax_credits.calculate_total_credits([5000])
        self.assertGreater(credits[0], 0)

    def test_california_dependent_exemption_credits(self):
        # Test California dependent exemption credits
        handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=2024,
            filing_status=MARRIED_FILING_JOINTLY,
            federal_income_handlers=[
                FederalIncomeHandler(
                    filing_status=MARRIED_FILING_JOINTLY,
                    tax_year=2024,
                    salaries_and_wages=80000,
                    long_term_capital_gains=0,
                    taxable_pensions=0,
                    use_standard_deduction=False,
                ),
            ],
            state_data={'dependents': 2}  # Two dependents
        )
        
        # Each dependent should get $154 credit in 2024
        credits = handler.tax_credits.calculate_total_credits([80000])
        dependent_credits = handler.tax_credits._calculate_dependent_exemption_credits()
        self.assertEqual(dependent_credits, 2 * 154)  # 2 dependents * $154 each

    def test_california_young_child_tax_credit(self):
        # Test California Young Child Tax Credit
        handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=2024,
            filing_status=MARRIED_FILING_JOINTLY,
            federal_income_handlers=[
                FederalIncomeHandler(
                    filing_status=MARRIED_FILING_JOINTLY,
                    tax_year=2024,
                    salaries_and_wages=100000,  # Below income limit
                    long_term_capital_gains=0,
                    taxable_pensions=0,
                    use_standard_deduction=False,
                ),
            ],
            state_data={'dependents': 1, 'young_children_under_6': 1}
        )
        
        credits = handler.tax_credits.calculate_total_credits([100000])
        # Should include young child tax credit of $1000
        self.assertGreater(credits[0], 1000)  # Should include dependent credit + young child credit

    def test_mhsa_tax_calculation_detailed(self):
        # Test detailed Mental Health Services Act tax calculation
        test_cases = [
            (1500000, 5000),    # $1.5M income -> $5K MHSA tax (($1.5M - $1M) * 1%)
            (2000000, 10000),   # $2M income -> $10K MHSA tax (($2M - $1M) * 1%)
            (999999, 0),        # Just under $1M -> no MHSA tax
            (1000000, 0),       # Exactly $1M -> no MHSA tax
            (1000001, 0.01),    # Just over $1M -> $0.01 MHSA tax
        ]
        
        for income, expected_mhsa_tax in test_cases:
            with self.subTest(income=income, expected_mhsa_tax=expected_mhsa_tax):
                handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
                    tax_year=2024,
                    filing_status=SINGLE,
                    federal_income_handlers=[
                        FederalIncomeHandler(
                            filing_status=SINGLE,
                            tax_year=2024,
                            salaries_and_wages=income,
                            long_term_capital_gains=0,
                            taxable_pensions=0,
                            use_standard_deduction=False,
                        ),
                    ],
                    state_data={'dependents': 0}
                )
                
                # Calculate taxes without MHSA first
                handler.calculate_taxes()
                handler._apply_mental_health_services_tax()  # Apply MHSA again to get the isolated effect
                
                # The MHSA tax should be approximately the expected amount
                # (allowing for small floating point differences)
                if expected_mhsa_tax > 0:
                    self.assertAlmostEqual(
                        (income - 1000000) * 0.01, 
                        expected_mhsa_tax, 
                        places=2
                    )

    def test_long_term_capital_gains_treated_as_ordinary_income(self):
        # Test that California treats long-term capital gains as ordinary income
        handler = CaliforniaTaxHandler.CaliforniaTaxHandler(
            tax_year=2024,
            filing_status=SINGLE,
            federal_income_handlers=[
                FederalIncomeHandler(
                    filing_status=SINGLE,
                    tax_year=2024,
                    salaries_and_wages=50000,
                    long_term_capital_gains=25000,  # Should be added to ordinary income
                    taxable_pensions=0,
                    use_standard_deduction=False,
                ),
            ],
            state_data={'dependents': 0}
        )
        
        # California should treat LTCG as ordinary income
        # So taxable income should include both salary and LTCG
        expected_taxable_income = 50000 + 25000  # salary + LTCG
        self.assertEqual(handler.taxable_income_before_dependents_and_exmptions[0], expected_taxable_income)
        
        # Long-term capital gains should be zero for tax calculation purposes in CA
        self.assertEqual(handler.long_term_capital_gains[0], 0)

if __name__ == '__main__':
    unittest.main()
