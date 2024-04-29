
# W poniższym przykładzie użyjemy wxPython do stworzenia prostego interfejsu
# z kilkoma przyciskami rozmieszczonymi za pomocą wx.BoxSizer, który jest
# narzędziem do zarządzania układem (layout) w aplikacjach wxPython.
# wx.BoxSizer pozwala na elastyczne rozmieszczanie kontrolek w poziomie
# (horyzontalnie) lub w pionie (wertykalnie), ułatwiając tworzenie zorganizowanych
# interfejsów.

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.panel = wx.Panel(self)

        # Utworzenie BoxSizer'a, który będzie zarządzał układem w pionie (wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Tworzenie przycisków
        # -1 jest specjalną wartością, która służy do wskazania,
        # że ma być użyte domyślne ID dla danego elementu interfejsu użytkownika.
        # Jest to przydatne, gdy nie potrzebujesz specyficznych identyfikatorów
        # dla poszczególnych kontrolek w interfejsie użytkownika.
        # W praktyce, jeśli nie planujesz odwoływać się do przycisku (lub innego elementu GUI)
        # za pomocą jego ID lub nie potrzebujesz przypisywać mu specyficznego identyfikatora
        # dla celów obsługi zdarzeń lub innych operacji, używanie -1 jest całkowicie akceptowalne i zalecane
        btn1 = wx.Button(self.panel, -1, "Przycisk 1")
        btn2 = wx.Button(self.panel, -1, "Przycisk 2")
        btn3 = wx.Button(self.panel, -1, "Przycisk 3")

        # Dodawanie przycisków do sizer'a z określeniem,
        # że mają się rozciągać (flaga wx.EXPAND)
        # i z określeniem marginesu z każdej strony (border=10)
        self.sizer.Add(btn1, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
        self.sizer.Add(btn2, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
        self.sizer.Add(btn3, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)

        # Ustawienie sizer'a jako głównego zarządzającego układem dla panelu
        self.panel.SetSizer(self.sizer)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Przykład z BoxSizer")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
