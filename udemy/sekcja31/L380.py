import wx
import os

class DirectoryViewer(wx.Frame):
    """
    Główne okno aplikacji służącej do przeglądania zawartości katalogu.
    """
    def __init__(self, parent, title):
        super(DirectoryViewer, self).__init__(parent, title=title, size=(600, 400))

        self.panel = wx.Panel(self)
        self.initUI()
        self.Centre()
        self.Show()

    def initUI(self):
        self.fileListCtrl = wx.TextCtrl(self.panel,
                                        style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        # Utworzenie sizer'a, który pozwala na rozciągnięcie kontrolki TextCtrl
        # na całe okno.
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.fileListCtrl, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizerAndFit(sizer)

        # Utworzenie menu.
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        openDirItem = fileMenu.Append(wx.ID_ANY, '&Wybierz katalog', 'Wybierz katalog')
        self.Bind(wx.EVT_MENU, self.onOpenDir, openDirItem)

        menubar.Append(fileMenu, '&Plik')
        self.SetMenuBar(menubar)

    def onOpenDir(self, event):
        with wx.DirDialog(self, "Wybierz katalog",
                          style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.fileListCtrl.Clear()
            directoryPath = dirDialog.GetPath()
            for root, dirs, files in os.walk(directoryPath):
                for filename in files:
                    filePath = os.path.join(root, filename)
                    self.fileListCtrl.AppendText(filePath + '\n')

if __name__ == '__main__':
    app = wx.App(False)
    frame = DirectoryViewer(None, 'Przeglądarka Katalogu')
    app.MainLoop()
