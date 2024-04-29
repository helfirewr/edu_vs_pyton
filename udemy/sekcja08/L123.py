# Formatowanie ciągów tekstowych w Pythonie umożliwia wstawianie wartości
# zmiennych bezpośrednio do tekstów, co ułatwia tworzenie dynamicznych
# wiadomości i raportów. Od wersji Python 3.6 dostępna jest wygodna metoda
# formatowania ciągów znaków znana jako f-string (formatted string literals).

# Podstawy f-string
# Aby użyć f-string, wystarczy poprzedzić ciąg znaków literą f lub F przed
# otwarciem cudzysłowu. Wewnątrz ciągu znaków, w nawiasach klamrowych {},
# można umieszczać wyrażenia, które zostaną zastąpione ich wartościami.

age = 32
print("age:", age)

print(f"Wiek użytkownika {age} lat.")

pi = 3.141592
print(f"Wartość liczby pi to dokładnie {pi:.2f}")

list = ["jabłko", "cytryna"]
print(f"Lista owoców: {list} ")

person = { "name": "Ania", "age": 32 }
print(f"User: {person}, {person['name']}")

a = 5
b = 10
print(f"Wynik dodawania liczb {a} i {b} to dokładnie: {a + b}")

score = 75
print(f"Test zakończony {('sukcesem' if score >= 70 else 'porażką' )}")
