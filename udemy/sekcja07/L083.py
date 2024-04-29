# Napisz dwie funkcje konwertujące temperaturę:
# 1) Funkcja cToF skonwertuje stopnie Celsjusza na Fahrenheita z wzoru:
#    fahrenheit = celsius * 9 / 5 + 32
# 2) Funkcja fToC konwertuje stopnie Fahrenheita na Celsjusza z wzoru:
#    celsius = (fahrenheit - 32) * 5 / 9;
# 3) Dodatkowo w konsoli pokaż wynik konwersji np:
#    "20 stopni Celsjusza to 68 stopni Fahrenheita" itd.
#    Jeśli chcesz użyj w string specjalnego znaku stopni ° za pomocą \xB0
# 4) Skonwertuj 20°C na Fahrenheita (68°F)
#    Skonwertuj 86°F na Celsjusza (30°C)

def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "stopni Celsjusza to", fahrenheit, "stopni fahrenheita")
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "\xB0 fahrenheita to", celsius, "\xB0  celsjusza")
    return celsius


f = cToF(20)
c = fToC(86)

