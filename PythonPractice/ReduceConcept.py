from functools import reduce

ll = [1,2,4,2,6]
num = reduce(lambda x,y:x+y, ll)
print(num)
