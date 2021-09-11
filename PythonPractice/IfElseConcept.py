#Taking the value during run time
x = int(input("Please enter the value of x : "))
print(x)

if(x<1):
    print("x is less than 1")
elif(x>2 and x<5):
    print("x is more than 2 and less than 3")
else:
    print("x is more than 5")

#logical opeartions "and" "not" "or"

total = 3
print("total : "+str(total))
print(f'{"total : "}{total}') #f string formula