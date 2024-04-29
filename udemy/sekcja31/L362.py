import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Inicjalizacja klasy nadrzędnej wx.Frame
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        # Tworzenie panelu w ramce
        self.panel = wx.Panel(self)

        # Utworzenie kontrolki ListCtrl
        # Argumenty wx.ListCtrl:
        # self.panel - określa rodzica kontrolki, tutaj jest to panel.
        # size=(400, 300) - określa rozmiar kontrolki.
        # style=wx.LC_REPORT | wx.BORDER_SUNKEN - określa styl kontrolki:
        # wx.LC_REPORT - pozwala na wyświetlanie elementów listy w formie tabeli z nagłówkami kolumn.
        # wx.BORDER_SUNKEN - dodaje efekt wciśniętej ramki wokół kontrolki.
        self.list_ctrl = wx.ListCtrl(self.panel, size=(400, 300),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN)

        # Dodawanie kolumn do ListCtrl
        # Argumenty metody InsertColumn:
        # 0, 1, 2 - indeks kolumny, kolejność dodawania kolumn zaczynając od 0.
        # 'ID', 'Nazwa', 'Opis' - etykieta nagłówka kolumny.
        # wx.LIST_FORMAT_LEFT - wyrównanie tekstu w kolumnie do lewej.
        # width=50, 150, 200 - szerokość kolumny w pikselach.
        self.list_ctrl.InsertColumn(0, 'ID', wx.LIST_FORMAT_LEFT, width=50)
        self.list_ctrl.InsertColumn(1, 'Nazwa', wx.LIST_FORMAT_LEFT, width=150)
        self.list_ctrl.InsertColumn(2, 'Opis', wx.LIST_FORMAT_LEFT, width=200)

        # Dodawanie elementów do ListCtrl
        # Dodanie nowego wiersza na pozycji 0 z wartością "1" w pierwszej kolumnie.
        self.list_ctrl.InsertItem(0, "1")
        # Ustawienie wartości w drugiej kolumnie wiersza 0.
        self.list_ctrl.SetItem(0, 1, "Element 1")
        # Ustawienie wartości w trzeciej kolumnie wiersza 0.
        self.list_ctrl.SetItem(0, 2, "To jest pierwszy element listy")

        # Dodanie nowego wiersza na pozycji 1 z wartością "2" w pierwszej kolumnie.
        self.list_ctrl.InsertItem(1, "2")
        # Ustawienie wartości w drugiej kolumnie wiersza 2.
        self.list_ctrl.SetItem(1, 1, "Element 2")
        # Ustawienie wartości w trzeciej kolumnie wiersza 2.
        self.list_ctrl.SetItem(1, 2, "To jest drugi element listy")


class MyApp(wx.App):
    def OnInit(self):
        # Tworzenie i pokazywanie głównego okna aplikacji.
        frame = MyFrame(None, "wxPython ListCtrl Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
