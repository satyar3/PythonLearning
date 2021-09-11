#while
count = 0

while(count<=3):
    print(count)
    count+=1;


count1 = 0
while(count1<=3):
    print(count1)
    count1+=1;
else:
    print("Reached the Number")


#For Loop
name = ["java","python","js"]
for i in name:
    print(i)

str = "I am loving python"
for i in str:
    print(i)


#Range --> excluding the last number
#range(x) --> from o till x-1
#range(x,y) --> from x till y-1
#range(x,y,z) --> from x till y-1, skipping z chars i.e range (1,10,3) --> 1,4,7

name = ["java","python","js"]
for i in range(len(name)):
    print(name[i])


#for loop with else
name = ["java","python","js"]
for i in range(len(name)):
    print(name[i])
else:
    print("end of the list")

name = ["java","python","js"]
for i in range(1):
    print(name[i])
else:
    print("end of the list")

str1 = ["java","python","js",".net","c#","groovy"]
for i in range(1,3):
    print(str1[i])

#Nested for loop
for i in range(1,5):
    for j in range(2,4):
        print(i,j)
        print(str1[i],str1[j])

for i in range(1,5):
    for j in range(i):
        print(i, end="*")
    print()

print("----------------------")

for i in range(1,10,3):
    print(i)

print("----------------------")

numbers = [5,2,5,2,2]
for i in numbers:
    print("*"*i)

print("----------------------")

for i in numbers:
    output = ""
    for j in range(i):
        output += "*"
    print(output)
