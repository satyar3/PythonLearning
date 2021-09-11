def test(name):
    print("inside def for name : "+name)

test("Hello")

#Default or optional parameter
def country_name(country = "india"):
    print("Country name : "+country)

country_name() #No need to pass any argument if the default paramter is present
country_name("spain")



def get_name(list):
    for i in list:
        print(i)

name=[11,22,33,44,55,66,77]
get_name(name)

#Function with return
def sum(a,b):
    return a+b

print(sum(2,5))

print("---------------------------")

#recursion
def recursion_example(i):
    if(i<=3):
        print(i)
        i += 1
        recursion_example(i)

recursion_example(2)

print("---------------------------")

#Factorial of a given number
def fact(i):
    if(i > 1):
        i = i * fact(i - 1)
    return i

print(fact(3))