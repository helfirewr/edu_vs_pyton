# Zadanie - organizacja imprezy
# W tym zadaniu skorzystasz z operacji na listach do zorganizowania listy gości
# oraz listy potraw na imprezie. Nauczysz się dodawać, usuwać elementy,
# sortować listy oraz wykonywać inne podstawowe operacje.
#
# 1) Stwórz listę `guests` z pięcioma imionami gości.
# 2) Wyświetl długość listy gości, aby sprawdzić, ilu masz gości.
# 3) Dodaj jeszcze dwóch gości na koniec listy.
# 4) Jeden z gości nie może przyjść. Usuń go z listy.
# 5) Posortuj listę gości alfabetycznie i wyświetl ją.
# 6) Stwórz listę `dishes` z trzema potrawami.
# 7) Dodaj do listy potraw jeszcze dwie nowe potrawy.
# 8) Wyświetl potrawę, która znajduje się na środku listy.
# 9) Usuń ostatnią potrawę z listy.
# 10) Sprawdź, czy na liście potraw znajduje się 'Pizza'. Jeśli tak,
#     wyświetl komunikat "Pizza jest na liście!", w przeciwnym razie
#     dodaj Pizzę do listy potraw.
#

guests = ["Anna", "Kasia", "Ewa", "Adam", "Karol"]
print("Ilość gości:", len(guests))

guests.append("Ola")
guests.append("Piotr")

guests.remove("Ewa")

guests.sort()
print("Posortowana lista gości:", guests)

dishes = ["Schabowy", "Ryba", "Pierogi"]
dishes.extend(["Tarta", "Wzetka"])

middleDish = dishes[len(dishes) // 2]

dishes.pop()

if "Pizza" in dishes:
    print("Pizza na liście")
else:
    dishes.append("Pizza")
    print("Pizza dodana do dań")

