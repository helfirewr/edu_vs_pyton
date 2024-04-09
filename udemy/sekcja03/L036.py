# 1) Oblicz zwrot z inwestycji po roku, zapisz poniższe
#    zmienne:
#    - capital - 5000
#    - rateOfInterest - 0.08  czyli 8%
#    - inflationRate - 0.15 czyli 15%
# 2) Oblicz zwrot z inwestycji oraz o ile spadła wartość
#    kapitału z uwagi na inflację, pokaż te kwoty w konsoli
# 3) Dodaj do kapitału zwrot z inwestycji oraz odejmij
#    utracony kapitał z uwagi na inflację, pokaż wartość
#    końcową w konsoli

capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

earnedMoney = capital * rateOfInterest
print("Zarobiona kwota:", earnedMoney)

lostMoney = capital * inflationRate
print("Utracona kwota:", lostMoney)

newCapital = capital + earnedMoney - lostMoney
print("Kwota końcowa:", newCapital)

