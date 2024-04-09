# Zadanie do wykonania:
# Wykorzystaj operator konkatenacji do łączenia stringów i list,
# oraz zastosuj prostą instrukcję warunkową if.
# 1) Połącz dwa stringi 'firstName' i 'lastName' w jeden string 'fullName'
#    i wyświetl go. Dodaj między nimi spację.
# 2) Stwórz dwie listy: 'listOne' z liczbami od 1 do 3 i 'listTwo' z liczbami
#    od 4 do 6. Połącz je w jedną listę 'combinedList' i wyświetl.
# 3) Jeśli długość 'combinedList' jest większa od 5, wyświetl "Lista jest długa".
# 4) Do zmiennej 'greeting' dodaj string 'Hello', a do niej 'fullName'.
#    Sprawdź, czy w 'greeting' znajduje się słowo 'Hello'. Jeśli tak,
#    wyświetl pełne powitanie.


firstName = "Adam"
lastName = "Kowalski"
fullName = firstName + " " + lastName
print(fullName)

listOne = [1,2,3]
listTwo = [4,5,6]
combinedList = listOne + listTwo
print(combinedList)

if len(combinedList) > 5:
    print("Lista jest długa")

greeting = "Hello " + fullName
if "Hello" in greeting:
    print(greeting)