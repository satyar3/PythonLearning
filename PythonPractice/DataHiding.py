class Employee:

    #hidden data member of Employee
    __salary = 100 #private varibale
    _age = 26 #Protected variable

emp = Employee();


#in python hidden data members can be accessed using tricky syntax
# unlike java the hidden data members can be access anywhere

#in order to access the hidden data member
print(emp._Employee__salary) #Name Mangling
print(emp._age)