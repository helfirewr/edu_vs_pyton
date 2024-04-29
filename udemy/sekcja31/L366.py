import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Inicjalizacja klasy nadrzędnej wx.Frame
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        # Tworzenie panelu w ramce
        self.panel = wx.Panel(self)

        # Tworzenie grupy przycisków opcji (radio buttons)
        # Argumenty wx.RadioButton:
        # self.panel - określa rodzica kontrolki, tutaj jest to panel.
        # label="Opcja X" - tekst wyświetlany obok przycisku opcji.
        # pos=(20, Y) - określa pozycję kontrolki na panelu.
        # style=wx.RB_GROUP - tylko pierwszy przycisk opcji w grupie powinien mieć ten styl,
        # oznacza to początek nowej grupy przycisków opcji.
        self.radio1 = wx.RadioButton(self.panel, label="Opcja 1", pos=(20, 20), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(self.panel, label="Opcja 2", pos=(20, 50))
        self.radio3 = wx.RadioButton(self.panel, label="Opcja 3", pos=(20, 80))

        # Utworzenie etykiety (label) do wyświetlania wybranej opcji
        self.selectedLabel = wx.StaticText(self.panel, label="Wybrana opcja: ", pos=(20, 120))

        # Powiązanie przycisków opcji z metodą OnRadioSelect, która
        # zostanie wywołana po wybraniu opcji
        self.radio1.Bind(wx.EVT_RADIOBUTTON, self.OnRadioSelect)
        self.radio2.Bind(wx.EVT_RADIOBUTTON, self.OnRadioSelect)
        self.radio3.Bind(wx.EVT_RADIOBUTTON, self.OnRadioSelect)

    # Metoda obsługująca zdarzenie wyboru przycisku opcji
    def OnRadioSelect(self, event):
        # Pobranie obiektu, który wygenerował zdarzenie
        radioSelected = event.GetEventObject()
        # Aktualizacja tekstu etykiety, aby odzwierciedlić wybraną opcję
        self.selectedLabel.SetLabel(f"Wybrana opcja: {radioSelected.GetLabel()}")

class MyApp(wx.App):
    def OnInit(self):
        # Tworzenie i pokazywanie głównego okna aplikacji.
        frame = MyFrame(None, "wxPython RadioButton Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
