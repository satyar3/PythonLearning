class Employee:

    no_of_leaves = 8

    def __init__(self, arg_name, arg_salary, arg_age):
        self.name = arg_name
        self.salary = arg_salary
        self.age = arg_age

    def print_name(self):
        print(f'Employee name is {self.name}, salary is {self.salary}, and age is {self.age}')

    # This will help to access class variables and we can change it
    # This can be accessible by either class or objects
    @classmethod
    def change_number_of_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


rohan = Employee("Rohan", 200, 25)
print(rohan.no_of_leaves)
karan = Employee("Karan",300,34)
rohan.change_number_of_leaves(20)
print(rohan.no_of_leaves)
print(karan.no_of_leaves)