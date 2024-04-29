import requests
import json

# Definiowanie adresu URL endpointu, do którego będziemy wysyłać zapytanie POST
url = 'https://httpbin.org/post'

# Dane, które chcemy wysłać
data = {
    'username': 'Ania',
    'password': 'sd#$TggDFG',
    'email': 'ania@example.com',
    'date_of_birth': '2000-01-01',
    'country': 'Polska'
}

# Wysyłanie zapytania POST z danymi
response = requests.post(url, data=data)

# Sprawdzenie statusu odpowiedzi
if response.status_code == 200:
    # Odpowiedź serwera jest automatycznie konwertowana z formatu JSON do słownika Pythona
    response_data = response.json()

    # Wyświetlenie przesłanych danych zwróconych przez serwer
    print("Odpowiedź z serwera:")
    # Sformatowanie i wyświetlenie danych JSON dla lepszej czytelności
    print(json.dumps(response_data, indent=4))
else:
    print(f"Nie udało się wysłać danych, kod statusu: {response.status_code}")
