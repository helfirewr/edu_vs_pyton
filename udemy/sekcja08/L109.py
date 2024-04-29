
print( "Hello " + "World!" )
print( "Hello" * 3 )

string = "Hello World!"
print( string[0] ) # H
print( string[0:5] ) # Hello

print( "Hello" in string ) # True
print( "Hello" not in string ) # False

multline = """line 1
line 2
line 3
"""

print( "ala".capitalize() )
print( "Ola ma kota, Ola ma psa.".count("Ola") )

print( "Hello".center(20, "-") )

print( string.startswith("Hello") )
print( string.endswith("World!") )


print( string.find("Ola") )
print( string.find("World") )
print( "Ola ma psa, Ola ma kota".rfind("Ola") ) # 12

print( "2342345234".isalnum() )
print( "2342345234.".isalnum() )
print( "2342345234 k".isalnum() )

print( "2342345234 k".isalpha() )
print( " kot".isalpha() )
print( "kot".isalpha() )
print( "kot2".isalpha() )

print( "test".islower() )
print( "tesT".islower() )
print( "TEST".isupper() )

print( "   \n\n\t ".isspace() )

print( "-|".join( ["Ala","Ola","Adam"] ) )

print( "Hello World".lower() )
print( "Hello World".upper() )
print( "Hello World".swapcase() )

print( "   \n \t Hello World \n\n \t ".lstrip() )
print( "   \n \t Hello World \n\n \t ".rstrip() )
print( "   \n \t Hello   World \n\n \t ".strip() )


print( "Ola ma psa, Ola ma kota".replace("Ola", "Kasia") )

print( "My name is {myName}, I'm from {country}".format(myName = "Kuba", country = "Poland") )
print( "My name is {myName}, my postal code is {code}".format(myName = "Kuba", code = 11798) )
print( "My name is {0}, my postal code is {1}".format("Kuba", 11798) )
print( "My name is {}, my postal code is {}".format("Kuba", 11798) )
