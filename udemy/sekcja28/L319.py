# import modułu unittest, który jest wbudowany w Pythona i służy
# do testowania jednostkowego
import unittest

# Definicja funkcji add, która będzie testowana.
def add(x, y):
    return x + y

# Dodatkowa funkcja subtract do testowania.
def subtract(x, y):
    return x - y

# Definicja klasy testowej ArithmeticOperationsTest, która dziedziczy po unittest.TestCase.
# TestCase jest podstawową klasą w unittest, służącą do tworzenia przypadków testowych.
class ArithmeticOperationsTest(unittest.TestCase):

    # Metoda testowa test_add, która sprawdza poprawność działania funkcji add.
    # Nazwa metody zawsze powinna zaczynać się od słowa "test".
    def test_add(self):
        # Wywołanie metody assertEqual, aby sprawdzić, czy wynik
        # funkcji add jest równy oczekiwanej wartości.
        # assertEqual przyjmuje dwa argumenty: pierwszy to wynik funkcji,
        # drugi to oczekiwana wartość.
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    # Metoda testowa test_subtract, która sprawdza, czy funkcja subtract
    # poprawnie oblicza różnicę między podanymi liczbami.
    def test_subtract(self):
        # Sprawdzanie, czy wynik funkcji subtract jest zgodny z oczekiwaniami.
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

# Warunek sprawdzający, czy skrypt został uruchomiony bezpośrednio,
# a nie zaimportowany jako moduł.
# Jeśli tak, to uruchamiana jest funkcja unittest.main(), która odpowiada
# za uruchomienie wszystkich testów zdefiniowanych w klasie.
if __name__ == '__main__':
    unittest.main()
