'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    assert Calculator.add(2,2) == 4

def test_subtraction():
    assert Calculator.subtract(3,2) == 1

def test_multiply():
    assert Calculator.multiply(2,2) == 4

def test_divide():
    assert Calculator.divide(4,2) == 2
    