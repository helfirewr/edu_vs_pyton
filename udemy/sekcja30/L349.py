# Importowanie niezbędnych modułów
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget

# Definicja klasy głównego okna aplikacji
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Przykład QGridLayout")  # Ustawienie tytułu okna
        self.setup_ui()  # Konfiguracja interfejsu użytkownika

    def setup_ui(self):
        # Utworzenie layoutu siatkowego
        layout = QGridLayout()

        # Tworzenie i dodawanie przycisków do layoutu siatkowego
        layout.addWidget(QPushButton("Przycisk 1"), 0, 0)  # Rząd 0, kolumna 0
        layout.addWidget(QPushButton("Przycisk 2"), 0, 1)  # Rząd 0, kolumna 1
        layout.addWidget(QPushButton("Przycisk 3"), 1, 0)  # Rząd 1, kolumna 0
        layout.addWidget(QPushButton("Przycisk 4"), 1, 1)  # Rząd 1, kolumna 1

        # Ustawienie layoutu siatkowego jako głównego layoutu okna
        self.setLayout(layout)

# Funkcja uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

if __name__ == "__main__":
    main()
