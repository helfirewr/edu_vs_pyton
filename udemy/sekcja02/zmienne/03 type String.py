
str = "Hello World!"
print(str);
print( len(str) )
print( type(str) )

print( str[ len(str) - 1 ] )

print( str[0:5] ) # Hello

print( str * 4 )

strX3 = str * 3
print(strX3)

str2 = str + " and Hello again!"
print(str2)

print(str2[6:]) # World! and Hello again!

print(str2[::3]) # HlWl deogn

multiLine = """Pierwsza linia
Druga linia
Trzecia linia
"""

print(multiLine)


multiLine2 = "Pierwsza linia\nDruga Linia\nTrzecia \t linia \" \\ "
print(multiLine2)