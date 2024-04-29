import wx

class MyDialog(wx.Dialog):
    """
    Klasa MyDialog definiuje wygląd i zachowanie naszego okna dialogowego.
    """
    def __init__(self, parent, title):
        super(MyDialog, self).__init__(parent, title=title, size=(250, 150))
        # Panel dla elementów interfejsu
        panel = wx.Panel(self)

        # wx.ID_OK i wx.ID_CANCEL są standardowymi identyfikatorami w wxPython,
        # pozwalają automatycznie obsługiwać zamykanie dialogu z odpowiednim wynikiem.
        self.btn_ok = wx.Button(panel, wx.ID_OK, label="OK", pos=(15, 15), size=(90, 28))
        self.btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Anuluj", pos=(115, 15), size=(90, 28))

class MyFrame(wx.Frame):
    """
    Główne okno aplikacji.
    """
    def __init__(self):
        super(MyFrame, self).__init__(None, title="Dialog Example", size=(350, 200))
        panel = wx.Panel(self)

        # Tworzymy przycisk, który będzie otwierał okno dialogowe.
        self.open_dialog_btn = wx.Button(panel, label="Otwórz Dialog", pos=(100, 50))
        self.open_dialog_btn.Bind(wx.EVT_BUTTON, self.on_open_dialog)

        # Etykieta do wyświetlenia wyniku wyboru z dialogu.
        self.result_label = wx.StaticText(panel, label="Wynik: Brak", pos=(100, 100))

        self.Centre()
        self.Show()

    def on_open_dialog(self, event):
        """
        Metoda wywoływana po kliknięciu przycisku.
        Otwiera dialog i wyświetla wynik wyboru.
        """
        dialog = MyDialog(self, "Prosty Dialog")
        result = dialog.ShowModal()  # Pokazuje dialog modalnie i zwraca wynik.

        if result == wx.ID_OK:
            self.result_label.SetLabel("Wynik: OK")
        else:
            self.result_label.SetLabel("Wynik: Anuluj")
        dialog.Destroy()  # Ważne jest, aby zniszczyć dialog po użyciu!

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
