import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        self.panel = wx.Panel(self)

        # Tworzenie checkbox'ów
        self.cb1 = wx.CheckBox(self.panel, label="Opcja 1", pos=(20, 20))
        self.cb2 = wx.CheckBox(self.panel, label="Opcja 2", pos=(20, 50))
        self.cb3 = wx.CheckBox(self.panel, label="Opcja 3", pos=(20, 80))

        # Tworzenie przycisku do sprawdzenia stanu checkbox'ów
        self.button = wx.Button(self.panel, label="Sprawdź", pos=(20, 110))
        self.button.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, event):
        # Metoda wywoływana po kliknięciu przycisku
        status = []

        # Sprawdzanie, które checkbox'y są zaznaczone
        if self.cb1.IsChecked():
            status.append(self.cb1.GetLabel()) # tekst etykiety
        if self.cb2.IsChecked():
            status.append(self.cb2.GetLabel())
        if self.cb3.IsChecked():
            status.append(self.cb3.GetLabel())

        # Wyświetlanie komunikatu z zaznaczonymi opcjami
        wx.MessageBox("Zaznaczone opcje: " + ", ".join(status), "Informacja")

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "wxPython Checkbox Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
