import os

print("Absolute path to script file", __file__)
scriptDir = os.path.dirname(__file__)
print("Absolute path to script directory: ", scriptDir)

pathToFile = scriptDir + "\\newFile.txt"
print("Path to file:", pathToFile)

fh = open(pathToFile, "w")
fh.write("content!")
fh.close()