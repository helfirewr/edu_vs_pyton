import re

# Metaznak \w w wyrażeniach regularnych oznacza "dopasuj dowolny znak alfanumeryczny lub podkreślenie".
# Konkretnie dopasowuje:
# - Dowolną literę (małą lub dużą) od a do z.
# - Dowolną cyfrę od 0 do 9.
# - Znak podkreślenia _.
# \w dopasuje każdy alfanumeryczny znak w tekście.

# Dopasowanie każdego znaku alfanumerycznego w tekście.
print(re.findall(r'\w', "Hello, world!"))  # ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

# Dopasowanie każdego całego słowa w tekście.
print(re.findall(r'\w+', "Hello, world!"))  # ['Hello', 'world']

# Dopasowanie wszystkich słów zaczynających się na 'H'.
print(re.findall(r'H\w+', "Hello, world! How are you?"))  # ['Hello', 'How']

# Lookahead w wyrażeniach regularnych pozwala na dopasowanie ciągu znaków,
# gdy kończy się on na inny określony ciąg znaków, ale bez włączania tego końcowego ciągu do wyniku.
tekst = "I have applejuice in the fridge, orangejuice, apple, test."
print(re.findall(r'apple(?=juice)', tekst))  # ['apple']

# Lookbehind działa podobnie do lookahead, ale sprawdza ciąg na początku.
tekst2 = "The railroad is long, road test."
print(re.findall(r'(?<=rail)road', tekst2))  # ['road']

# Negatywny lookbehind sprawdza, czy przed słowem NIE występuje dane słowo.
tekst3 = "I have a birthday cake today and chocolatecake tomorrow"
print(re.findall(r'(?<!chocolate)cake', tekst3))  # ['cake']

# Użycie nazwanych grup przechwytujących do dopasowania daty.
regex_date = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
result = regex_date.search("Test 2031-05-29 example")
if result:
    print(result.groupdict())  # {'year': '2031', 'month': '05', 'day': '29'}
    print(result.group('year'))  # 2031
