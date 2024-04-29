
number = 5

while number > 0:
    print(number)
    number -= 1


number = 1

while number < 6:
    print(number)
    number += 1


num = 0
while True:
    print("Wprawdź liczbę lub exit aby aby zakończyć")
    strData = input()
    if strData.upper() == "EXIT" : break
    num += int(strData)
    print("Wartość po dodaniu liczby: " + str(num))


number = 3
while number > 0:
    print(number)
    number -= 1
else:
    print("number po pętli: " + str(number))


