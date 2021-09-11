class Base1(object):

    def __init__(self, name):
        self.name = name
        print("Base 1")


class Base2(object):

    def __init__(self, age, salary):
        self.age = age
        self.salary = salary
        print("Base 2")


# Multiple Inheritance
class Child(Base1, Base2):

    def __init__(self, name, age, salary):
        Base1.__init__(self, name)
        Base2.__init__(self, age, salary)

    def print_child(self):
        print(self.name, self.age, self.salary)


c = Child("Satya", 20, 2000)
c.print_child()

# Note:
# In case of Multiple inheritance, order of the arguments the child class matters
# In case both the parent has constructors, only 1st class constructor can be given to avoid error
# In case the same variable name is defined in both the places, then the 1st class takes priority
