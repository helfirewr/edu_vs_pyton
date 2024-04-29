import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        """Inicjalizacja aplikacji z interfejsem użytkownika."""
        self.root = root
        self.root.title("Konwerter walut")

        # Pobranie kursów walut i zapisanie ich w słowniku na początku działania programu
        self.currency_rates = self.fetch_currency_rates()

        # Utworzenie elementów UI
        self.create_widgets()

        # Wywołanie metody calculate na początku, aby od razu pokazać kursy walut
        self.calculate()

    def fetch_currency_rates(self):
        """Pobiera aktualne kursy walut z API NBP i zwraca je jako słownik."""
        response = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/?format=json')
        rates = response.json()[0]['rates']
        currency_rates = {rate['code']: rate['mid'] for rate in rates}
        return currency_rates

    def create_widgets(self):
        """Tworzy komponenty interfejsu użytkownika."""
        # Etykieta i pole tekstowe do wprowadzania kwoty w PLN
        self.pln_label = ttk.Label(self.root, text="Wprowadź kwotę w PLN:")
        self.pln_label.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        self.pln_entry = ttk.Entry(self.root)
        self.pln_entry.grid(column=1, row=0, padx=10, pady=10, sticky="WE")
        self.pln_entry.bind('<KeyRelease>', self.calculate)  # Aktualizuje wartości przy każdej zmianie tekstu

        # Etykiety pokazujące wartość w walutach obcych
        self.usd_label = ttk.Label(self.root, text="USD:")
        self.usd_label.grid(column=0, row=1, padx=10, pady=10, sticky="W")
        self.eur_label = ttk.Label(self.root, text="EUR:")
        self.eur_label.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        self.jpy_label = ttk.Label(self.root, text="JPY:")
        self.jpy_label.grid(column=0, row=3, padx=10, pady=10, sticky="W")

    def calculate(self, event=None):
        """Oblicza i aktualizuje wartości walut na podstawie wprowadzonej kwoty w PLN."""
        try:
            # Pobranie kwoty w PLN od użytkownika
            amount_pln = float(self.pln_entry.get())
        except ValueError:
            # Jeśli wartość nie jest liczbą, ustaw domyślnie na 1 PLN
            amount_pln = 1.0
            self.pln_entry.delete(0, tk.END)
            self.pln_entry.insert(0, "1")

        # Obliczanie wartości w walutach obcych i aktualizacja etykiet z kursami
        for label, currency in [(self.usd_label, 'USD'), (self.eur_label, 'EUR'), (self.jpy_label, 'JPY')]:
            if currency in self.currency_rates:
                value = amount_pln / self.currency_rates[currency]
                label.config(text=f"{currency} ({self.currency_rates[currency]} PLN): {value:.2f}")
            else:
                label.config(text=f"{currency} (kurs nieznany): N/A")

if __name__ == '__main__':
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
