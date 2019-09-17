import matplotlib.pyplot as plt
import numpy
import timeit
import math
import random

def list_del_test(l, to_del):
    del l[to_del]

def dict_del_test(dictionary,to_del):
    del dictionary[to_del]

lengths=[x for x in range(100,10000,100)]
list_del_test_results=[]
dict_del_test_results=[]

for length in lengths:
    l =[x for x in range(int(length))]
    keys = [x for x in range(int(length))]
    values = [(x*5) for x in keys]
    dictionary = dict(zip(keys,values))
    to_del = random.randrange(len(l))

    list_del_test_results.append((timeit.timeit("list_del_test(l,to_del)", setup = "from __main__ import list_del_test,to_del, l", number = 1)))
    dict_del_test_results.append((timeit.timeit("dict_del_test(dictionary,to_del)", setup = "from __main__ import dict_del_test,to_del, dictionary", number = 1)))


plt.plot(lengths,list_del_test_results, label = "list_del() results")
plt.plot(lengths,dict_del_test_results, label = "dict_del() results")
plt.xlabel("Number of Elements")
plt.ylim(.00000,.0001)
plt.ylabel("Timeit Values")
plt.legend(loc='upper left')
plt.show()
    
