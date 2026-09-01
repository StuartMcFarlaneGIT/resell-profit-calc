import pytest
from calculator import promotion_fees, profit_calculator, profit_percentage


def profit_percentage_normal():
    assert profit_percentage(100, 81) == 81

def test_profit_percentage_zero_buy():
    assert profit_percentage(0, 50) == 0.00

def test_profit_calculator():
    assert profit_calculator(10, 20, 0.60, 2.94) == pytest.approx(6.46)

def test_promotion_fees():
    assert promotion_fees(100, 0.03) == 3.00
