def print_name(name):
    print(f'name is {name}')


def add_num(a, b):
    print(f'Sum is {a + b}')


print("Inside file 1")
print(__name__)

# If the below condition is not given, then while importing the file as a module in other program, it'll execute the
# entire file
if __name__ == '__main__':
    print_name("Satya")
    add_num(2, 3)
