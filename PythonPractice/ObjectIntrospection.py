# To know the type of the object
print(type("hello"))
print(type(1))

# To know the id of the object
print(id("Hello"))
print(id("world"))


class A:
    var = "Class Var"

    def __init__(self, name):
        self.name = name

    def print_name(self, name):
        print(f'Printing name : {name}')


a = A("Satya")

# All the methods defined in the class
print(dir(a))

import inspect
print(inspect.getmembers(a))

print(inspect.get(a))
