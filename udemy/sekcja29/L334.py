import re

# Tworzenie wzorca regex do wyszukiwania litery 'a' w tekście.
simple_regex = re.compile('a')

# Sprawdzanie, czy wzorzec znajduje się w tekście "apple".
print(simple_regex.search("apple") is not None)  # True, "apple" zawiera 'a'
print(simple_regex.search("cherry") is not None)  # False, "cherry" nie zawiera 'a'

# Znalezienie wszystkich dopasowań 'ap' w "apple".
print(re.findall('ap', "apple"))  # ['ap']

# Znalezienie wszystkich dopasowań 'l' w "apple".
print(re.findall('l', "apple"))  # ['l']

# Wyszukiwanie wszystkich wystąpień 'a' w "banana", ignorując wielkość liter.
print(re.findall('a', "banana", re.IGNORECASE))  # ['a', 'a', 'a']

# Wyszukiwanie wszystkich wystąpień 'n' i 'N' w "banana BANana".
print(re.findall('[nN]', "banana BANana"))  # ['n', 'n', 'N', 'n']

# Wyszukiwanie wszystkich wystąpień 'b', 'n' i 'N' w "banana BANana".
print(re.findall('[BnN]', "banana BANana"))  # ['n', 'n', 'B', 'N', 'n']

# Wyszukiwanie wszystkich wystąpień 't' w tekście, ignorując wielkość liter.
# ['T', 't', 'T', 'T', 't']
print(re.findall('t', "Temperature in Tokyo is Too high today", re.IGNORECASE))

# Wyszukiwanie wszystkich wystąpień "city" w tekście, ignorując wielkość liter.
tekst = ("I love the city. City is beautiful, especially in the CITY center. "
         "The electricity bill is high.")
print(re.findall('city', tekst, re.IGNORECASE))  # ['city', 'City', 'CITY', 'city']

# Wyszukiwanie dokładnych wystąpień "city" w tekście, używając granic słowa (\b).
print(re.findall(r'\bcity\b', tekst, re.IGNORECASE))  # ['city', 'City', 'CITY']

# Wyszukiwanie słów "mountain" lub "sea" w tekście, używając operatora alternatywy (|).
tekst2 = ("The mountain view is breathtaking. I also love the serenity "
          "of the sea. Sea is nice.")
print(re.findall(r'\b(mountain|sea)\b', tekst2, re.IGNORECASE))  # ['mountain', 'sea', 'Sea']

# Wyszukiwanie pierwszego wystąpienia cyfry w tekście "I have 3 cats and 20 dogs.".
print(re.search(r'\d', "I have 3 cats and 20 dogs."))  # Zwraca obiekt Match dla '3'

# Wyszukiwanie wszystkich wystąpień cyfr w tekście.
print(re.findall(r'\d', "I have 3 cats and 20 dogs."))  # ['3', '2', '0']

# Wyszukiwanie ciągów cyfr w tekście, używając kwantyfikatora '+'.
print(re.findall(r'\d+', "I have 3 cats and 20 dogs."))  # ['3', '20']
