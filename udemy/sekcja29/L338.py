import re

# Dopasowanie pojedynczego znaku alfanumerycznego lub podkreślenia przed znakiem '@'.
print(re.findall(r'[a-zA-Z0-9]@', "My email is example@email.com"))  # ['e@']

# Dopasowanie jednego lub więcej znaków alfanumerycznych przed '@'.
print(re.findall(r'[a-zA-Z0-9]+@', "My email is example@email.com"))  # ['example@']

# Dopasowanie ciągu znaków alfanumerycznych przed '@', a następnie ciągu znaków alfanumerycznych.
print(re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+', "My email is example@email.com"))  # ['example@email']

# Dopasowanie pełnego adresu e-mail.
print(re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+', "My email is example@email.com"))
# ['example@email.com']

# Dopasowanie adresu e-mail z wieloma segmentami domenowymi.
# Dopasowuje adres e-mail z jednym lub więcej segmentami domenowymi.
# Wynik: ['example@email.com.pl'] - dopasowuje adres e-mail z kilkoma końcówkami domenowymi.
email_regex = r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
print(re.findall(email_regex, "My email is example@email.com.pl"))  # ['example@email.com.pl']

# Ten wzorzec jest bardziej kompleksowy i obsługuje różne przypadki adresów e-mail.
# - [a-zA-Z0-9._+-]+: Dopasowuje nazwę użytkownika składającą się z liter, cyfr,
#   kropek, podkreśleń, plusów i myślników.
# - @[a-zA-Z0-9.-]+: Dopasowuje nazwę domeny, która może zawierać litery, cyfry,
#   kropki i myślniki.
# - \.[a-zA-Z]{2,}: Dopasowuje końcówkę domeny, zaczynającą się od kropki,
