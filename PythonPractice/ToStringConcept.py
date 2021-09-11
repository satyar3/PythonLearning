#String reprentation of objects
class Test:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    #represenation of object
    def __repr__(self):
        return f"value is x is {self.x} and y is {self.y}"

    #similar to to string
    def __str__(self):
        return f"the value is x is {self.x} and y is {self.y}"


t = Test(1,2)
print(t)
#print(id(t))

# In case of str method is present the the str method gets called
# in case of str method, then the repr method gets called
# In case both are absent then the object memory lcoation gets printed