import matplotlib.pyplot as plt
import numpy
import timeit
import math
import random


def example():
    mylist=[math.sqrt(x) for x in range(100)]
    return mylist


def get_test(length):
    # keys = [x for x in range(int(length))]
    # values = [(x*5) for x in keys]
    # dictionary = dict(zip(keys,values))
    to_get = random.randrange(100)
    return dictionary.get(to_get)

def update_test(length):
    # keys = [x for x in range(int(length))]
    # values = [(x*5) for x in keys]
    # dictionary = dict(zip(keys,values))
    to_update = random.randrange(100)
    d1={to_update:to_update*8}
    dictionary.update(d1)

lengths=[math.pow(2,x) for x in range(3,18)]
get_test_results=[]
update_test_results=[]
for length in lengths:
    keys = [x for x in range(int(length))]
    values = [(x*5) for x in keys]
    dictionary = dict(zip(keys,values))

    get_test_results.append((timeit.timeit("get_test(length)", setup = "from __main__ import get_test, length", number = 1000)))
    update_test_results.append((timeit.timeit("update_test(length)", setup = "from __main__ import update_test, length", number = 1000)))

plt.plot(lengths,get_test_results, label = "get() results")
plt.plot(lengths,update_test_results, label = "update() results")
plt.xlabel("Number of Elements")
plt.ylabel("Timeit Values")
plt.legend(loc='upper left')
plt.show()
    
