#
# Funkcja z domyślnymi wartościami parametrów
# 1) Napisz funkcję z parametrami:
#    - email
#    - country z domyślną wartością "Polska"
#    - company z domyślną wartością "Example Ltd"
# 2) Zwróć z funkcji słownik z elementami jak parametry
# 3) Przetestuj funkcję z jednym argumentem ola@example.com
#    oraz drugi przypadek z kasia@example.com będąca z UK

def getEmployee(email, country = "Polska", company = "Example Ltd"):
    return {
        "email": email,
        "country": country,
        "company": company
    }

print( getEmployee("ola@example.com") )
print( getEmployee("kasia@example.com", "UK") )
print( getEmployee("adam@example.com", "DE", "Test Ltd") )