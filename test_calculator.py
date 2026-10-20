import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    # Фикстура (создаёт экземпляр калькулятора для каждого теста)
    return Calculator()

# Тесты для add
def test_add_positive(calc):
    assert calc.add(2, 3) == 5

def test_add_negative(calc):
    assert calc.add(-2, -3) == -5

def test_add_zero(calc):
    assert calc.add(0, 5) == 5

# Тесты для subtract
def test_subtract_positive(calc):
    assert calc.subtract(10, 4) == 6

def test_subtract_negative_result(calc):
    assert calc.subtract(4, 10) == -6

# Тесты для multiply
def test_multiply_positive(calc):
    assert calc.multiply(6, 7) == 42

def test_multiply_by_zero(calc):
    assert calc.multiply(100, 0) == 0

# Тесты для divide
def test_divide_positive(calc):
    assert calc.divide(10, 2) == 5

def test_divide_fractional(calc):
    assert calc.divide(5, 2) == 2.5

# Тесты для is_prime_number
def test_is_prime_true(calc):
    assert calc.is_prime_number(7) is True

def test_is_prime_false(calc):
    assert calc.is_prime_number(8) is False

def test_divide_by_zero_raises_exception(calc):
    # При делении на ноль должно выбрасываться ValueError
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_divide_by_zero_message(calc):
    # Проверка текста сообщения об ошибке
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        calc.divide(10, 0)