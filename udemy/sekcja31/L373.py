import wx

# Notebook czyli zakładki - tabs

class MyNotebookApp(wx.Frame):
    """
    Główne okno aplikacji z wx.Notebook.
    """
    def __init__(self):
        # Inicjalizacja okna głównego z tytułem i rozmiarem.
        super(MyNotebookApp, self).__init__(None, title="Przykład wx.Notebook", size=(400, 300))

        # Tworzymy panel, który będzie podstawą dla innych kontrolki, w tym dla wx.Notebook.
        panel = wx.Panel(self)

        # Tworzymy obiekt wx.Notebook na panelu.
        self.notebook = wx.Notebook(panel)

        # Tworzymy strony (zakładki) dla wx.Notebook.
        self.create_pages()

        # Ustawiamy układ (sizer), który zarządza rozmieszczeniem wx.Notebook w panelu.
        sizer = wx.BoxSizer()
        sizer.Add(self.notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        # Centrujemy okno na ekranie i pokazujemy je.
        self.Centre()
        self.Show()

    def create_pages(self):
        """
        Metoda do tworzenia stron (zakładek) dla wx.Notebook.
        """
        # Tworzymy dwie strony (panele) jako zakładki.
        page1 = wx.Panel(self.notebook)
        page2 = wx.Panel(self.notebook)

        # Dodajemy strony do wx.Notebook z etykietami.
        self.notebook.AddPage(page1, "Zakładka 1")
        self.notebook.AddPage(page2, "Zakładka 2")

        # Dodajemy przykładową zawartość do stron.
        wx.StaticText(page1, label="To jest zawartość zakładki 1", pos=(10, 10))
        wx.StaticText(page2, label="To jest zawartość zakładki 2", pos=(10, 10))

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyNotebookApp()
    app.MainLoop()
