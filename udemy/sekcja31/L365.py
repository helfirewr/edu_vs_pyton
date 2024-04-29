import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Inicjalizacja klasy nadrzędnej wx.Frame
        super(MyFrame, self).__init__(parent, title=title, size=(400, 200))

        # Tworzenie panelu w ramce
        self.panel = wx.Panel(self)

        # Utworzenie suwaka (slidera) z zakresem wartości od 0 do 100 i początkową wartością na 50
        # Argumenty wx.Slider:
        # self.panel - określa rodzica kontrolki, tutaj jest to panel.
        # value=50 - początkowa wartość suwaka.
        # minValue=0, maxValue=100 - określa zakres wartości, przez które może się poruszać suwak.
        # pos=(20, 20) - określa pozycję kontrolki na panelu.
        # size=(300, -1) - określa rozmiar kontrolki; -1 w wysokości oznacza domyślną wartość.
        # style=wx.SL_HORIZONTAL - określa orientację suwaka jako poziomą.
        self.slider = wx.Slider(self.panel, value=50, minValue=0, maxValue=100,
                                pos=(20, 20), size=(300, -1),
                                style=wx.SL_HORIZONTAL)

        # Utworzenie etykiety (label) do wyświetlania aktualnej wartości suwaka
        self.label = wx.StaticText(self.panel, label="Aktualna wartość: 50", pos=(20, 60))

        # Powiązanie suwaka z metodą OnSliderScroll, która zostanie wywołana
        # przy zmianie wartości suwaka
        self.slider.Bind(wx.EVT_SLIDER, self.OnSliderScroll)

    # Metoda obsługująca zdarzenie przesuwania suwaka
    def OnSliderScroll(self, event):
        # Pobranie aktualnej wartości suwaka
        value = self.slider.GetValue()
        # Aktualizacja tekstu etykiety, aby odzwierciedlić aktualną wartość suwaka
        self.label.SetLabel(f"Aktualna wartość: {value}")

class MyApp(wx.App):
    def OnInit(self):
        # Tworzenie i pokazywanie głównego okna aplikacji.
        frame = MyFrame(None, "wxPython Slider Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

