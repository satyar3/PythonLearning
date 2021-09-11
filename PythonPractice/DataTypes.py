#No need to declare any type of the variable

i = 32
print (i)
print(type(i))

i = i+0.1
print (i)
print(type(i))

i = "Test"
print (i)
print(type(i))

x=32
y=x

print (x)
print (y)

# to print identity of x & y to check if both are allocated to the same memory
print (id(x))
print (id(y))


#Standard way of declaring variable
#when there are multiple words --> number_of_months (use "_" to separate)

miles = 10
name = "tom"
print(miles,name)

#Multiple Assignment
a=b=c=1
print(a,b,c)

a,b,c = 3,4,5
print(a,b,c)

s1 = "Hello world"
print (s1[0])
print (s1[2:4])
print (s1[2:])
print (s1*2)
print (s1+ " Python")
print (s1[:0])