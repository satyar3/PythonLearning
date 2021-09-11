#object is super class of all the class
# giving object name inside the bracket means, providing the parent class name
class Person(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


# In child class when there is no constructor defined then it'll take the structure from parent class
#If the constructor is defined then it'll take the copy of the latest defined constructor inside the child class
class Employee(Person):

    #Example of method overriding
    def is_employee(self):
        return True


#Test Person
emp = Person("Satya")
emp.name
print(emp.get_name(), emp.is_employee())

emp1 = Employee("ram")
print(emp1.get_name(), emp1.is_employee())