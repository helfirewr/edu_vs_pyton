# Importowanie niezbędnych modułów z PySide6 do tworzenia aplikacji i widgetów
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QAction  # Poprawny import QAction

# Definicja klasy głównego okna aplikacji, dziedzicząca po QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Lekcja 4: Menu i Akcje")  # Ustawienie tytułu okna
        self.resize(400, 300)  # Ustawienie rozmiaru okna

        # Tworzenie akcji wyjścia
        exit_action = QAction("&Wyjdź", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)  # Połączenie sygnału z metodą close

        # Dodawanie paska menu
        menu_bar = self.menuBar()  # Pobranie paska menu głównego okna
        file_menu = menu_bar.addMenu("&Plik")  # Dodanie menu "Plik"
        file_menu.addAction(exit_action)  # Dodanie akcji wyjścia do menu "Plik"

        # Tworzenie akcji 'O aplikacji'
        about_action = QAction("&O aplikacji", self)
        about_action.triggered.connect(self.about_dialog)  # Połączenie z metodą about_dialog
        help_menu = menu_bar.addMenu("&Pomoc")  # Dodanie menu "Pomoc"
        help_menu.addAction(about_action)  # Dodanie akcji 'O aplikacji' do menu "Pomoc"

    # Metoda wyświetlająca okno dialogowe 'O aplikacji'
    def about_dialog(self):
        QMessageBox.about(self, "O aplikacji", "To jest przykładowa aplikacja PySide6.")

# Funkcja main uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna aplikacji
    window.show()  # Wyświetlenie głównego okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

# Sprawdzenie, czy skrypt został uruchomiony bezpośrednio
if __name__ == "__main__":
    main()  # Wywołanie funkcji main
