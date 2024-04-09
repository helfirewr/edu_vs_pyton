#
# Zadanie - operacje na rachunku bankowym, skorzystaj
# z skróconych operatorów przypisania z operacją
# matematyczną np:  +=  -=  *=  /=  itd
# Uwaga, po każdej operacji wyświetl saldo w konsoli
# 1) Stwórz zmienną balance z wartością początkową 1000
# 2) Dodaj wartość nowej pensji 7000
# 3) Odejmij 2000 kosztów za mieszkanie
# 4) Błąd banku pomnożył Twoje saldo trzykrotnie
# 5) Odejmij 4000 na komputer
# 6) Bank zorientował się że powstał błąd i cofa ostatnie
#    transakcje. Dodaj do salda 4000, podziel je przez 3
#    i dopiero teraz odejmij 4000
# 7) Pokaż saldo końcowe

balance = 1000
balance += 7000
print("saldo po wpływie pensji: " + str(balance))
balance -= 2000
print("saldo po wydatkach na mieszkanie: ", balance)
balance *= 3
print("saldo po błędzie banku: ", balance)
balance -= 4000
print("saldo po zakupie komputera: ", balance)
balance = ((balance + 4000) / 3) - 4000
print("saldo po poprawieniu błędu banku: ", balance)