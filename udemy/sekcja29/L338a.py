import re

# Dopasowanie numeru telefonu w formacie '123-456-789'.
numer_telefonu = "My phone number is 123-456-789"
print(re.findall(r'[0-9]{3}-[0-9]{3}-[0-9]{3}', numer_telefonu))  # ['123-456-789']

# Dopasowanie pełnych adresów URL z https, http i ftp.
# Wzorzec dopasowuje 'http://', 'https://' lub 'ftp://',
# a następnie jeden lub więcej znaków alfanumerycznych, kropek lub myślników,
# kończących się na co najmniej jednej kropce i ciągu liter.
tekst_url = ("Visit my website at https://www.example.com.pl or "
             "ftp://files.example.com or http://www.example.com.pl for more information.")
url_pattern = r'https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|ftp:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
urls = re.findall(url_pattern, tekst_url)
print(urls)  # ['https://www.example.com.pl', 'ftp://files.example.com', 'http://www.example.com.pl']

# Dopasowanie znaczników HTML takich jak <div>, </div>, <p>, </p>.
tekst_html = "This is a <div>container</div> with a <p>paragraph</p> inside."
print(re.findall(r'<\/?[a-zA-Z]+>', tekst_html))  # ['<div>', '</div>', '<p>', '</p>']

