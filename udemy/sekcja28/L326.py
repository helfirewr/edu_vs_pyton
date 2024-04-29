
# pip install pytest
# uruchomienie testów to wywołanie po prostu "pytest" w terminalu

# Wprowadzenie:
# Pytest to framework do testowania kodu Python, umożliwiający pisanie prostych
# oraz zaawansowanych testów.
# W tej lekcji dowiesz się, jak zainstalować Pytest, stworzyć podstawowy test, oraz uruchomić testy.
# Zacznijmy od instalacji Pytest za pomocą pip, a następnie przejdziemy
# do tworzenia i uruchamiania prostego testu.


# Przykład funkcji do testowania i testu:

# Definicja prostej funkcji, którą będziemy testować
def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# Test sprawdzający poprawność działania funkcji `add`
def test_add():
    """Checks if the `add` function works correctly."""
    assert add(2, 3) == 5  # Verifies that adding 2 and 3 results in 5

# W test_add, używamy instrukcji assert do sprawdzenia, czy wynik działania funkcji add(2, 3) jest równy 5.
# Jeśli tak, test zostaje zaliczony. W przeciwnym razie, Pytest zgłosi błąd.

# Uruchamianie testów:
# Aby uruchomić testy, otwórz terminal w katalogu z plikami testowymi i wpisz `pytest`.


# Wprowadzenie:
# Parametryzacja testów w Pytest pozwala na uruchomienie tego samego testu z różnymi zestawami danych.
# Jest to szczególnie użyteczne, gdy chcemy przetestować funkcję z różnymi wartościami wejściowymi.
# W tej lekcji nauczymy się, jak używać parametryzacji w Pytest.

import pytest

# Przykład funkcji do testowania
def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

# Użycie parametryzacji w Pytest do testowania funkcji `multiply` z różnymi zestawami
# danych
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),  # Test case 1: 2 * 3 = 6
    (3, 7, 21),  # Test case 2: 3 * 7 = 21
    (5, 5, 25),  # Test case 3: 5 * 5 = 25
    (0, 4, 0)    # Test case 4: 0 * 4 = 0
])
def test_multiply(x, y, expected):
    """Checks if the `multiply` function works correctly with different sets of inputs."""
    assert multiply(x, y) == expected  # Verifies that multiply(x, y) results in expected output

# W funkcji test_multiply, parametry `x`, `y` i `expected` są wartościami, które
# będą różne dla każdego zestawu danych.
# Dekorator @pytest.mark.parametrize jest używany do określenia zestawów danych
# (parametrów testowych) oraz oczekiwanych wyników.
# Dla każdego zestawu danych, Pytest automatycznie generuje i wykonuje test.
