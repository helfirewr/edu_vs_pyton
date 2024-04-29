import math
import random


distance=random.randint(100,1000)
fuelConsuptionPer100=7.3
expectedFuelConsuption=round(distance/100)*fuelConsuptionPer100
print("distance="+str(distance)+" złuzycie paliwa: "+str(expectedFuelConsuption))

fuelPrice=((random.uniform(5.6, 7.4)))
cost=fuelPrice*expectedFuelConsuption
print("koszt podróży: ", round(cost,2))
if(cost>400):
    print("WYsokie koszty")
else:
    print("przystępne koszty")






