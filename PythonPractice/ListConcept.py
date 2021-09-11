# List is collection of data
# List is order based i.e. stores data according to index

score = [10, 20, 56]
print(score)
print((score[0]))

# slicing
print(score[1:3])
print(score[-3])  # the concept is same as string where right to left -1,-2,-3...

# shallow copy the list or new copy a list
print(score[:])

# concatinating with another list
print(score + [3, 4, 5])

# List are mutable
num = [1, 2, 3, 4, 5]
num[3] = 50
print(num)

# Appened
num.append(100)
print(num)

num.append(7 ** 3)
print(num)

# Insert
num.insert(1, 3000)
print(num)

# remove
num.remove(3000)

# clearing the list
num22 = [1, 2, 3, 4, 5]
num22.clear()

# Checking exsitance of a value in a list
print(num.index(2))
print(5 in num22)

# Sort
num22.sort()
num22.reverse()

# Copy
num33 = num22.copy()

# Replace value within a range
num[2:5] = ["A", "B", "C"]
print(num)
num[2:5] = []  # Assigning blank
print(num)
print(len(num))

# Making the entire list as empty
num[:] = []
print(num)

# Nested List
a = [1, 2, 3]
n = [4, 5, 6]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])  # go to 0th index and then get 1st index

t1 = ["zjava", "js", "python", "jz"]
print(max(t1))
print(min(t1))

# converting anything to list object
print(list((1, 2, 3, 4)))
print(list([1, 2, 3, 4]))
print(list({1, 2, 3, 4}))

ll = [1, 2, 3, 4, 5, 6, 7, 8]
print(ll[1:1])
print(ll[:10])
print(ll[::2])
print(ll[1::2])


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


# Driver code
str1 = "ABCD"
print(list(str1))
print(Convert(str1))

# **********************************
# Finding largest number from a list
list2 = [4, 6, 1, 8]
for i in list2:
    max = 0;
    if (i > max):
        max = i
print("********************")
print(max)

# Remove Duplicate from a list
list3 = [333, 1, 1, 2, 6, 7, 2, 2]
list4 = []
for i in list3:
    if (i not in list4):
        list4.append(i)

print(list4)
list4.sort()


def a_first(input):
    return input[0]


a1 = [[12, 1], [1, 2], [8, 23]]
a1.sort(key=a_first)
print(a1)

# or

a1.sort(key=lambda x : x[1])
print(a1)


# Join function
li = ['1','2','3','4','5','6']
ak = " and ".join(li)
print(ak)