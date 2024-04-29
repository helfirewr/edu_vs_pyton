# Importowanie niezbędnych modułów z PySide6
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QSpinBox
from PySide6.QtCore import Qt

# Definicja klasy głównego okna aplikacji
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Lekcja 8: Synchronizacja QSlider i QSpinBox")  # Ustawienie tytułu okna
        self.resize(400, 200)  # Ustawienie rozmiaru okna

        # Utworzenie layoutu pionowego
        layout = QVBoxLayout()

        # Utworzenie QSlider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)  # Ustawienie minimalnej wartości
        self.slider.setMaximum(100)  # Ustawienie maksymalnej wartości
        self.slider.valueChanged.connect(self.slider_changed)  # Połączenie sygnału zmiany wartości z metodą
        layout.addWidget(self.slider)  # Dodanie QSlider do layoutu

        # Utworzenie QSpinBox
        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(0)  # Ustawienie minimalnej wartości
        self.spin_box.setMaximum(100)  # Ustawienie maksymalnej wartości
        self.spin_box.valueChanged.connect(self.spin_box_changed)  # Połączenie sygnału zmiany wartości z metodą
        layout.addWidget(self.spin_box)  # Dodanie QSpinBox do layoutu

        # Ustawienie centralnego widgetu z powyższym layoutem
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Metoda wywoływana przy zmianie wartości QSlider
    def slider_changed(self, value):
        self.spin_box.setValue(value)  # Synchronizacja wartości z QSpinBox

    # Metoda wywoływana przy zmianie wartości QSpinBox
    def spin_box_changed(self, value):
        self.slider.setValue(value)  # Synchronizacja wartości z QSlider

# Funkcja uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń

if __name__ == "__main__":
    main()  # Wywołanie funkcji main
