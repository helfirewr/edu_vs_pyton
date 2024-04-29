# import modułu unittest, który jest wbudowany w Pythona i służy
# do testowania jednostkowego
import unittest


# Definicja funkcji divide, która będzie testowana.
# Funkcja dzieli x przez y i zwraca wynik. W przypadku próby dzielenia przez zero,
# funkcja zgłasza wyjątek ValueError.
def divide(x, y):
    if y == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return x / y


# Klasa MockDatabase służąca do symulacji zewnętrznego zasobu, jakim jest baza danych.
# W kontekście testów jednostkowych, użyjemy tej klasy do symulowania
# interakcji z bazą danych.
class MockDatabase:
    def __init__(self):
        self.data = {'id1': 100, 'id2': 200}

    def get_data(self, id):
        return self.data.get(id)


# Definicja klasy testowej ComplexOperationsTest, która dziedziczy po unittest.TestCase.
# W tej klasie skupimy się na testowaniu funkcji zależnych od zewnętrznych
# zasobów oraz na obsłudze wyjątków.
class ComplexOperationsTest(unittest.TestCase):

    # Metoda testowa test_divide, która sprawdza poprawność działania funkcji divide.
    def test_divide(self):
        # Sprawdzenie, czy funkcja poprawnie dzieli liczby.
        self.assertEqual(divide(10, 2), 5)
        # Sprawdzenie, czy funkcja rzuci wyjątek ValueError przy próbie
        # dzielenia przez zero.
        with self.assertRaises(ValueError):
            divide(10, 0)

    # Metoda testowa test_mock_database, która sprawdza interakcję
    # z symulowaną bazą danych.
    def test_mock_database(self):
        # Utworzenie instancji symulowanej bazy danych.
        db = MockDatabase()
        # Sprawdzenie, czy metoda get_data zwraca poprawne wartości.
        self.assertEqual(db.get_data('id1'), 100)
        # Sprawdzenie, czy metoda get_data zwraca None, gdy podany
        # jest nieistniejący identyfikator.
        self.assertIsNone(db.get_data('id3'))


# Warunek sprawdzający, czy skrypt został uruchomiony bezpośrednio,
# a nie zaimportowany jako moduł.
# Jeśli tak, to uruchamiana jest funkcja unittest.main(), która odpowiada
# za uruchomienie wszystkich testów zdefiniowanych w klasie.
if __name__ == '__main__':
    unittest.main()
