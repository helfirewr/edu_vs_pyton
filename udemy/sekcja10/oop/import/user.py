class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "User: " + self.name



user1 = User("Ola")
print(user1)


class Employee(User):
    def __init__(self, name):
        User.__init__(self, name)

    def __str__(self):
        return "Employee: " + self.name