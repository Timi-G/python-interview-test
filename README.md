# python-interview-test

Instructions
Submission format: .py file
Submission Time: Before EOD

Create a Python tax calculator with the following specifications:

First ₦200,000 of salary is tax-free
Next ₦500,000 is taxed at 10%
Next ₦300,000 is taxed at 15%
Any amount above ₦1,000,000 is taxed at 20%
Bonuses are not taxed, but are included in gross pay
The function should return a response with tax amount, gross pay, and net pay

Requirements:

- Complete the implementation of the TaxRequest class to hold appropriate input data
- Implement the calculate_tax function according to the specifications
- Handle edge cases appropriately
- Add docstrings and type hints
- Use pytest to test and verify solution, test for errors also.
- Attach requirement.txt if needed

```python
class TaxRequest:

    # TODO: Implement this class with appropriate fields

    pass



class TaxResponse:

    tax_amount: Decimal

    gross_pay: Decimal

    net_pay: Decimal


def calculate_tax(request: TaxRequest) -> TaxResponse:

    # TODO: Implement the tax calculation logic

    pass



def test_calculate_tax():

    """Test with pytest"""

    # test_case_1 = TaxRequest(...)

    # response_1 = calculate_tax(test_case_1)

    # assert response_1.tax_amount == expected_tax_amount

    # assert response_1.gross_pay == expected_gross_pay

    # assert response_1.net_pay == expected_net_pay
```
