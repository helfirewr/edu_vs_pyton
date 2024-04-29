# String - zadanie:
# 1) Napisz funkcję getEmailParts przyjmującą
#    parametr email.
# 2) Wykorzystaj pobieranie fragmentów tekstu w python aby rozłożyć
#    email na części i zapisz je w zmiennych:
#    - user - od początku emaila do ostatniego znaku przed @
#    - domainName - tekst za @ i przed kropką
#    - domainExt - tekst za ostatnią kropką do końca
#    Uwaga: pamiętaj że określając początek i koniec fragmentu z stringa
#    możesz korzystać z zmiennych np:
#    monkeyInd = 5
#    user = email[0:monkeyInd]
# 3) Zwróć słownik z funkcji z elementami jak powyższe
#    zmienne. Pamiętaj aby użyć find aby określić
#    pozycję indeksu małpy w email, jeśli go nie ma
#    zwróć None z funkcji, podobnie z kropką.
# 4) Przetestuj funkcję na emailu:
#    ola@domena.com
#    W konsoli powinna pojawić się informacja:
#    {'user': 'ola', 'domainName': 'domena', 'domainExt': 'com'}


def getEmailParts(email):
    monkekInd = email.find("@")
    if monkekInd == -1: return None

    dotInd = email.rfind(".")
    if dotInd == -1: return None

    user = email[0:monkekInd]
    domainName = email[monkekInd+1 : dotInd]
    domainExt = email[dotInd+1 : len(email)]

    return {
        "user": user,
        "domainName": domainName,
        "domainExt": domainExt
    }

print(getEmailParts("ola@domena.com"))