# Wprowadzenie:
# W tej lekcji skupimy się na mockowaniu w Pytest, używając modułu `unittest.mock`.
# Mockowanie pozwala symulować zachowania zewnętrznych zależności, co jest kluczowe
# dla izolowania testów i zapewnienia ich niezawodności.
# Poznamy podstawy stosowania obiektów mock oraz jak kontrolować
# ich zachowanie i weryfikować interakcje.

from unittest.mock import MagicMock, patch
import pytest

# Przykład funkcji wykorzystującej zewnętrzną zależność (np. wysyłanie zapytania do API)
def fetch_data(api_client, url):
    """Fetches data from a URL using an API client."""
    response = api_client.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Testowanie funkcji z użyciem mocka
def test_fetch_data():
    """Tests the fetch_data function using a mock API client."""
    # Tworzenie mocka dla API klienta
    # Użycie `MagicMock` do symulacji API klienta umożliwia
    # kontrolowanie zwracanych wartości oraz sprawdzanie,
    # jakie wywołania zostały wykonane na mocku. Metoda `get.return_value`
    # pozwala zdefiniować wartość zwracaną
    # przez metodę `get` naszego mocka. Dzięki `return_value.json.return_value`,
    # możemy również określić wynik, jaki zostanie zwrócony po wywołaniu metody
    # `json` na obiekcie zwróconym przez `get`.
    mock_api_client = MagicMock()
    mock_api_client.get.return_value.status_code = 200
    mock_api_client.get.return_value.json.return_value = {"data": "Test data"}

    # Wywołanie funkcji z mockowanym klientem API
    result = fetch_data(mock_api_client, "https://fakeurl.com")

    # Sprawdzanie, czy wynik jest zgodny z oczekiwaniami
    assert result == {"data": "Test data"}

    # Weryfikacja, czy mock został wywołany z oczekiwanym URL
    mock_api_client.get.assert_called_with("https://fakeurl.com")


# Funkcja `assert_called_with` pozwala na weryfikację, czy mockowany obiekt
# został wywołany z określonymi argumentami,
# co jest przydatne do sprawdzania poprawności interakcji z zależnościami.
