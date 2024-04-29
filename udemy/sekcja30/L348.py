# Importowanie niezbędnych modułów z PySide6
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QLineEdit, QInputDialog

# QMessageBox jest wykorzystane do wyświetlenia prostego komunikatu dla użytkownika.
# QFileDialog pozwala użytkownikowi na wybór pliku z systemu plików.
# QInputDialog pozwala na pobranie od użytkownika dowolnego tekstu.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicjalizacja klasy nadrzędnej QMainWindow
        self.setWindowTitle("Przykład okien dialogowych")  # Ustawienie tytułu okna głównego

        layout = QVBoxLayout()  # Utworzenie layoutu pionowego

        # Utworzenie przycisku do pokazywania QMessageBox
        self.button_msgbox = QPushButton("Pokaż QMessageBox")
        self.button_msgbox.clicked.connect(self.show_msgbox)  # Połączenie sygnału kliknięcia z metodą show_msgbox
        layout.addWidget(self.button_msgbox)  # Dodanie przycisku do layoutu

        # Utworzenie przycisku do otwierania QFileDialog
        self.button_file_dialog = QPushButton("Otwórz QFileDialog")
        self.button_file_dialog.clicked.connect(self.open_file_dialog)  # Połączenie sygnału kliknięcia z metodą open_file_dialog
        layout.addWidget(self.button_file_dialog)  # Dodanie przycisku do layoutu

        # Utworzenie QLineEdit do wpisywania tekstu
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)  # Dodanie QLineEdit do layoutu

        # Utworzenie przycisku do pokazywania QInputDialog
        self.button_input_dialog = QPushButton("Pokaż QInputDialog")
        self.button_input_dialog.clicked.connect(self.show_input_dialog)  # Połączenie sygnału kliknięcia z metodą show_input_dialog
        layout.addWidget(self.button_input_dialog)  # Dodanie przycisku do layoutu

        central_widget = QWidget()  # Utworzenie centralnego widgetu
        central_widget.setLayout(layout)  # Ustawienie layoutu dla centralnego widgetu
        self.setCentralWidget(central_widget)  # Ustawienie centralnego widgetu dla okna głównego

    def show_msgbox(self):
        QMessageBox.information(self, "Informacja", "To jest QMessageBox.")  # Wyświetlenie okna dialogowego z informacją

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Otwórz plik")  # Otwarcie okna dialogowego do wyboru pliku
        if file_name:  # Sprawdzenie, czy użytkownik wybrał plik
            print(f"Wybrany plik: {file_name}")  # Wydrukowanie ścieżki wybranego pliku

    def show_input_dialog(self):
        text, ok = QInputDialog.getText(self, "QInputDialog", "Wpisz tekst:")  # Otwarcie okna dialogowego do wpisania tekstu
        if ok and text:  # Sprawdzenie, czy użytkownik wpisał tekst i kliknął OK
            self.line_edit.setText(text)  # Ustawienie tekstu w QLineEdit na wpisany tekst

def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji okna głównego
    window.show()  # Wyświetlenie okna głównego
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

if __name__ == "__main__":
    main()  # Uruchomienie funkcji main, jeśli skrypt jest uruchamiany bezpośrednio
