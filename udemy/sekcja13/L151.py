import os

scriptDir = os.path.dirname(__file__)
print(scriptDir)

fh = open( scriptDir + "/ogonki.txt", "w" , encoding="utf-8" )
fh.write("tekst z ogonkami: ąśół\n")
fh.write("tekst z ogonkami: ąśół\n")
fh.write("tekst z ogonkami: ąśół\n")
fh.close()