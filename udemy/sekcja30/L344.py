# Importowanie niezbędnych modułów z PySide6 do tworzenia aplikacji i widgetów
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QLabel

# Definicja klasy głównego okna aplikacji, dziedzicząca po QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Lekcja 6: Lista Elementów i Etykieta")  # Ustawienie tytułu okna
        self.resize(400, 300)  # Ustawienie rozmiaru okna

        # Utworzenie layoutu pionowego
        layout = QVBoxLayout()

        # Utworzenie QListWidget
        self.list_widget = QListWidget()
        # Dodanie elementów do listy
        self.list_widget.addItems(["Element 1", "Element 2", "Element 3"])
        # Połączenie sygnału zmiany zaznaczenia z metodą on_item_changed
        self.list_widget.currentItemChanged.connect(self.on_item_changed)
        layout.addWidget(self.list_widget)  # Dodanie QListWidget do layoutu

        # Utworzenie QLabel do wyświetlania informacji o zaznaczonym elemencie
        self.info_label = QLabel("Wybierz element z listy")
        layout.addWidget(self.info_label)  # Dodanie QLabel do layoutu

        # Ustawienie centralnego widgetu z powyższym layoutem
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Metoda wywoływana przy zmianie zaznaczonego elementu
    def on_item_changed(self, current, previous):
        if current is not None:
            self.info_label.setText(f"Zaznaczono: {current.text()}")  # Aktualizacja tekstu QLabel

# Funkcja main uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna aplikacji
    window.show()  # Wyświetlenie głównego okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

# Sprawdzenie, czy skrypt został uruchomiony bezpośrednio
if __name__ == "__main__":
    main()  # Wywołanie funkcji main
