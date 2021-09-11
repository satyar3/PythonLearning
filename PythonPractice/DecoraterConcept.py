def fun_1():
    print('inside fun1')


fun2 = fun_1
del fun_1
fun2()


##########################################################
def fun_3():
    return fun2


print(fun_3())


##########################################################
def fun_4(fun):
    fun("Hello")


fun_4(print)


##########################################################

def dec1(fun11):
    def now_exec():
        print("Execute now")
        fun11()
        print("Executed")
    return now_exec

@dec1
def test_1():
    print("In Test 1")

print("#####################")
# Without @dec1 annotaion
# test_1()
# test_1 = dec1(test_1)
# test_1()
print("#####################")
# With @dec1 annotation
test_1()