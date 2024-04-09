# 1. Stwórz krotkę z wartościami: 50, 100, 150, 200, 250
# 2. Pokaż typ krotki w konsoli
# 3. Pokaż w konsoli ilość elementów krotki
# 4. Pokaż ostatni element krotki wykorzystując len() -1
# 5. Następnie pokaż elementy od drugiego do czwartego
# 6. Pokaż trzeci element od końca z ujemnym indeksem

data = (50, 100, 150, 200, 250)
print(type(data))
print(len(data))
print("Ostatni element:", data[ len(data)-1 ])

print(data[2:4])
print(data[-3])
