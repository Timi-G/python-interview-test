import pytest

class TaxRequest:
    # TODO: Implement this class with appropriate fields
    tax_rate = {200000: 0, 500000: 10, 300000: 15, 1000000: 20}
    
    def __init__(self,gross_pay: float, bonus: float):
        self.gross_pay = gross_pay
        self.bonus = bonus
        self.taxable = gross_pay - bonus


class TaxResponse:
    tax_amount: float

    gross_pay: float

    net_pay: float


def calculate_tax(request: TaxRequest) -> TaxResponse:

    # TODO: Implement the tax calculation logic
    gross = request.gross_pay
    taxable = request.taxable
    tax_amount = 0

    # loop through rates to get the amount that is taxable (taxable) and tax to be paid (tax_amount)
    for amount,rate in request.tax_rate.items():
        taxable = taxable - amount
        # tax calculation when amount is above 1000000 (please note that it is the excess above 1000000 that is taxed)
        if amount == 1000000:
            if taxable > 0:
                tax_amount += taxable*(rate/100)
            break
        # calculate tax amount using provided tax rate
        tax_amount += amount*(rate/100) if rate > 0 else 0
        # stop when pay is no longer taxable
        if taxable <= 0:
            break
    TaxResponse.gross_pay = gross
    TaxResponse.tax_amount = tax_amount
    TaxResponse.net_pay = gross - tax_amount
    return TaxResponse


def test_calculate_tax():

    """Test with pytest"""

    test_case_1 = TaxRequest(0,20000)

    response_1 = calculate_tax(test_case_1)

    assert response_1.tax_amount == 50000

    assert response_1.gross_pay == 300000

    assert response_1.net_pay == 250000