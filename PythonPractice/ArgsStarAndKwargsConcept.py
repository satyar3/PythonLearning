# Here in th below case the entire list is given to the function as tuple
# In case both normal argument and */** argument is given, the 1st should be normal argument and then */** argument is allowed
# both *args and **kwargs are optional

def list_p(*args):
    print(type(args))
    print(args[0])


a = [1, 2, 3, 4, 4, 2]
list_p(*a)


# **kwargs

def get_student_marks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"for key {key} the value is {value}")


dd = {'1': '1', '2': '2', '3': '3'}
# mm = {}
# for key,value in dd.items():
#     mm[str(key)] = str(value)
# print(mm)

# The key type must be a string always
get_student_marks(**dd)


