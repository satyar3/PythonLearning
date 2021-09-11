"""

Iterable = Any object which is having __iter__ or __getitem__ method is iterable i.e. the object can be looped
over

Iterator = Any object when called with __iter_- or __getitem__ return an iterator object which helps to
determine the next value using __next__ method


Iteration = Iterator is the process of looping over and it'll be
stopped when the program throws stop iteration error when the iterator is exhausted


Generator = It'll behave like a factory which can generate next values. it'll not generate and store the value rather
it'll generate the value on the fly when the iterator object is acted by __next__ method

"""


###### Generator

def gen_fun(n):
    for i in n:
        yield i


g = gen_fun(3)
k = g.__iter__()
k.__next__()
