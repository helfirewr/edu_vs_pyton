import os

print("Current working directory: ", os.getcwd() )

files = os.listdir(".")
print(files) # current working dir

files = os.listdir("../sekcja12/")
print(files)

files = os.listdir("../sekcja11/")
print(files)

files = os.listdir("../sekcja10/")
print(files)
