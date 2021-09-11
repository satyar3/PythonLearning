class Employee:

    no_of_leaves = 8

    def __init__(self, arg_name, arg_salary, arg_age):
        self.name = arg_name
        self.salary = arg_salary
        self.age = arg_age

    def print_name(self):
        print(f'Employee name is {self.name}, salary is {self.salary}, and age is {self.age}')

    # static method doesn't take any argument like class or self object
    @staticmethod
    def static_method_test(name):
        print(f'Hello {name}')



rohan = Employee("Rohan","200","25")
rohan.static_method_test("World")
Employee.static_method_test("Karan")