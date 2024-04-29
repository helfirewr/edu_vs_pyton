# Importujemy moduł wx do pracy z wxPython
import wx

# Definiujemy klasę głównego okna aplikacji dziedziczącą po wx.Frame
class ScrollBarExample(wx.Frame):
    def __init__(self, parent, title):
        # Wywołujemy konstruktor klasy bazowej, inicjalizując okno
        super(ScrollBarExample, self).__init__(parent, title=title, size=(300, 200))

        # Tworzymy panel, który będzie zawierał wszystkie inne widgety
        self.panel = wx.Panel(self)

        # Tworzymy etykietę (Label) do wyświetlania wartości wybranej na ScrollBar
        self.label = wx.StaticText(self.panel, label="Przewiń, aby zobaczyć wartość", pos=(40, 10))

        # Tworzymy ScrollBar
        self.scrollbar = wx.ScrollBar(self.panel, pos=(40, 40), size=(200, -1), style=wx.SB_HORIZONTAL)
        # Ustawiamy ScrollBar (wartość, rozmiar kciuka, zakres, rozmiar strony)
        self.scrollbar.SetScrollbar(0, 1, 100, 1)

        # Powiązujemy zdarzenie przewijania ScrollBar z metodą onScroll
        self.scrollbar.Bind(wx.EVT_SCROLL, self.onScroll)

        # Wyświetlamy okno
        self.Centre()
        self.Show()

    # Metoda wywoływana podczas przewijania ScrollBar
    def onScroll(self, event):
        # Pobieramy pozycję ScrollBar
        position = self.scrollbar.GetThumbPosition()
        # Aktualizujemy tekst etykiety zgodnie z pozycją ScrollBar
        self.label.SetLabel(f'Wybrana wartość: {position}')

# Inicjalizacja aplikacji wx
if __name__ == '__main__':
    app = wx.App(False)
    frame = ScrollBarExample(None, 'ScrollBar Example')
    app.MainLoop()

