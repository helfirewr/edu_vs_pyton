import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Inicjalizacja klasy nadrzędnej wx.Frame
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        # Tworzenie panelu w ramce
        self.panel = wx.Panel(self)

        # Lista opcji dla listy rozwijanej
        choices = ["Opcja 1", "Opcja 2", "Opcja 3"]

        # Tworzenie listy rozwijanej
        # Argumenty wx.ComboBox:
        # self.panel - określa rodzica kontrolki, tutaj jest to panel.
        # pos=(50, 50) - określa pozycję kontrolki na panelu.
        # choices=choices - lista opcji dostępnych w liście rozwijanej.
        # style=wx.CB_READONLY - styl listy rozwijanej; CB_READONLY oznacza, że użytkownik
        # nie może wpisywać własnych wartości, tylko wybierać z dostępnych opcji.
        self.comboBox = wx.ComboBox(self.panel, pos=(50, 50), choices=choices,
                                    style=wx.CB_READONLY)

        # Dodanie obsługi zdarzenia wyboru opcji z listy rozwijanej
        self.comboBox.Bind(wx.EVT_COMBOBOX, self.OnCombo)

    # Metoda wywoływana po wybraniu opcji z listy rozwijanej
    def OnCombo(self, event):
        # Pobranie wybranej opcji
        selected = self.comboBox.GetValue()
        # Wyświetlenie komunikatu z wybraną opcją
        wx.MessageBox(f"Wybrałeś: {selected}", "Wybrano")

class MyApp(wx.App):
    def OnInit(self):
        # Tworzenie i pokazywanie głównego okna aplikacji.
        frame = MyFrame(None, "wxPython ComboBox Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
