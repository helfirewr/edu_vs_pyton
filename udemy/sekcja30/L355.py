import sys  # Importowanie modułu sys do zarządzania argumentami linii poleceń.

# Importowanie klas z PySide6 do tworzenia interfejsu graficznego.
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton)

class LoanCalculatorApp(QWidget):  # Definicja klasy aplikacji, dziedzicząca po QWidget.
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej.
        self.setWindowTitle("Kalkulator Odsetek Kredytu")  # Ustawienie tytułu okna aplikacji.
        self.resize(400, 300)  # Ustawienie rozmiaru okna aplikacji.
        self.setup_ui()  # Wywołanie metody konfigurującej interfejs użytkownika.

    def setup_ui(self):
        # Utworzenie głównego układu aplikacji (layout), który będzie zawierał wszystkie elementy interfejsu.
        main_layout = QVBoxLayout()

        # Utworzenie pól do wprowadzania danych przez użytkownika i ich konfiguracja.
        self.amount_input = QLineEdit()  # Pole do wprowadzenia kwoty kredytu.
        self.interest_input = QLineEdit()  # Pole do wprowadzenia stopy procentowej.
        self.years_input = QLineEdit()  # Pole do wprowadzenia długości kredytu w latach.
        self.result_label = QLabel("Wynik: Nie obliczono")  # Etykieta do wyświetlenia wyniku.

        # Dodanie etykiet i pól do głównego układu.
        main_layout.addWidget(QLabel("Kwota kredytu:"))
        main_layout.addWidget(self.amount_input)
        main_layout.addWidget(QLabel("Stopa procentowa:"))
        main_layout.addWidget(self.interest_input)
        main_layout.addWidget(QLabel("Długość kredytu (lata):"))
        main_layout.addWidget(self.years_input)

        # Utworzenie przycisku do obliczania odsetek i konfiguracja jego zachowania.
        calculate_button = QPushButton("Oblicz")
        calculate_button.clicked.connect(self.calculate_interest)  # Połączenie przycisku z metodą obliczającą odsetki.

        # Dodanie przycisku i etykiety wyniku do głównego układu.
        main_layout.addWidget(calculate_button)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)  # Ustawienie głównego układu jako układu okna aplikacji.

    def calculate_interest(self):
        # Metoda obliczająca miesięczną ratę kredytu.
        amount = float(self.amount_input.text())  # Pobranie kwoty kredytu z pola tekstowego.
        interest_rate = float(self.interest_input.text())  # Pobranie stopy procentowej z pola tekstowego.
        years = int(self.years_input.text())  # Pobranie długości kredytu z pola tekstowego.

        # Obliczenie miesięcznej stopy procentowej i liczby miesięcy.
        monthly_interest_rate = interest_rate / 100 / 12
        months = years * 12

        # Obliczenie miesięcznej raty kredytu.
        monthly_payment = (amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)

        # Wyświetlenie wyniku w etykiecie.
        self.result_label.setText(f"Wynik: Miesięczna rata wynosi {monthly_payment:.2f}")

def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji.
    window = LoanCalculatorApp()  # Utworzenie instancji głównego okna aplikacji.
    window.show()  # Wyświetlenie okna aplikacji.
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji.

if __name__ == "__main__":
    main()  # Wywołanie głównej funkcji aplikacji.
