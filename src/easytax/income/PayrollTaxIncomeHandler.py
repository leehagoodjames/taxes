# Income handler for Payroll/FICA taxes (Social Security and Medicare)
class PayrollTaxIncomeHandler:
    def __init__(self,
                # Income
                salaries_and_wages: float = 0, 
                ):

        # Income fields
        self.salaries_and_wages = salaries_and_wages

        # Notably omit long_term_capital_gains
        self.income_sources = [
            self.salaries_and_wages
        ]

        for i in self.income_sources:
            if type(i) not in (int, float):
                raise TypeError(f"Unsupported income type {type(i)} for income {i}")
        self.total_income = sum(self.income_sources)


        self.taxable_income = max(self.total_income, 0)
        if self.taxable_income < 0:
            raise ValueError(f"Taxable Income cannot be less than zero. Got {self.taxable_income}")
    
    def __eq__(self, other):
        if not isinstance(other, PayrollTaxIncomeHandler):
            return NotImplemented

        return (
            # Income
            self.salaries_and_wages == other.salaries_and_wages
        )

    def __str__(self):
        return (
            f"Payroll Income Handler:\n"
            f"Salaries and Wages: {self.salaries_and_wages}\n"
        )

    @classmethod
    def from_dict(cls, data: dict):

        # Set default values to 0 if not provided in data
        default_values = {
            # Income
            "salaries_and_wages": 0,
        }

        # Update default values with those provided in data
        for key in default_values.keys():
            if key in data:
                default_values[key] = data[key]

        for key in data.keys():
            if key not in default_values.keys():
                raise ValueError(f"Unsupported income for key {key}")

        # Create an instance of the class with the updated values
        return cls(**default_values)