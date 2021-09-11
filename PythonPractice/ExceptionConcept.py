import sys

try:
    age = int(input("Age : "))
    print(age)
except ValueError as e:
    print(f"Invalid Value -> {e}")
except Exception as e:
    print(f"In Exception Block -> {e}")
else:
    print("Successfully without exception")


try:
    age = int(input("Age : "))
    print(age)
except ValueError as e:
    print(f"Invalid Value -> {e}")
except Exception as e:
    print(f"In Exception Block -> {e}")
finally:
    print("Inside Finally")


try:
    age = int(input("Age : "))
    print(age)
except ValueError as e:
    print(f"Invalid Value -> {e}")
except Exception as e:
    print(f"In Exception Block -> {e}")
else:
    print("Successfully without exception")
finally:
    print("Inside Finally")


try:
    age = int(input("Age : "))
    print(age)
    sys.exit("Exiting ....")
except ValueError as e:
    print(f"Invalid Value -> {e}")
except Exception as e:
    print(f"In Exception Block -> {e}")
else:
    print("Successfully without exception")
finally:
    print("Inside Finally")
