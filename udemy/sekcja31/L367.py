import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Inicjalizacja klasy nadrzędnej wx.Frame z tytułem i rozmiarem okna
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        # Tworzenie panelu w ramce
        self.panel = wx.Panel(self)

        # Utworzenie kontrolki SpinCtrl
        # Pozwala użytkownikowi wybrać liczbę z przedziału 0 do 100, z początkową wartością
        # ustawioną na 0
        # Argumenty wx.SpinCtrl:
        # self.panel - określa rodzica kontrolki, tutaj jest to panel.
        # value='0' - początkowa wartość wyświetlana w SpinCtrl jako string.
        # pos=(20, 20) - określa pozycję kontrolki na panelu.
        # size=(100, -1) - określa rozmiar kontrolki; -1 w wysokości oznacza domyślną wartość.
        # min=0, max=100 - zakres wartości, które można wybrać.
        # initial=0 - początkowa wartość SpinCtrl jako liczba.
        # name="spinControl" - nazwa kontrolki, używana w programowaniu dla identyfikacji.
        self.spinCtrl = wx.SpinCtrl(self.panel, value='0', pos=(20, 20), size=(100, -1),
                                    min=0, max=100, initial=0, name="spinControl")

        # Utworzenie etykiety (label) do wyświetlania wybranej wartości
        self.label = wx.StaticText(self.panel, label="Wybrana wartość: 0", pos=(20, 60))

        # Powiązanie SpinCtrl z metodą OnSpinCtrl, która zostanie wywołana przy zmianie wartości
        self.spinCtrl.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl)

    # Metoda obsługująca zmianę wartości w SpinCtrl
    def OnSpinCtrl(self, event):
        # Pobranie aktualnej wartości z SpinCtrl
        value = self.spinCtrl.GetValue()
        # Aktualizacja tekstu etykiety, aby odzwierciedlić wybraną wartość
        self.label.SetLabel(f"Wybrana wartość: {value}")

class MyApp(wx.App):
    def OnInit(self):
        # Tworzenie i pokazywanie głównego okna aplikacji.
        frame = MyFrame(None, "wxPython SpinCtrl Example")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
