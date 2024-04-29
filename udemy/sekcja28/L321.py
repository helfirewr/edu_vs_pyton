import unittest

# Definicja funkcji is_even, która sprawdza, czy liczba jest parzysta.
# Zwraca True, jeśli liczba jest parzysta, w przeciwnym razie False.
def is_even(number):
    return number % 2 == 0

# Definicja funkcji filter_even, która filtruje z listy liczby parzyste.
# Zwraca listę zawierającą tylko parzyste liczby z podanej listy.
def filter_even(numbers_list):
    return [num for num in numbers_list if is_even(num)]

# Definicja klasy testowej BooleanAndListOperationsTest, która dziedziczy
# po unittest.TestCase.
# Ta klasa testowa skupia się na funkcjach zwracających wartości boolowskie
# oraz operacjach na listach.
class BooleanAndListOperationsTest(unittest.TestCase):

    # Metoda testowa test_is_even, która sprawdza, czy funkcja is_even
    # poprawnie identyfikuje liczby parzyste.
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

    # Metoda testowa test_filter_even, która sprawdza, czy funkcja filter_even
    # poprawnie filtruje liczby parzyste z listy.
    def test_filter_even(self):
        input_list = [1, 2, 3, 4, 5, 6]
        expected_output = [2, 4, 6]
        self.assertEqual(filter_even(input_list), expected_output)

# Warunek sprawdzający, czy skrypt został uruchomiony bezpośrednio,
# a nie zaimportowany jako moduł.
# Jeśli tak, to uruchamiana jest funkcja unittest.main(), która odpowiada
# za uruchomienie wszystkich testów zdefiniowanych w klasie.
if __name__ == '__main__':
    unittest.main()
