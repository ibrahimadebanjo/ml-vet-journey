# dictionary Analysis
# Comparing efficieny of a list and dictionary
import timeit
import random

for i in range(10000, 10000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random, x")
    # the list 
    x = list(range(i))
    lst_time = t.timeit(number = 1000)
    # The Dictionary
    x = { j : None for j in range(i)}
    d_time = t.timeit(number = 1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
# time for the contains operator on a dictionary is constant even as the dictionary size grows. In
#  fact for a dictionary size of 10000 the contains operation took 0004 milliseconds and for the
#  dictionary size of 990000 it also took 0004 milliseconds.