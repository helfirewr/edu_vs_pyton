# Importowanie niezbędnych modułów z PySide6 do tworzenia aplikacji i widgetów
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QLabel

# Definicja klasy głównego okna aplikacji, dziedzicząca po QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Lekcja 3: Sygnały i Sloty")  # Ustawienie tytułu okna
        self.resize(400, 300)  # Ustawienie rozmiaru okna

        # Utworzenie layoutu pionowego
        layout = QVBoxLayout()

        # Utworzenie i konfiguracja QLineEdit
        self.line_edit = QLineEdit("Wpisz coś tutaj...")
        # Połączenie sygnału zmiany tekstu z metodą on_text_changed
        self.line_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.line_edit)  # Dodanie QLineEdit do layoutu

        # Utworzenie etykiety, która będzie wyświetlać wpisany tekst
        self.label = QLabel("Tutaj pojawi się wpisany tekst")
        layout.addWidget(self.label)  # Dodanie QLabel do layoutu

        # Ustawienie centralnego widgetu z powyższym layoutem
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Metoda wywoływana przy zmianie tekstu w QLineEdit
    def on_text_changed(self, text):
        # Ustawienie tekstu QLabel na tekst z QLineEdit
        self.label.setText(text)

# Funkcja main uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna aplikacji
    window.show()  # Wyświetlenie głównego okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

# Sprawdzenie, czy skrypt został uruchomiony bezpośrednio
if __name__ == "__main__":
    main()  # Wywołanie funkcji main
