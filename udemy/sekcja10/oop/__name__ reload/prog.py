import mathModule 
import importlib

print( mathModule.addNumbers(10,2) )
print( "prog.py: " + __name__ )

importlib.reload(mathModule)
importlib.reload(mathModule)
importlib.reload(mathModule)
