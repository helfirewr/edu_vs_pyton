
print(bool()) # False

# falsy values, czyli wartości które dają false przy konwersji na boolean
print( bool(False) ) # False
print( bool(0) ) # False
print( bool(0.0) ) # False
print( bool( () ) ) # False
print( bool( [] ) ) # False
print( bool( {} ) ) # False
print( bool( '' ) ) # False
print( bool( None ) ) # False

print( bool(True) ) # True
print( bool(10) ) # True
print( bool(-10) ) # True
print( bool(-12.234) ) # True
print( bool( (1,2,3) ) ) # True
print( bool( [0] ) ) # True
print( bool( {0} ) ) # True
print( bool( "z" ) ) # True
