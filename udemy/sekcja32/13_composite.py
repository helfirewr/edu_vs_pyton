# Wzorzec projektowy Kompozyt jest używany do organizowania 
# obiektów w struktury drzewiaste,
# umożliwiając klientom traktowanie pojedynczych obiektów 
# i ich GRUP w jednolity sposób.

# Zalety:
# 1. Uproszczenie kodu klienta, który używa kompozytu i pojedynczych obiektów.
# 2. Ułatwia zarządzanie hierarchiami obiektów.

# Wady:
# 1. Może sprawić, że projekt stanie się zbyt ogólny, co utrudnia 
#    ograniczenie funkcji do konkretnych komponentów.
# 2. W niektórych przypadkach może być trudno ograniczyć 
#    funkcjonalność poszczególnych komponentów.

from abc import ABC, abstractmethod

# Interfejs komponentu systemu plików
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Pojedynczy plik
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Plik: {self.name}")

# Folder zawierający pliki lub inne foldery
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.display()

# Użycie wzorca Kompozyt
root_folder = Folder("Root")
documents_folder = Folder("Dokumenty")
music_folder = Folder("Muzyka")

file1 = File("CV.pdf")
file2 = File("Wydatki.xlsx")
file3 = File("Ulubione.mp3")

documents_folder.add(file1)
documents_folder.add(file2)
music_folder.add(file3)

root_folder.add(documents_folder)
root_folder.add(music_folder)

root_folder.display()
