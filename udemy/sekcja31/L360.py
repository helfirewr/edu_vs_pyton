import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 100))

        self.panel = wx.Panel(self)

        # Utworzenie BoxSizer'a, który będzie zarządzał układem w poziomie (wx.HORIZONTAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Tworzenie przycisków
        btn1 = wx.Button(self.panel, -1, "Przycisk 1")
        btn2 = wx.Button(self.panel, -1, "Przycisk 2")
        btn3 = wx.Button(self.panel, -1, "Przycisk 3")

        # Dodawanie przycisków do sizer'a z określeniem,
        # że mają się rozciągać (flaga wx.EXPAND)
        # i z określeniem marginesu z każdej strony (border=10)
        # W układzie poziomym, wx.EXPAND pozwoli przyciskom rozciągać się w pionie,
        # wypełniając dostępną przestrzeń.
        self.sizer.Add(btn1, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
        self.sizer.Add(btn2, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
        self.sizer.Add(btn3, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)

        # Ustawienie sizer'a jako głównego zarządzającego układem dla panelu
        self.panel.SetSizer(self.sizer)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Przykład z BoxSizer - Poziomo")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
