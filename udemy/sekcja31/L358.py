import wx

# Definicja klasy głównego okna aplikacji
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        # Tworzenie panelu w ramce
        self.panel = wx.Panel(self)

        # Tworzenie przycisku
        self.button = wx.Button(self.panel, label="Kliknij mnie", pos=(100, 50))

        # Powiązanie przycisku z metodą on_button_click
        # EVT_BUTTON to zdarzenie klknięcia przycisku
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

    # Metoda wywoływana po kliknięciu przycisku
    def on_button_click(self, event):
        wx.MessageBox("Przycisk został kliknięty!", "Informacja")

# Definicja klasy aplikacji
class MyApp(wx.App):
    def OnInit(self):
        # Tworzenie instancji klasy MyFrame
        self.frame = MyFrame(parent=None, title="Przykład wxPython")
        self.frame.Show()
        return True

# Główna część programu
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
