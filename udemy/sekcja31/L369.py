# Importujemy moduł wx do pracy z wxPython
import wx

# Definiujemy klasę głównego okna aplikacji dziedziczącą po wx.Frame
class GaugeExample(wx.Frame):
    def __init__(self, parent, title):
        # Wywołujemy konstruktor klasy bazowej, inicjalizując okno
        super(GaugeExample, self).__init__(parent, title=title, size=(300, 200))

        # Tworzymy panel, który będzie zawierał wszystkie inne widgety
        self.panel = wx.Panel(self)

        # Tworzymy etykietę (Label) do wyświetlania postępu
        self.label = wx.StaticText(self.panel, label="Postęp: 0%", pos=(20, 20))

        # Tworzymy Gauge (pasek postępu)
        # 'range' określa maksymalną wartość postępu (tutaj 100)
        self.gauge = wx.Gauge(self.panel, range=100, pos=(20, 50), size=(250, 25))

        # Tworzymy przycisk do symulowania postępu
        self.button = wx.Button(self.panel, label='Zwiększ postęp', pos=(20, 90))
        # Powiązujemy zdarzenie kliknięcia przycisku z metodą onButtonClick
        self.button.Bind(wx.EVT_BUTTON, self.onButtonClick)

        # Ustawiamy wartość początkową postępu
        self.progress = 0

        # Wyświetlamy okno
        self.Centre()
        self.Show()

    # Metoda wywoływana po kliknięciu przycisku
    def onButtonClick(self, event):
        # Zwiększamy wartość postępu
        self.progress += 10
        if self.progress > 100:
            self.progress = 0  # Resetujemy postęp, jeśli przekroczy maksimum

        # Aktualizujemy pasek postępu i etykietę
        self.gauge.SetValue(self.progress)
        self.label.SetLabel(f"Postęp: {self.progress}%")

# Inicjalizacja aplikacji wx
if __name__ == '__main__':
    app = wx.App(False)
    frame = GaugeExample(None, 'Przykład wx.Gauge')
    app.MainLoop()

