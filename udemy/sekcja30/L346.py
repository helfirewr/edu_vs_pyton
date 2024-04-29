# Importowanie niezbędnych modułów z PySide6
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel

# Definicja klasy głównego okna aplikacji
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Lekcja 7: Użycie QComboBox")  # Ustawienie tytułu okna
        self.resize(400, 200)  # Ustawienie rozmiaru okna

        # Utworzenie layoutu pionowego
        layout = QVBoxLayout()

        # Utworzenie QComboBox
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Opcja 1", "Opcja 2", "Opcja 3"])  # Dodanie opcji do QComboBox
        self.combo_box.currentIndexChanged.connect(self.index_changed)  # Połączenie sygnału zmiany indeksu z metodą
        layout.addWidget(self.combo_box)  # Dodanie QComboBox do layoutu

        # Utworzenie QLabel do wyświetlania wybranej opcji
        self.label = QLabel("Wybierz opcję z listy powyżej")
        layout.addWidget(self.label)  # Dodanie QLabel do layoutu

        # Ustawienie centralnego widgetu z powyższym layoutem
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Metoda wywoływana przy zmianie wybranej opcji w QComboBox
    def index_changed(self, index):
        option_text = self.combo_box.currentText()  # Pobranie aktualnie wybranej opcji jako tekst
        self.label.setText(f"Wybrano: {option_text}")  # Ustawienie tekstu QLabel na wybraną opcję

# Funkcja uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń

if __name__ == "__main__":
    main()  # Wywołanie funkcji main
