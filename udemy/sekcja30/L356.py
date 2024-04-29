import sys  # Importowanie modułu sys potrzebnego do uruchomienia aplikacji.
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog, QFileDialog  # Importowanie klas z PySide6 do tworzenia interfejsu użytkownika.
from PySide6.QtGui import QPainter, QPen, QPixmap  # Importowanie klas do obsługi rysowania.
from PySide6.QtCore import Qt, QPoint  # Importowanie klas dla obsługi zdarzeń i punktów.

# Definicja klasy okna aplikacji do rysowania.
class DrawingArea(QMainWindow):
    def __init__(self):
        super().__init__()  # Wywołanie konstruktora klasy bazowej QMainWindow.
        self.title = 'Aplikacja do Rysowania'  # Tytuł aplikacji.
        self.drawing = False  # Flaga, czy użytkownik rysuje.
        self.last_point = QPoint()  # Ostatni punkt narysowany przez użytkownika.
        self.pen_color = Qt.black  # Domyślny kolor pióra.
        self.canvas = QPixmap(800, 600)  # Płótno do rysowania o wymiarach 800x600.
        self.canvas.fill(Qt.white)  # Wypełnienie płótna kolorem białym.

        self.initUI()  # Inicjalizacja interfejsu użytkownika.

    def initUI(self):
        self.setWindowTitle(self.title)  # Ustawienie tytułu okna.
        self.setGeometry(100, 100, 800, 600)  # Ustawienie geometrii okna.
        self.save_button = QPushButton('Zapisz', self)  # Utworzenie przycisku do zapisywania obrazu.
        self.save_button.move(10, 10)  # Umieszczenie przycisku zapisu w oknie.
        self.save_button.clicked.connect(self.save)  # Połączenie przycisku z funkcją zapisu.
        self.color_button = QPushButton('Kolor', self)  # Utworzenie przycisku do zmiany koloru pióra.
        self.color_button.move(100, 10)  # Umieszczenie przycisku zmiany koloru w oknie.
        self.color_button.clicked.connect(self.select_color)  # Połączenie przycisku zmiany koloru z funkcją wyboru koloru.
        self.show()  # Wyświetlenie okna aplikacji.

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # Sprawdzenie, czy naciśnięto lewy przycisk myszy.
            self.drawing = True  # Ustawienie flagi rysowania na true.
            self.last_point = event.pos()  # Zapisanie obecnej pozycji jako ostatni punkt.

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing:  # Sprawdzenie, czy lewy przycisk myszy jest wciśnięty podczas rysowania.
            painter = QPainter(self.canvas)  # Utworzenie obiektu QPainter dla płótna.
            pen = QPen(self.pen_color, 2, Qt.SolidLine)  # Ustawienie pióra z wybranym kolorem i grubością.
            painter.setPen(pen)  # Ustawienie pióra dla malowania.
            painter.drawLine(self.last_point, event.pos())  # Rysowanie linii od ostatniego punktu do obecnej pozycji kursora.
            self.last_point = event.pos()  # Aktualizacja ostatniego punktu.
            self.update()  # Odświeżenie okna, aby pokazać narysowane linie.

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:  # Sprawdzenie, czy zwolniono lewy przycisk myszy.
            self.drawing = False  # Ustawienie flagi rysowania na false.

    def paintEvent(self, event):
        painter = QPainter(self)  # Utworzenie obiektu QPainter dla okna.
        painter.drawPixmap(self.rect(), self.canvas)  # Rysowanie całego płótna na oknie.

    def select_color(self):
        self.pen_color = QColorDialog.getColor()  # Wyświetlenie okna dialogowego wyboru koloru.

    def save(self):
        # Wyświetlenie okna dialogowego do zapisu pliku.
        file_path, _ = QFileDialog.getSaveFileName(self, "Zapisz obraz", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if file_path == '':  # Sprawdzenie, czy ścieżka pliku nie jest pusta.
            return  # Jeśli ścieżka jest pusta, nie rób nic.
        self.canvas.save(file_path)  # Zapisanie płótna do pliku o wybranej ścieżce.

def main():
    app = QApplication(sys.argv)  # Utworzenie instancji aplikacji.
    window = DrawingArea()  # Utworzenie instancji okna aplikacji.
    window.show()  # Wyświetlenie okna aplikacji.
    sys.exit(app.exec())  # Rozpoczęcie pętli zdarzeń aplikacji.

if __name__ == '__main__':
    main()  # Wywołanie funkcji main.
