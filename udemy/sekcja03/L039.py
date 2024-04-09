
# operatory porównania

result = 12 == 4
print(result)

print( 12 != 4 ) # True
print( 12 != 12 ) # False

print( 8 > 1 ) # True
print( 7 > 10 ) # False
print( 2 < 10 ) # True

print( 5 >= 3 ) # True
print( 5 >= 5 ) # True
print( 10 <= 10 ) # True
print( 9 <= 10 ) # True
print( 20 <= 10 ) # False

if 10 > 5:
    print("10 większe od 5")


a = 12
b = 8

if b < a:
    print(" a mniejsze od b")


a=[1,2,3]
b=[1,2,3,4]
print(a==b)
print(id(a))
print(id(b))