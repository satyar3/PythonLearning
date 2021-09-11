class BaseClass(object):
    pass # Empty Class


class ChildClass(BaseClass):
    pass

#Test Code

# issubclass --> to verify is a class is child of another class

print(issubclass(ChildClass, BaseClass))

c = ChildClass()
b = BaseClass()
print(isinstance(b,ChildClass))