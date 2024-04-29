import wx
import os

class ImageFrame(wx.Frame):
    """
    Główne okno aplikacji do wyświetlania obrazka.
    """
    def __init__(self, parent, title):
        super(ImageFrame, self).__init__(parent, title=title, size=(600, 400))

        panel = wx.Panel(self)

        # Uzyskanie ścieżki do bieżącego skryptu.
        current_dir = os.path.dirname(__file__)
        # Budowanie ścieżki do obrazka na bazie ścieżki do skryptu.
        image_path = os.path.join(current_dir, "images", "bird.jpg")

        # BITMAP_TYPE_ANY czyli automatycznie rozpoznawała format obrazka
        # na podstawie zawartości pliku
        image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
        bitmap = wx.Bitmap(image)

        wx.StaticBitmap(panel, -1, bitmap)

        self.SetSize((bitmap.GetWidth() + 50, bitmap.GetHeight() + 50))
        self.Centre()
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = ImageFrame(None, "Wyświetlacz obrazka")
    app.MainLoop()
