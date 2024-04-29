# Importowanie niezbędnych modułów
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt

# Definicja klasy głównego okna aplikacji
class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")  # Ustawienie tytułu okna aplikacji
        self.initUI()  # Inicjalizacja interfejsu użytkownika

    def initUI(self):
        self.centralWidget = QWidget(self)  # Utworzenie centralnego widgetu
        self.setCentralWidget(self.centralWidget)  # Ustawienie centralnego widgetu w głównym oknie
        self.mainLayout = QVBoxLayout(self.centralWidget)  # Utworzenie głównego układu pionowego

        self.display = QLabel("0")  # Utworzenie wyświetlacza jako etykiety QLabel z początkową wartością "0"
        self.display.setStyleSheet("border: 1px solid black; padding: 10px;")  # Styl wyświetlacza
        self.display.setAlignment(Qt.AlignRight)  # Wyrównanie tekstu wyświetlacza do prawej
        self.mainLayout.addWidget(self.display)  # Dodanie wyświetlacza do głównego układu

        self.buttonsLayout = QGridLayout()  # Utworzenie układu siatki dla przycisków
        buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', 'C', '0', '=', '+']  # Lista etykiet przycisków
        self.createButtons(buttons)  # Utworzenie przycisków na podstawie listy etykiet

        self.mainLayout.addLayout(self.buttonsLayout)  # Dodanie układu siatki przycisków do głównego układu

    def createButtons(self, buttons):
        row, col = 0, 0  # Inicjalizacja początkowej pozycji przycisku w siatce
        for button in buttons:
            if col > 3:  # Jeśli osiągnięto koniec rzędu, przejdź do nowego rzędu
                row += 1
                col = 0
            btn = QPushButton(button)  # Utworzenie przycisku z etykietą
            btn.clicked.connect(self.onButtonClick)  # Połączenie sygnału kliknięcia przycisku z metodą obsługi
            self.buttonsLayout.addWidget(btn, row, col)  # Dodanie przycisku do układu siatki
            col += 1  # Przejście do następnej kolumny

    def onButtonClick(self):
        sender = self.sender()  # Pobranie obiektu przycisku, który wywołał metodę
        if sender.text() == 'C':  # Jeśli kliknięto przycisk "C", zresetuj wyświetlacz
            self.display.setText("0")
        elif sender.text() == '=':  # Jeśli kliknięto przycisk "=", oblicz i pokaż wynik
            try:
                result = str(eval(self.display.text()))  # Użycie funkcji eval do obliczenia wyrażenia matematycznego
                self.display.setText(result)  # Ustawienie wyniku na wyświetlaczu
            except Exception as e:
                self.display.setText("Error")  # W przypadku błędu, pokaż komunikat "Error"
        else:  # Dla pozostałych przycisków, dodaj ich etykietę do tekstu wyświetlacza
            if self.display.text() == "0":  # Jeśli na wyświetlaczu jest tylko "0", zastąp go etykietą przycisku
                self.display.setText(sender.text())
            else:  # W przeciwnym przypadku, dołącz etykietę przycisku do tekstu wyświetlacza
                self.display.setText(self.display.text() + sender.text())

def main():
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
