#
# Zadanie String replace
# 1) Stwórz funkcję cleanText, która będzie czyścić
#    przekazany tekst z określonych słów.
# 2) Użyj funkcję replace do zamiany podanych słów na
#    wykropkowane, które wielokrotnie może pojawić się
#    w przekazanym łańcuchu. Dla uproszczenia będziesz
#    zamieniać nazwy języków programowania ;)  np.
#    php zmienisz na ***, java na **** itd
# 3) Zastąp następujące słowa kluczowe:
#    JavaScript, java, php, html, css
# 4) Zwróć wyczyszczony tekst z funkcji cleanText.
# 5) Wywołaj funkcję na następującym lub podobnym tekście:
#   """Programowanie zacząłem z językiem php, następnie
#    poznałem: html i css, ale obecnie skupiam się na
#    JavaScript"""
#    Wynik pokaż w konsoli.

def cleanText(text):
    text = text.replace("javascript", "********")
    text = text.replace("java", "*" * 4)
    text = text.replace("php", "*" * 3)
    text = text.replace("html", "*" * 4)
    text = text.replace("css", "*" * 3)
    return text

content = """Programowanie zacząłem z językiem php, następnie korzystałem z
html i css, a na koniec poznałem python, java i javascript """

newContent = cleanText(content)
print(newContent)