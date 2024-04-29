# Przykład aplikacji z użyciem wx.FlexGridSizer, który jest bardziej zaawansowaną
# wersją wx.GridSizer w wxPython, umożliwiającym bardziej elastyczne zarządzanie
# układem widgetów w siatce. wx.FlexGridSizer pozwala na określenie kolumn lub wierszy,
# które mogą się rozciągać, dostosowując się do zawartości lub rozmiaru okna.

import wx

class FlexGridSizerExample(wx.Frame):
    """
    Główne okno aplikacji demonstrujące użycie wx.FlexGridSizer.
    """
    def __init__(self):
        # Inicjalizacja okna głównego z tytułem i rozmiarem.
        super(FlexGridSizerExample, self).__init__(None,
                                                   title="Przykład wx.FlexGridSizer", size=(400, 300))

        # Tworzymy panel, który będzie podstawą dla innych kontrolki.
        panel = wx.Panel(self)

        # Utworzenie wx.FlexGridSizer z 3 wierszami, 2 kolumnami i odstępami 10 pikseli pomiędzy widgetami.
        flex_sizer = wx.FlexGridSizer(rows=3, cols=2, vgap=10, hgap=10)

        # Pozwalamy na rozciąganie się ostatniej kolumny i pierwszego wiersza.
        flex_sizer.AddGrowableCol(1, 1)
        flex_sizer.AddGrowableRow(0, 1)

        # Dodajemy etykiety i pola tekstowe do wx.FlexGridSizer.
        labels = ["Imię", "Nazwisko", "Adres email"]
        for label in labels:
            lbl = wx.StaticText(panel, label=label)
            txt = wx.TextCtrl(panel)
            # wx.ALIGN_RIGHT sprawia, że etykieta jest wyrównana do prawej,
            # wx.ALIGN_CENTER_VERTICAL wertykalnie centruje tekst etykiety względem pola tekstowego.
            # wx.EXPAND pozwala na rozciągnięcie pola tekstowego, aby wypełniło dostępną przestrzeń.
            flex_sizer.Add(lbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            flex_sizer.Add(txt, 0, wx.EXPAND)

        # Ustawienie wx.FlexGridSizer jako układu zarządzającego dla panelu.
        panel.SetSizer(flex_sizer)

        # Centrujemy okno na ekranie i pokazujemy je.
        self.Centre()
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)  # Tworzymy aplikację wx.
    frame = FlexGridSizerExample()  # Tworzymy instancję klasy okna.
    app.MainLoop()  # Uruchamiamy pętlę zdarzeń aplikacji.
