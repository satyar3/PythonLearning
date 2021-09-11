# Stores data in key value pair
# key should be immutable type
data = {"name1": "satya", "name2": "peter"}
print(data)

# getting a value based on key
print(data["name1"])
print(data.get("name2"))

# if we want to print something when there is not data present for that key
print(data.get("name2", "not found"))
print(data.get("name3", "not found"))

# Adding a data to disctionary
data["name33"] = "tommy"
print(data)

# deleting data from dictionary
del data["name33"]
print(data)

# creating dictionary using list
keys = ["name1", "name2", "name3"]
values = ["satya", "tom", "peter"]
print(dict(zip(keys, values)))

list11 = [
    ['har', 1],
    ['ram', 2],
    ['sam', 3]
]

dct = dict(list11)
print(dct)

for key, val in list11:
    print(f'key is {key} and value is {val}')

for key, val in dct.items():
    print(f'key is {key} and value is {val}')
