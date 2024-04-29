# Wprowadzenie:
# Testowanie różnych podstawowych typów danych w Pythonie jest kluczowe
# dla zapewnienia poprawności działania kodu.
# W tej lekcji zobaczymy, jak za pomocą Pytest testować funkcje
# obsługujące liczby, napisy, listy i słowniki.

import pytest

# Funkcje do testowania

def reverse_string(s):
    """Reverses a string and returns the result."""
    return s[::-1]

def add_to_list(lst, item):
    """Adds an item to a list and returns the list."""
    lst.append(item)
    return lst

def update_dictionary(dct, key, value):
    """Updates a dictionary with a key-value pair and returns the dictionary."""
    dct[key] = value
    return dct

# Testy

def test_reverse_string():
    """Tests if a string is correctly reversed."""
    assert reverse_string("hello") == "olleh"  # Test reversing a simple string

@pytest.mark.parametrize("lst, item, expected", [
    ([1, 2], 3, [1, 2, 3]),  # Adding to a list of integers
    (["a", "b"], "c", ["a", "b", "c"]),  # Adding to a list of strings
])
def test_add_to_list(lst, item, expected):
    """Tests if an item is correctly added to a list."""
    assert add_to_list(lst, item) == expected

@pytest.mark.parametrize("dct, key, value, expected", [
    ({"a": 1}, "b", 2, {"a": 1, "b": 2}),  # Adding a new key-value pair
    ({"x": 10}, "x", 20, {"x": 20}),  # Updating an existing key
])
def test_update_dictionary(dct, key, value, expected):
    """Tests if a dictionary is correctly updated with a key-value pair."""
    assert update_dictionary(dct, key, value) == expected

# Uruchamianie testów:
# Aby uruchomić testy, użyj polecenia `pytest` w terminalu.
