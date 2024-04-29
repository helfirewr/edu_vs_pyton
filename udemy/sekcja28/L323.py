import unittest

# Klasa Person, reprezentująca osobę z imieniem i wiekiem.
# Posiada metodę introduction, która zwraca napis z przywitaniem.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Klasa Employee, która dziedziczy po klasie Person i rozszerza ją o pole position (stanowisko).
# Nadpisuje metodę introduction, dodając informacje o stanowisku.
class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def introduction(self):
        return super().introduction() + f" I work as a {self.position}."


# Ta klasa skupia się na testowaniu zachowań obiektów klas Person i Employee.
class PersonAndEmployeeTest(unittest.TestCase):

    # Metoda setUp służy do przygotowania kontekstu dla każdego testu.
    # Jest wywoływana przed każdą metodą testową.
    def setUp(self):
        self.person = Person("John", 30)
        self.employee = Employee("Anna", 40, "Engineer")

    # Metoda tearDown służy do sprzątania po testach.
    # Jest wywoływana po każdej metodzie testowej.
    def tearDown(self):
        del self.person
        del self.employee

    # Test sprawdzający, czy metoda introduction klasy Person działa poprawnie.
    def test_person_introduction(self):
        self.assertEqual(self.person.introduction(),
                         "My name is John and I am 30 years old.")

    # Test sprawdzający, czy metoda introduction klasy Employee działa poprawnie
    # i czy prawidłowo rozszerza zachowanie metody z klasy bazowej.
    def test_employee_introduction(self):
        self.assertEqual(self.employee.introduction(),
                         "My name is Anna and I am 40 years old. I work as a Engineer.")


if __name__ == '__main__':
    unittest.main()
