import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

# Параметризованные тесты сложения
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, -3, -5),
    (0, 5, 5),
    (100, 200, 300),
    (0.5, 0.25, 0.75),
    (-1, 1, 0),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

# Параметризованные тесты вычитания
@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (4, 10, -6),
    (0, 0, 0),
    (100, 100, 0),
    (-5, -3, -2),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

# Параметризованные тесты умножения
@pytest.mark.parametrize("a, b, expected", [
    (6, 7, 42),
    (100, 0, 0),
    (-3, 4, -12),
    (-3, -4, 12),
    (2.5, 2, 5),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

# Параметризованные тесты деления
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (-10, 2, -5),
    (0, 5, 0),
    (100, 4, 25),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected

# Тесты проверки простого числа 
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
    (1, False),
    (0, False),
    (-5, False),
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) is expected

@pytest.mark.parametrize("a, b", [
    (10, 0),
    (0, 0),
    (-5, 0),
    (100, 0),
    (0.5, 0),
])
def test_divide_by_zero(calc, a, b):
    with pytest.raises(ValueError):
        calc.divide(a, b)