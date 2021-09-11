# Factorial
def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1


print(fact(3))


# Fibonacci
# 0 1 1 2 3 5 8 13

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(13))
