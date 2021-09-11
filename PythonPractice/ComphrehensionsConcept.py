# Writing 1 liner

# list comprehension
'''
Multi Liner :

ll = []
for i in range(100):
    if(i %3 == 0):
        ll.append(i)

'''
ll = [i for i in range(100) if i % 3 == 0]
print(ll)

# Dictionary Comprehension
'''
Expected Dict = {1: "Item1", 2: "Item2", .... 100: "Item100"}
'''

dd = {i: f'Item{i}' for i in range(1, 100) if i % 2 == 0}
print(dd)

dd1 = {value: key for key, value in dd.items()}
print(dd1)

# Set Comprehension
st1 = {i for i in [1, 1, 1, 1, 2, 3, 4, 2, 9, 1, 1, 2, 3, 3, 3]}
print(st1)

# Generator Comprehension
gen1 = (i for i in range(100) if i % 2 == 0)
print(gen1)
