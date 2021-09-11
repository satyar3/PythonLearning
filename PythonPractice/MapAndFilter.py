items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

# Filter
x = list(filter(lambda item: item[1] > 9, items))
print(x)

y = set(filter(lambda item: "2" in item[0], items))
print(y)

# Map
z = list(map(lambda x: x[0], items))
print(z)

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

############################################################
ll = ['1', '2', '3']

k = list(map(lambda x: int(x), ll))
print(k)

# Or

k1 = list(map(int, ll))
print(k1)

############################################################
def square_fun(x):
    return x ** 2

ll1 = [1, 2, 3]
k3 = list(map(square_fun, ll1))
print(k3)

# Or

ll2 = [1, 2, 3]

k3 = list(map(lambda x: x ** 2, ll2))
print(k3)

############################################################

def sq_fun(x):
    return x**2

def cube_fun(x):
    return x**3

fun_list = [sq_fun, cube_fun]

for i in range(5):
    ll = list(map(lambda x: x(i),fun_list))
    print(ll)