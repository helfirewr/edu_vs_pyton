# Wprowadzenie:
# Ta lekcja skupia się na testowaniu wyjątków w Pythonie z użyciem Pytest.
# Testowanie wyjątków pozwala sprawdzić, czy nasz kod odpowiednio reaguje na błędy
# lub nieprawidłowe dane. Pytest oferuje prostą składnię do testowania
# rzucanych wyjątków, co jest kluczowe dla budowania odpornych aplikacji.

import pytest

# Przykładowa funkcja, która może rzucić wyjątek
def divide(x, y):
    """Divides x by y. Raises ValueError if y is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

# Test sprawdzający, czy funkcja divide rzuci odpowiedni wyjątek przy dzieleniu przez zero
def test_divide_zero():
    """Tests if the `divide` function raises a ValueError when attempting to divide by zero."""
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    # Sprawdza, czy komunikat wyjątku jest prawidłowy
    assert "Cannot divide by zero" in str(excinfo.value)

# Test sprawdzający, czy funkcja divide zwraca poprawny wynik dla prawidłowych danych
def test_divide_valid():
    """Tests if the `divide` function returns the correct result when dividing two numbers."""
    assert divide(10, 2) == 5  # Sprawdza, czy 10 podzielone przez 2 równa się 5
