class Car:
    # class variables
    # when a class variable is changed by an object, then system creates an instance variable for that object
    wheels = 4

    # any variable defined inside method or constructor, then it's called instance variable

    # constructor of the pass
    # Meaning of self is the object on which operations is being performed
    def __init__(self):
        print("inside constructor")

    # There is no concept of constructor overloading
    # in case of multiple constructor defined inside a class, the latest copy of the constructor gets called
    def __init__(self, car_color):
        self.car_color = car_color
        print("Car color is : " + self.car_color)

    def test(self):
        print("test method")

    # any variable defined inside method or constructor, then it's called instace variable
    def set_price(self, price):
        self.price = price

    def get_price(self, ):
        return self.price


#### once the latest line of the constructor is defined then the previous line of constructor woll not work
## i.e. contructor overloading is not possible in python
#   How to create object of a class
# c1 = Car()
# c1.test()
#
# Class variables can be access by the object name or by the class itself but when a class varibale is changed by the
# object, then system creates an instance variable for that object print(Car.wheels) print(c1.wheels)
#
# c1.set_price(2000)
# print(c1.get_price())

c2 = Car("Red")
c3 = Car("white")


# How to create a blank class
class BlankClass:
    pass


p1 = BlankClass()

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


class Point(object):
    def draw(self):
        print("Print Point")


p1 = Point()
p1.draw()
p1.x = 10
print(p1.x)

p2 = Point()
p2.draw()
print(p2.x)  # --> Attribute Error
