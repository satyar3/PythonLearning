class Employee:

    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal

    def print_name(self):
        return f'This Employee {self.name}, {self.age}, {self.sal}'

    @property # to use the below method as an attribute
    def email(self):
        if self.name == None:
            print("No name set, use setter")
        return f'{self.name} and {self.age}'

    @email.setter # to set the attribute value using setter
    def email(self, name):
        self.name = name

    @email.deleter # to delete the attribute
    def email(self):
        self.name = None

emp1 = Employee('satya', 200,26)
emp2 = Employee('rohan', 23, 201)

print(emp1.print_name())
print(emp2.print_name())

print(emp1.email)
emp1.email = "Satyarrrr"
print(emp1.print_name())

del emp1.email
print(emp1.email)

