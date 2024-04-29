# W poniższym przykładzie zastosujemy wx.GridSizer, który jest jednym z układów
# (sizerów) w wxPython, umożliwiającym rozmieszczanie widgetów w siatce (gridzie).
# wx.GridSizer automatycznie zarządza rozmiarem i pozycją widgetów w siatce o określonej
# liczbie wierszy i kolumn. Przykład będzie prostą aplikacją, która wykorzystuje
# wx.GridSizer do utworzenia siatki przycisków.

import wx

class GridSizerExample(wx.Frame):
    """
    Główne okno aplikacji demonstrujące użycie wx.GridSizer.
    """
    def __init__(self):
        # Inicjalizacja okna głównego z tytułem i rozmiarem.
        super(GridSizerExample, self).__init__(None, title="Przykład wx.GridSizer", size=(300, 200))

        # Tworzymy panel, który będzie zawierał wszystkie widgety.
        panel = wx.Panel(self)

        # Utworzenie wx.GridSizer z 2 wierszami, 3 kolumnami i odstępami 5 pikseli pomiędzy widgetami.
        grid_sizer = wx.GridSizer(rows=2, cols=3, vgap=5, hgap=5)

        # Dodajemy przyciski do wx.GridSizer.
        for i in range(6):
            button = wx.Button(panel, label=f"Przycisk {i+1}")
            # wx.EXPAND sprawia, że przyciski będą rozciągnięte, aby wypełnić
            # przestrzeń komórki siatki.
            grid_sizer.Add(button, 0, wx.EXPAND)

        # Ustawienie wx.GridSizer jako układu zarządzającego dla panelu.
        panel.SetSizer(grid_sizer)

        # Wyśrodkowanie okna na ekranie i pokazanie go.
        self.Centre()
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)  # Tworzenie aplikacji wx.
    frame = GridSizerExample()  # Tworzenie instancji klasy okna.
    app.MainLoop()  # Uruchomienie pętli zdarzeń aplikacji.
