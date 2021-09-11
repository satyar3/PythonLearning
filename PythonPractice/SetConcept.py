# Set is not order based i.e. doesn't store data according to index
# It can store different data
# It performs different mathematical operation
# It doesn't store duplicate element
# Syntax is {}

s1 = {100,200,"tom"}
print(s1)

s2 = {200,1,2,200,"Satya"}
print(s2)


# Converting a string into set
s3 = set("python")
print(s3)


# while creating a set object, you can store only numbers, strings and tuple
# List and dictionary objects are not allowed

# getting set object from list
s4 = set([1,2,3,45,5])
print(s4)

# getting set object from Tuple
s5 = set((1,4,5,2,43,534,6))
print(s5)

print(max(s5))




# Mathematical operation
p1 = {1,2,3,4}
p2 = {3,4,5,6}

#union
print(p1 | p2)
print(p1.union(p2))

#intersection
print(p1 & p2)
print(p1.intersection(p2))

#Difference
print(p1 - p2) # --> present only in p1 not in p2
print(p1.difference(p2))

print(p2 - p1) # --> present only in p2 not in p1
print(p2.difference(p1))

#Symetric difference --> prints all but not common elements between 2 sets
print(p1^p2)
print(p1.symmetric_difference(p2))

#Inbuild method
#add --> adding a single value to set
s1 = {"java","python","c++"}
s1.add("pearl")

print(s1)

#update --> Adding multiple values to the set
s1.update(['C',"c#"]) #-> adding list elements to the set
print(s1)

#clear
s1.clear() # -> Empty set
print(s1)


#copy
s3 = s2.copy()
print(s3)

#discard --> it doesn't throw error when there is no element found which needs to be removed
s3.discard(200) #-> removing an element from the set
print(s3)
s3.discard(404004)
print(s3)

#Remove # ---> it'll behave same way as discard but in case element not found, it'll throw error
s3.remove(1)
print(s3)
#s3.remove(404004)
#print(s3)