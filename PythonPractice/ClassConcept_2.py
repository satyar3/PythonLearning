class Employee:

    def __init__(self, arg_name, arg_salary, arg_age):
        self.name = arg_name
        self.salary = arg_salary
        self.age = arg_age

    def print_name(self):
        print(f'Employee name is {self.name}, salary is {self.salary}, and age is {self.age}')


# Without Constructor
# rohan = Employee()
# rohan.name = 'Rohan'
# rohan.salary = 100
# rohan.age = 23

# Since rohan has the above attributes, then it'll print all the details
# rohan.print_name()  # Here as an argument, rohan object will be given

# Below will throw error as there is no attribute as name, salary,age
# satya = Employee()
# satya.print_name()


# With Constructor
rohan = Employee("Rohan", 200, 25)
print(rohan.age)
