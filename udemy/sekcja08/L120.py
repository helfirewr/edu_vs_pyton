# Zadanie - zarządzanie książką adresową
# W tym zadaniu będziesz używać słowników do zarządzania prostą
# książką adresową. Nauczysz się dodawać, usuwać, kopiować oraz
# przeszukiwać dane w słowniku.
#
# 1) Stwórz słownik `addressBook` zawierający początkowo jedną
#    osobę: Jan Kowalski, mieszka w Gdańsku, kod pocztowy 80-000.
# 2) Dodaj do książki adresowej nową osobę: Anna Nowak, mieszka w
#    Warszawie, kod pocztowy 00-001.
# 3) Usuń Jan Kowalski z książki adresowej.
# 4) Skopiuj książkę adresową do nowej zmiennej i sprawdź, czy
#    kopia jest identyczna (porównaj referencje i zawartość).
# 5) Sprawdź, czy w skopiowanej książce adresowej jest osoba
#    mieszka w Krakowie. Jeśli nie, wyświetl odpowiedni komunikat.
# 6) Wyświetl wszystkie klucze i wartości w książce adresowej.
#


addressBook = {
    "Jan Kowalski": {"city": "Gdańsk", "postalCode": "80-000"}
}
print("Początkowa wartość książki adresowej:", addressBook)

addressBook["Anna Nowak"] = {"city": "Warszawa", "postalCode": "00-001"}
print("Książka po aktualizacji", addressBook)

del addressBook["Jan Kowalski"]
print("Książka po skasowaniu elementu:", addressBook)

addressBookCopy = addressBook.copy()
print("Czy zawartość jest identyczna:", addressBook == addressBookCopy)
print("Czy referencje są identyczne:", addressBook is addressBookCopy)

found = False
for person in addressBook.values():
    if person["city"] == "Kraków":
        found = True
        print("W książce adresowej jest osoba z Krakowa")

if not found:
    print("W książce adresowej nie ma osoby z Krakowa")


print("Klucze:", addressBook.keys())
print("Wartości:", addressBook.values())

