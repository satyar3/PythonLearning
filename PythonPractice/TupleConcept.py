#   Tuple is a collection of elements of any type
#   But it can't be modified as it's immutable
#   syntax names = (1,2,3)
#   Tuple is order based i.e. stores data according to index


names = ("java","js","python")
# names[1] = ".net" --> not allowed to change
print(names)


#to delete the object from memory
del names
#print(names[1])


#Concatination
t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)

#Repetation
print(t1*4)

#Slicing
print(t1[1:])

# in
print(6 in t2)
print(5 not in t2)

for i in t2:
    print(i)

print(len(t2))

#Max Number
print(max(t2))
print(min(t1))

#Here in the below case, te index having highest alphabatical word will be returned
t1 = ("javazzzz","js","python")
print(max(t1))

t1 = ("zjava","js","python","jz")
print(max(t1))
print(min(t1))

#converting anything to tuple object
print(tuple((1,2,3,4)))
print(tuple([1,2,3,4]))
print(tuple({1,2,3,4}))
