
# wxPython to biblioteka do tworzenia interfejsów graficznych w Pythonie,
# pierwszym krokiem jest jej instalacja. wxPython działa na wielu platformach,
# w tym na Windows, macOS i Linux. Przykładowa lekcja poniżej pomoże Ci
# stworzyć prosty interfejs użytkownika z wykorzystaniem wxPython.

# pip install wxPython

import wx  # Importowanie modułu wx do pracy z wxPython.

# Definicja klasy głównej aplikacji dziedziczącej po wx.App.
class MyApp(wx.App):
    def OnInit(self):  # Metoda inicjalizująca aplikację.
        # Utworzenie ramki głównej aplikacji.
        self.frame = MyFrame(None, title="Pierwsza aplikacja wxPython")
        self.frame.Show()  # Wyświetlenie ramki.
        return True

# Definicja klasy ramki dziedziczącej po wx.Frame.
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Wywołanie konstruktora klasy bazowej z tytułem okna.
        super().__init__(parent, title=title)
        self.panel = wx.Panel(self)  # Utworzenie panelu w ramce.
        # Dodanie tekstu do panelu.
        self.text = wx.StaticText(self.panel, label="Witaj w wxPython!", pos=(10,10))

# Uruchomienie aplikacji.
if __name__ == "__main__":
    app = MyApp()  # Utworzenie instancji aplikacji.
    app.MainLoop()  # Uruchomienie pętli zdarzeń aplikacji.

