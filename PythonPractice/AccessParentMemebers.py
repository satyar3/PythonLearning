class Base(object):

    def __init__(self, x):
        self.x = x

class Child(Base):

    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def print_work(self):
        print(Base.x, self.y)


c = Child(1, 2)
c.print_work()