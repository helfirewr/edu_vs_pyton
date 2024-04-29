import os
import pickle

scriptDir = os.path.dirname(__file__)

number = 123456
listData = ["Ania", "Ola", "Kasia", 12345]
strData = "Test ąśćłó"

fh = open(scriptDir + "/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(listData, fh)
pickle.dump(strData, fh)
fh.close()


fh = open(scriptDir + "/data.dat", "rb")
numberInfo = pickle.load(fh)
listInfo = pickle.load(fh)
strInfo = pickle.load(fh)
fh.close()

print(numberInfo)
print(listInfo)
print(strInfo)


