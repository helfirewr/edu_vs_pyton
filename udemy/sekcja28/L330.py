# Wprowadzenie:
# Ta lekcja koncentruje się na testowaniu klas w Pythonie z użyciem Pytest,
# w tym na metodach instancji, statycznych oraz metodach klasy.
# Testowanie klas jest kluczowe dla zapewnienia
# poprawności obiektowo zorientowanego kodu.
# Przyjrzymy się, jak przygotować testy dla różnych typów metod
# oraz jak weryfikować zwracane przez nie wartości.

import pytest

# Przykład klasy do testowania
class MathOperations:
    """Class that performs basic math operations."""

    def __init__(self, base_value=0):
        self.base_value = base_value

    def add(self, value):
        """Adds a value to the base_value."""
        return self.base_value + value

    @staticmethod
    def subtract(a, b):
        """Subtracts two values."""
        return a - b

    @classmethod
    def multiply(cls, a, b):
        """Multiplies two values."""
        return a * b

# Testowanie metody instancji
def test_add():
    """Tests the add method of MathOperations class."""
    math_op = MathOperations(10)  # Inicjalizacja instancji klasy z base_value = 10
    assert math_op.add(5) == 15  # Testowanie metody add

# Testowanie metody statycznej
def test_subtract():
    """Tests the static method subtract of the MathOperations class."""
    assert MathOperations.subtract(10, 5) == 5  # Testowanie metody statycznej subtract

# Testowanie metody klasy
def test_multiply():
    """Tests the class method multiply of the MathOperations class."""
    assert MathOperations.multiply(3, 4) == 12  # Testowanie metody klasy multiply
