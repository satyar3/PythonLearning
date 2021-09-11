user_input = input("Enter Name : ")

if user_input.isnumeric():
    raise Exception("I don't accept Number")
else:
    print(user_input)
