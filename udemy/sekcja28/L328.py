# Import Pytest
import pytest

# W tej lekcji skoncentrujemy się na wykorzystaniu fixture w Pytest, które są potężnym
# narzędziem do tworzenia danych wejściowych dla testów, konfiguracji środowiska testowego,
# lub czyszczenia po wykonaniu testów. Fixtures pozwalają na ponowne używanie kodu w testach,
# co jest szczególnie przydatne w przypadku, gdy potrzebujesz tych samych danych
# wejściowych lub stanu środowiska dla wielu testów.

# Fixture to funkcja, która jest uruchamiana przez Pytest przed (i opcjonalnie po)
# wykonaniem testów, które jej wymagają. Służy do przygotowania środowiska testowego
# lub dostarczenia danych do testów. Można ją zdefiniować za pomocą
# dekoratora @pytest.fixture.

# Załóżmy, że chcemy przetestować funkcje działające na listach - na przykład funkcję,
# która sprawdza, czy lista jest posortowana. Najpierw zdefiniujmy fixture, która
# dostarczy różne listy do testowania, a następnie napiszmy testy wykorzystujące
# ten fixture.

# Fixture zwracająca listy do testów
@pytest.fixture(params=[
    ([1, 2, 3], True),  # Posortowana lista
    ([3, 2, 1], False),  # Nieposortowana lista
    ([], True),  # Pusta lista
])
def list_data(request):
    """Fixture returning lists and expected result if they are sorted."""
    return request.param

# Funkcja do testowania
def is_sorted(lst):
    """Checks if a list is sorted."""
    # all zwróci true jeśli wszystkie elementy są prawdziwe
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Test używający fixture
def test_is_sorted(list_data):
    """Tests if lists are correctly identified as sorted or not."""
    lst, expected = list_data
    assert is_sorted(lst) == expected

