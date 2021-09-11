def login(user_name,password):
    print(f"user name is {user_name} and password is {password}")

login("hello","world")
login(user_name="cool",password="stuff")


# * argument --> you can pass n number of parameters and it'll
# behave like array
def get_marks(*arg):
    for x in arg:
        print(x)

get_marks(10,20,34)
get_marks("satya")


#keyword arguments --> ** (using key and value pair)
def get_student_marks(**args):
    for key,val in args.items():
        print("for key %s, the value is %s"%(key,val))

#This is keyword arguments
#if you are miing posotional arguments with keyword arguments, then use keyword arguments
#after the positional arguments
get_student_marks(satya=1,ram=2,shyam=3)


#lambda or anonymous function --> function without have any name
cube = lambda x: x*3
print(cube(4))

