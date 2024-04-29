import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import QDate, QLocale
from PySide6.QtGui import QFont

# Definicja klasy aplikacji kalendarza, dziedziczącej po QWidget.
class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej.
        self.current_date = QDate.currentDate()  # Pobranie bieżącej daty.
        self.initializeUI()  # Inicjalizacja interfejsu użytkownika.
        self.resize(400, 300)  # Ustawienie rozmiaru okna aplikacji.
        self.show()  # Wyświetlenie okna aplikacji.

    # Metoda inicjalizująca interfejs użytkownika.
    def initializeUI(self):
        self.layout = QVBoxLayout()  # Utworzenie głównego układu pionowego.
        self.grid_layout = QGridLayout()  # Utworzenie układu siatki dla kalendarza.
        self.layout.addLayout(self.grid_layout)  # Dodanie układu siatki do głównego układu.
        self.setLayout(self.layout)  # Ustawienie głównego układu dla widgetu.

        # Utworzenie i konfiguracja przycisków nawigacyjnych.
        prev_button = QPushButton("< Poprzedni")
        prev_button.clicked.connect(self.showPreviousMonth)  # Połączenie sygnału kliknięcia z metodą.
        next_button = QPushButton("Następny >")
        next_button.clicked.connect(self.showNextMonth)  # Połączenie sygnału kliknięcia z metodą.

        # Dodanie przycisków do głównego układu.
        self.layout.addWidget(prev_button)
        self.layout.addWidget(next_button)

        # Wyświetlenie kalendarza dla bieżącego miesiąca.
        self.showCalendar(self.current_date.year(), self.current_date.month())

    # Metoda wyświetlająca kalendarz.
    def showCalendar(self, year, month):
        locale = QLocale(QLocale.Polish)  # Ustawienie lokalizacji na polską.
        month_name = locale.monthName(month)  # Pobranie nazwy miesiąca.
        self.setWindowTitle(f"Kalendarz: {month_name} {year}")  # Ustawienie tytułu okna.

        # Usunięcie wszystkich widgetów z układu siatki przed dodaniem nowych.
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            widget.deleteLater()

        # Dodanie nazw dni tygodnia do układu siatki.
        days_of_week = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Niedz"]
        for i, day in enumerate(days_of_week):
            self.grid_layout.addWidget(QLabel(day), 0, i)

        first_day_of_month = QDate(year, month, 1)  # Data pierwszego dnia miesiąca.
        offset = first_day_of_month.dayOfWeek() - 1  # Obliczenie przesunięcia pierwszego dnia miesiąca.

        # Dodanie etykiet dni do układu siatki.
        for day in range(1, first_day_of_month.daysInMonth() + 1):
            day_date = QDate(year, month, day)  # Ustawienie daty dla danego dnia.
            day_label = QLabel(str(day))  # Utworzenie etykiety z numerem dnia.
            # Wyróżnienie bieżącego dnia.
            if day_date == QDate.currentDate():
                font = day_label.font()  # Pobranie aktualnej czcionki etykiety.
                font.setBold(True)  # Ustawienie czcionki na pogrubioną.
                day_label.setFont(font)  # Ustawienie nowej czcionki dla etykiety.
            # Dodanie etykiety dnia do układu siatki.
            self.grid_layout.addWidget(day_label,
                                       (day + offset - 1) // 7 + 1,
                                       (day + offset - 1) % 7)

# Metoda obsługująca wyświetlenie poprzedniego miesiąca.
    def showPreviousMonth(self):
        self.current_date = self.current_date.addMonths(-1)  # Przejście do poprzedniego miesiąca.
        # Wyświetlenie kalendarza dla nowo ustawionej daty.
        self.showCalendar(self.current_date.year(), self.current_date.month())

    # Metoda obsługująca wyświetlenie następnego miesiąca.
    def showNextMonth(self):
        self.current_date = self.current_date.addMonths(1)  # Przejście do następnego miesiąca.
        # Wyświetlenie kalendarza dla nowo ustawionej daty.
        self.showCalendar(self.current_date.year(), self.current_date.month())

# Funkcja główna uruchamiająca aplikację.
def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji Qt.
    window = CalendarApp()  # Utworzenie głównego okna aplikacji.
    window.show()  # Wyświetlenie okna aplikacji.
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń i oczekiwanie na zakończenie aplikacji.

# Sprawdzenie, czy skrypt został uruchomiony bezpośrednio, a nie zaimportowany.
if __name__ == "__main__":
    main()
