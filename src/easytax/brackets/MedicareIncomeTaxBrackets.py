# Local Imports
from easytax.base import FlatTax
from easytax.base import FlatTaxBracket


# 2022 Medicare Employee Rate
# Source: https://www.irs.gov/publications/p80#:~:text=Social%20security%20and%20Medicare%20tax%20for%202023.&text=The%20Medicare%20tax%20rate%20is,in%20cash%20wages%20in%202023.
medicare_employee_2022_tax = FlatTax.FlatTax(FlatTaxBracket.FlatTaxBracket(0.0145))

# 2023 Medicare Employee Rate
# Source: https://www.irs.gov/publications/p80#:~:text=Social%20security%20and%20Medicare%20tax%20for%202023.&text=The%20Medicare%20tax%20rate%20is,in%20cash%20wages%20in%202023.
medicare_employee_2023_tax = FlatTax.FlatTax(FlatTaxBracket.FlatTaxBracket(0.0145))
