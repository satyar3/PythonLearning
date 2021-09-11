class Employee:
    num_of_leave = 8

    # Dunder Constructor
    def __init__(self, arg_name, arg_age, arg_sal):
        self.name = arg_name
        self.age = arg_age
        self.sal = arg_sal

    def print_det(self):
        print(f'name is {self.name}, age is {self.age}, sal is {self.sal}')

    @classmethod
    def cls_emthod(cls):
        cls.num_of_leave = 10

    # Operator Overloading
    def __add__(self, other):
        return self.sal + other.sal


emp = Employee('Satya', 20, 200)
emp.print_det()
print(emp.num_of_leave)
emp.cls_emthod()
print(emp.num_of_leave)

emp2 = Employee("Rohan", 40, 100)
print(emp+emp2)



# Any method starts with "__" called as Dunder method or magic methods
# Operator Overloading is possible
