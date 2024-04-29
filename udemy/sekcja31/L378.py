import wx

class TextEditor(wx.Frame):
    """
    Główne okno aplikacji będącej prostym edytorem tekstu.
    """
    def __init__(self, *args, **kw):
        # Inicjalizacja klasy bazowej wx.Frame z podanymi argumentami.
        super(TextEditor, self).__init__(*args, **kw)

        self.SetTitle("Prosty Edytor Tekstu")  # Ustawiamy tytuł okna aplikacji.

        self.init_ui()  # Wywołujemy metodę inicjalizującą interfejs użytkownika.

        self.SetSize((800, 600))  # Ustawiamy rozmiar okna.

        self.Centre()  # Centrujemy okno na ekranie.

    def init_ui(self):
        menubar = wx.MenuBar()  # Tworzymy pasek menu.

        fileMenu = wx.Menu()  # Tworzymy menu "Plik".

        # Dodajemy opcje "Otwórz" i "Zapisz" do menu "Plik".
        # wx.ID_OPEN i wx.ID_SAVE to predefiniowane identyfikatory wxWidgets dla
        # akcji otwarcia i zapisu.
        openItem = fileMenu.Append(wx.ID_OPEN, '&Otwórz', 'Otwórz plik')
        self.Bind(wx.EVT_MENU, self.on_open, openItem)  # Powiązanie zdarzenia z metodą on_open.

        saveItem = fileMenu.Append(wx.ID_SAVE, '&Zapisz', 'Zapisz plik')
        self.Bind(wx.EVT_MENU, self.on_save, saveItem)  # Powiązanie zdarzenia z metodą on_save.

        menubar.Append(fileMenu, '&Plik')  # Dodanie menu "Plik" do paska menu.
        self.SetMenuBar(menubar)  # Ustawienie paska menu dla okna.

        # Tworzymy kontrolkę wx.TextCtrl, która służy jako pole tekstowe do wprowadzania
        # i edycji tekstu.
        # wx.TE_MULTILINE pozwala na wprowadzanie tekstu wieloliniowego.
        self.text_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.text_ctrl.SetFocus()  # Ustawiamy fokus na polu tekstowym.

    def on_open(self, event):
        # Utworzenie dialogu do otwierania plików z filtrem na pliki tekstowe.
        with wx.FileDialog(self, "Otwórz plik tekstowy", wildcard="Pliki tekstowe (*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # Anulowanie dialogu przez użytkownika.
            path = fileDialog.GetPath()  # Pobranie ścieżki do wybranego pliku.
            try:
                with open(path, 'r') as file:
                    self.text_ctrl.SetValue(file.read())  # Wczytanie zawartości pliku do kontrolki tekstowej.
            except IOError:
                wx.LogError(f"Nie można otworzyć pliku '{path}'.")

    def on_save(self, event):
        # Utworzenie dialogu do zapisywania plików z opcją nadpisywania istniejących plików.
        with wx.FileDialog(self, "Zapisz plik tekstowy", wildcard="Pliki tekstowe (*.txt)|*.txt",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # Anulowanie dialogu przez użytkownika.
            path = fileDialog.GetPath()  # Pobranie ścieżki, gdzie plik ma być zapisany.
            try:
                with open(path, 'w') as file:
                    # Zapisanie zawartości kontrolki tekstowej do pliku.
                    file.write(self.text_ctrl.GetValue())
            except IOError:
                wx.LogError(f"Nie można zapisać pliku '{path}'.")

if __name__ == '__main__':
    app = wx.App(False)
    frame = TextEditor(None)
    frame.Show()
    app.MainLoop()
