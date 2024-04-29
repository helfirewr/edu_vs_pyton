
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# pip install PySide6

# Definicja klasy głównego okna aplikacji
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja Pierwsza Aplikacja") # Ustawienie tytułu okna
        self.resize(400, 300) # Ustawienie rozmiarów okna

# Funkcja główna, która uruchamia aplikację
def main():
    app = QApplication(sys.argv) # Tworzenie instancji aplikacji
    window = MainWindow() # Tworzenie instancji głównego okna
    window.show() # Wyświetlanie głównego okna
    sys.exit(app.exec()) # Uruchomienie pętli zdarzeń aplikacji

if __name__ == "__main__":
    main()
