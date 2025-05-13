import pytest


class TaxRequest:
    # TODO: Implement this class with appropriate fields
    tax_rate = {200000: 0, 500000: 10, 300000: 15, 1000000: 20}
    
    def __init__(self,salary: float, bonus: float):
        self.salary = salary
        self.bonus = bonus
        self.gross_pay = salary + bonus


class TaxResponse:
    tax_amount: float
    gross_pay: float
    net_pay: float


def calculate_tax(request: TaxRequest) -> TaxResponse:
    # TODO: Implement the tax calculation logic
    gross = request.gross_pay
    taxable = request.salary
    tax_amount = 0

    amount_levels=list(request.tax_rate)
    # loop through tax_rates dictionary to get the amount that is taxable (taxable)
    for amount,rate in request.tax_rate.items():
        taxable = taxable - amount
        # tax calculation when amount is above 1000000 or highest taxable level (please note that it is the excess above 1000000 or highest level that is taxed)
        if amount == amount_levels[-1]:
            if taxable > 0:
                tax_amount += taxable*(rate/100)
            break

        # stop when pay is no longer taxable
        if taxable <= 0:
            tax_amount += (taxable+amount)*(rate/100) if rate > 0 else 0
            break
        # calculate tax amount using provided tax rate
        tax_amount += amount*(rate/100) if rate > 0 else 0

    TaxResponse.gross_pay = gross
    TaxResponse.tax_amount = tax_amount
    TaxResponse.net_pay = gross - tax_amount
    return TaxResponse


'''
Instantiate Tax Request with positional parameters like this --> TaxRequest(salary, bonus)
'''
def test_calculate_tax():
    """Test with pytest"""
    
    test_case_1 = TaxRequest(0,50000)

    response_1 = calculate_tax(test_case_1)

    assert response_1.tax_amount == 0

    assert response_1.gross_pay == 50000

    assert response_1.net_pay == 50000


def test_calculate_tax_2():
    """Test with pytest"""

    test_case_2 = TaxRequest(500000,0)

    response_2 = calculate_tax(test_case_2)

    assert response_2.tax_amount == 30000

    assert response_2.gross_pay == 500000

    assert response_2.net_pay == 470000

def test_calculate_tax_3():
    """Test with pytest"""

    test_case_3 = TaxRequest(10000000,500000)

    response_3 = calculate_tax(test_case_3)

    assert response_3.tax_amount == 1695000

    assert response_3.gross_pay == 10500000

    assert response_3.net_pay == 8805000