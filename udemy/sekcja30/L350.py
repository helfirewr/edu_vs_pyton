# Importowanie niezbędnych modułów
import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QLabel, QVBoxLayout, QWidget

# Definicja klasy głównego okna aplikacji
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Przykład QCheckBox")  # Ustawienie tytułu okna
        self.setup_ui()  # Konfiguracja interfejsu użytkownika

    def setup_ui(self):
        # Utworzenie layoutu pionowego
        layout = QVBoxLayout()

        # Utworzenie QCheckBox i dodanie ich do layoutu
        self.checkbox1 = QCheckBox("Opcja 1")
        self.checkbox1.stateChanged.connect(self.checkbox_changed)  # Połączenie sygnału ze slotem
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox("Opcja 2")
        self.checkbox2.stateChanged.connect(self.checkbox_changed)  # Połączenie sygnału ze slotem
        layout.addWidget(self.checkbox2)

        # Utworzenie QLabel do wyświetlania statusu
        self.status_label = QLabel("Wybierz opcję")
        layout.addWidget(self.status_label)

        # Ustawienie layoutu pionowego jako głównego layoutu okna
        self.setLayout(layout)

    def checkbox_changed(self):
        # Aktualizacja tekstu QLabel na podstawie statusu QCheckBox
        status = []
        if self.checkbox1.isChecked():
            status.append(self.checkbox1.text())
        if self.checkbox2.isChecked():
            status.append(self.checkbox2.text())

        self.status_label.setText("Wybrano: " + ", ".join(status) if status else "Nic nie wybrano")

# Funkcja uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

if __name__ == "__main__":
    main()
