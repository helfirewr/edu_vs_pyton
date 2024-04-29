# HtmlWindow to Kontrolka która umożliwia wyświetlanie treści HTML bezpośrednio w aplikacji

import wx
import wx.html

class HtmlWindowExample(wx.Frame):
    """
    Główne okno aplikacji z wx.html.HtmlWindow.
    """
    def __init__(self):
        # Inicjalizacja okna głównego z tytułem i rozmiarem.
        super(HtmlWindowExample, self).__init__(None, title="Przykład wx.html.HtmlWindow",
                                                size=(600, 400))

        # Tworzymy wx.html.HtmlWindow na tym oknie.
        self.html_win = wx.html.HtmlWindow(self)

        # Ustawiamy treść HTML, którą chcemy wyświetlić.
        self.html_win.SetPage("""
            <h1>Witaj w wxPython!</h1>
            <p>
                WxPython to biblioteka do tworzenia interfejsów graficznych (GUI) 
                dla języka programowania Python.
            </p>
            <p>
                <a href="http://wxpython.com/">Odwiedź oficjalną stronę wxPython</a> 
                po więcej informacji.
            </p>
        """)

        # Centrujemy okno na ekranie i pokazujemy je.
        self.Centre()
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)  # Tworzymy aplikację wx.
    frame = HtmlWindowExample()  # Tworzymy instancję głównego okna.
    app.MainLoop()  # Uruchamiamy pętlę zdarzeń aplikacji.
