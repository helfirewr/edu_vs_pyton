
class Employee:
    "Employee class describing company employee"
    # static variables for all objects based on Employee
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
        "Constructor for Employee"
        """
            line 1
            line 2
        """
        self.name = name

        Employee.numEmployees += 1
        print(self.name, "numEmployees: ", Employee.numEmployees)

        Employee.employeesList.append(self)


    def printAllEmployees(self):
        for el in Employee.employeesList:
            print(el.name)

    def printDocString(self):
        print(Employee.__doc__)


employee1 = Employee("Ola")
employee2 = Employee("Kasia")
employee3 = Employee("Adam")
employee4 = Employee("Karol")

print("Employee.numEmployees: ", Employee.numEmployees)
print()

employee1.printAllEmployees()

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

print("name attr in Employee: ", hasattr(employee1, "name") )
print("city attr in Employee: ", hasattr(employee1, "city") )
employee1.city = "Krk"
print("city attr in Employee: ", hasattr(employee1, "city") )

setattr(employee1, "name", "Kasia")
print("employee1.name: ", getattr(employee1, "name") )
