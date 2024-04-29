# Importujemy niezbędne moduły z PySide6 do tworzenia aplikacji i obsługi interfejsu użytkownika
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QToolBar
from PySide6.QtGui import QAction  # Poprawny import QAction

# Definiujemy klasę głównego okna aplikacji, która dziedziczy po QMainWindow
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołujemy konstruktor klasy bazowej QMainWindow
        self.setWindowTitle("Prosty Edytor Tekstowy")  # Ustawiamy tytuł głównego okna aplikacji
        self.resize(600, 400)  # Ustawiamy rozmiar głównego okna

        self.text_edit = QTextEdit()  # Tworzymy widget QTextEdit, który pozwala na edycję wieloliniowego tekstu
        self.setCentralWidget(self.text_edit)  # Ustawiamy QTextEdit jako centralny widget głównego okna

        self.toolbar = QToolBar("Główne narzędzia")  # Tworzymy pasek narzędziowy
        self.addToolBar(self.toolbar)  # Dodajemy pasek narzędziowy do głównego okna

        open_action = QAction("Otwórz", self)  # Tworzymy akcję "Otwórz"
        open_action.triggered.connect(self.open_file)  # Łączymy akcję z metodą otwierającą plik
        self.toolbar.addAction(open_action)  # Dodajemy akcję "Otwórz" do paska narzędziowego

        save_action = QAction("Zapisz", self)  # Tworzymy akcję "Zapisz"
        save_action.triggered.connect(self.save_file)  # Łączymy akcję z metodą zapisującą plik
        self.toolbar.addAction(save_action)  # Dodajemy akcję "Zapisz" do paska narzędziowego

    # Metoda odpowiedzialna za otwieranie pliku
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Otwórz plik", "",
                                                   "Pliki tekstowe (*.txt);;Wszystkie pliki (*)")
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_edit.setText(content)  # Wczytujemy zawartość pliku do QTextEdit

    # Metoda odpowiedzialna za zapisywanie pliku
    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self,
                                                   "Zapisz plik", "",
                                                   "Pliki tekstowe (*.txt);;Wszystkie pliki (*)")
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_edit.toPlainText()
                file.write(content)  # Zapisujemy zawartość QTextEdit do pliku

# Główna funkcja uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)  # Tworzymy instancję aplikacji QApplication
    editor = TextEditor()  # Tworzymy instancję naszego edytora tekstowego
    editor.show()  # Wyświetlamy główne okno edytora
    sys.exit(app.exec())  # Uruchamiamy pętlę zdarzeń aplikacji

if __name__ == "__main__":
    main()  # Uruchamiamy główną funkcję, jeśli skrypt jest uruchamiany bezpośrednio
