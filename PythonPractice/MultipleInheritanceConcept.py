class Base1(object):

    def __init__(self):
        self.str1 = "Satya"
        print("Base 1")


class Base2(object):

    def __init__(self):
        self.str2 = "Tom"
        print("Base 2")


#Multiple Inheritance
class Child(Base1, Base2):

    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Child Class")


    def print_child(self):
        print(self.str1, self.str2)


c = Child()
c.print_child()