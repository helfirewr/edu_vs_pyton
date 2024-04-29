
class Car:
    def __init__(self, brand, name, color, year ):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1   
        self.setTopSpeed(230)
        self.printInfo()

    def printInfo(self):
        print(self.brand, self.name, 
            self.color, self.year, self.mileage, self.topSpeed)

    def setTopSpeed(self, newTopSpeed):
        self.topSpeed = newTopSpeed


mustang = Car("Ford", "Mustang", "red", 1970)
mustang.mileage = 100
mustang.setTopSpeed(235) 
mustang.printInfo() 

charger = Car("Dodge", "Charger", "Blue", 1971) 
charger.setTopSpeed(232)
charger.printInfo()