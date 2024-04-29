import re

# Używanie nawiasów kwadratowych [] w wyrażeniach regularnych do definiowania dopasowań znaków.
# Pozwalają one na dopasowanie jednego z wielu możliwych znaków określonych wewnątrz nawiasów.
tekst = "Apple, banana, cherry"
print(re.findall('[abc]', tekst))  # Znajduje 'b', 'a', 'a', 'a', 'c'

# Używanie flagi re.IGNORECASE (gi w JavaScript) do ignorowania wielkości liter.
print(re.findall('[abc]', tekst, re.IGNORECASE))  # Znajduje 'A', 'b', 'a', 'a', 'a', 'c'

# Dopasowanie małych liter od 'a' do 'z'.
print(re.findall('[a-z]', tekst))  # Znajduje wszystkie małe litery
# ['p', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y']

# Dopasowanie dużych liter od 'A' do 'Z'.
print(re.findall('[A-Z]', tekst))  # Znajduje tylko 'A' czyli ['A']

# Dopasowanie zarówno małych, jak i dużych liter (a-z, A-Z).
print(re.findall('[a-zA-Z]', tekst))  # Znajduje wszystkie litery
# ['A', 'p', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y']

# Dopasowanie liter i cyfr (a-z, A-Z, 0-9).
tekst2 = "Apple, test123"
print(re.findall('[a-zA-Z0-9]', tekst2))  # Znajduje litery i cyfry
# ['A', 'p', 'p', 'l', 'e', 't', 'e', 's', 't', '1', '2', '3']

# Dopasowanie wszystkiego poza 'p', 'e', i przecinkiem.
print(re.findall('[^pe,]', tekst2))  # Znajduje wszystko poza 'p', 'e' i ','
# ['A', 'l', ' ', 't', 's', 't', '1', '2', '3']

# Dopasowanie znaków specjalnych poprzez użycie ukośnika `\` przed nimi.
tekst3 = "apple [banana] {cherry} date"
print(re.findall(r'[\[\]{}]', tekst3))  # Znajduje '[', ']', '{', '}'

# Dopasowanie białych znaków (spacje, tabulacje, znaki nowej linii) za pomocą \s.
tekst4 = "Console laptop \n \t computer"
print(re.findall(r'\s', tekst4))  # Znajduje białe znaki: [' ', ' ', '\n', ' ', '\t', ' ']

# Użycie nawiasów klamrowych {} jako kwantyfikatorów.
# Dopasowanie dokładnej liczby wystąpień: 'a{4}' dopasowuje 'aaaa'.
tekst5 = "aaaaa bb aa cc aaaa"
print(re.findall('a{4}', tekst5))  # Znajduje ['aaaa', 'aaaa']

# Dopasowanie dokładnego ciągu 'aaaa' jako oddzielnego słowa.
print(re.findall(r'\ba{4}\b', tekst5))  # Znajduje 'aaaa' jako oddzielne słowo czyli ['aaaa']

# Dopasowanie od 3 do 5 wystąpień 'a'.
print(re.findall(r'\ba{3,5}\b', tekst5))  # ['aaaaa', 'aaaa']

# Dopasowanie minimum 3 wystąpień 'a'.
print(re.findall(r'\ba{3,}\b', tekst5))  # ['aaaaa', 'aaaa']

# Dopasowanie od 1 do 4 wystąpień 'a'.
print(re.findall(r'\ba{1,4}\b', tekst5))  # ['aa', 'aaaa']
