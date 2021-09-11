s1 = "test selenium"
s2 = 'hello world'

print (s1)
print (s2)

print(s1, end='')
print(s2)


print(s1, end='__')
print(s2)

print (s1[0])
print(s1[0:5]) #this is called string slicing
#print (s1[15]) #IndexError: string index out of range

print ("hello \nworld")
print("hello\tworld")
print ("test"*5)


#To check if any string is present in another string
print("test " in s1)
print("test " not in s1)

#Formatiing
print("My name is %s and age is %d" %("Tom",25))
print ("hey {0} how are you {1}".format("satya", "doing"))
total = 3

#f string formula
print(f'{"total : "}{total}')

def login(user_name,password):
    print(f"user name is {user_name} and password is {password}")

login("hello","world")

#Writing a paragraph
para = '''para 1
then 2 
and then 3'''

print(para)

#String literals
print ('hi I am \' satya\'')

str = "this is my python code"

#Only the 1st Letter will be capitalized
print (str.capitalize())

#count of the string inside another string
print(str.count("python"))

#to get the index of the string inside another string
print(str.find("code"))
print(str.find("code1"))


#length of a string
print(len(str))

print(str.lower())

#Strip
str1 = " hello "
print(str1.lstrip())
print(str1.rstrip())

#Highest Alphabate char present inside a string
print(max("kjdadx"))
print((min("sadsaz")))
print((min(" sadsaz"))) # in case of space it gives space

#replace
str3 = "Hello Test Python"
print(str3.replace("Python", "code"))

str4 = "hello java hello python hello java"
str5 = str4.split("hello")
print (str5)
print (str5[1])

print(str4.upper())

str5 = "python"
print(str5[-1]) #in reverse python assigns the indes as -1,-2,-3 .. from right to left
print(str5[5])
print(str5[::-1])
print(str5[::-2])

#String comparion
a = "hello"
b = "hello"
print(a is b) #here the identity will be compared
print(a == b) #here the value will be compared

