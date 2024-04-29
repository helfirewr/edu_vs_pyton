import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Inicjalizacja klasy nadrzędnej wx.Frame
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        # Tworzenie MenuBar - paska menu, który pojawi się na górze okna aplikacji
        menuBar = wx.MenuBar()

        # Tworzenie obiektów wx.Menu, które będą działać jako poszczególne menu w MenuBar
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        helpMenu = wx.Menu()

        # Dodawanie pozycji do menu 'Plik'
        # wx.ID_ABOUT i wx.ID_EXIT to predefiniowane identyfikatory w wxPython, które
        # mogą być użyte do łatwego tworzenia standardowych pozycji menu
        # Uwaga "&O programie" wskazuje nie tylko treść ale i skrót, czyli
        # będąc w menu kliknięcie klawisza o wybierze tą opcję
        fileMenu.Append(wx.ID_ABOUT, "&O programie", " Informacje o aplikacji")
        fileMenu.AppendSeparator()  # Dodaje separator linii do menu
        fileMenu.Append(wx.ID_EXIT, "E&xit", " Zakończ aplikację")

        # Dodawanie pozycji do menu 'Edycja'
        editMenu.Append(wx.NewId(), "&Kopiuj", " Kopiuj tekst")
        editMenu.Append(wx.NewId(), "&Wklej", " Wklej tekst")

        # Dodawanie pozycji do menu 'Pomoc'
        helpMenu.Append(wx.NewId(), "&Dokumentacja", " Otwórz dokumentację")

        # Dodawanie zbudowanych menu do MenuBar
        menuBar.Append(fileMenu, "&Plik")
        menuBar.Append(editMenu, "&Edycja")
        menuBar.Append(helpMenu, "&Pomoc")

        # Przypisanie MenuBar do okna aplikacji
        self.SetMenuBar(menuBar)

        # Dodanie obsługi zdarzeń dla pozycji menu
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)

    # Metoda obsługująca zdarzenie kliknięcia 'O programie'
    def OnAbout(self, event):
        wx.MessageBox("To jest prosty przykład aplikacji z MenuBar", "O programie")

    # Metoda obsługująca zdarzenie kliknięcia 'Exit'
    def OnExit(self, event):
        self.Close(True)  # Zamknięcie aplikacji

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "wxPython MenuBar Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
