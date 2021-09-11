'''

There can be some scenarios where we need to call the same function again and again
and that might take sometime to execute.

functools module has a decorator called lru_cache which helps
to cache the functions given by user (that many times) so that it can
save time

'''

import time
from functools import lru_cache

# max 5 LAST calls will be cached into memory
i = 10


@lru_cache(maxsize=i)
def run_some_fun(n):
    time.sleep(n)
    return n


# When function will be cached
if __name__ == "__main__":
    print("Starting ..")
    k = run_some_fun(4)
    print(f'k == {k}')
    print("Ending and calling again ...")
    m = run_some_fun(4)
    print(f'm == {m}')
    print("Ending")

# When function won't be cached
if __name__ == "__main__":
    print("Starting ..")
    k = run_some_fun(4)
    print(f'k == {k}')
    print("Ending and calling again ...")
    m = run_some_fun(5)
    print(f'm == {m}')
    print("Ending")
