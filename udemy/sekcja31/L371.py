# Importujemy moduł wx do pracy z wxPython
import wx

# Definiujemy klasę głównego okna aplikacji dziedziczącą po wx.Frame
class ToolbarExample(wx.Frame):
    def __init__(self, parent, title):
        # Wywołujemy konstruktor klasy bazowej, inicjalizując okno
        super(ToolbarExample, self).__init__(parent, title=title, size=(300, 200))

        # Tworzymy panel, na którym będą umieszczone pozostałe widgety
        self.panel = wx.Panel(self)

        # Tworzymy etykietę, która będzie pokazywać wynik akcji z paska narzędzi
        self.label = wx.StaticText(self.panel, label="Wybierz akcję z paska narzędzi", pos=(10, 10))

        # Inicjalizujemy pasek narzędzi
        self.toolbar = self.CreateToolBar()
        # Dodajemy narzędzia (przyciski) do paska narzędzi
        # każde ma etykietę i ikonę
        t1 = self.toolbar.AddTool(wx.ID_ANY, 'Akcja 1', wx.ArtProvider.GetBitmap(wx.ART_COPY))
        t2 = self.toolbar.AddTool(wx.ID_ANY, 'Akcja 2', wx.ArtProvider.GetBitmap(wx.ART_PASTE))
        # Realizujemy pasek narzędzi, co jest wymagane, aby był widoczny
        self.toolbar.Realize()

        # Powiązujemy zdarzenia kliknięcia narzędzia z odpowiednimi metodami
        self.Bind(wx.EVT_TOOL, self.onAction1, t1)
        self.Bind(wx.EVT_TOOL, self.onAction2, t2)

        # Wyświetlamy okno
        self.Centre() # wyśrodkowanie okna
        self.Show()

    # Metoda wywoływana po kliknięciu "Akcja 1"
    def onAction1(self, event):
        self.label.SetLabel("Wybrano Akcję 1")

    # Metoda wywoływana po kliknięciu "Akcja 2"
    def onAction2(self, event):
        self.label.SetLabel("Wybrano Akcję 2")

# Inicjalizacja aplikacji wx
if __name__ == '__main__':
    app = wx.App(False)
    frame = ToolbarExample(None, 'Przykład wx.ToolBar')
    app.MainLoop()

