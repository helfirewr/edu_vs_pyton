# Napisz program sprawdzający wymagania potencjalnego kandydata na programistę
# 1) Dodaj zmienną experience z wartością 2, kolejną languages z listą elementów:
#    "python", "typescript", "javascript", "java"
#    Ostatnią zmienną będzie contractType o wartości "b2b" jaką chce kandydat
# 2) Wykorzystaj instrukcję if z operatorem and do sprawdzenia czy
#    doświadczenie kandydata to dwa lub więcej lat oraz czy zna język python
#    i java. Pamiętaj o wykorzystaniu operatora in do sprawdzenia czy
#    wartość jest w liście
# 3) Jeśli powyższe warunki są spełnione zrób kolejny if i sprawdź czy
#    typ kontraktu jest "b2b" lub "employment", pamiętaj o użyciu operatora or.
#    Zaprezentuj w terminalu informację że kandydat jest przyjęty, gdy warunki
#    są spełnione.
# 4) W przypadku, gdy warunki w if nie są spełnione pokaż w konsoli po else
#    odpowiednią informację

experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if experience >= 2 and "python" in languages and "java" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("Pracownik spełnia warunki do zatrudnienia")
    else:
        print("Pracownik nie spełnia wymogu typu zatrudnienia:", contractType)
else:
    print("Kandydat nie spełnia podstawowych warunków")



