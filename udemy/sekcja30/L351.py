# Importowanie niezbędnych modułów
import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QTabWidget

# Definicja klasy głównego okna aplikacji
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Przykład QTabWidget")  # Ustawienie tytułu okna
        self.setup_ui()  # Konfiguracja interfejsu użytkownika

    def setup_ui(self):
        # Utworzenie layoutu pionowego
        layout = QVBoxLayout()

        # Utworzenie QTabWidget
        tab_widget = QTabWidget()
        layout.addWidget(tab_widget)  # Dodanie QTabWidget do layoutu

        # Utworzenie zawartości dla pierwszej zakładki
        tab1_content = QWidget()  # Widget, który będzie zawartością zakładki
        tab1_layout = QVBoxLayout()  # Layout dla zawartości zakładki
        tab1_layout.addWidget(QLabel("Zawartość zakładki 1"))
        tab1_content.setLayout(tab1_layout)

        # Utworzenie zawartości dla drugiej zakładki
        tab2_content = QWidget()  # Widget, który będzie zawartością zakładki
        tab2_layout = QVBoxLayout()  # Layout dla zawartości zakładki
        tab2_layout.addWidget(QLabel("Zawartość zakładki 2"))
        tab2_content.setLayout(tab2_layout)

        # Dodanie zakładek do QTabWidget
        tab_widget.addTab(tab1_content, "Zakładka 1")
        tab_widget.addTab(tab2_content, "Zakładka 2")

        # Ustawienie layoutu pionowego jako głównego layoutu okna
        self.setLayout(layout)

# Funkcja uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

if __name__ == "__main__":
    main()
