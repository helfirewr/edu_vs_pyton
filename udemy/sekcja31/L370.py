import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Inicjalizacja klasy nadrzędnej wx.Frame
        super(MyFrame, self).__init__(parent, title=title, size=(300, 150))

        # Tworzenie panelu w ramce
        self.panel = wx.Panel(self)

        # Utworzenie kontrolki wx.TextCtrl, która służy jako pole do wprowadzania tekstu
        # Argumenty wx.TextCtrl:
        # self.panel - określa rodzica kontrolki, tutaj jest to panel.
        # value="" - początkowa wartość tekstu w polu tekstowym, tutaj puste.
        # pos=(20, 20) - określa pozycję kontrolki na panelu.
        # size=(260, 20) - określa rozmiar kontrolki.
        self.textCtrl = wx.TextCtrl(self.panel, value="", pos=(20, 20), size=(260, 20))

        # Utworzenie przycisku do wysyłania wprowadzonego tekstu
        # Argumenty wx.Button:
        # self.panel - określa rodzica przycisku, tutaj jest to panel.
        # label="Pokaż" - tekst wyświetlany na przycisku.
        # pos=(100, 50) - określa pozycję przycisku na panelu.
        # size=(100, 30) - określa rozmiar przycisku.
        self.button = wx.Button(self.panel, label="Pokaż", pos=(100, 50), size=(100, 30))

        # Powiązanie przycisku z metodą OnButtonClick, która zostanie wywołana
        # po jego kliknięciu
        self.button.Bind(wx.EVT_BUTTON, self.OnButtonClick)

    # Metoda obsługująca kliknięcie przycisku
    def OnButtonClick(self, event):
        # Pobranie tekstu z kontrolki TextCtrl
        userText = self.textCtrl.GetValue()
        # Wyświetlenie pobranego tekstu w oknie dialogowym
        wx.MessageBox(userText, "Wprowadzony tekst")

class MyApp(wx.App):
    def OnInit(self):
        # Tworzenie i pokazywanie głównego okna aplikacji.
        frame = MyFrame(None, "wxPython TextCtrl Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
