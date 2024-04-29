import wx

class ImageViewer(wx.Frame):
    """
    Główne okno aplikacji służącej jako prosta przeglądarka obrazków.
    """
    def __init__(self, parent, title):
        super(ImageViewer, self).__init__(parent, title=title, size=(500, 400))

        self.panel = wx.Panel(self)
        self.image = None

        self.initUI()
        self.Centre()
        self.Show()

    def initUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        # wx.ID_OPEN to predefiniowany identyfikator dla akcji otwierania plików.
        openItem = fileMenu.Append(wx.ID_OPEN, '&Otwórz', 'Otwórz obrazek')
        self.Bind(wx.EVT_MENU, self.onOpen, openItem)

        menubar.Append(fileMenu, '&Plik')
        self.SetMenuBar(menubar)

    def onOpen(self, event):
        """
        Otwiera okno dialogowe do wyboru obrazka i wyświetla go.
        """
        # wx.FD_OPEN oznacza, że okno dialogowe jest używane do otwierania plików.
        # wx.FD_FILE_MUST_EXIST wymusza, aby wybrany plik musiał istnieć.
        with wx.FileDialog(self, "Otwórz obrazek",
                           wildcard="Pliki obrazów (*.png;*.jpeg;*.jpg)|*.png;*.jpeg;*.jpg",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # Użytkownik anulował okno dialogowe.

            # Pobranie ścieżki do wybranego pliku.
            imagePath = fileDialog.GetPath()
            self.displayImage(imagePath)

    def displayImage(self, path):
        """
        Wyświetla wybrany obrazek.
        """
        # Wczytanie obrazka i konwersja do bitmapy.
        self.image = wx.Image(path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self.panel, -1, self.image, (10, 10), (self.image.GetWidth(), self.image.GetHeight()))
        self.SetSize((self.image.GetWidth() + 100, self.image.GetHeight() + 100))

if __name__ == '__main__':
    app = wx.App(False)
    frame = ImageViewer(None, 'Prosta przeglądarka obrazków')
    app.MainLoop()
