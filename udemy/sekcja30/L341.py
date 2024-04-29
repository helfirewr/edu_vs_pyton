import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QMessageBox

# Przykład poniżej demonstruje mechanizm sygnałów i slotów w PySide6, który jest
# kluczowym elementem komunikacji między różnymi częściami aplikacji GUI.
# Sygnały i sloty umożliwiają obiektom komunikowanie się ze sobą, gdy zachodzą
# różne zdarzenia (np. kliknięcie przycisku). Poniższy kod przedstawia prostą
# aplikację z przyciskiem, który po kliknięciu wywołuje metodę (slot), wyświetlającą
# komunikat.

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej QWidget
        self.setWindowTitle("Przykład Signals and Slots")  # Ustawienie tytułu okna
        self.setup_ui()  # Wywołanie metody konfigurującej interfejs użytkownika

    def setup_ui(self):
        # Utworzenie przycisku
        self.button = QPushButton("Kliknij mnie")
        # Połączenie sygnału clicked z metoda on_button_clicked
        self.button.clicked.connect(self.on_button_clicked)

        # Ustawienie layoutu
        layout = QVBoxLayout(self)  # Utworzenie layoutu pionowego
        layout.addWidget(self.button)  # Dodanie przycisku do layoutu

    def on_button_clicked(self):
        # Slot reagujący na sygnał clicked przycisku
        # Wyświetlenie okna dialogowego z informacją
        QMessageBox.information(self, "Informacja", "Przycisk został kliknięty")

def main():
    app = QApplication(sys.argv)  # Utworzenie instancji QApplication
    window = MainWindow()  # Utworzenie instancji głównego okna
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

if __name__ == "__main__":
    main()  # Wywołanie funkcji main
