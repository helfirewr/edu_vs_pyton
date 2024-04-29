import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt  # Dodajemy import Qt do użycia Qt.AlignCenter

# Definicja klasy głównego okna aplikacji
class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej QWidget
        self.setWindowTitle("Przykład QLabel i Obrazy")  # Ustawienie tytułu okna
        self.setup_ui()  # Konfiguracja interfejsu użytkownika

    def setup_ui(self):
        layout = QVBoxLayout(self)  # Utworzenie layoutu pionowego dla widgetów

        # Utworzenie QLabel i ustawienie obrazu
        self.image_label = QLabel()

        # Budowanie pełnej ścieżki do obrazka
        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_dir, ".", "bird.jpg")

        self.image_label.setPixmap(QPixmap(image_path))  # Ładowanie i ustawienie obrazu
        self.image_label.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie obrazu w QLabel

        layout.addWidget(self.image_label)  # Dodanie QLabel do layoutu

def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = ImageWindow()  # Utworzenie instancji głównego okna
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

if __name__ == "__main__":
    main()  # Wywołanie funkcji main
