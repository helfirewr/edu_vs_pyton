import unittest
from unittest.mock import MagicMock

# Definicja funkcji reverse_string, która odwraca napis.
def reverse_string(s):
    return s[::-1]

# Definicja funkcji capitalize_string, która zmienia pierwszą literę napisu na wielką.
def capitalize_string(s):
    return s.capitalize()

# Klasa ExternalService, która symuluje zewnętrzną usługę, np. serwis pogodowy.
class ExternalService:
    def get_weather(self, city):
        # Tutaj miałoby miejsce rzeczywiste połączenie z zewnętrznym serwisem
        pass

# Definicja klasy testowej StringAndMockOperationsTest, która dziedziczy
# po unittest.TestCase.
# Ta klasa skupia się na testowaniu operacji na napisach oraz użyciu atrap
# do testowania funkcji z zewnętrznymi zależnościami.
class StringAndMockOperationsTest(unittest.TestCase):

    # Metoda testowa test_reverse_string, która sprawdza, czy funkcja reverse_string
    # poprawnie odwraca napisy.
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string("Hello"), "olleH")

    # Metoda testowa test_capitalize_string, która sprawdza, czy funkcja capitalize_string
    # poprawnie zmienia pierwszą literę napisu na wielką.
    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("test"), "Test")

    # Metoda testowa test_external_service, która używa atrapy (mock) do symulowania
    # odpowiedzi z zewnętrznej usługi.
    def test_external_service(self):
        # Utworzenie atrapy dla ExternalService
        mock_service = ExternalService()
        mock_service.get_weather = MagicMock(return_value="Sunny")

        # Sprawdzenie, czy atrapa zwraca oczekiwaną wartość
        self.assertEqual(mock_service.get_weather("Warsaw"), "Sunny")

        # Weryfikacja, czy metoda get_weather została wywołana z oczekiwanym argumentem
        mock_service.get_weather.assert_called_with("Warsaw")


if __name__ == '__main__':
    unittest.main()
