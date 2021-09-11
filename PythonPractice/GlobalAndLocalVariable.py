# Global Variable
i = 10


def try_a_fun(n):
    # if the below line is not used, then error will be thrown
    global i
    i += 1
    k = 23
    print(n)


print(i)
try_a_fun(22)

#######################################################

rr = 10
def test_local_global():
    # the below rr is the local scope tp the function and not global
    rr = 5
    print(rr)

test_local_global()

# Since there is no global variable called k, below line line will throw error
# print(k)

#######################################################

# IMP --> In case global keyword is used and there is no such variable, then it'll create that variable

def global_key_word():
    global zz
    zz = 399
    print(zz)


def global_key_word_2():
    print(zz)


global_key_word()
global_key_word_2()
