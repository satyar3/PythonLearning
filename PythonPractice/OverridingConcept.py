class A(object):
    class_var_1 = "In class A"

    def __init__(self):
        self.class_var_1 = "In instance var class A"
        print()


class B(A):
    class_var_1 = "In class B"

    def __init__(self):
        super().__init__()
        self.class_var_1 = "In instance var class B"
        print()


a = A()
b = B()

# print(a.class_var_1)
print(b.class_var_1)

# In case of Overriding:
# 1 - 1st it'll check for instance variable in the same class
# 2 - Then it'll check for the instance variable in the super class ( if no constructor is defined ) if defined it'll print the class varible of B
# 3 - Then it'll check in the self class class variable
# 4 - Then it'll check for the super class class variable
