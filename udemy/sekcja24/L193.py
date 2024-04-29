import requests
import json  # Importowanie modułu json do formatowania danych

# Definiowanie URL serwisu
url = 'https://httpbin.org/get'

# Definiowanie parametrów zapytania
params = {
    'username': 'nowy_uzytkownik',
    'page': '5'
}

# Wysyłanie zapytania GET z parametrami
response = requests.get(url, params=params)

# Sprawdzenie statusu odpowiedzi
if response.status_code == 200:
    # Wyświetlenie danych zwróconych przez serwis w formacie JSON
    # Używamy json.dumps do sformatowania danych JSON dla lepszej czytelności
    print("Otrzymane dane:")
    formatted_json = json.dumps(response.json(), indent=4)  # Formatowanie danych z wcięciami
    print(formatted_json)
else:
    print(f"Błąd zapytania: {response.status_code}")
