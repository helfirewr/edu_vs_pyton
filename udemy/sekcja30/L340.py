# Import niezbędnych modułów z PySide6 do stworzenia aplikacji i widgetów
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# Widgety to elementy GUI takie jak przyciski, etykiety,
# pola tekstowe, które umożliwiają użytkownikowi interakcję z aplikacją.

# Definicja klasy głównego okna aplikacji, dziedziczącej po QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.setWindowTitle("Lekcja 2: Widgety i Zdarzenia")  # Ustawienie tytułu okna
        self.resize(400, 300)  # Ustawienie rozmiaru okna

        # Utworzenie obiektu layoutu pionowego
        layout = QVBoxLayout()

        # Utworzenie etykiety i dodanie jej do layoutu
        self.label = QLabel("Kliknij przycisk")
        layout.addWidget(self.label)

        # Utworzenie przycisku i dodanie go do layoutu
        button = QPushButton("Kliknij mnie")
        # Połączenie sygnału kliknięcia przycisku z metodą on_button_clicked
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)

        # Ustawienie widgetu, który będzie centralnym widgetem okna
        centralWidget = QWidget()
        # Przypisanie wcześniej utworzonego layoutu do centralnego widgetu
        centralWidget.setLayout(layout)
        # Ustawienie centralnego widgetu dla głównego okna
        self.setCentralWidget(centralWidget)

    # Metoda wywoływana po kliknięciu przycisku, zmienia tekst na etykiecie
    def on_button_clicked(self):
        self.label.setText("Przycisk został kliknięty!")

# Funkcja main, gdzie tworzona jest aplikacja i główne okno, a następnie uruchamiana pętla zdarzeń
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji
    window = MainWindow()  # Utworzenie instancji głównego okna aplikacji
    window.show()  # Wyświetlenie głównego okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń aplikacji

# Sprawdzenie, czy skrypt został uruchomiony bezpośrednio, a nie zaimportowany
if __name__ == "__main__":
    main()  # Wywołanie funkcji main
