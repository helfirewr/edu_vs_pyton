# pip install requests

import requests

def fetch_exchange_rates():
    """
    Funkcja do pobierania i wyświetlania kursów walut z API NBP.
    """
    url = 'http://api.nbp.pl/api/exchangerates/tables/a/?format=json'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy odpowiedź serwera jest błędem (np. 404, 500 itd.)

        # Przetwarzanie odpowiedzi
        data = response.json()
        print("Otrzymano kursy walut:")
        for rate in data[0]['rates']:
            print(f"{rate['currency']}: {rate['code']} = {rate['mid']}")

    except requests.exceptions.HTTPError as err:
        print(f"Błąd podczas pobierania danych: {err}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == '__main__':
    fetch_exchange_rates()
