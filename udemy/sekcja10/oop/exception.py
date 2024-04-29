import sys

data = ["Ola", "Ania", "Adam", "Kasia"]

print(data[0])

index = 2
try:
    print(data[index])
    print(data[index - 1])
    raise InterruptedError("some error!")
except IndexError:
    print("Error IndexError!", sys.exc_info()[0] )
except InterruptedError:
    print("Error InterruptedError!", sys.exc_info()[0] )
except:
    print("Error!", sys.exc_info()[0] )
else:
    print("No error!")


print(data[3])