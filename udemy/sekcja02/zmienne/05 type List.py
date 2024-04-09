
list = ["Ola", "Ania", 23, 99, "Rafał"]
print( type(list) ) # <class 'list'>
print(list)

print(list[0])
print( len(list) )
print( list[4] )
print( list[len(list)-1] )
# print( list[5] ) # IndexError: list index out of range

print( list[-1] )
print( list[-2] )
# print( list[-6] ) # IndexError: list index out of range

print( list[1:4] ) # ['Ania', 23, 99]
print( list[2:] ) # [23, 99, 'Rafał']

list[0] = "Kasia"
print(list) # ['Kasia', 'Ania', 23, 99, 'Rafał']

del list[2]
print(list) # ['Kasia', 'Ania', 99, 'Rafał']

print( 99 in list )
print( "Rafał" in list )
print( "Ola" in list )

if "Ania2" in list: 
    print("Ania jest w liście list")
    print("Kolejny kod")

print("Dalszy kod")


for el in list:
    print(el)


data = [ 
    ["Daniel", "Rafał"],
    ["Kasia", "Ania"],
    ["Ola", "Adam"]
 ]

print(len(data))

print(data[1][0]) # Kasia
print(data[2][1]) # Adam

data1 = [1, 2, 3]
data2 = [4, 5, 6]

numbers = data1 + data2
print(numbers)

numbersX2 = numbers * 2
print(numbersX2)
