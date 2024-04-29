import unittest
import requests  # pip install requests


class TestExchangeRatesAPI(unittest.TestCase):

    # Test sprawdzający, czy odpowiedź z API jest prawidłowym JSON i czy status HTTP to 200 (OK)
    def test_fetch_exchange_rates(self):
        # Wywołanie funkcji, która wykonuje zapytanie do API
        response = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/?format=json')

        # Sprawdzenie, czy status odpowiedzi HTTP to 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie, czy odpowiedź zawiera prawidłowy JSON
        try:
            rates = response.json()[0]['rates']
            # Upewnienie się, że otrzymano listę kursów walut
            self.assertTrue(isinstance(rates, list))
            # Sprawdzenie, czy każdy kurs waluty zawiera kluczowe pola
            for rate in rates:
                self.assertIn('currency', rate)
                self.assertIn('code', rate)
                self.assertIn('mid', rate)
        except ValueError:
            # Rzucenie błędu testu, jeśli odpowiedź nie jest prawidłowym JSON
            self.fail("Response is not a valid JSON")


if __name__ == '__main__':
    unittest.main()
