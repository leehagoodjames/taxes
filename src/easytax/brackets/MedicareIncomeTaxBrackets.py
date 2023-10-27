# Local Imports
from ..base import FlatTax
from ..base import FlatTaxBracket


# 2023 Medicare Employee Rate
# Source: https://www.irs.gov/publications/p80#:~:text=Social%20security%20and%20Medicare%20tax%20for%202023.&text=The%20Medicare%20tax%20rate%20is,in%20cash%20wages%20in%202023.
individual_2023_tax = FlatTax.FlatTax(FlatTaxBracket.FlatTaxBracket(0.0145))

# 2022 Medicare Employee Rate
# Source: https://www.irs.gov/publications/p80#:~:text=Social%20security%20and%20Medicare%20tax%20for%202023.&text=The%20Medicare%20tax%20rate%20is,in%20cash%20wages%20in%202023.
individual_2022_tax = FlatTax.FlatTax(FlatTaxBracket.FlatTaxBracket(0.0145))

