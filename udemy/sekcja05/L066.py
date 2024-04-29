lista=range(-4,5)
for i in lista:
    if i==0:
        print("Zero jest parzyste")
    elif i%2==0:
        print(str(i), "liczba parzysta")
    else:
        print(str(i), "liczba nieparzysta")